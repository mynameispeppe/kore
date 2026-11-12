#!/usr/bin/env python3
"""Kore palette: derives a project's color tokens from its base colors
(references/rules/custom-palette.md) and measures them (Contrast).

Usage: python3 kore_palette.py [--themes light,dark] [--given light|dark]
                               [--canvas C] [--primary C] [--accent C]

C is one hex, for the theme --given names (light by default), or
light=#hex,dark=#hex. A role not given follows Missing colors; canvas or
primary must be given. Prints one table per theme: token, value, lowest
contrast and the surface where it is lowest, source.
Exit code 0 when every token can be used, 1 when one cannot, 2 on bad input.

Example: python3 kore_palette.py --canvas '#F8FAFB' --primary 'light=#212121,dark=#fcfdff'
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
# utils/color_utils.ts, utils/math_utils.ts); only ARGB -> HCT and HCT -> ARGB
# (the solver), in the default viewing conditions.
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

# ---------------------------------------------------------------- end of the port

# ---------------------------------------------------------------- harmony (CIE LCh, D50)
# Palette method of palettable.dev, rewritten here; color math as the colord npm
# package does it (lch plugin), rounding included, so the hex match cell by cell.

WHITE_POINT_D50 = [96.422, 100.0, 82.521]
D65_TO_D50 = [[1.0478112, 0.0228866, -0.050127], [0.0295424, 0.9904844, -0.0170491], [-0.0092345, 0.0150436, 0.7521316]]
D50_TO_D65 = [[0.9555766, -0.0230393, 0.0631636], [-0.0282895, 1.0099416, 0.0210077], [0.0122982, -0.020483, 1.3299098]]
SRGB_TO_XYZ = [[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.072175], [0.0193339, 0.119192, 0.9503041]]
XYZ_TO_SRGB = [[0.032404542, -0.015371385, -0.004985314], [-0.00969266, 0.018760108, 0.00041556],
               [0.000556434, -0.002040259, 0.010572252]]
HARMONY_OFFSETS = {
    "vibrant": [y * 20 for y in range(-4, 5)],
    "monochrome": [y * 2 for y in range(-4, 5)],
    "analogous": [y * 8 for y in range(-4, 5)],
    "tetradic": [-180, -120, -60, -30, 0, 30, 60, 120, 180],
    "quadratic": [-180, -135, -90, -45, 0, 45, 90, 135, 180],
}
FEATURED = [(2, 4), (0, 2), (1, 3), (3, 6), (0, 7)]


def js_round(value, decimals=0):
    scale = 10 ** decimals
    return math.floor(scale * value + 0.5) / scale + 0


def clamp(value, low, high):
    return min(max(value, low), high)


def lch_from_rgb(rgb):
    """(l, c, h) of an sRGB triple (0..255, not rounded), rounded to 2 decimals as colord does."""
    lin = [v / 12.92 if v < 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in (c / 255 for c in rgb)]
    xyz = matrix_multiply([100 * v for v in matrix_multiply(lin, SRGB_TO_XYZ)], D65_TO_D50)
    fx, fy, fz = (lab_f(clamp(v, 0, white) / white) for v, white in zip(xyz, WHITE_POINT_D50))
    a, b = js_round(500 * (fx - fy), 3), js_round(200 * (fy - fz), 3)
    hue = math.degrees(math.atan2(b, a))
    return js_round(116 * fy - 16, 2), js_round(math.hypot(a, b), 2), js_round(hue + 360 if hue < 0 else hue, 2) % 360


def rgb_from_lch(l, c, h):
    """Unrounded sRGB triple (0..255) of an LCh color, each channel clamped as colord does."""
    l, h = clamp(l, 0, 100), h % 360
    a, b = c * math.cos(math.radians(h)), c * math.sin(math.radians(h))
    fy = (l + 16) / 116
    xyz = [lab_invf(fy + a / 500) * WHITE_POINT_D50[0], lab_invf(fy) * WHITE_POINT_D50[1],
           lab_invf(fy - b / 200) * WHITE_POINT_D50[2]]
    lin = matrix_multiply(matrix_multiply(xyz, D50_TO_D65), XYZ_TO_SRGB)
    return [clamp(255 * (1.055 * v ** (1 / 2.4) - 0.055 if v > 0.0031308 else 12.92 * v), 0, 255) for v in lin]


def harmony(color, mode):
    """4x9 matrix of uppercase hex and the 5 featured cells: color is (r, g, b[, a]), mode a key of HARMONY_OFFSETS."""
    l, c, h = lch_from_rgb(color[:3])
    mids = []
    for m, offset in enumerate(HARMONY_OFFSETS[mode]):
        y = m - 4
        mids.append(rgb_from_lch(clamp(l - y * 6, 0, 100), clamp(c + y * 5, 0, 100), (h + offset + 360) % 360))
    rows = [[], [], [], []]
    for rgb in mids:
        cl, cc, ch = lch_from_rgb(rgb)
        rows[0].append(rgb_from_lch(clamp(cl + 25, 0, 100), clamp(cc - 15, 0, 100), (ch - 5 + 360) % 360))
        rows[1].append(rgb_from_lch(clamp(cl + 5, 0, 100), clamp(cc - 25, 0, 100), ch))
        rows[2].append(rgb)
        rows[3].append(rgb_from_lch(clamp(cl - 25, 0, 100), clamp(cc + 10, 0, 100), (ch + 5) % 360))
    matrix = [["#%02X%02X%02X" % tuple(int(js_round(v)) for v in rgb) for rgb in row] for row in rows]
    return matrix, [matrix[r][k] for r, k in FEATURED]


# ---------------------------------------------------------------- palette (custom-palette.md)

ROOT = Path(__file__).resolve().parent.parent
THEMES = ("light", "dark")
ROLES = ("canvas", "primary", "accent")
HEX = re.compile(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})")
BASE_TONE = {"canvas": (98, 3), "primary": (40, 80), "accent": (40, 80)}  # Themes, light and dark
MISSING = {"canvas": ("primary", 0, 6), "primary": ("canvas", 0, 36), "accent": ("primary", None, None)}  # from, hue +, chroma
ACCENT_CELL = ("analogous", 0, 8)  # Missing colors: the accent is this harmony cell of primary
GRAY = 5  # below this HCT chroma a color has no hue (score.ts)
NEUTRAL_CHROMA = 6
CANVAS_STEPS = {  # Derived tokens: canvas tone +, light and dark
    "surface-card": (1, 3), "surface-elevated": (-1.5, 9), "surface-deep": (1, -1), "surface-float": (1, 8),
    "surface-float-active": (-1.5, 8 + 7),  # dark: surface-float tone +7
    "surface-hover": (-3.5, 9.5), "surface-pressed": (-6, 12),
}
SURFACES = ["canvas", *CANVAS_STEPS]
KINDS = ["danger", "warning", "success", "info"]
GLOWS = ["accent", "warning", "info", "success", "danger"]
UNMEASURED = ["scrim", "veil-photo", "veil-cover", "on-photo", "on-photo-mute"]
CHARTS = [f"chart-{n}" for n in range(1, 9)]
FILLS = {"primary-pressed", "danger-pressed", "on-vivid"}  # measured on a fill, not on the surfaces
WHITE, BLACK = (255, 255, 255, 1.0), (0, 0, 0, 1.0)


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


def last_passing(hue, chroma, tone, step, measure, minimum):
    """mute, hairline-strong: from a passing tone, one tone at a time, the last tone that still passes."""
    while 0 <= tone + step <= 100 and measure(at(hue, chroma, tone + step))[0] >= minimum:
        tone += step
    return at(hue, chroma, tone)


def mix_black(color):
    """The *-edge tokens: the fill mixed in sRGB, 80% with 20% black."""
    return tuple(int(v * 0.8 + 0.5) for v in color[:3]) + (1.0,)


def kore_colors(root=ROOT):
    tokens = read_tokens((Path(root) / "references" / "tokens.yaml").read_text(encoding="utf-8"))
    return {theme: {key: parse_color(value) for key, entries in tokens.items()
                    for path, value in entries if path[:2] == ["colors", theme]} for theme in THEMES}


def base_colors(given, themes, kore):
    """Method step 1: {theme: {role: (color, source)}}, and the notes to tell the user."""
    base, notes = {}, []
    order = ROLES if "canvas" in given else ("primary", "canvas", "accent")  # a missing canvas comes from primary
    for theme in themes:
        i, base[theme] = THEMES.index(theme), {}
        for role in order:
            own = given.get(role, {})
            if theme in own:
                color, source = own[theme], "given"
            elif own:  # Themes: the other theme's hue and chroma, this theme's tone
                hue, chroma, _ = hct(next(iter(own.values())))
                if role == "canvas":
                    chroma = min(chroma, NEUTRAL_CHROMA)
                color, source = at(hue, chroma, BASE_TONE[role][i]), "derived"
            elif not {"canvas", "primary"} & set(given):  # only an accent given: Kore's canvas and primary (How many colors)
                color, source = kore[theme][role], "Kore's value"
            else:  # Missing colors, step 3: the derived value
                from_role, shift, chroma = MISSING[role]
                mine = given.get(from_role, {})  # the given color: a derived one at tone 3 has lost its hue
                start = mine.get(theme) or next(iter(mine.values()), None) or base[theme][from_role][0]
                hue, from_chroma, _ = hct(start)
                if from_chroma < GRAY or (not mine and base[theme][from_role][1] == "Kore's value"):  # Kore's pair stays whole
                    color, source = kore[theme][role], "Kore's value"
                elif role == "accent":
                    mode, row, col = ACCENT_CELL
                    color, source = parse_color(harmony(start, mode)[0][row][col]), "derived"
                    if mine and theme not in mine:  # Themes: the other theme's hue and chroma, this theme's tone
                        hue, chroma, _ = hct(color)
                        color = at(hue, chroma, BASE_TONE[role][i])
                else:
                    color, source = at(hue + shift, chroma, BASE_TONE[role][i]), "derived"
            hue, chroma, tone = hct(color)
            if role == "canvas" and round(tone) in (0, 100):
                notes.append(f"{theme}: the canvas {fmt(color)} is at tone {round(tone)} and leaves no room for the "
                             f"surfaces (Pure white or black canvas): its tone moves to {BASE_TONE['canvas'][i]}.")
                color, source = at(hue, chroma, BASE_TONE["canvas"][i]), "derived"
            base[theme][role] = (color, source)
    return base, notes


def derive(theme, base, on_vivid, kore, dark=None):
    """Method steps 2 and 3 for one theme: {token: [color, source, (ratio, where) or None]},
    the tokens that cannot be used as (token, minimum, where), and the notes. dark: the dark
    theme's tokens as derive gives them, for on-vivid."""
    i = THEMES.index(theme)
    away = -1 if theme == "light" else 1  # Method step 3: down in light, up in dark
    tokens, failed, notes = {}, [], []

    def put(name, color, source="derived", measure=None, minimum=None, step=away, keep=False):
        if minimum and not keep and measure(color)[0] < minimum:
            moved = move(color, measure, minimum, step)
            if moved is None:
                failed.append((name, minimum, measure(color)[1]))
            else:
                color, source = moved, "moved to pass Contrast"
        tokens[name] = [color, source, measure(color) if measure else None]
        return color

    canvas = put("canvas", *base["canvas"])
    hue, chroma, tone = hct(canvas)
    chroma = min(chroma, NEUTRAL_CHROMA)  # Neutral tokens: canvas hue and chroma, at most 6
    for name, steps in CANVAS_STEPS.items():
        put(name, at(hue, chroma, tone + steps[i]))
    surfaces = {name: tokens[name][0] for name in SURFACES}

    def on_surfaces(color):
        return lowest(color, surfaces)

    put("hairline-medium", at(hue, chroma, tone + (-9.5, 16.5)[i]), measure=on_surfaces)
    ink = move(at(hue, chroma, (17, 96)[i]), on_surfaces, 4.5, away, (hue, chroma))
    if ink is None:
        failed.append(("ink", 4.5, on_surfaces(at(hue, chroma, (0, 100)[i]))[1]))
        return tokens, failed, notes
    put("ink", ink, measure=on_surfaces)
    body = ink[:3] + (0.86,)
    r, where = on_surfaces(body)
    if r < 4.5:  # Translucent text (Contrast): a solid color for that pair, then moved as Method step 3
        body = tuple(round(v) for v in over(body, surfaces[where]))
        notes.append(f"{theme}: body is solid in this palette: ink at 86% fails 4.5:1 on {where} (Translucent text).")
    body = put("body", body, "moved to pass Contrast" if r < 4.5 else "derived", on_surfaces, 4.5)
    ink_tone = hct(ink)[2]
    mute = put("mute", last_passing(hue, chroma, ink_tone, -away, on_surfaces, 4.5), measure=on_surfaces)
    strong = put("hairline-strong", last_passing(hue, chroma, ink_tone, -away, on_surfaces, 3), measure=on_surfaces)
    put("stone", at(hue, chroma, (tone + hct(mute)[2]) / 2), measure=on_surfaces)
    put("hairline", ink[:3] + (0.06,), measure=on_surfaces)
    put("focus-ring", strong, measure=on_surfaces, minimum=3)
    put("surface-card-edge", mix_black(surfaces["surface-card"]), measure=on_surfaces)

    danger = put("danger", kore[theme]["danger"], "Kore's value", on_surfaces, 4.5)  # danger text
    for kind, color in (("primary", base["primary"][0]), ("danger", danger)):
        # whichever of white and black contrasts more reaches at least 4.58:1 (1.05 / sqrt(0.0525)) on any solid fill
        on = max((WHITE, BLACK), key=lambda c: ratio(c, color))

        def on_fill(c, kind=kind, on=on):
            return ratio(on, c), f"{kind}-on"
        if kind == "primary":  # keeps its given value; danger is measured as text above
            put(kind, *base[kind], on_fill)
        step = -1 if on == WHITE else 1  # a fill moves away from its on-color
        f_hue, f_chroma, f_tone = hct(color)
        pressed = put(f"{kind}-pressed", at(f_hue, f_chroma, f_tone + (6 if tone > f_tone else -6)),
                      "derived", on_fill, 4.5, step)
        put(f"{kind}-on", on, measure=lambda c, b={kind: color, f"{kind}-pressed": pressed}: lowest(c, b))
        put(f"{kind}-edge", mix_black(color), measure=on_surfaces)

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
    base, notes = base_colors(given, themes, kore)
    if "dark" in base:
        on_vivid = base["dark"]["canvas"][0]
    else:
        hue, chroma, _ = hct(base["light"]["canvas"][0])
        on_vivid = at(hue, chroma, 3)
    tables, problems = {}, []
    # dark first: on-vivid is measured in both themes on the dark kinds as derived
    dark = derive("dark", base["dark"], on_vivid, kore) if "dark" in base else ({}, [], [])
    for theme in themes:
        tables[theme], failed, theme_notes = dark if theme == "dark" else derive(theme, base[theme], on_vivid, kore, dark[0])
        notes += theme_notes
        problems += [f"{theme}: {name} cannot reach {m}:1 on {where}, even at tone 0 or 100 (Method step 3): "
                     "ask for another color." for name, m, where in failed]
        if any(name not in FILLS for name, _, _ in failed):
            hue, chroma, _ = hct(base[theme]["canvas"][0])
            tone = BASE_TONE["canvas"][THEMES.index(theme)]
            problems.append(f"{theme}: the canvas fails (Canvas that fails): propose another canvas, or (recommended) keep its hue "
                            f"and chroma and move its tone to {tone}: --canvas {theme}={fmt(at(hue, chroma, tone))}.")
    return tables, notes, problems


