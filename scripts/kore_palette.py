#!/usr/bin/env python3
"""Kore palette: derives a project's color tokens from its base colors
(references/rules/custom-palette.md) and measures them (Contrast).

Usage: python3 kore_palette.py [--themes light,dark] [--given light|dark]
                               (--primary #hex | --canvas C --primary C --accent C --ink C)
                               [--typology glassmorphism]

One color: --primary alone, one hex; Material Color Utilities (SchemeFidelity)
derives the rest. A palette (Kore's or a candidate): its four colors, each C one
hex for the theme --given names (light by default) or light=#hex,dark=#hex, in
every theme shipped. Prints one table per theme: token, value, lowest
contrast and the surface where it is lowest, source.
With --typology glassmorphism, each theme's table ends with the text tokens moved on the glass (Text on glass), plus page-background for one color only.
Exit code 0 when every token can be used, 1 when one cannot, 2 on bad input.

Example: python3 kore_palette.py --primary '#017e44'
"""
import argparse
import math
import re
import sys
from pathlib import Path
from types import SimpleNamespace

from check_references import read_tokens
from kore_check import over, parse_color, ratio

# ---------------------------------------------------------------- HCT
# Ported to Python from Material Color Utilities, TypeScript:
# https://github.com/material-foundation/material-color-utilities/tree/main/typescript
# (hct/hct.ts, hct/cam16.ts, hct/viewing_conditions.ts, hct/hct_solver.ts,
# utils/color_utils.ts, utils/math_utils.ts): ARGB -> HCT and HCT -> ARGB
# (the solver), in the default viewing conditions; and SchemeFidelity, spec 2021,
# contrastLevel 0 (mcu(), files listed above it).
#
# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

WHITE_POINT_D65 = [95.047, 100.0, 108.883]


def signum(num):
    return -1 if num < 0 else 0 if num == 0 else 1


def lerp(start, stop, amount):
    return (1.0 - amount) * start + amount * stop


def sanitize_degrees(degrees):
    return degrees % 360.0


def matrix_multiply(row, matrix):
    return [row[0] * m[0] + row[1] * m[1] + row[2] * m[2] for m in matrix]


def argb_from_rgb(red, green, blue):
    return 0xFF000000 | (red & 255) << 16 | (green & 255) << 8 | blue & 255


def linearized(rgb_component):
    normalized = rgb_component / 255.0
    if normalized <= 0.040449936:
        return normalized / 12.92 * 100.0
    return ((normalized + 0.055) / 1.055) ** 2.4 * 100.0


def delinearized(rgb_component):
    normalized = rgb_component / 100.0
    if normalized <= 0.0031308:
        delin = normalized * 12.92
    else:
        delin = 1.055 * normalized ** (1.0 / 2.4) - 0.055
    return min(255, max(0, math.floor(delin * 255.0 + 0.5)))  # JS Math.round


def argb_from_linrgb(linrgb):
    return argb_from_rgb(*(delinearized(c) for c in linrgb))


def lab_f(t):
    e, kappa = 216.0 / 24389.0, 24389.0 / 27.0
    return t ** (1.0 / 3.0) if t > e else (kappa * t + 16) / 116


def lab_invf(ft):
    e, kappa = 216.0 / 24389.0, 24389.0 / 27.0
    ft3 = ft * ft * ft
    return ft3 if ft3 > e else (116 * ft - 16) / kappa


def y_from_lstar(lstar):
    return 100.0 * lab_invf((lstar + 16.0) / 116.0)


def argb_from_lstar(lstar):
    component = delinearized(y_from_lstar(lstar))
    return argb_from_rgb(component, component, component)


def lstar_from_argb(argb):
    r, g, b = (linearized(argb >> s & 255) for s in (16, 8, 0))
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    return 116.0 * lab_f(y / 100.0) - 16.0


def default_viewing_conditions():
    """ViewingConditions.make() with its default arguments."""
    xyz = WHITE_POINT_D65
    adapting_luminance = (200.0 / math.pi) * y_from_lstar(50.0) / 100.0
    rgb_w = [xyz[0] * 0.401288 + xyz[1] * 0.650173 + xyz[2] * -0.051461,
             xyz[0] * -0.250268 + xyz[1] * 1.204414 + xyz[2] * 0.045854,
             xyz[0] * -0.002079 + xyz[1] * 0.048952 + xyz[2] * 0.953127]
    f = 0.8 + 2.0 / 10.0  # surround 2.0
    c = lerp(0.59, 0.69, (f - 0.9) * 10.0) if f >= 0.9 else lerp(0.525, 0.59, (f - 0.8) * 10.0)
    d = min(1.0, max(0.0, f * (1.0 - (1.0 / 3.6) * math.exp((-adapting_luminance - 42.0) / 92.0))))
    rgb_d = [d * (100.0 / w) + 1.0 - d for w in rgb_w]
    k = 1.0 / (5.0 * adapting_luminance + 1.0)
    k4 = k * k * k * k
    k4f = 1.0 - k4
    fl = k4 * adapting_luminance + 0.1 * k4f * k4f * (5.0 * adapting_luminance) ** (1.0 / 3.0)
    n = y_from_lstar(50.0) / xyz[1]  # background L* 50
    nbb = 0.725 / n ** 0.2
    factors = [(fl * dw / 100.0) ** 0.42 for dw in (rgb_d[i] * rgb_w[i] for i in range(3))]
    rgb_a = [400.0 * x / (x + 27.13) for x in factors]
    return SimpleNamespace(n=n, aw=(2.0 * rgb_a[0] + rgb_a[1] + 0.05 * rgb_a[2]) * nbb, nbb=nbb, ncb=nbb,
                           c=c, nc=f, rgb_d=rgb_d, fl=fl, fl_root=fl ** 0.25, z=1.48 + math.sqrt(n))


VC = default_viewing_conditions()


def cam16_hue_chroma(argb):
    """Cam16.fromInt, hue and chroma only."""
    red_l, green_l, blue_l = (linearized(argb >> s & 255) for s in (16, 8, 0))
    x = 0.41233895 * red_l + 0.35762064 * green_l + 0.18051042 * blue_l
    y = 0.2126 * red_l + 0.7152 * green_l + 0.0722 * blue_l
    z = 0.01932141 * red_l + 0.11916382 * green_l + 0.95034478 * blue_l
    r_c = 0.401288 * x + 0.650173 * y - 0.051461 * z
    g_c = -0.250268 * x + 1.204414 * y + 0.045854 * z
    b_c = -0.002079 * x + 0.048952 * y + 0.953127 * z
    adapted = []
    for d, comp in zip(VC.rgb_d, (r_c, g_c, b_c)):
        af = (VC.fl * abs(d * comp) / 100.0) ** 0.42
        adapted.append(signum(d * comp) * 400.0 * af / (af + 27.13))
    r_a, g_a, b_a = adapted
    a = (11.0 * r_a + -12.0 * g_a + b_a) / 11.0
    b = (r_a + g_a - 2.0 * b_a) / 9.0
    u = (20.0 * r_a + 20.0 * g_a + 21.0 * b_a) / 20.0
    p2 = (40.0 * r_a + 20.0 * g_a + b_a) / 20.0
    hue = sanitize_degrees(math.atan2(b, a) * 180.0 / math.pi)
    ac = p2 * VC.nbb
    j = 100.0 * (ac / VC.aw) ** (VC.c * VC.z)
    hue_prime = hue + 360 if hue < 20.14 else hue
    e_hue = 0.25 * (math.cos(hue_prime * math.pi / 180.0 + 2.0) + 3.8)
    p1 = (50000.0 / 13.0) * e_hue * VC.nc * VC.ncb
    t = p1 * math.sqrt(a * a + b * b) / (u + 0.305)
    alpha = t ** 0.9 * (1.64 - 0.29 ** VC.n) ** 0.73
    return hue, alpha * math.sqrt(j / 100.0)


