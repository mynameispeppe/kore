#!/usr/bin/env python3
"""Kore check: measures a project's code against the rules of Kore that a
script can measure without a browser, and with --url the rendered pages
(references/checks.md, Measure).

Usage: python3 kore_check.py <project folder> [--changed | --staged | --base <ref>] [--url <url> ...] [--shots <folder>] [--typology <name>] [--skip <path> ...]

The typology (a folder of Kore's typologies/) is --typology <name>, otherwise
the Typology: line of the project's KORE-DECISIONS.md, otherwise minimalism.

Each option reports only some files, plus the findings about the whole
project (contrast on the token file, global styles), which always read
every file. Without git it checks every file.
  --changed       files git lists as changed, staged or new (after an edit);
  --staged        files in the staging area (pre-commit). The file on disk
                  is read, so a staged file edited again is read as edited;
  --base <ref>    files changed since the branch left <ref> (a pull request).

Reads styles wherever the project writes them, through kore_readers: CSS,
SCSS, Less and PostCSS files and <style> blocks; style attributes; CSS in
template literals (styled-components, emotion, Lit, Angular); style objects
(React style and MUI sx, Vue :style, Angular [ngStyle]); Tailwind classes,
@apply and theme. Sass indented syntax and Stylus are reported as not
checked. Prints one line per finding:
  ✗ <where> · <Rule> · <severity> · <message>: a rule is broken, fix it. The severity is
    blocking, broken, visible or hidden (GLOSSARY.md, Severity); the ✗ lines come
    sorted by severity in that order, then by path and line;
  ? a rule may be broken: check it against the rule named;
  – a finding the code waives, with its reason: `kore-ignore <Rule>: <reason>`
    on the line or `kore-ignore-next-line <Rule>: <reason>` above it, in any
    comment; on a page, `data-kore-ignore="<Rule>: <reason>"` on the element
    or an ancestor. Never counted.
Exit code 1 when there is at least one ✗.

--url <url> also opens that page in a browser (kore_browser, phase 2), once
per page; it needs Playwright and an installed Chrome or Edge, and exits
with 1 when they are missing. Its findings are always shown.
--shots <folder> also saves each page, whole, at 375 and 1440px in each
theme, as <page>-<width>-<theme>.png, and lists the files; it needs --url.
--skip <path> never reads that file, written relative to the folder; repeatable.

Token definitions (blocks on :root, html, [data-theme], .dark and .light) are the source
of the values and are never reported as free values.
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from check_references import replaced_ids, tokens_for, walk
from kore_readers import Tailwind, line_of, read_attributes, read_css, read_objects, read_templates, tailwind_config

KORE = Path(__file__).resolve().parent.parent
SKIP_DIRS = {"node_modules", "dist", "build", "out", "coverage", "vendor", "target", "__pycache__"}
SOURCE_DOT_DIRS = {".storybook", ".vitepress", ".vuepress"}  # hidden folders that hold source


def skipped(folder):
    """Whether a folder of the project is never read: build output, dependencies, hidden folders (.git, .venv)."""
    return folder in SKIP_DIRS or (folder.startswith(".") and folder not in SOURCE_DOT_DIRS)
STYLE_FILES = {".css": "css", ".pcss": "css", ".postcss": "css", ".scss": "scss", ".less": "less"}
UNCHECKED_STYLES = {".sass", ".styl"}  # indented syntaxes, no braces to parse
MARKUP_FILES = {".html", ".htm", ".astro", ".vue", ".svelte"}
SCRIPT_FILES = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".mts", ".cts"}
TAILWIND_CONFIG = re.compile(r"^tailwind\.config\.[cm]?[jt]s$")

findings = []


def report(kind, path, line, rule, message):
    findings.append((kind, str(path), line, rule, message))


SEVERITY_RANK = {"blocking": 0, "broken": 1, "visible": 2, "hidden": 3}  # GLOSSARY.md, Severity
SEVERITY = {
    **dict.fromkeys(
        ["Contrast", "Accessibility", "Touch targets", "Adjacent targets", "Page language", "Typographic levels",
         "Code order", "Zoom", "Themes", "Safe areas", "Popover", "Menu", "Select"], "blocking"),
    "Decisions file": "hidden",
    **dict.fromkeys(
        ["Never invent values", "Token file", "Motion", "Typography rules", "Images", "Browser surfaces", "States",
         "Stacking order", "Spacing", "Right to left", "Extremes", "Button", "Borders inside the edge", "Usability",
         "Cards", "AI tells", "Meaning", "Copy", "Sections", "Scroll reveal", "Text hierarchy", "Scanning patterns",
         "Top bar", "The One Winner Rule", "The One Primary Rule", "The Distance Ratio Rule", "Radius by role",
         "Proximity and hierarchy", "One rest per page", "Hero", "Grouping and separation", "Grouping actions",
         "From role to style", "Equal side margins", "Content", "Breakpoints", "Blank stretches"], "visible"),
}


def severity(rule, message):
    """The severity of a ✗ (GLOSSARY.md, Severity): a message check first, then the rule's level. An unmapped rule raises KeyError."""
    if (message.startswith("the page is ") and " wide on a " in message) or message.startswith(("text cut:", "text over text:")):
        return "broken"
    # in, not endswith: the browser appends " (320 light)" to the message
    if rule == "Images" and "shows no image: point it to its file or to the placeholder" in message:
        return "broken"
    if rule == "Usability" and message.startswith("the page logs an error"):
        return "broken"
    if (rule, message) in {("Images", "an <img> without alt"),
                           ("Button", "an <a> without href (a link is an <a href>)"),
                           ("Button", 'role="link" on another element (a link is an <a href>)'),
                           ("Typography rules", "the viewport blocks zoom"),
                           ("Motion", "animations without a prefers-reduced-motion block")}:
        return "blocking"
    if rule == "States" and "is a link with the look of a button: on focus" in message:
        return "blocking"
    if rule == "Never invent values" and "(the value of " in message:
        return "hidden"
    if rule == "Token file" and ("copies a value" in message or message == "no token file defining --canvas"):
        return "hidden"
    return SEVERITY[rule]