def read_candidates(path=ROOT / "references" / "candidates.md"):
    """{"canvas": rows of the canvas sections, "palettes": rows of Palettes}, each row (name, theme, {role: color}), in file order."""
    candidates, section = {"canvas": [], "palettes": []}, None
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
        cells = [c.strip().strip("`") for c in line.strip().split("|")[1:-1]]
        if section in ("canvas — light", "canvas — dark") and len(cells) > 1 and HEX.fullmatch(cells[1]):
            candidates["canvas"].append((cells[0], section.rpartition(" ")[2], {"canvas": parse_color(cells[1])}))
        elif section == "Palettes" and len(cells) == 5 and cells[1] in THEMES:
            candidates["palettes"].append((cells[0], cells[1], {
                role: parse_color(c) for role, c in zip(ROLES, cells[2:]) if HEX.fullmatch(c)}))
    return candidates


def propose(given, themes, kore, candidates):
    """Missing colors, step (2), for the first missing role: the lines to print (none when no role is missing)."""
    role = next((r for r in ROLES if r not in given), None)
    if role is None:
        return []
    base, _ = base_colors(given, THEMES, kore)  # step (3)'s derived value, in any theme a candidate row has
    if role == "canvas":  # one proposal per theme some color is given for
        pools = [([t], candidates["canvas"]) for t in themes if any(t in own for own in given.values())]
    else:  # primary or accent comes after canvas, so canvas is given: the rows of its themes
        pools = [([t for t in THEMES if t in given["canvas"]], candidates["palettes"])]

    def passes(theme, color):
        if role == "canvas":
            return not any("(Canvas that fails)" in p for p in palette({"canvas": {theme: color}}, [theme], kore)[2])
        if role == "primary":
            return max(ratio(WHITE, color), ratio(BLACK, color)) >= 4.5
        return palette({**given, "accent": {theme: color}}, [theme], kore)[0][theme]["accent"][1] == "given"

    def order(row):  # by hue distance to the derived value; gray candidates last; a gray or Kore's target keeps file order
        target, source = base[row[1]][role]
        t_hue, t_chroma, _ = hct(target)
        hue, chroma, _ = hct(row[2][role])
        if source == "Kore's value" or t_chroma < GRAY:
            return 0, 0
        return (1, 0) if chroma < GRAY else (0, min(abs(hue - t_hue), 360 - abs(hue - t_hue)))

    lines = []
    for pool_themes, rows in pools:
        rows = [row for row in rows if row[1] in pool_themes and role in row[2]]
        best = next((row for row in sorted(rows, key=order) if passes(row[1], row[2][role])), None)  # sorted is stable
        if best:
            name, theme, colors = best
            lines.append(f"Missing colors, step (2): propose {role} {name} {fmt(colors[role]).upper()} ({theme}) and wait "
                         f"for the OK; if the user declines, rerun with --{role} {theme}={fmt(base[theme][role][0])}.")
        else:
            lines += [f"Missing colors, step (2): no candidate passes for {role} ({t}): use the derived value "
                      f"{fmt(base[t][role][0])}." for t in pool_themes]
    return lines