def hct_from_argb(argb):
    """Hct.fromInt: (hue, chroma, tone)."""
    return (*cam16_hue_chroma(argb), lstar_from_argb(argb))


# HctSolver
SCALED_DISCOUNT_FROM_LINRGB = [
    [0.001200833568784504, 0.002389694492170889, 0.0002795742885861124],
    [0.0005891086651375999, 0.0029785502573438758, 0.0003270666104008398],
    [0.00010146692491640572, 0.0005364214359186694, 0.0032979401770712076],
]
LINRGB_FROM_SCALED_DISCOUNT = [
    [1373.2198709594231, -1100.4251190754821, -7.278681089101213],
    [-271.815969077903, 559.6580465940733, -32.46047482791194],
    [1.9622899599665666, -57.173814538844006, 308.7233197812385],
]
Y_FROM_LINRGB = [0.2126, 0.7152, 0.0722]
CRITICAL_PLANES = [
    0.015176349177441876, 0.045529047532325624, 0.07588174588720938,
    0.10623444424209313, 0.13658714259697685, 0.16693984095186062,
    0.19729253930674434, 0.2276452376616281, 0.2579979360165119,
    0.28835063437139563, 0.3188300904430532, 0.350925934958123,
    0.3848314933096426, 0.42057480301049466, 0.458183274052838,
    0.4976837250274023, 0.5391024159806381, 0.5824650784040898,
    0.6277969426914107, 0.6751227633498623, 0.7244668422128921,
    0.775853049866786, 0.829304845476233, 0.8848452951698498,
    0.942497089126609, 1.0022825574869039, 1.0642236851973577,
    1.1283421258858297, 1.1946592148522128, 1.2631959812511864,
    1.3339731595349034, 1.407011200216447, 1.4823302800086415,
    1.5599503113873272, 1.6398909516233677, 1.7221716113234105,
    1.8068114625156377, 1.8938294463134073, 1.9832442801866852,
    2.075074464868551, 2.1693382909216234, 2.2660538449872063,
    2.36523901573795, 2.4669114995532007, 2.5710888059345764,
    2.6777882626779785, 2.7870270208169257, 2.898822059350997,
    3.0131901897720907, 3.1301480604002863, 3.2497121605402226,
    3.3718988244681087, 3.4967242352587946, 3.624204428461639,
    3.754355295633311, 3.887192587735158, 4.022731918402185,
    4.160988767090289, 4.301978482107941, 4.445716283538092,
    4.592217266055746, 4.741496401646282, 4.893568542229298,
    5.048448422192488, 5.20615066083972, 5.3666897647573375,
    5.5300801301023865, 5.696336044816294, 5.865471690767354,
    6.037501145825082, 6.212438385869475, 6.390297286737924,
    6.571091626112461, 6.7548350853498045, 6.941541251256611,
    7.131223617812143, 7.323895587840543, 7.5195704746346665,
    7.7182615035334345, 7.919981813454504, 8.124744458384042,
    8.332562408825165, 8.543448553206703, 8.757415699253682,
    8.974476575321063, 9.194643831691977, 9.417930041841839,
    9.644347703669503, 9.873909240696694, 10.106627003236781,
    10.342513269534024, 10.58158024687427, 10.8238400726681,
    11.069304815507364, 11.317986476196008, 11.569896988756009,
    11.825048221409341, 12.083451977536606, 12.345119996613247,
    12.610063955123938, 12.878295467455942, 13.149826086772048,
    13.42466730586372, 13.702830557985108, 13.984327217668513,
    14.269168601521828, 14.55736596900856, 14.848930523210871,
    15.143873411576273, 15.44220572664832, 15.743938506781891,
    16.04908273684337, 16.35764934889634, 16.66964922287304,
    16.985093187232053, 17.30399201960269, 17.62635644741625,
    17.95219714852476, 18.281524751807332, 18.614349837764564,
    18.95068293910138, 19.290534541298456, 19.633915083172692,
    19.98083495742689, 20.331304511189067, 20.685334046541502,
    21.042933821039977, 21.404114048223256, 21.76888489811322,
    22.137256497705877, 22.50923893145328, 22.884842241736916,
    23.264076429332462, 23.6469514538663, 24.033477234264016,
    24.42366364919083, 24.817520537484558, 25.21505769858089,
    25.61628489293138, 26.021211842414342, 26.429848230738664,
    26.842203703840827, 27.258287870275353, 27.678110301598522,
    28.10168053274597, 28.529008062403893, 28.96010235337422,
    29.39497283293396, 29.83362889318845, 30.276079891419332,
    30.722335150426627, 31.172403958865512, 31.62629557157785,
    32.08401920991837, 32.54558406207592, 33.010999283389665,
    33.4802739966603, 33.953417292456834, 34.430438229418264,
    34.911345834551085, 35.39614910352207, 35.88485700094671,
    36.37747846067349, 36.87402238606382, 37.37449765026789,
    37.87891309649659, 38.38727753828926, 38.89959975977785,
    39.41588851594697, 39.93615253289054, 40.460400508064545,
    40.98864111053629, 41.520882981230194, 42.05713473317016,
    42.597404951718396, 43.141702194811224, 43.6900349931913,
    44.24241185063697, 44.798841244188324, 45.35933162437017,
    45.92389141541209, 46.49252901546552, 47.065252796817916,
    47.64207110610409, 48.22299226451468, 48.808024568002054,
    49.3971762874833, 49.9904556690408, 50.587870934119984,
    51.189430279724725, 51.79514187861014, 52.40501387947288,
    53.0190544071392, 53.637271562750364, 54.259673423945976,
    54.88626804504493, 55.517063457223934, 56.15206766869424,
    56.79128866487574, 57.43473440856916, 58.08241284012621,
    58.734331877617365, 59.39049941699807, 60.05092333227251,
    60.715611475655585, 61.38457167773311, 62.057811747619894,
    62.7353394731159, 63.417162620860914, 64.10328893648692,
    64.79372614476921, 65.48848194977529, 66.18756403501224,
    66.89098006357258, 67.59873767827808, 68.31084450182222,
    69.02730813691093, 69.74813616640164, 70.47333615344107,
    71.20291564160104, 71.93688215501312, 72.67524319850172,
    73.41800625771542, 74.16517879925733, 74.9167682708136,
    75.67278210128072, 76.43322770089146, 77.1981124613393,
    77.96744375590167, 78.74122893956174, 79.51947534912904,
    80.30219030335869, 81.08938110306934, 81.88105503125999,
    82.67721935322541, 83.4778813166706, 84.28304815182372,
    85.09272707154808, 85.90692527145302, 86.72564993000343,
    87.54890820862819, 88.3767072518277, 89.2090541872801,
    90.04595612594655, 90.88742016217518, 91.73345337380438,
    92.58406282226491, 93.43925555268066, 94.29903859396902,
    95.16341895893969, 96.03240364439274, 96.9059996312159,
    97.78421388448044, 98.6670533535366, 99.55452497210776,
]