# A finding the author waives in the code, with the reason: `kore-ignore <Rule>: <reason>` on the line, or
# `kore-ignore-next-line <Rule>: <reason>` on the line above, in any comment.
# Several rules are separated by commas; without a reason nothing is waived.
WAIVER = re.compile(r"kore-ignore(-next-line)?\s+([^:\n]+?)\s*:\s*(.+?)\s*(?:\*/|-->|\}|$)")


def waiver(root, path, line, rule, cache={}):
    """The reason the code gives for waiving this finding, or None."""
    if not line:
        return None
    if path not in cache:
        try:
            cache[path] = (root / path).read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            cache[path] = []
    lines = cache[path]
    for number, wanted in ((line, None), (line - 1, "-next-line")):
        if 0 < number <= len(lines):
            for m in WAIVER.finditer(lines[number - 1]):
                if m.group(1) == wanted and rule.lower() in [r.strip().lower() for r in m.group(2).split(",")]:
                    return m.group(3)
    return None


# ---------------------------------------------------------------- typology

def typology_line(text):
    """The typology the Typology: line of KORE-DECISIONS.md names, minimalism without the line."""
    m = re.search(r"(?m)^Typology:(.*)$", text)
    return m.group(1).strip() if m else "minimalism"


def typology_names(kore=KORE):
    """The folders of Kore's typologies/, _template left out."""
    return sorted(p.name for p in (Path(kore) / "typologies").iterdir()
                  if p.is_dir() and p.name != "_template" and not p.name.startswith("."))


def space_scale(typology, kore=KORE):
    """{px: space token} of the spacing group of Kore's tokens with the typology's."""
    return {int(value.removesuffix("px")): name for name, entries in tokens_for(kore, typology).items()
            for path, value in entries if path[0] == "spacing"}


def replaced_by(typology, kore=KORE):
    """The ids of the default rules the typology's files replace."""
    return {rid for path in walk(Path(kore), f"typologies/{typology}/**/*.md")
            for rid in replaced_ids(path.read_text(encoding="utf-8"))}


# ---------------------------------------------------------------- reading

NOT_CHECKED = "Sass or Stylus syntax not checked: measure by hand"


def project_files(root, skip=()):
    inside = []
    for path in sorted(root.rglob("*")):
        if any(skipped(part) for part in path.relative_to(root).parts[:-1]) or not path.is_file():
            continue
        if ".min." in path.name or path.name.endswith(".d.ts") or relative(path, root) in skip:
            continue
        inside.append(path)
        yield path
    # Local stylesheets the pages link from outside the folder (a token file shared by two sites)
    linked = set()
    for page in inside:
        if page.suffix.lower() not in MARKUP_FILES:
            continue
        for href in re.findall(r"""<link\b[^>]*\brel=["']?stylesheet[^>]*\bhref=["']([^"'#?]+)""", page.read_text(errors="replace"), re.I):
            if "//" in href or href.startswith("/"):
                continue
            css = (page.parent / href).resolve()
            if css.is_file() and not css.is_relative_to(root.resolve()):
                linked.add(css)
    yield from sorted(linked)