def show(ratio_where):
    if not ratio_where:
        return "—", "—"
    r, where = ratio_where
    return f"{math.floor(r * 100) / 100:.2f}:1", where  # never round up: 4.499 shows 4.49


def main(argv=None):
    parser = argparse.ArgumentParser(
        usage="python3 kore_palette.py [--themes light,dark] [--given light|dark] [--canvas C] [--primary C] [--accent C]",
        description="Derives the color tokens from the base colors (references/rules/custom-palette.md) "
                    "and measures them. C is one hex, for the theme --given names, or light=#hex,dark=#hex. "
                    "Then proposes the candidate of references/candidates.md for the first missing role "
                    "(Missing colors, step 2).",
        epilog="Example: python3 kore_palette.py --canvas '#F8FAFB' --primary 'light=#212121,dark=#fcfdff'")
    parser.add_argument("--themes", default="light,dark", help="the themes the project ships (default both)")
    parser.add_argument("--given", choices=THEMES, default="light", help="the theme a single hex is given for (default light)")
    for role in ROLES:
        parser.add_argument(f"--{role}", metavar="C")
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
    kore = kore_colors()
    themes = [t for t in THEMES if t in names]
    tables, notes, problems = palette(given, themes, kore)
    for theme, tokens in tables.items():
        print(f"{theme}\n{'token':<22} {'value':<26} {'lowest':<8} {'on':<42} source")
        for name in (n for n in kore[theme] if n in tokens):  # in the order of tokens.yaml
            color, source, measured = tokens[name]
            print(f"{name:<22} {fmt(color):<26} {show(measured)[0]:<8} {show(measured)[1]:<42} {source}")
        print()
    for line in notes + problems + propose(given, themes, kore, read_candidates()):
        print(line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