def sanitize_radians(angle):
    return (angle + math.pi * 8) % (math.pi * 2)


def true_delinearized(rgb_component):
    normalized = rgb_component / 100.0
    if normalized <= 0.0031308:
        delin = normalized * 12.92
    else:
        delin = 1.055 * normalized ** (1.0 / 2.4) - 0.055
    return delin * 255.0


def chromatic_adaptation(component):
    af = abs(component) ** 0.42
    return signum(component) * 400.0 * af / (af + 27.13)


def hue_of(linrgb):
    scaled = matrix_multiply(linrgb, SCALED_DISCOUNT_FROM_LINRGB)
    r_a, g_a, b_a = (chromatic_adaptation(c) for c in scaled)
    a = (11.0 * r_a + -12.0 * g_a + b_a) / 11.0
    b = (r_a + g_a - 2.0 * b_a) / 9.0
    return math.atan2(b, a)


def are_in_cyclic_order(a, b, c):
    return sanitize_radians(b - a) < sanitize_radians(c - a)


def set_coordinate(source, coordinate, target, axis):
    t = (coordinate - source[axis]) / (target[axis] - source[axis])
    return [source[i] + (target[i] - source[i]) * t for i in range(3)]


def nth_vertex(y, n):
    k_r, k_g, k_b = Y_FROM_LINRGB
    coord_a = 0.0 if n % 4 <= 1 else 100.0
    coord_b = 0.0 if n % 2 == 0 else 100.0
    if n < 4:
        g, b = coord_a, coord_b
        r = (y - g * k_g - b * k_b) / k_r
        return [r, g, b] if 0.0 <= r <= 100.0 else [-1.0, -1.0, -1.0]
    if n < 8:
        b, r = coord_a, coord_b
        g = (y - r * k_r - b * k_b) / k_g
        return [r, g, b] if 0.0 <= g <= 100.0 else [-1.0, -1.0, -1.0]
    r, g = coord_a, coord_b
    b = (y - r * k_r - g * k_g) / k_b
    return [r, g, b] if 0.0 <= b <= 100.0 else [-1.0, -1.0, -1.0]


def bisect_to_segment(y, target_hue):
    left = right = [-1.0, -1.0, -1.0]
    left_hue = right_hue = 0.0
    initialized, uncut = False, True
    for n in range(12):
        mid = nth_vertex(y, n)
        if mid[0] < 0:
            continue
        mid_hue = hue_of(mid)
        if not initialized:
            left = right = mid
            left_hue = right_hue = mid_hue
            initialized = True
            continue
        if uncut or are_in_cyclic_order(left_hue, mid_hue, right_hue):
            uncut = False
            if are_in_cyclic_order(left_hue, target_hue, mid_hue):
                right, right_hue = mid, mid_hue
            else:
                left, left_hue = mid, mid_hue
    return left, right


def bisect_to_limit(y, target_hue):
    left, right = bisect_to_segment(y, target_hue)
    left_hue = hue_of(left)
    for axis in range(3):
        if left[axis] != right[axis]:
            if left[axis] < right[axis]:
                l_plane = math.floor(true_delinearized(left[axis]) - 0.5)
                r_plane = math.ceil(true_delinearized(right[axis]) - 0.5)
            else:
                l_plane = math.ceil(true_delinearized(left[axis]) - 0.5)
                r_plane = math.floor(true_delinearized(right[axis]) - 0.5)
            for _ in range(8):
                if abs(r_plane - l_plane) <= 1:
                    break
                m_plane = math.floor((l_plane + r_plane) / 2.0)
                mid = set_coordinate(left, CRITICAL_PLANES[m_plane], right, axis)
                mid_hue = hue_of(mid)
                if are_in_cyclic_order(left_hue, target_hue, mid_hue):
                    right, r_plane = mid, m_plane
                else:
                    left, left_hue, l_plane = mid, mid_hue, m_plane
    return [(left[i] + right[i]) / 2 for i in range(3)]


def inverse_chromatic_adaptation(adapted):
    adapted_abs = abs(adapted)
    base = max(0, 27.13 * adapted_abs / (400.0 - adapted_abs))
    return signum(adapted) * base ** (1.0 / 0.42)


def find_result_by_j(hue_radians, chroma, y):
    j = math.sqrt(y) * 11.0
    t_inner_coeff = 1 / (1.64 - 0.29 ** VC.n) ** 0.73
    e_hue = 0.25 * (math.cos(hue_radians + 2.0) + 3.8)
    p1 = e_hue * (50000.0 / 13.0) * VC.nc * VC.ncb
    h_sin, h_cos = math.sin(hue_radians), math.cos(hue_radians)
    for iteration_round in range(5):
        j_normalized = j / 100.0
        alpha = 0.0 if chroma == 0.0 or j == 0.0 else chroma / math.sqrt(j_normalized)
        t = (alpha * t_inner_coeff) ** (1.0 / 0.9)
        ac = VC.aw * j_normalized ** (1.0 / VC.c / VC.z)
        p2 = ac / VC.nbb
        gamma = 23.0 * (p2 + 0.305) * t / (23.0 * p1 + 11 * t * h_cos + 108.0 * t * h_sin)
        a, b = gamma * h_cos, gamma * h_sin
        r_a = (460.0 * p2 + 451.0 * a + 288.0 * b) / 1403.0
        g_a = (460.0 * p2 - 891.0 * a - 261.0 * b) / 1403.0
        b_a = (460.0 * p2 - 220.0 * a - 6300.0 * b) / 1403.0
        linrgb = matrix_multiply([inverse_chromatic_adaptation(c) for c in (r_a, g_a, b_a)],
                                 LINRGB_FROM_SCALED_DISCOUNT)
        if linrgb[0] < 0 or linrgb[1] < 0 or linrgb[2] < 0:
            return 0
        fnj = Y_FROM_LINRGB[0] * linrgb[0] + Y_FROM_LINRGB[1] * linrgb[1] + Y_FROM_LINRGB[2] * linrgb[2]
        if fnj <= 0:
            return 0
        if iteration_round == 4 or abs(fnj - y) < 0.002:
            if linrgb[0] > 100.01 or linrgb[1] > 100.01 or linrgb[2] > 100.01:
                return 0
            return argb_from_linrgb(linrgb)
        # Newton's method, with 2 * fn(j) / j as the approximation of fn'(j).
        j = j - (fnj - y) * j / (2 * fnj)
    return 0