def relative(path, root):
    return Path(os.path.relpath(path, root))


def read_source(path, rel, text):
    """Rules and the text the whole-project checks search, from one file;
    None for a file that holds no styles."""
    suffix = path.suffix.lower()
    if suffix in STYLE_FILES:
        return read_css(text, STYLE_FILES[suffix])
    if suffix in UNCHECKED_STYLES:
        report("?", rel, 0, "Building anything", NOT_CHECKED)
        return [], ""
    if suffix not in MARKUP_FILES | SCRIPT_FILES:
        return None
    rules, clean = read_templates(text)
    if suffix in MARKUP_FILES:
        for m in re.finditer(r"<style([^>]*)>(.*?)</style>", text, re.S | re.I):
            lang = re.search(r"\blang\s*=\s*[\"']?(\w+)", m.group(1))
            dialect = lang.group(1).lower() if lang else "css"
            if dialect in ("sass", "stylus", "styl"):
                report("?", rel, line_of(text, m.start()), "Building anything", NOT_CHECKED)
                continue
            found, css = read_css(m.group(2), dialect, line_of(text, m.start(2)) - 1)
            rules, clean = rules + found, clean + css
    return rules + read_attributes(text) + read_objects(text), clean


def as_text(rules):
    """Rules written back as CSS, for the checks that search the whole project."""
    return "\n".join(" ".join(chain) + " {" + "; ".join(f"{p}: {v}" for p, v, *_ in decls) + "}"
                     for chain, decls in rules)


def is_token_block(chain, decls):
    """A block on :root, html, a theme attribute or a theme class that mostly defines custom properties."""
    if not re.search(r":root|\bhtml\b|data-theme|\.(?:dark|light)\b", chain[-1]) or not decls:
        return False
    return sum(p.startswith("--") for p, *_ in decls) * 2 >= len(decls)


# ---------------------------------------------------------------- tokens

def read_tokens(rules):
    """Light and dark token values from the token blocks."""
    light, dark = {}, {}
    for chain, decls in rules:
        if not is_token_block(chain, decls):
            continue
        context = " ".join(chain)
        target = dark if re.search(r"dark", context) else light
        for prop, value, *_ in decls:
            if prop.startswith("--"):
                target[prop] = value
    return light, {**light, **dark}


def read_themes(token_path, rules):
    """The themes the token file defines, from the color-scheme of each block
    that defines --canvas (Token file, Themes): {"light" | "dark": None when
    the system preference shows it, or the selector to set on <html>}. Both
    themes, with a finding, when a block declares no color-scheme."""
    themes = {}
    for chain, decls in rules:
        canvas = next((line for p, _, line, *_ in decls if p == "--canvas"), None)
        if canvas is None or not is_token_block(chain, decls):
            continue
        scheme = next((v for p, v, *_ in decls if p == "color-scheme"), "")
        if scheme not in ("light", "dark"):
            report("✗", token_path, canvas, "Token file", "a theme block declares color-scheme: light or dark")
            return {"light": None, "dark": None}
        selector = re.sub(r"^\s*(:root|html)", "", chain[-1].split(",")[0]).strip()
        if any("prefers-color-scheme" in s for s in chain) or not selector:
            themes[scheme] = None
        else:
            themes.setdefault(scheme, selector)
    return themes or {"light": None, "dark": None}


def resolve(value, tokens, depth=0):
    if depth > 10:
        return value
    return re.sub(r"var\((--[\w-]+)(?:,[^)]*)?\)",
                  lambda m: resolve(tokens.get(m.group(1), m.group(0)), tokens, depth + 1), value)


def parse_color(value):
    value = value.strip().lower()
    m = re.fullmatch(r"#([0-9a-f]{3,8})", value)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(ch * 2 for ch in h)
        r, g, b = (int(h[k:k + 2], 16) for k in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return r, g, b, a
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", value)
    if m:
        a = m.group(4)
        alpha = 1.0 if a is None else (float(a[:-1]) / 100 if a.endswith("%") else float(a))
        return float(m.group(1)), float(m.group(2)), float(m.group(3)), alpha
    return None


def over(fg, bg):
    a = fg[3]
    return tuple(fg[k] * a + bg[k] * (1 - a) for k in range(3)) + (1.0,)


def luminance(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])


