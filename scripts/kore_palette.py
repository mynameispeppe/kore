#!/usr/bin/env python3
"""Kore palette: derives a project's color tokens from its base colors
(references/rules/custom-palette.md) and measures them (Contrast).

Usage: python3 kore_palette.py [--themes light,dark] [--given light|dark]
                               [--canvas C] [--primary C] [--accent C]
                               [--typology glassmorphism]

C is one hex, for the theme --given names (light by default), or
light=#hex,dark=#hex. A role not given follows Missing colors; canvas or
primary must be given. Prints one table per theme: token, value, lowest
contrast and the surface where it is lowest, source.
With --typology glassmorphism, each theme's table ends with glass-fill, glass-fill-strong and page-background (typologies/glassmorphism/SKILL.md, Glass fill).
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

# ---------------------------------------------------------------- helpers

def js_round(value, decimals=0):
    scale = 10 ** decimals
    return math.floor(scale * value + 0.5) / scale + 0


def clamp(value, low, high):
    return min(max(value, low), high)


# ---------------------------------------------------------------- palette (custom-palette.md)

ROOT = Path(__file__).resolve().parent.parent
THEMES = ("light", "dark")
ROLES = ("canvas", "primary", "accent")
HEX = re.compile(r"#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})")
BASE_TONE = {"canvas": (98, 3), "primary": (40, 80), "accent": (40, 80)}  # Themes, light and dark
MISSING = {"primary": ("canvas", 0, 36)}  # from, hue +, chroma
GRAY = 5  # below this HCT chroma a color has no hue (score.ts)
SURFACES = ["canvas", "surface-card", "surface-elevated", "surface-deep", "surface-float", "surface-float-active",
            "surface-hover", "surface-pressed"]
# Derived tokens: token -> (light source, dark source, the Huecode scale it moves along to pass Contrast, or None).
# A source is a CSS var of huecode() ("--surface") or "role step" of its scales ("neutral 100").
HUECODE_MAP = {
    "surface-card": ("--surface", "--surface", None),
    "surface-elevated": ("--surface-2", "--surface-2", None),
    "surface-deep": ("--surface", "neutral 950", None),
    "surface-float": ("--surface", "--surface-2", None),
    "surface-float-active": ("--surface-2", "--surface-2", None),
    "surface-hover": ("--surface-2", "--surface-2", None),
    "surface-pressed": ("neutral 100", "--surface-2", None),  # Huecode's surface-3 (neutral 200 / 600) leaves no text step above 4.5:1
    "hairline-medium": ("--border", "--border", None),
    "hairline-strong": ("--border-strong", "--border-strong", "neutral"),
    "ink": ("--text", "--text", "neutral"),
    "stone": ("neutral 400", "neutral 500", None),
    "primary-on": ("--accent-fg", "--accent-fg", None),
    "primary-pressed": ("--accent-hover", "--accent-hover", "primary"),
}
KINDS = ["danger", "warning", "success", "info"]
GLOWS = ["accent", "warning", "info", "success", "danger"]
UNMEASURED = ["scrim", "veil-photo", "veil-cover", "on-photo", "on-photo-mute"]
CHARTS = [f"chart-{n}" for n in range(1, 9)]
FILLS = {"primary-pressed", "danger-pressed", "on-vivid"}  # measured on a fill, not on the surfaces
WHITE, BLACK = (255, 255, 255, 1.0), (0, 0, 0, 1.0)
# typologies/glassmorphism/SKILL.md, Glass fill and Page background
GLASS_GLOW = 0.60  # the core of the two glows: accent and primary at 60% over canvas
GLASS_SATURATE = 1.40  # glass-saturate
PAGE_TONE = {"light": 63, "dark": 38}  # page background: the tone of its colors
GLASS_TINT = {"light": (255, 255, 255), "dark": (32, 32, 32)}
GLASS_MINIMUM = {**dict.fromkeys(["ink", "body", "mute", "link", "danger", "warning", "success", "info"], 4.5),
                 **dict.fromkeys(["accent", "hairline-strong", "focus-ring"], 3)}


# ---------------------------------------------------------------- Huecode
# Ported to Python from Huecode, TypeScript:
# https://github.com/larisabarabas/huecode, commit 68b88c9
# (src/lib/color.ts, paletteBuilder.ts, previewTheme.ts, types.ts); only the fixed path
# of buildPaletteFromBase (no rng) and the hex vars of paletteToCssVars (no --ring, no --shadow-*).
#
# MIT License
#
# Copyright (c) 2026 Stefania Barabas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

HUECODE_STEPS = (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950)
HUECODE_ROLES = ("primary", "secondary", "accent", "neutral", "success", "warning", "error", "info")
HUECODE_LIGHT_SIDE = {50: 0, 100: 0.067, 200: 0.244, 300: 0.467, 400: 0.733, 500: 1}
HUECODE_DARK_SIDE = {500: 0, 600: 0.2, 700: 0.4, 800: 0.6, 900: 0.8, 950: 1}
HUECODE_ANCHORS = {"success": (142, 65, 42), "warning": (38, 92, 50), "error": (4, 78, 52), "info": (217, 80, 52)}
HUECODE_TARGET = {"light": ((500, 600, 700), 50), "dark": ((300, 400, 500), 65)}  # pick: candidate steps, HSL lightness
HUECODE_SEMANTIC = {"ok": "success", "warn": "warning", "err": "error", "info": "info"}


def huecode_hsl_to_hex(h, s, l):
    sat, light, hue = clamp(s, 0, 100) / 100, clamp(l, 0, 100) / 100, (h % 360 + 360) % 360
    a = sat * min(light, 1 - light)

    def f(n):
        k = (n + hue / 30) % 12
        return light - a * max(-1, min(k - 3, min(9 - k, 1)))

    return "#" + "".join(f"{int(js_round(f(n) * 255)):02x}" for n in (0, 8, 4))


def huecode_hex_to_rgb(hexa):
    clean = hexa.replace("#", "")
    num = int(clean, 16)
    return (num >> 16) & 255, (num >> 8) & 255, num & 255


def huecode_hex_to_hsl(hexa):
    r, g, b = (c / 255 for c in huecode_hex_to_rgb(hexa))
    top, low = max(r, g, b), min(r, g, b)
    l = (top + low) / 2
    if top == low:
        return 0, 0, l * 100
    d = top - low
    s = d / (2 - top - low) if l > 0.5 else d / (top + low)
    if top == r:
        h = (g - b) / d + (6 if g < b else 0)
    elif top == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return h * 60, s * 100, l * 100


def huecode_shade_scale(h, s, l):
    mid = clamp(l, 15, 90)
    scale = {}
    for step in HUECODE_STEPS:
        light_side = step <= 500
        span = 97 - mid if light_side else mid - 12
        fraction = (HUECODE_LIGHT_SIDE if light_side else HUECODE_DARK_SIDE)[step]
        target = 97 - fraction * span if light_side else mid - fraction * span
        distance = 0 if span == 0 else abs(target - mid) / span
        scale[str(step)] = huecode_hsl_to_hex(h, clamp(s * (1 - distance * 0.28), 0, 100), target)
    return scale


def huecode_luminance(hexa):
    return sum(w * (c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
               for w, c in zip((0.2126, 0.7152, 0.0722), (v / 255 for v in huecode_hex_to_rgb(hexa))))


def huecode_contrast(a, b):
    la, lb = huecode_luminance(a), huecode_luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def huecode_readable(background):
    return "#000000" if huecode_contrast(background, "#000000") >= huecode_contrast(background, "#ffffff") else "#ffffff"


def huecode_mix_hue(h1, h2, weight):
    return (h1 + ((h2 - h1 + 540) % 360 - 180) * weight + 360) % 360


def huecode_semantic(anchor, primary):
    shift = clamp((primary[0] - anchor[0] + 540) % 360 - 180, -28, 28)
    return ((anchor[0] + shift + 360) % 360, clamp(anchor[1] * 0.65 + primary[1] * 0.35, 0, 100),
            clamp(anchor[2] * 0.8 + primary[2] * 0.2, 0, 100))


def huecode_pick_contrast(scale, background, candidates, minimum):
    for step in candidates:
        if huecode_contrast(scale[str(step)], background) >= minimum:
            return scale[str(step)]
    return scale[str(candidates[-1])]


def huecode_pick_lightness(scale, candidates, target):
    best, best_distance = scale[str(candidates[0])], math.inf
    for step in candidates:
        distance = abs(huecode_hex_to_hsl(scale[str(step)])[2] - target)
        if distance < best_distance:
            best, best_distance = scale[str(step)], distance
    return best


def huecode_css_vars(palette, dark):
    neutral, primary, v = palette["neutral"], palette["primary"], {}
    if dark:
        v.update({"--bg": neutral["900"], "--surface": neutral["800"], "--surface-2": neutral["700"],
                  "--surface-3": neutral["600"], "--border": neutral["600"], "--border-strong": neutral["500"]})
        v["--text"] = huecode_pick_contrast(neutral, v["--bg"], [50, 100], 7)
        v["--text-2"] = huecode_pick_contrast(neutral, v["--bg"], [100, 200, 300], 4.5)
        v["--text-3"] = huecode_pick_contrast(neutral, v["--bg"], [200, 300, 400], 4.5)
    else:
        v.update({"--surface": "#ffffff", "--bg": neutral["50"], "--surface-2": neutral["50"],
                  "--surface-3": neutral["200"], "--border": neutral["200"], "--border-strong": neutral["300"]})
        v["--text"] = huecode_pick_contrast(neutral, v["--bg"], [900, 950], 7)
        v["--text-2"] = huecode_pick_contrast(neutral, v["--bg"], [600, 700, 800], 4.5)
        v["--text-3"] = huecode_pick_contrast(neutral, v["--bg"], [500, 600, 700], 4.5)
    candidates, target = HUECODE_TARGET["dark" if dark else "light"]
    accent = huecode_pick_lightness(primary, candidates, target)
    soft = primary["900"] if dark else primary["50"]
    v["--accent"] = accent
    v["--accent-hover"] = huecode_pick_lightness(primary, candidates, target + (12 if dark else -12))
    v["--accent-fg"] = huecode_readable(accent)
    v["--accent-soft"] = soft
    v["--accent-soft-fg"] = huecode_pick_contrast(primary, soft, [100, 200, 300] if dark else [700, 800, 900], 4.5)
    for prefix, role in HUECODE_SEMANTIC.items():
        scale = palette[role]
        base = scale["400"] if dark else scale["600"]
        v[f"--{prefix}"] = base
        v[f"--{prefix}-soft"] = scale["900"] if dark else scale["50"]
        v[f"--{prefix}-fg"] = huecode_readable(base)
    return v


def huecode(primary_hex):
    """Huecode's palette of one primary hex: its 8 shade scales and its light and dark CSS vars."""
    base = huecode_hex_to_hsl(primary_hex)
    roles = {
        "primary": base,
        "secondary": (huecode_mix_hue(base[0], base[0] - 30, 1), clamp(base[1] * 0.85, 0, 100), base[2]),
        "accent": (huecode_mix_hue(base[0], base[0] + 180, 1), clamp(base[1] * 1.1, 0, 100), base[2]),
        "neutral": (base[0], min(base[1] * 0.15, 12), clamp(50, 38, 46)),
        **{role: huecode_semantic(anchor, base) for role, anchor in HUECODE_ANCHORS.items()},
    }
    scales = {role: huecode_shade_scale(*roles[role]) for role in HUECODE_ROLES}
    return {"scales": scales, "light": huecode_css_vars(scales, False), "dark": huecode_css_vars(scales, True)}