def solve_to_int(hue_degrees, chroma, lstar):
    """HctSolver.solveToInt: the in-gamut ARGB closest to (hue, chroma, tone)."""
    if chroma < 0.0001 or lstar < 0.0001 or lstar > 99.9999:
        return argb_from_lstar(lstar)
    hue_radians = sanitize_degrees(hue_degrees) / 180 * math.pi
    y = y_from_lstar(lstar)
    exact = find_result_by_j(hue_radians, chroma, y)
    if exact != 0:
        return exact
    return argb_from_linrgb(bisect_to_limit(y, hue_radians))


# SchemeFidelity, spec 2021, contrastLevel 0: the roles MCU_ROLES of one source color.
# (scheme/scheme_fidelity.ts, dynamiccolor/dynamic_scheme.ts, dynamiccolor/color_spec_2021.ts,
# dynamiccolor/dynamic_color.ts, palettes/tonal_palette.ts, temperature/temperature_cache.ts,
# dislike/dislike_analyzer.ts, contrast/contrast.ts), at commit f242efc. An Hct is (hue, chroma, tone, argb).

SRGB_TO_XYZ = [[0.41233895, 0.35762064, 0.18051042], [0.2126, 0.7152, 0.0722], [0.01932141, 0.11916382, 0.95034478]]


def lstar_from_y(y):
    return lab_f(y / 100.0) * 116.0 - 16.0


def hct_of_argb(argb):
    return (*hct_from_argb(argb), argb)


def hct_from(hue, chroma, tone):
    """Hct.from: solved to an in-gamut ARGB, then read back."""
    return hct_of_argb(solve_to_int(hue, chroma, tone))


def raw_temperature(argb):
    x, y, z = (sum(m * linearized(argb >> s & 255) for m, s in zip(row, (16, 8, 0))) for row in SRGB_TO_XYZ)
    fx, fy, fz = lab_f(x / WHITE_POINT_D65[0]), lab_f(y / WHITE_POINT_D65[1]), lab_f(z / WHITE_POINT_D65[2])
    a, b = 500.0 * (fx - fy), 200.0 * (fy - fz)
    hue = sanitize_degrees(math.atan2(b, a) * 180.0 / math.pi)
    return -0.5 + 0.02 * math.hypot(a, b) ** 1.07 * math.cos(sanitize_degrees(hue - 50.0) * math.pi / 180.0)


def is_between(angle, a, b):
    return a <= angle <= b if a < b else a <= angle or angle <= b


def complement(source):
    """TemperatureCache.complement."""
    by_hue = [hct_from(hue, source[1], source[2]) for hue in range(361)]
    temps = [raw_temperature(h[3]) for h in by_hue + [source]]  # index 361 is the input, as in tempsByHct
    by_temp = sorted(range(362), key=temps.__getitem__)  # stable, as JS sort
    coldest, warmest = by_temp[0], by_temp[-1]
    cold_temp, rng = temps[coldest], temps[warmest] - temps[coldest]
    cold_hue, warm_hue = (by_hue + [source])[coldest][0], (by_hue + [source])[warmest][0]
    input_relative = 0.5 if rng == 0 else (temps[361] - cold_temp) / rng
    start, end = (warm_hue, cold_hue) if is_between(source[0], cold_hue, warm_hue) else (cold_hue, warm_hue)
    smallest, answer = 1000.0, by_hue[int(js_round(source[0]))]
    for addend in range(361):
        hue = sanitize_degrees(start + addend)
        if not is_between(hue, start, end):
            continue
        index = int(js_round(hue))
        error = abs(1.0 - input_relative - (temps[index] - cold_temp) / rng)
        if error < smallest:
            smallest, answer = error, by_hue[index]
    return answer


def fix_if_disliked(h):
    """DislikeAnalyzer.fixIfDisliked: dark yellow-greens move to tone 70."""
    if 90 <= js_round(h[0]) <= 111 and js_round(h[1]) > 16 and js_round(h[2]) < 65:
        return hct_from(h[0], h[1], 70.0)
    return h


def palette_tone(palette, tone):
    """TonalPalette.tone, as ARGB."""
    hue, chroma = palette
    if tone == 99 and 105 <= hue < 125:  # Hct.isYellow: the mean of tones 98 and 100
        a, b = palette_tone(palette, 98), palette_tone(palette, 100)
        return argb_from_rgb(*(int(js_round(((a >> s & 255) + (b >> s & 255)) / 2)) for s in (16, 8, 0)))
    return solve_to_int(hue, chroma, tone)


def ratio_of_tones(a, b):
    ya, yb = y_from_lstar(clamp(a, 0.0, 100.0)), y_from_lstar(clamp(b, 0.0, 100.0))
    return (max(ya, yb) + 5.0) / (min(ya, yb) + 5.0)


def contrast_lighter(tone, wanted):
    if not 0.0 <= tone <= 100.0:
        return -1.0
    dark_y = y_from_lstar(tone)
    light_y = wanted * (dark_y + 5.0) - 5.0
    real = (max(light_y, dark_y) + 5.0) / (min(light_y, dark_y) + 5.0)
    if real < wanted and abs(real - wanted) > 0.04:
        return -1.0
    value = lstar_from_y(light_y) + 0.4
    return -1.0 if value < 0 or value > 100 else value


def contrast_darker(tone, wanted):
    if not 0.0 <= tone <= 100.0:
        return -1.0
    light_y = y_from_lstar(tone)
    dark_y = (light_y + 5.0) / wanted - 5.0
    real = (max(light_y, dark_y) + 5.0) / (min(light_y, dark_y) + 5.0)
    if real < wanted and abs(real - wanted) > 0.04:
        return -1.0
    value = lstar_from_y(dark_y) - 0.4
    return -1.0 if value < 0 or value > 100 else value


def foreground_tone(bg, wanted):
    """DynamicColor.foregroundTone."""
    lighter = contrast_lighter(bg, wanted)
    lighter = 100.0 if lighter < 0 else lighter
    darker = contrast_darker(bg, wanted)
    darker = 0.0 if darker < 0 else darker
    light_ratio, dark_ratio = ratio_of_tones(lighter, bg), ratio_of_tones(darker, bg)
    if js_round(bg) < 60:  # tonePrefersLightForeground
        negligible = abs(light_ratio - dark_ratio) < 0.1 and light_ratio < wanted and dark_ratio < wanted
        return lighter if light_ratio >= wanted or light_ratio >= dark_ratio or negligible else darker
    return darker if dark_ratio >= wanted or dark_ratio >= light_ratio else lighter