def ratio(fg, bg):
    l1, l2 = sorted((luminance(fg), luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


# The pairs Contrast in references/rules/color.md sets, on the surfaces they may sit on.
TEXT = ["--ink", "--body", "--mute", "--link"]
STROKE = ["--hairline-strong", "--focus-ring"]
SURFACES = ["--canvas", "--surface-card", "--surface-elevated", "--surface-float", "--surface-hover"]
FILLS = [("--primary-on", "--primary"), ("--danger-on", "--danger"), ("--primary-on", "--primary-pressed"), ("--danger-on", "--danger-pressed")]


def check_contrast(token_path, light, dark, themes):
    for theme, tokens in (("light", light), ("dark", dark)):
        if theme not in themes:
            continue
        if len(themes) == 1:
            tokens = dark  # one block, wherever it is written: the dark values fall back on it
        def color(name):
            return parse_color(resolve(tokens.get(name, ""), tokens)) if name in tokens else None
        for names, minimum in ((TEXT, 4.5), (STROKE, 3.0)):
            for fg_name in names:
                for bg_name in SURFACES:
                    fg, bg = color(fg_name), color(bg_name)
                    if not fg or not bg:
                        continue
                    r = ratio(over(fg, bg), bg)
                    if r < minimum:
                        report("✗", token_path, 0, "Contrast",
                               f"{theme}: {fg_name[2:]} on {bg_name[2:]} is {r:.2f}:1, below {minimum}:1")
        for fg_name, bg_name in FILLS:
            fg, bg = color(fg_name), color(bg_name)
            if fg and bg:
                r = ratio(over(fg, bg), bg)
                if r < 4.5:
                    report("✗", token_path, 0, "Contrast", f"{theme}: {fg_name[2:]} on {bg_name[2:]} is {r:.2f}:1, below 4.5:1")


# ---------------------------------------------------------------- declarations

FREE_COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch|oklab|lab|lch)\(")
LENGTH = re.compile(r"(?<![\w.-])(-?\d*\.?\d+)(px|rem|em)\b")
DURATION = re.compile(r"(?<![\w.-])\d*\.?\d+m?s\b")
LAYOUT_PROPS = r"\b(width|height|top|left|right|bottom|margin[\w-]*|padding[\w-]*|inset[\w-]*|max-width|max-height|min-width|min-height|(?:min-|max-)?(?:inline|block)-size)\b"
PHYSICAL = {"margin-left", "margin-right", "padding-left", "padding-right", "left", "right",
            "border-left", "border-right", "border-left-width", "border-right-width",
            "border-left-color", "border-right-color"}
INTERACTIVE = re.compile(r"\b(button|a|input|select|textarea|summary|label|option)\b|:hover|:active|:focus|\[role=|\[href|\.btn|click|link|toggle|tab\b|checkbox|radio|switch|chip|slider|thumb|stepper")


SPACING = re.compile(r"^(margin|padding|gap|row-gap|column-gap|inset|top|right|bottom|left|scroll-padding|scroll-margin)")
OFFSETS = re.compile(r"^(inset|top|right|bottom|left)")
SIZES = re.compile(r"^(width|height|min-width|min-height|max-width|max-height|(min-|max-)?(inline|block)-size|flex|grid-template|grid-auto)")
LINE_PROPS = re.compile(r"^(text-decoration|text-underline-offset|outline|outline-offset|border|box-shadow|stroke)")


def px_of(number, unit):
    return number * 16 if unit in ("rem", "em") else number


def token_lengths(light):
    """{"size" | "radius": {px: token name}} of the tokens whose value is one length, spacing and type roles left out."""
    out = {"size": {}, "radius": {}}
    for name, value in light.items():
        m = re.fullmatch(r"(\d*\.?\d+)(px|rem)", value.strip())
        if m and not re.match(r"--space-|.*-(fontSize|lineHeight|letterSpacing)$", name):
            out["radius" if name.startswith("--rounded-") else "size"].setdefault(px_of(float(m.group(1)), m.group(2)), name)
    return out


def check_lengths(path, line, prop, value, bare, what, selector, lengths={"size": {}, "radius": {}},
                  scale=space_scale("minimalism")):
    """Spacing only from the space tokens (scale, {px: token}); element sizes and radii a token's value written as its token."""
    if prop in ("transform", "translate"):
        return  # motion distances, set by a component's file (a card's lift)
    for m in LENGTH.finditer(bare):
        number, unit = float(m.group(1)), m.group(2)
        px = abs(px_of(number, unit))
        if px == 0:
            continue
        if LINE_PROPS.match(prop) and px <= 4:
            continue  # 1px borders and outlines, the 2px link focus underline at 4px (States)
        if number < 0 and OFFSETS.match(prop) and "::" in selector:
            continue  # a pseudo-element grown past its element: hit area (Touch targets) or focus ring
        if SPACING.match(prop):
            if px in scale:
                hint = f", the value of {scale[px]}"
            else:  # the tokens on either side, so the fix comes from the scale
                near = [v for v in (max((s for s in scale if s < px), default=None),
                                    min((s for s in scale if s > px), default=None)) if v]
                hint = ": nearest " + " or ".join(f"{scale[v]} ({v}px)" for v in near)
            report("✗", path, line, "Spacing", f"{what} ({m.group(0)} instead of a space token{hint})")
        elif SIZES.match(prop):
            if name := lengths["size"].get(px):
                report("✗", path, line, "Never invent values", f"{what} (the value of {name}: use var({name}))")
            elif px % 4 and px != 1:
                report("?", path, line, "Spacing", f"{what} ({m.group(0)} is off the 4px grid: is it set by a component's file?)")
        elif prop.startswith("border") and "radius" in prop:
            if name := lengths["radius"].get(px):
                report("✗", path, line, "Never invent values", f"{what} (the value of {name}: use var({name}))")
            else:
                report("?", path, line, "Shapes", f"{what} ({m.group(0)} is not on the rounded scale: computed by The Concentric Rule?)")
        elif "filter" in prop:
            report("?", path, line, "Shadows", f"{what} (glass and blur only where a component's file prescribes them)")
        elif prop in ("font", "font-size", "line-height", "letter-spacing"):
            report("✗", path, line, "Typography rules", f"{what} (use the type role's variables)")
        else:
            report("✗", path, line, "Never invent values", f"{what} ({m.group(0)} outside the tokens)")
        return


COLOR_LITERAL = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch|oklab|lab|lch)\([^)]*\)")