def huecode_root(mine, theme_primary):
    """Huecode's base: the given primary (the light one first), else this theme's primary."""
    return fmt(mine.get("light") or next(iter(mine.values()))) if mine else fmt(theme_primary)


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


def mix_black(color):
    """The *-edge tokens: the fill mixed in sRGB, 80% with 20% black."""
    return tuple(int(v * 0.8 + 0.5) for v in color[:3]) + (1.0,)


def saturate(color, amount):
    """CSS saturate(): the feColorMatrix saturate matrix on the sRGB values, clamped; alpha 1.0."""
    s, (r, g, b) = amount, color[:3]
    return (clamp((0.213 + 0.787 * s) * r + (0.715 - 0.715 * s) * g + (0.072 - 0.072 * s) * b, 0, 255),
            clamp((0.213 - 0.213 * s) * r + (0.715 + 0.285 * s) * g + (0.072 - 0.072 * s) * b, 0, 255),
            clamp((0.213 - 0.213 * s) * r + (0.715 - 0.715 * s) * g + (0.072 + 0.928 * s) * b, 0, 255), 1.0)


def glass(theme, colors):
    """Glass fill: {name: (fill, failed)}; the lowest alpha at which every token of GLASS_MINIMUM meets its
    minimum on the worst point behind the glass; fill None and failed [(token, minimum, where)] when none does."""
    behind = {"canvas": colors["canvas"], **{f"{k} glow": over(colors[k][:3] + (GLASS_GLOW,), colors["canvas"])
                                             for k in ("accent", "primary")}}
    result = {}
    for name, extra in (("glass-fill", {}), ("glass-fill-strong", {"black": BLACK} if theme == "light" else {"white": WHITE})):
        points = {n: saturate(c, GLASS_SATURATE) for n, c in {**behind, **extra}.items()}

        def failing(alpha):
            glass_points = {n: over(GLASS_TINT[theme] + (alpha,), p) for n, p in points.items()}
            return [(t, m, w) for t, m in GLASS_MINIMUM.items() for r, w in [lowest(colors[t], glass_points)] if r < m]
        alpha = next((a / 100 for a in range(101) if not failing(a / 100)), None)
        result[name] = (GLASS_TINT[theme] + (alpha,), []) if alpha is not None else (None, failing(1))
    return result