# role: (palette, raw tone (light, dark) or a function of the scheme, isBackground, background, contrast at level 0, tone-delta pair (nearer, farther))
HIGHEST = "highestSurface"  # surfaceDim in light, surfaceBright in dark
MCU_SPEC = {
    "surface": ("neutral", (98, 6), True, None, None, None),
    "surfaceDim": ("neutral", (87, 6), True, None, None, None),
    "surfaceBright": ("neutral", (98, 24), True, None, None, None),
    "surfaceContainerLowest": ("neutral", (100, 4), True, None, None, None),
    "surfaceContainerLow": ("neutral", (96, 10), True, None, None, None),
    "surfaceContainer": ("neutral", (94, 12), True, None, None, None),
    "surfaceContainerHigh": ("neutral", (92, 17), True, None, None, None),
    "surfaceContainerHighest": ("neutral", (90, 22), True, None, None, None),
    "onSurface": ("neutral", (10, 90), False, HIGHEST, 4.5, None),
    "onSurfaceVariant": ("neutralVariant", (30, 80), False, HIGHEST, 3, None),
    "outline": ("neutralVariant", (50, 60), False, HIGHEST, 1.5, None),
    "outlineVariant": ("neutralVariant", (80, 30), False, HIGHEST, 1, None),
    "primary": ("primary", (40, 80), True, HIGHEST, 3, ("primaryContainer", "primary")),
    "primaryContainer": ("primary", lambda s: s["source"][2], True, HIGHEST, 1, ("primaryContainer", "primary")),
    "onPrimaryContainer": ("primary", lambda s: foreground_tone(raw_tone(s, "primaryContainer"), 4.5), False,
                           "primaryContainer", 4.5, None),
    "tertiary": ("tertiary", (40, 80), True, HIGHEST, 3, ("tertiaryContainer", "tertiary")),
    "tertiaryContainer": ("tertiary", lambda s: fix_if_disliked(hct_of_argb(palette_tone(s["tertiary"], s["source"][2])))[2],
                          True, HIGHEST, 1, ("tertiaryContainer", "tertiary")),
}
MCU_ROLES = ["surface", "onSurface", "primaryContainer", "tertiaryContainer", "onPrimaryContainer",
             "surfaceContainerLowest", "surfaceContainerLow", "surfaceContainer", "surfaceContainerHigh",
             "surfaceContainerHighest", "onSurfaceVariant", "outline", "outlineVariant"]


def raw_tone(s, role):
    tone = MCU_SPEC[role][1]
    return tone(s) if callable(tone) else tone[s["dark"]]


def background_of(s, role):
    bg = MCU_SPEC[role][3]
    return ("surfaceBright" if s["dark"] else "surfaceDim") if bg == HIGHEST else bg


def get_tone(s, role):
    """ColorCalculationDelegateImpl2021.getTone, contrastLevel 0."""
    _, _, is_background, _, wanted, pair = MCU_SPEC[role]
    bg = background_of(s, role)
    if pair:
        nearer, farther = pair
        delta, expansion = 10, 1 if s["dark"] else -1
        n_tone, f_tone = raw_tone(s, nearer), raw_tone(s, farther)
        if bg:
            bg_tone = get_tone(s, bg)
            n_wanted, f_wanted = MCU_SPEC[nearer][4], MCU_SPEC[farther][4]
            if ratio_of_tones(bg_tone, n_tone) < n_wanted:
                n_tone = foreground_tone(bg_tone, n_wanted)
            if ratio_of_tones(bg_tone, f_tone) < f_wanted:
                f_tone = foreground_tone(bg_tone, f_wanted)
        if (f_tone - n_tone) * expansion < delta:
            f_tone = clamp(n_tone + delta * expansion, 0, 100)
            if (f_tone - n_tone) * expansion < delta:
                n_tone = clamp(f_tone - delta * expansion, 0, 100)
        if 50 <= n_tone < 60:
            n_tone = 60 if expansion > 0 else 49
            f_tone = max(f_tone, n_tone + delta) if expansion > 0 else min(f_tone, n_tone - delta)
        elif 50 <= f_tone < 60:  # stayTogether is false for every pair here
            f_tone = 60 if expansion > 0 else 49
        return n_tone if role == nearer else f_tone
    answer = raw_tone(s, role)
    if not bg:
        return answer
    bg_tone = get_tone(s, bg)
    if ratio_of_tones(bg_tone, answer) < wanted:
        answer = foreground_tone(bg_tone, wanted)
    if is_background and 50 <= answer < 60:
        answer = 49 if ratio_of_tones(49, bg_tone) >= wanted else 60
    return answer


def mcu(color):
    """SchemeFidelity on one color: {"light": {role: hex}, "dark": {role: hex}} for MCU_ROLES, and "palettes"."""
    source = hct_of_argb(int(fmt(parse_color(color))[1:], 16) | 0xFF000000)
    hue, chroma = source[:2]
    tertiary = fix_if_disliked(complement(source))
    palettes = {"primary": (hue, chroma), "tertiary": tertiary[:2], "neutral": (hue, chroma / 8.0),
                "neutralVariant": (hue, chroma / 8.0 + 4.0)}
    result = {}
    for theme in THEMES:
        s = {**palettes, "source": source, "dark": theme == "dark"}
        result[theme] = {role: "#%06x" % (palette_tone(s[MCU_SPEC[role][0]], get_tone(s, role)) & 0xFFFFFF)
                         for role in MCU_ROLES}
    result["palettes"] = palettes  # (hue, chroma) of each MCU palette, for Method step 3
    return result

# ---------------------------------------------------------------- end of the port

# ---------------------------------------------------------------- helpers

def js_round(value, decimals=0):
    scale = 10 ** decimals
    return math.floor(scale * value + 0.5) / scale + 0


def clamp(value, low, high):
    return min(max(value, low), high)


# ---------------------------------------------------------------- palette (custom-palette.md)

ROOT = Path(__file__).resolve().parent.parent
THEMES = ("light", "dark")
ROLES = ("canvas", "primary", "accent", "ink")  # a palette's four colors (ways 1 and 2)
HEX = re.compile(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})")
BASE_TONE = {"canvas": (98, 3)}  # Pure white or black canvas, light and dark
SURFACES = ["canvas", "surface-card", "surface-elevated", "surface-deep", "surface-float", "surface-float-active",
            "surface-hover", "surface-pressed"]
# Issue #14, step 1. One color (way 3): the base colors are these MCU roles.
WAY3 = {"canvas": "surface", "primary": "primaryContainer", "accent": "tertiaryContainer", "ink": "onSurface"}
# token -> (MCU role in light, in dark, the MCU palette it moves along to pass Contrast, or None)
MCU_MAP = {
    "surface-card": ("surfaceContainerLowest", "surfaceContainerLow", None),
    "surface-elevated": ("surfaceContainer", "surfaceContainer", None),
    "surface-deep": ("surfaceContainerLowest", "surfaceContainerLowest", None),
    "surface-float": ("surfaceContainerLowest", "surfaceContainerHigh", None),
    "surface-float-active": ("surfaceContainer", "surfaceContainerHighest", None),
    "hairline-medium": ("outlineVariant", "outlineVariant", None),
    "hairline-strong": ("outline", "outline", "neutralVariant"),
    "mute": ("onSurfaceVariant", "onSurfaceVariant", "neutralVariant"),
    "primary-on": ("onPrimaryContainer", "onPrimaryContainer", "primary"),
}
# Material 3 state layers: token -> (color under, color over, opacity), the solid sRGB mix
STATE = {"stone": ("canvas", "ink", 0.38), "surface-hover": ("canvas", "ink", 0.08), "surface-pressed": ("canvas", "ink", 0.10),
         "primary-pressed": ("primary", "primary-on", 0.10), "danger-pressed": ("danger", "danger-on", 0.10)}