def token_colors(light, dark):
    """Each color value of the token file: the token's name, and whether only the dark theme holds it."""
    colors = {}
    for theme, tokens in (("dark", dark), ("light", light)):
        for name, value in tokens.items():
            c = parse_color(resolve(value, tokens))
            if c:
                colors[c] = (name, theme == "dark")  # the light pass overwrites shared values
    return colors


def check_color(path, line, bare, what, colors):
    for m in COLOR_LITERAL.finditer(bare):
        c = parse_color(m.group(0))
        if c not in colors:
            report("✗", path, line, "Never invent values", f"{what} (a color outside the tokens)")
        elif colors[c][1]:
            report("?", path, line, "Never invent values",
                   f"{what} (the dark value of {colors[c][0]}: var() unless it stays the same in both themes)")
        else:
            report("✗", path, line, "Never invent values", f"{what} (the value of {colors[c][0]}: use var({colors[c][0]}))")


def casts_shadow(value):
    """A shadow token or a layer with blur; layers without blur are 1px hairlines
    drawn inside (Borders inside the edge) and rings."""
    if "--shadow" in value:
        return True
    for layer in re.split(r",(?![^(]*\))", re.sub(r"var\([^)]*\)", "", value)):
        lengths = re.findall(r"-?\d*\.?\d+(?:px|rem|em)?(?=\s|$)", layer.replace("inset", "").strip())
        if len(lengths) >= 3 and float(re.sub(r"[a-z]+$", "", lengths[2])) != 0:
            return True
    return False