SHAPES = {
    "linear": "linear-gradient(135deg, {0}, {1})",
    "radial": "radial-gradient(circle at 30% 30%, {0}, transparent 60%), radial-gradient(circle at 75% 75%, {1}, transparent 60%)",
    "mesh": ("radial-gradient(at 0% 0%, {0}, transparent 50%), radial-gradient(at 100% 0%, {1}, transparent 50%), "
             "radial-gradient(at 100% 100%, {0}, transparent 50%), radial-gradient(at 0% 100%, {1}, transparent 50%)"),
}


def page_background(base):
    """Page background: {theme: background-image} behind the glass, from the light theme's primary and accent."""
    primary, accent = base["primary"], base["accent"]
    gray = [hct(c)[1] < GRAY for c in (primary, accent)]

    def opposite(other):  # Huecode's accent of the other color, rule B at the light target
        scale = huecode(fmt(other))["scales"]["accent"]
        return parse_color(huecode_pick_lightness(scale, HUECODE_STEPS, HUECODE_TARGET["light"][1]))
    if all(gray):
        return None
    primary, accent = opposite(accent) if gray[0] else primary, opposite(primary) if gray[1] else accent
    hues = [hct(c)[0] for c in (primary, accent)]
    colors = {t: [fmt(at(h, 200, tone)) for h in hues] for t, tone in PAGE_TONE.items()}
    shape = ("linear", "radial", "mesh")[int(hues[0] // 120)]
    return {t: SHAPES[shape].format(*c) for t, c in colors.items()}


def kore_colors(root=ROOT):
    tokens = read_tokens((Path(root) / "references" / "tokens.yaml").read_text(encoding="utf-8"))
    return {theme: {key: parse_color(value) for key, entries in tokens.items()
                    for path, value in entries if path[:2] == ["colors", theme]} for theme in THEMES}


def base_colors(given, themes, kore):
    """Method step 1: {theme: {role: (color, source)}}, and the notes to tell the user."""
    base, notes = {}, []
    for theme in themes:
        i, base[theme] = THEMES.index(theme), {}
        steps, target = HUECODE_TARGET[theme]
        for role in ("primary", "canvas", "accent"):  # canvas and accent come from the primary
            own = given.get(role, {})
            if role != "primary":
                mine = given.get("primary", {})
                root = huecode_root(mine, base[theme]["primary"][0])
            if theme in own:
                color, source = own[theme], "given"
            elif role == "primary" and own:  # Huecode pick on the given primary's scale
                scale = huecode(fmt(next(iter(own.values()))))["scales"]["primary"]
                color, source = parse_color(huecode_pick_lightness(scale, steps, target)), "derived"
            elif role == "accent" and own:  # rule B on the scale of the given accent
                scale = huecode_shade_scale(*huecode_hex_to_hsl(fmt(next(iter(own.values())))))
                color, source = parse_color(huecode_pick_lightness(scale, HUECODE_STEPS, target)), "derived"
            elif not {"canvas", "primary"} & set(given):  # only an accent given: Kore's canvas and primary (How many colors)
                color, source = kore[theme][role], "Kore's value"
            elif role == "canvas":
                color, source = parse_color(huecode(root)[theme]["--bg"]), "derived"
            elif role == "accent":
                if hct(parse_color(root))[1] < GRAY or (not mine and base[theme]["primary"][1] == "Kore's value"):  # Kore's pair stays whole
                    color, source = kore[theme][role], "Kore's value"
                else:
                    scale = huecode(root)["scales"]["accent"]
                    color, source = parse_color(huecode_pick_lightness(scale, HUECODE_STEPS, target)), "derived"
            else:  # Missing colors, step 3: the primary from the given canvas
                from_role, shift, chroma = MISSING["primary"]
                start = given[from_role].get(theme) or next(iter(given[from_role].values()))
                hue, from_chroma, _ = hct(start)
                if from_chroma < GRAY:
                    color, source = kore[theme][role], "Kore's value"
                else:
                    color, source = at(hue + shift, chroma, BASE_TONE[role][i]), "derived"
            hue, chroma, tone = hct(color)
            if role == "canvas" and round(tone) in (0, 100):
                notes.append(f"{theme}: the canvas {fmt(color)} is at tone {round(tone)} and leaves no room for the "
                             f"surfaces (Pure white or black canvas): its tone moves to {BASE_TONE['canvas'][i]}.")
                color, source = at(hue, chroma, BASE_TONE["canvas"][i]), "derived"
            base[theme][role] = (color, source)
    return base, notes


def derive(theme, base, h, on_vivid, kore, dark=None):
    """Method steps 2 and 3 for one theme: {token: [color, source, (ratio, where) or None]},
    the tokens that cannot be used as (token, minimum, where), and the notes. h: huecode() of the
    theme's Huecode base (huecode_root), the source of HUECODE_MAP. dark: the dark theme's tokens
    as derive gives them, for on-vivid."""
    i = THEMES.index(theme)
    away = -1 if theme == "light" else 1  # Method step 3: down in light, up in dark
    tokens, failed, notes = {}, [], []

    def put(name, color, source="derived", measure=None, minimum=None, step=away, keep=False, scale=None):
        if minimum and not keep and measure(color)[0] < minimum:
            if scale:  # the next steps of the scale toward more contrast, the first that passes
                hexes = list(scale.values())
                at_step = hexes.index(fmt(color))
                nearer = hexes[at_step + 1:] if step < 0 else hexes[:at_step][::-1]
                moved = next((c for c in map(parse_color, nearer) if measure(c)[0] >= minimum), None)
            else:
                moved = move(color, measure, minimum, step)
            if moved is None:
                failed.append((name, minimum, measure(color)[1]))
            else:
                color, source = moved, "moved to pass Contrast"
        tokens[name] = [color, source, measure(color) if measure else None]
        return color

    def mapped(name, measure=None, minimum=None, step=away):
        source, role = HUECODE_MAP[name][i], HUECODE_MAP[name][2]
        hexa = h[theme][source] if source.startswith("--") else h["scales"][source.split()[0]][source.split()[1]]
        return put(name, parse_color(hexa), "derived", measure, minimum, step, scale=h["scales"][role] if role else None)

    put("canvas", *base["canvas"])
    for name in SURFACES[1:]:
        mapped(name)
    surfaces = {name: tokens[name][0] for name in SURFACES}

    def on_surfaces(color):
        return lowest(color, surfaces)

    mapped("hairline-medium", on_surfaces)
    ink = mapped("ink", on_surfaces, 4.5)
    body = ink[:3] + (0.86,)
    r, where = on_surfaces(body)
    if r < 4.5:  # Translucent text (Contrast): a solid color for that pair, then moved as Method step 3
        body = tuple(round(v) for v in over(body, surfaces[where]))
        notes.append(f"{theme}: body is solid in this palette: ink at 86% fails 4.5:1 on {where} (Translucent text).")
    body = put("body", body, "moved to pass Contrast" if r < 4.5 else "derived", on_surfaces, 4.5)
    # mute: the neutral step nearest the canvas that reaches 4.5:1 on every surface (Huecode's text-3 passes only on --bg)
    steps = list(h["scales"]["neutral"].values())
    mute = next((c for c in map(parse_color, steps if theme == "light" else steps[::-1]) if on_surfaces(c)[0] >= 4.5), None)
    if mute is None:
        failed.append(("mute", 4.5, on_surfaces(ink)[1]))
    else:
        put("mute", mute, measure=on_surfaces)
    strong = mapped("hairline-strong", on_surfaces, 3)
    mapped("stone", on_surfaces)
    put("hairline", ink[:3] + (0.06,), measure=on_surfaces)
    put("focus-ring", strong, measure=on_surfaces, minimum=3)
    put("surface-card-edge", mix_black(surfaces["surface-card"]), measure=on_surfaces)

    danger = put("danger", kore[theme]["danger"], "Kore's value", on_surfaces, 4.5)  # the kinds stay Kore's (user, 2026-11-18)
    for kind, color in (("primary", base["primary"][0]), ("danger", danger)):
        # whichever of white and black contrasts more reaches at least 4.58:1 (1.05 / sqrt(0.0525)) on any solid fill
        on = max((WHITE, BLACK), key=lambda c: ratio(c, color))

        def on_fill(c, kind=kind, on=on):
            return ratio(on, c), f"{kind}-on"
        if kind == "primary":  # keeps its given value; danger is measured as text above
            put(kind, *base[kind], on_fill)
        step = -1 if on == WHITE else 1  # a fill moves away from its on-color
        if kind == "primary":
            pressed = mapped("primary-pressed", on_fill, 4.5, step)
            mapped("primary-on", lambda c, b={kind: color, "primary-pressed": pressed}: lowest(c, b))
        else:
            f_hue, f_chroma, f_tone = hct(color)
            pressed = put("danger-pressed", at(f_hue, f_chroma, f_tone + (6 if hct(tokens["canvas"][0])[2] > f_tone else -6)),
                          "derived", on_fill, 4.5, step)
            put("danger-on", on, measure=lambda c, b={kind: color, "danger-pressed": pressed}: lowest(c, b))
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
    def derived(theme, *args):
        return derive(theme, base[theme], huecode(huecode_root(given.get("primary", {}), base[theme]["primary"][0])),
                      on_vivid, kore, *args)
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
        # Huecode's canvas is primary's hue at chroma ~3, below GRAY: a canvas is ordered by primary's hue
        target, source = base[row[1]]["primary" if role == "canvas" else role]
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
        usage="python3 kore_palette.py [--themes light,dark] [--given light|dark] [--canvas C] [--primary C] [--accent C] "
              "[--typology glassmorphism]",
        description="Derives the color tokens from the base colors (references/rules/custom-palette.md) "
                    "and measures them. C is one hex, for the theme --given names, or light=#hex,dark=#hex. "
                    "Then proposes the candidate of references/candidates.md for the first missing role "
                    "(Missing colors, step 2).",
        epilog="Example: python3 kore_palette.py --canvas '#F8FAFB' --primary 'light=#212121,dark=#fcfdff'")
    parser.add_argument("--themes", default="light,dark", help="the themes the project ships (default both)")
    parser.add_argument("--given", choices=THEMES, default="light", help="the theme a single hex is given for (default light)")
    for role in ROLES:
        parser.add_argument(f"--{role}", metavar="C")
    parser.add_argument("--typology", choices=["glassmorphism"], help="also print the glass fills of this typology (Glass fill)")
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
    if args.typology:
        base = tables.get("light") or next(iter(tables.values()))  # the theme's own table when light is not shipped
        page = page_background({k: base[k][0] for k in ("primary", "accent")})
    for theme, tokens in tables.items():
        print(f"{theme}\n{'token':<22} {'value':<26} {'lowest':<8} {'on':<42} source")
        for name in (n for n in kore[theme] if n in tokens):  # in the order of tokens.yaml
            color, source, measured = tokens[name]
            print(f"{name:<22} {fmt(color):<26} {show(measured)[0]:<8} {show(measured)[1]:<42} {source}")
        if args.typology:
            for name, (fill, failed) in glass(theme, {n: v[0] for n, v in tokens.items()}).items():
                print(f"{name:<22} {fmt(fill) if fill else '—':<26} {'—':<8} {'—':<42} Glass fill")
                problems += [f"{theme}: {name} cannot reach {m}:1 for {token} on the glass over {where}, even at alpha 1 "
                             "(Glass fill): ask for another color." for token, m, where in failed]
            print(f"{'page-background':<22} {page[theme]}" if page else
                  f"{'page-background':<22} — (primary and accent are gray: canvas only)")
        print()
    for line in notes + problems + propose(given, themes, kore, read_candidates()):
        print(line)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