KINDS = ["danger", "warning", "success", "info"]
GLOWS = ["accent", "warning", "info", "success", "danger"]
UNMEASURED = ["scrim", "veil-photo", "veil-cover", "on-photo", "on-photo-mute"]
CHARTS = [f"chart-{n}" for n in range(1, 9)]
FILLS = {"primary-on", "primary-pressed", "danger-pressed", "on-vivid"}  # measured on a fill, not on the surfaces
WHITE, BLACK = (255, 255, 255, 1.0), (0, 0, 0, 1.0)
# typologies/glassmorphism/SKILL.md, Text on glass and Page background
GLASS_SATURATE = {"light": 1.2, "dark": 1.5}  # glass-backdrop saturate
GLASS_MINIMUM = {**dict.fromkeys(["ink", "body", "mute", "link", "danger", "warning", "success", "info"], 4.5),
                 **dict.fromkeys(["accent", "hairline-strong", "focus-ring"], 3)}


def hct(color):
    return hct_from_argb(argb_from_rgb(*(int(round(v)) for v in color[:3])))


def at(hue, chroma, tone, alpha=1.0):
    argb = solve_to_int(hue, chroma, tone)
    return argb >> 16 & 255, argb >> 8 & 255, argb & 255, alpha


def fmt(color):
    r, g, b = (int(round(v)) for v in color[:3])
    return f"#{r:02x}{g:02x}{b:02x}" if color[3] == 1 else f"rgba({r}, {g}, {b}, {color[3]:.2f})"


def lowest(color, backgrounds):
    """(ratio, name) on the background where color contrasts least, composited over it first."""
    return min((ratio(over(color, bg), bg), name) for name, bg in backgrounds.items())


def move(color, measure, minimum, step, hue_chroma=None):
    """Method step 3: one tone at a time (step -1 down, +1 up), keeping hue and chroma, until
    measure(color) passes; None when it reaches tone 0 or 100 without passing."""
    hue, chroma, tone = hct(color)
    hue, chroma = hue_chroma or (hue, chroma)
    while measure(color)[0] < minimum:
        if (tone <= 0) if step < 0 else (tone >= 100):
            return None
        tone = min(100, max(0, tone + step))
        color = at(hue, chroma, tone, color[3])
    return color


def mix(top, alpha, under):
    """The solid sRGB mix of top at alpha over under (the *-edge tokens, the state layers)."""
    return tuple(int(t * alpha + u * (1 - alpha) + 0.5) for t, u in zip(top[:3], under[:3])) + (1.0,)


def saturate(color, amount):
    """CSS saturate(): the feColorMatrix saturate matrix on the sRGB values, clamped; alpha 1.0."""
    s, (r, g, b) = amount, color[:3]
    return (clamp((0.213 + 0.787 * s) * r + (0.715 - 0.715 * s) * g + (0.072 - 0.072 * s) * b, 0, 255),
            clamp((0.213 - 0.213 * s) * r + (0.715 + 0.285 * s) * g + (0.072 - 0.072 * s) * b, 0, 255),
            clamp((0.213 - 0.213 * s) * r + (0.715 - 0.715 * s) * g + (0.072 + 0.928 * s) * b, 0, 255), 1.0)


def glass(theme, colors, stops):
    """Text on glass: {token: (moved color, [])} for each token of GLASS_MINIMUM below its minimum on the glass over
    the canvas and the 5 hex stops of this theme's Page background; (None, [(token, minimum, where)]) when tone 0 or 100 fails."""
    saturated = {"canvas": saturate(colors["canvas"], GLASS_SATURATE[theme]),
                 **{f"stop {i}": saturate(parse_color(h), GLASS_SATURATE[theme]) for i, h in enumerate(stops, 1)}}
    if theme == "light":
        points = {n: over(WHITE[:3] + (0.30,), p) for n, p in saturated.items()}
    else:
        card = {n: over(colors["surface-card"][:3] + (0.50,), p) for n, p in saturated.items()}
        points = {**card, **{f"{n} sheen": over(WHITE[:3] + (0.09,), p) for n, p in card.items()}}
    result = {}
    for token, minimum in GLASS_MINIMUM.items():
        ratio_where = lowest(colors[token], points)
        if ratio_where[0] < minimum:
            moved = move(colors[token], lambda c: lowest(c, points), minimum, -1 if theme == "light" else 1)
            result[token] = (moved, []) if moved else (None, [(token, minimum, ratio_where[1])])
    return result


# mycolor.space/gradient: sRGB <-> CIE LCH, the XYZ matrices at 4 decimals (not MCU's)
D65 = (0.95047, 1.0, 1.08883)
TO_XYZ = ((0.4124, 0.3576, 0.1805), (0.2126, 0.7152, 0.0722), (0.0193, 0.1192, 0.9505))
FROM_XYZ = ((3.2406, -1.5372, -0.4986), (-0.9689, 1.8758, 0.0415), (0.0557, -0.2040, 1.0570))


def lch(color):
    lin = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in (v / 255 for v in color[:3])]
    f = [lab_f(sum(m * c for m, c in zip(row, lin)) / w) for row, w in zip(TO_XYZ, D65)]
    a, b = 500 * (f[0] - f[1]), 200 * (f[1] - f[2])
    return 116 * f[1] - 16, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def hex_from_lch(l, c, h):
    fy = (l + 16) / 116
    fa, fb = fy + c * math.cos(math.radians(h)) / 500, fy - c * math.sin(math.radians(h)) / 200
    xyz = [lab_invf(f) * w for f, w in zip((fa, fy, fb), D65)]
    lin = [sum(m * v for m, v in zip(row, xyz)) for row in FROM_XYZ]
    rgb = [12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055 for v in lin]
    return "#" + "".join(f"{int(clamp(js_round(v * 255), 0, 255)):02x}" for v in rgb)


def page_background(colors):
    """Page background {theme: gradient} behind the glass: primary to accent in CIE LCH, 5 stops (mycolor.space/gradient)."""
    result = {}
    for theme, pair in colors.items():
        (l0, c0, h0), (l1, c1, h1) = lch(pair["primary"]), lch(pair["accent"])
        dh = (h1 - h0 + 180) % 360 - 180
        stops = [hex_from_lch(l0 + (l1 - l0) * t, c0 + (c1 - c0) * t, h0 + dh * t) for t in (0, 0.25, 0.5, 0.75, 1)]
        result[theme] = f"linear-gradient(to right top, {', '.join(stops)})"
    return result


def kore_colors(root=ROOT):
    tokens = read_tokens((Path(root) / "references" / "tokens.yaml").read_text(encoding="utf-8"))
    return {theme: {key: parse_color(value) for key, entries in tokens.items()
                    for path, value in entries if path[:2] == ["colors", theme]} for theme in THEMES}