def check_declarations(path, rules, colors, lengths, scale, replaced):
    in_keyframes = lambda chain: any(s.lstrip().startswith("@keyframes") for s in chain)
    for chain, decls in rules:
        if is_token_block(chain, decls):
            continue
        selector = chain[-1]
        theme = any(s.startswith("@theme") for s in chain)
        for prop, value, line, label in decls:
            what = label or f"{prop}: {value}"  # a Tailwind class names itself
            if prop.startswith("--"):
                if theme and not value.startswith("var(") and value != "initial" and not prop.startswith("--breakpoint-"):
                    report("✗", path, line, "Token file", f"{prop}: {value} in @theme copies a value (map it to Kore's token with var())")
                continue
            if prop.startswith("@"):
                continue
            bare = re.sub(r"var\([^)]*\)", "", value)
            if FREE_COLOR.search(bare) and not prop.startswith(("mask", "-webkit-mask")):
                check_color(path, line, bare, what, colors)
            check_lengths(path, line, prop, value, bare, what, selector, lengths, scale)
            if re.search(r"transition|animation", prop):
                bare = ",".join(part for part in bare.split(",")
                                if not re.search(r"(?<![\w.-])0m?s\b", part))  # instant switches (visibility 0s)
                if DURATION.search(bare):
                    report("✗", path, line, "Never invent values", f"{what} (a duration outside the motion tokens)")
                if "cubic-bezier" in bare or re.search(r"\b(ease(-in|-out|-in-out)?|linear)\b", bare):
                    report("✗", path, line, "Never invent values", f"{what} (an easing outside the motion tokens)")
                if re.search(r"transition", prop) and re.search(LAYOUT_PROPS + r"|\ball\b", value):
                    report("✗", path, line, "Motion", f"{what} (only transform and opacity animate)")
            if in_keyframes(chain) and re.fullmatch(LAYOUT_PROPS, prop):
                report("✗", path, line, "Motion", f"@keyframes changes {prop} (only transform and opacity animate)")
            if prop == "z-index" and re.fullmatch(r"-?\d+", value) and value not in ("0",):
                report("✗", path, line, "Stacking order", f"{what} (use the zIndex tokens)")
            if prop == "font-weight" and re.fullmatch(r"\d+", value) and value not in ("400", "500"):
                report("✗", path, line, "Typography rules", f"{what} (only 400 and 500, or 600 as --fontWeight-strong)")
            if prop in PHYSICAL or (prop in ("text-align", "float") and value in ("left", "right")):
                report("✗", path, line, "Right to left", f"{what} (use logical properties)")
            if re.search(r"(?<![dsl])\b\d+vh\b", value):
                report("✗", path, line, "Extremes", f"{what} (use dvh, never vh)")
            if prop == "text-transform" and value == "uppercase" and re.search(r"\bbutton\b|\.btn\b", selector):
                report("✗", path, line, "Button", f"{what} on {selector} (a label keeps the case it is written in)")
            if prop == "forced-color-adjust" and value == "none":
                report("✗", path, line, "Themes", f"{what} blocks forced colors")
            if prop == "box-shadow" and casts_shadow(value) and not INTERACTIVE.search(" ".join(chain)) \
                    and "elevation.the-hairline-rule" not in replaced:
                report("?", path, line, "The Hairline Rule", f"{label + ' on ' + chain[0] if label else selector} has a shadow: is it clickable?")
            if re.fullmatch(r"border(-(top|right|bottom|left|inline-start|inline-end))?(-width)?", prop):
                m = re.search(r"(\d+)px", value)
                if m and int(m.group(1)) > 1:
                    report("✗", path, line, "Borders inside the edge", f"{what} (borders are 1px)")


def check_globals(all_css, has_interactive):
    if has_interactive and "-webkit-tap-highlight-color" not in all_css:
        report("✗", "project", 0, "States", "no -webkit-tap-highlight-color: transparent")
    if "::selection" not in all_css:
        report("✗", "project", 0, "Browser surfaces", "no ::selection style")
    if "caret-color" not in all_css:
        report("✗", "project", 0, "Browser surfaces", "no caret-color")
    if "prefers-reduced-motion" not in all_css and re.search(r"transition|animation", all_css):
        report("✗", "project", 0, "Motion", "animations without a prefers-reduced-motion block")


# ---------------------------------------------------------------- markup

def check_markup(path, text, insets):
    """insets: whether the project uses env(safe-area-inset-*), which reads 0 without viewport-fit=cover (Safe areas)."""
    for m in re.finditer(r"<meta[^>]+name=[\"']viewport[\"'][^>]*>", text, re.I):
        tag = m.group(0)
        if re.search(r"user-scalable\s*=\s*(no|0)|maximum-scale\s*=\s*1(\.0)?\b", tag):
            report("✗", path, line_of(text, m.start()), "Typography rules", "the viewport blocks zoom")
        if insets and "viewport-fit=cover" not in tag:
            report("✗", path, line_of(text, m.start()), "Safe areas", "the viewport has no viewport-fit=cover")
        if not insets and "viewport-fit=cover" in tag:
            report("✗", path, line_of(text, m.start()), "Safe areas",
                   "viewport-fit=cover without env(safe-area-inset-*): content runs under the notch")
    for m in re.finditer(r"<img\b[^>]*>", text, re.I):
        tag, line = m.group(0), line_of(text, m.start())
        if not re.search(r"\balt\s*=", tag):
            report("✗", path, line, "Images", "an <img> without alt")
        if not (re.search(r"\bwidth\s*=", tag) and re.search(r"\bheight\s*=", tag)):
            report("✗", path, line, "Images", "an <img> without width and height")
    for m in re.finditer(r"<a(?=[\s>])(?![^>]*(\bhref\b|\{\.\.\.|v-bind|routerLink))[^>]*>", text):
        report("✗", path, line_of(text, m.start()), "Button", "an <a> without href (a link is an <a href>)")
    for m in re.finditer(r"<(?!a\b)\w+\b[^>]*\brole\s*=\s*[\"']link[\"']", text, re.I):
        report("✗", path, line_of(text, m.start()), "Button", 'role="link" on another element (a link is an <a href>)')
    for m in re.finditer(r"<\w+\b[^>]*\bdata-kore-sample\b[^>]*>([^<]*)", text, re.I):
        sample = m.group(1).strip()
        report("?", path, line_of(text, m.start()), "Building anything",
               f"sample value{f' ({sample[:30]})' if sample else ''}: replace it with the real one before publishing")
    for m in re.finditer(r"onpaste\s*=\s*[\"'][^\"']*(return false|preventDefault)", text, re.I):
        report("✗", path, line_of(text, m.start()), "Usability", "paste is blocked")