def base_colors(given, themes):
    """Method step 1: {theme: {role: (color, source)}}, {theme: mcu() of the color MCU runs on}, and the notes.
    given: {"primary": {theme: color}} with one color (way 3), or a palette's four ROLES in every theme (ways 1 and 2)."""
    base, sources, notes = {}, {}, []
    one = list(given) == ["primary"]
    for theme in themes:
        i = THEMES.index(theme)
        sources[theme] = mcu(fmt(next(iter(given["primary"].values())) if one else given["primary"][theme]))
        if one:  # way 3: MCU derives the four colors; the given color stays given where MCU keeps it
            colors = {role: parse_color(sources[theme][theme][r]) for role, r in WAY3.items()}
            base[theme] = {role: (c, "given" if role == "primary" and fmt(c) == fmt(next(iter(given["primary"].values())))
                                  else "derived") for role, c in colors.items()}
        else:  # ways 1 and 2: the palette's colors as written
            base[theme] = {role: (given[role][theme], "given") for role in ROLES}
        color = base[theme]["canvas"][0]
        hue, chroma, tone = hct(color)
        if round(tone) in (0, 100):
            notes.append(f"{theme}: the canvas {fmt(color)} is at tone {round(tone)} and leaves no room for the "
                         f"surfaces (Pure white or black canvas): its tone moves to {BASE_TONE['canvas'][i]}.")
            base[theme]["canvas"] = (at(hue, chroma, BASE_TONE["canvas"][i]), "derived")
    return base, sources, notes


def derive(theme, base, m, on_vivid, kore, dark=None):
    """Method steps 2 and 3 for one theme: {token: [color, source, (ratio, where) or None]},
    the tokens that cannot be used as (token, minimum, where), and the notes. m: mcu() of the theme's
    MCU color, the source of MCU_MAP. dark: the dark theme's tokens as derive gives them, for on-vivid."""
    i = THEMES.index(theme)
    away = -1 if theme == "light" else 1  # Method step 3: down in light, up in dark
    tokens, failed, notes = {}, [], []

    def put(name, color, source="derived", measure=None, minimum=None, step=away, keep=False, hue_chroma=None):
        if minimum and not keep and measure(color)[0] < minimum:
            moved = move(color, measure, minimum, step, hue_chroma)
            if moved is None:
                failed.append((name, minimum, measure(color)[1]))
            else:
                color, source = moved, "moved to pass Contrast"
        tokens[name] = [color, source, measure(color) if measure else None]
        return color

    def mapped(name, measure=None, minimum=None, step=away):
        role, pal = MCU_MAP[name][i], MCU_MAP[name][2]
        return put(name, parse_color(m[theme][role]), "derived", measure, minimum, step, hue_chroma=m["palettes"][pal] if pal else None)

    def state(name, colors, measure=None, minimum=None, step=away):
        under, top, alpha = STATE[name]
        return put(name, mix(colors[top], alpha, colors[under]), "derived", measure, minimum, step)

    canvas = put("canvas", *base["canvas"])
    for name in SURFACES[1:6]:
        mapped(name)
    # shortcut: hover and pressed mix the base ink, not the ink Method step 3 may move below; recompute if ink moves often
    for name in SURFACES[6:]:
        state(name, {"canvas": canvas, "ink": base["ink"][0]})
    surfaces = {name: tokens[name][0] for name in SURFACES}

    def on_surfaces(color):
        return lowest(color, surfaces)

    mapped("hairline-medium", on_surfaces)
    ink = put("ink", *base["ink"], on_surfaces, 4.5)
    body = ink[:3] + (0.86,)
    r, where = on_surfaces(body)
    if r < 4.5:  # Translucent text (Contrast): a solid color for that pair, then moved as Method step 3
        body = tuple(round(v) for v in over(body, surfaces[where]))
        notes.append(f"{theme}: body is solid in this palette: ink at 86% fails 4.5:1 on {where} (Translucent text).")
    body = put("body", body, "moved to pass Contrast" if r < 4.5 else "derived", on_surfaces, 4.5)
    mapped("mute", on_surfaces, 4.5)
    strong = mapped("hairline-strong", on_surfaces, 3)
    state("stone", {"canvas": canvas, "ink": ink}, on_surfaces)
    put("hairline", ink[:3] + (0.06,), measure=on_surfaces)
    put("focus-ring", strong, measure=on_surfaces, minimum=3)
    put("surface-card-edge", mix(BLACK, 0.2, surfaces["surface-card"]), measure=on_surfaces)

    primary = put("primary", *base["primary"])
    on = mapped("primary-on", lambda c: lowest(c, {"primary": primary}), 4.5,
                1 if hct(parse_color(m[theme][MCU_MAP["primary-on"][i]]))[2] > hct(primary)[2] else -1)
    on_primary = lambda c: (ratio(on, c), "primary-on")  # noqa: E731
    tokens["primary"][2] = on_primary(primary)
    pressed = state("primary-pressed", {"primary": primary, "primary-on": on}, on_primary, 4.5,
                    -1 if hct(on)[2] > hct(primary)[2] else 1)  # a fill moves away from its on-color
    tokens["primary-on"][2] = lowest(on, {"primary": primary, "primary-pressed": pressed})
    put("primary-edge", mix(BLACK, 0.2, primary), measure=on_surfaces)

    danger = put("danger", kore[theme]["danger"], "Kore's value", on_surfaces, 4.5)  # the kinds stay Kore's (user, 2026-11-18)
    # whichever of white and black contrasts more reaches at least 4.58:1 (1.05 / sqrt(0.0525)) on any solid fill
    danger_on = max((WHITE, BLACK), key=lambda c: ratio(c, danger))
    pressed = state("danger-pressed", {"danger": danger, "danger-on": danger_on}, lambda c: (ratio(danger_on, c), "danger-on"),
                    4.5, -1 if danger_on == WHITE else 1)
    put("danger-on", danger_on, measure=lambda c: lowest(c, {"danger": danger, "danger-pressed": pressed}))
    put("danger-edge", mix(BLACK, 0.2, danger), measure=on_surfaces)

    for kind in ("warning", "success", "info"):
        put(kind, kore[theme][kind], "Kore's value", on_surfaces, 4.5)
    put("link", kore[theme]["info"], "derived", on_surfaces, 4.5)

    accent = put("accent", *base["accent"], on_surfaces, 3)  # large text only (The accent is rare)

    for name, color in [(f"{k}-glow", tokens[k][0]) for k in GLOWS] + [("selection", accent)]:
        if theme == "light":
            alpha = 0.20
        else:  # the lowest opacity, raised 1% at a time, that reaches 1.5:1 on every surface
            alpha = next((p / 100 for p in range(1, 101) if all(
                ratio(over(color[:3] + (p / 100,), bg), bg) >= 1.5 for bg in surfaces.values())), None)
        glow = color[:3] + (alpha or 1.0,)
        under = {s: over(glow, bg) for s, bg in surfaces.items()}
        measured = min(lowest(text, under) for text in ((ink,) if name == "selection" else (ink, body)))
        usable = alpha is not None and measured[0] >= 4.5
        tokens[name] = [glow, "derived" if usable else "not used", measured]
        if not usable:
            notes.append(f"{theme}: {name} is not used: the text over it fails 4.5:1 on {measured[1]} (Derived tokens).")

    dark = tokens if theme == "dark" else dark or {}  # Alert: the kind's dark-theme value as derived in this run
    vivid = {f"{k} (dark)": dark[k][0] if k in dark else kore["dark"][k] for k in KINDS}  # no dark theme: Kore's
    for k in KINDS:  # vivid-*: the dark theme's kind colors, in both themes (Derived tokens)
        put(f"vivid-{k}", vivid[f"{k} (dark)"], "derived" if k in dark else "Kore's value")
    put("on-vivid", on_vivid, "derived", lambda c: lowest(c, vivid), 3, -1)  # away from the lighter vivid fills
    for name in UNMEASURED:
        put(name, kore[theme][name], "Kore's value")
    for name in CHARTS:
        put(name, kore[theme][name], "Kore's value", on_surfaces, 3, keep=True)
        r, where = tokens[name][2]
        if r < 3:
            notes.append(f"{theme}: {name} is below 3:1 on {where}: it keeps its value and needs the legend, "
                         "visible direct labels or the table view (Contrast).")
    return tokens, failed, notes


def palette(given, themes, kore):
    """{theme: tokens} as derive gives them, the notes, and the problems that stop the palette."""
    base, sources, notes = base_colors(given, themes)
    if "dark" in base:
        on_vivid = base["dark"]["canvas"][0]
    else:
        hue, chroma, _ = hct(base["light"]["canvas"][0])
        on_vivid = at(hue, chroma, 3)
    tables, problems = {}, []
    # dark first: on-vivid is measured in both themes on the dark kinds as derived
    def derived(theme, *args):
        return derive(theme, base[theme], sources[theme], on_vivid, kore, *args)
    dark = derived("dark") if "dark" in base else ({}, [], [])
    for theme in themes:
        tables[theme], failed, theme_notes = dark if theme == "dark" else derived(theme, dark[0])
        notes += theme_notes
        problems += [f"{theme}: {name} cannot reach {m}:1 on {where}, even at the end of its scale or at tone 0 or 100 (Method step 3): "
                     "ask for another color." for name, m, where in failed]
        if any(name not in FILLS for name, _, _ in failed):
            hue, chroma, _ = hct(base[theme]["canvas"][0])
            tone = BASE_TONE["canvas"][THEMES.index(theme)]
            problems.append(f"{theme}: the canvas fails (Canvas that fails): propose another canvas, or (recommended) keep its hue "
                            f"and chroma and move its tone to {tone}: --canvas {theme}={fmt(at(hue, chroma, tone))}.")
    return tables, notes, problems


def show(ratio_where):
    if not ratio_where:
        return "—", "—"
    r, where = ratio_where
    return f"{math.floor(r * 100) / 100:.2f}:1", where  # never round up: 4.499 shows 4.49


def main(argv=None):
    parser = argparse.ArgumentParser(
        usage="python3 kore_palette.py [--themes light,dark] [--given light|dark] (--primary #hex | "
              "--canvas C --primary C --accent C --ink C) [--typology glassmorphism]",
        description="Derives the color tokens (references/rules/custom-palette.md) and measures them. "
                    "One color: --primary alone, one hex; MCU derives the rest. A palette: --canvas, --primary, "
                    "--accent and --ink, each one hex for the theme --given names or light=#hex,dark=#hex, in every theme shipped.",
        epilog="Example: python3 kore_palette.py --primary '#017e44'")
    parser.add_argument("--themes", default="light,dark", help="the themes the project ships (default both)")
    parser.add_argument("--given", choices=THEMES, default="light", help="the theme a single hex is given for (default light)")
    for role in ROLES:
        parser.add_argument(f"--{role}", metavar="C")
    parser.add_argument("--typology", choices=["glassmorphism"], help="also print the text tokens this typology moves (Text on glass)")
    args = parser.parse_args(argv)
    names = args.themes.split(",")
    if not names or any(t not in THEMES for t in names) or len(set(names)) < len(names):
        parser.error(f"--themes {args.themes}: light, dark or light,dark")
    given = {}
    for role in ROLES:
        value = getattr(args, role)
        for part in (value.split(",") if value and "=" in value else [f"{args.given}={value}"] if value else []):
            theme, _, color = (s.strip() for s in part.partition("="))
            m = HEX.fullmatch(color)
            if theme not in THEMES or not m or theme in given.get(role, {}):
                parser.error(f"--{role} {value}: one hex (#rgb or #rrggbb) or light=#hex,dark=#hex")
            given.setdefault(role, {})[theme] = parse_color("#" + m.group(1))
    if not given:
        parser.error("no color given: with 0 colors Kore's own palette is used and nothing is derived")
    themes = [t for t in THEMES if t in names]
    one = list(given) == ["primary"] and len(given["primary"]) == 1
    if not one and (set(given) != set(ROLES) or any(t not in own for own in given.values() for t in themes)):
        parser.error("give one color (--primary alone, one hex) or a palette (--canvas, --primary, --accent and --ink "
                     f"in every theme shipped: {','.join(themes)})")
    kore = kore_colors()
    tables, notes, problems = palette(given, themes, kore)
    page = page_background({t: {k: tab[k][0] for k in ("primary", "accent")} for t, tab in tables.items()}) \
        if args.typology and one else None  # a palette's gradient is stored in candidates.md and tokens.yaml
    gradients = page_background({t: {k: tab[k][0] for k in ("primary", "accent")} for t, tab in tables.items()})
    for theme, tokens in tables.items():
        print(f"{theme}\n{'token':<22} {'value':<26} {'lowest':<8} {'on':<42} source")
        for name in (n for n in kore[theme] if n in tokens):  # in the order of tokens.yaml
            color, source, measured = tokens[name]
            print(f"{name:<22} {fmt(color):<26} {show(measured)[0]:<8} {show(measured)[1]:<42} {source}")
        if args.typology:
            other = THEMES[1 - THEMES.index(theme)]
            if other not in gradients:
                problems.append(f"{theme}: glassmorphism needs the other theme's primary and accent for Page background: ship both themes.")
            else:
                stops = re.findall(r"#[0-9a-f]{6}", gradients[other])
                for name, (color, failed) in glass(theme, {n: v[0] for n, v in tokens.items()}, stops).items():
                    print(f"{name:<22} {fmt(color) if color else '—':<26} {'—':<8} {'—':<42} Text on glass")
                    problems += [f"{theme}: {token} cannot reach {m}:1 on the glass over {where}, even at tone 0 or 100 "
                                 "(Text on glass): ask for another color." for token, m, where in failed]
            if page:
                print(f"{'page-background':<22} {page[theme]}")
        print()
    for line in notes + problems:
        print(line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