# ---------------------------------------------------------------- changed files

def git_files(root, mode, base=None):
    """Paths relative to root that git lists for the mode; None without git."""
    def git(*args):
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    try:
        top = git("rev-parse", "--show-toplevel")
    except FileNotFoundError:
        return None
    if top.returncode:
        return None
    if mode == "changed":
        names, skip = [], False
        for entry in git("status", "--porcelain=v1", "-z", "--untracked-files=all").stdout.split("\0"):
            if not skip and len(entry) > 3:
                names.append(entry[3:])
            skip = not skip and len(entry) > 3 and entry[0] in "RC"  # the next entry is the old name
    else:
        diff = ["--cached"] if mode == "staged" else [f"{base}...HEAD"]
        result = git("diff", "--name-only", "-z", "--diff-filter=ACMR", *diff)
        if result.returncode:
            sys.exit(f"kore_check: git diff failed: {result.stderr.strip()}")
        names = [n for n in result.stdout.split("\0") if n]
    files = set()
    for name in names:
        path = Path(top.stdout.strip()) / name
        if path.is_file():
            try:
                files.add(str(path.resolve().relative_to(root.resolve())))
            except ValueError:
                pass  # outside the project folder
    return files


# ---------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(
        usage="python3 kore_check.py <project folder> [--changed | --staged | --base <ref>] [--url <url> ...] [--shots <folder>] [--typology <name>] [--skip <path> ...]")
    parser.add_argument("folder")
    only = parser.add_mutually_exclusive_group()
    only.add_argument("--changed", action="store_true")
    only.add_argument("--staged", action="store_true")
    only.add_argument("--base", metavar="ref")
    parser.add_argument("--url", action="append", default=[])
    parser.add_argument("--shots", metavar="folder", type=Path)
    parser.add_argument("--typology", metavar="name")
    parser.add_argument("--skip", metavar="path", action="append", default=[])
    args = parser.parse_args()
    if args.shots and not args.url:
        parser.error("--shots needs --url")
    root = Path(args.folder)
    if not root.is_dir():
        parser.error(f"{root} is not a folder")
    for path in args.skip:
        if ".." in relative(root / path, root).parts or not (root / path).is_file():
            parser.error(f"--skip {path}: no such file in {root}")
    skip = {relative(root / path, root) for path in args.skip}
    decisions = root / "KORE-DECISIONS.md"
    from kore_hierarchy import names_file, needs_table, tables, type_rows, validate  # lazy: kore_hierarchy imports kore_check
    if decisions.is_file():
        for error in validate(decisions.read_text(encoding="utf-8")):
            report("✗", "KORE-DECISIONS.md", 0, "Decisions file", error)
    typology = args.typology or typology_line(decisions.read_text(encoding="utf-8") if decisions.is_file() else "")
    if typology not in typology_names():
        parser.error(f"typology {typology}: no folder typologies/{typology}")
    scale, replaced = space_scale(typology), replaced_by(typology)
    sources, theme_names, uses_tailwind = [], set(), False
    for path in project_files(root, skip):
        rel, text = relative(path, root), path.read_text(errors="replace")
        if TAILWIND_CONFIG.match(path.name):
            uses_tailwind = True
            keys, copies = tailwind_config(text)
            theme_names |= keys
            for line, literal in copies:
                report("✗", rel, line, "Token file", f"'{literal}' copies a value (map it to Kore's token with var())")
            continue
        if path.name == "package.json" and '"tailwindcss"' in text:
            uses_tailwind = True
        read = read_source(path, rel, text)
        if read is None:
            continue
        rules, clean = read
        sources.append((path, rel, text, rules, clean))
        for chain, decls in rules:
            if any(s.startswith("@theme") for s in chain):
                theme_names |= {p for p, *_ in decls if p.startswith("--")}
        if re.search(r"""@import\s+(url\()?["']tailwindcss|@tailwind\b|@theme\b""", clean):
            uses_tailwind = True

    named = tables(decisions.read_text(encoding="utf-8") if decisions.is_file() else "")
    for path, rel, text, rules, clean in sources:
        if needs_table(path, text) and not names_file(named, rel.as_posix()):
            report("✗", rel, 1, "Decisions file", "no table in KORE-DECISIONS.md names this file: write its Order of decisions")
    all_css, light, dark, token_path, has_interactive = "", {}, {}, None, False
    themes = {"light": None, "dark": None}
    for path, rel, text, rules, clean in sources:
        l, d = read_tokens(rules)
        if "--canvas" in l and token_path is None:
            light, dark, token_path = l, d, path
            themes = read_themes(rel, rules)
    space = {}
    for name, value in light.items():
        m = re.fullmatch(r"(\d*\.?\d+)(px|rem)", value)
        if name.startswith("--space-") and m:
            space[px_of(float(m.group(1)), m.group(2))] = name
    tailwind = Tailwind(theme_names, space) if uses_tailwind else None
    colors, lengths = token_colors(light, dark), token_lengths(light)
    insets = any("safe-area-inset" in text for _, _, text, _, _ in sources)
    for path, rel, text, rules, clean in sources:
        if tailwind:
            rules = tailwind.expand_apply(rules)
            if path.suffix.lower() in MARKUP_FILES | SCRIPT_FILES:
                rules += tailwind.read_classes(text)
        all_css += clean + "\n" + as_text(rules)
        check_declarations(rel, rules, colors, lengths, scale, replaced)
        if path.suffix.lower() in MARKUP_FILES | {".jsx", ".tsx"}:
            if re.search(r"<(button|a|input|select|textarea)\b", text, re.I):
                has_interactive = True
            check_markup(rel, text, insets)
    if token_path:
        check_contrast(relative(token_path, root), light, dark, themes)
    else:
        report("✗", "project", 0, "Token file", "no token file defining --canvas")
    check_globals(all_css, has_interactive)
    browser_ran, saved = True, []
    if args.url:
        import kore_browser
        product = root / "PRODUCT.md"  # its Mode: Site or App (references/start/product-file.md)
        site = re.search(r"\bMode:\s*(Site|App)\b", product.read_text(encoding="utf-8"), re.I) if product.is_file() else None
        saved = kore_browser.check(args.url, report, themes, args.shots,
                                   type_rows(decisions.read_text(encoding="utf-8") if decisions.is_file() else ""),
                                   site and site.group(1).lower())
        browser_ran = saved is not None

    shown = findings
    mode = "changed" if args.changed else "staged" if args.staged else "base" if args.base else None
    if mode:
        files = git_files(root, mode, args.base)
        if files is None:
            print("Not a git repository: checking every file.")
        else:
            print(f"{len(files)} files from --{mode}; contrast and whole-project checks read every file.")
            shown = [f for f in findings if f[1] == "project" or f[3] == "Contrast" or f[1] in files or f[1] in args.url]
    waived = []
    for f in shown:
        reason = waiver(root, f[1], f[2], f[3]) if f[0] != "ignored" else f[4]
        if reason:
            waived.append((f, reason))
    shown = [f for f in shown if f not in {w[0] for w in waived}]
    levels = {id(f): severity(f[3], f[4]) if f[0] == "✗" else None for f in shown}
    for f in sorted(shown, key=lambda f: (f[0] != "✗", SEVERITY_RANK.get(levels[id(f)], 0), f[1], f[2])):
        kind, path, line, rule, message = f
        where = f"{path}:{line}" if line else path
        print(f"{kind} {where} · {rule} · " + (f"{levels[id(f)]} · " if kind == "✗" else "") + message)
    for (kind, path, line, rule, message), reason in waived:
        where = f"{path}:{line}" if line else path
        print(f"– {where} · {rule} · ignored: {reason}")
    for path in sorted(skip):
        print(f"– {path} · skipped (--skip)")
    errors = sum(1 for f in shown if f[0] == "✗")
    print(f"\n{errors} ✗, {len(shown) - errors} ?" + (f", {len(waived)} ignored" if waived else ""))
    if saved:
        print("Screenshots, to read once each:\n" + "\n".join(f"  {path}" for path in saved))
    if not browser_ran:
        print("The pages were not checked in a browser.")
    sys.exit(1 if errors or not browser_ran else 0)


if __name__ == "__main__":
    main()
