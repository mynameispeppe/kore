"""Readers for kore_check: each one turns a way of writing styles into the
same rules, (selector chain, [(property, value, line, label)]), so one set
of checks in kore_check measures them all. The label, when set, names what
the author wrote (a Tailwind class) in place of "property: value".

  read_css         CSS, SCSS, Less and PostCSS: files, <style> blocks;
  read_attributes  style="…", Svelte style:prop, Angular [style.prop];
  read_templates   styled.x`…`, css`…`, createGlobalStyle, keyframes,
                   Angular styles: [`…`];
  read_objects     style={{…}} and sx={{…}} in JSX, Vue :style,
                   Angular [ngStyle];
  Tailwind         classes and @apply, translated to the declaration
                   Tailwind generates, with the theme's names.
"""
import re

QUOTES = "\"'`"
OPENERS = {"{": "}", "[": "]", "(": ")"}


def line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def blank(text):
    """Spaces in place of text, newlines kept, so offsets and lines hold."""
    return re.sub(r"[^\n]", " ", text)


def tag_at(text, offset):
    """The element whose opening tag holds the offset, as a selector."""
    m = re.match(r"<([A-Za-z][\w.-]*)", text[text.rfind("<", 0, offset):])
    return m.group(1).lower() if m else "element"


# ---------------------------------------------------------------- scanning JS

def string_end(text, i):
    """Index after the string, or template literal, opening at i."""
    quote, j = text[i], i + 1
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if quote == "`" and text.startswith("${", j):
            j = closing(text, j + 1) + 1
            continue
        if c == quote or (c == "\n" and quote != "`"):
            return j + 1
        j += 1
    return len(text)


def closing(text, i):
    """Index of the bracket closing the one at i, skipping strings."""
    depth, j = 0, i
    while j < len(text):
        c = text[j]
        if c in QUOTES:
            j = string_end(text, j)
            continue
        if c in OPENERS:
            depth += 1
        elif c in "}])":
            depth -= 1
            if depth == 0:
                return j
        j += 1
    return len(text) - 1


def without_interpolations(body):
    """A template literal's body with every ${…} blanked."""
    out, j = list(body), 0
    while (j := body.find("${", j)) != -1:
        end = closing(body, j + 1)
        out[j:end + 1] = blank(body[j:end + 1])
        j = end + 1
    return "".join(out)


def string_literals(text, start, end):
    """(offset, content) of every string between start and end."""
    i = start
    while i < end:
        if text[i] in QUOTES:
            stop = string_end(text, i)
            body = text[i + 1:stop - 1]
            yield i + 1, without_interpolations(body) if text[i] == "`" else body
            i = stop
        else:
            i += 1


def entries(text, open_i, close_i):
    """(start, end) of each comma-separated item inside a bracket pair."""
    i = start = open_i + 1
    while i < close_i:
        c = text[i]
        if c in QUOTES:
            i = string_end(text, i)
            continue
        if c in OPENERS:
            i = closing(text, i) + 1
            continue
        if c == ",":
            yield start, i
            start = i + 1
        i += 1
    if text[start:close_i].strip():
        yield start, close_i


# ---------------------------------------------------------------- CSS with braces

def read_css(css, dialect="css", line_offset=0):
    """Rules and the text without comments, from CSS, SCSS, Less or PostCSS."""
    css = re.sub(r"/\*.*?\*/", lambda m: blank(m.group(0)), css, flags=re.S)
    if dialect in ("scss", "less"):
        css = re.sub(r"(?:^|(?<=[\s;{}]))//[^\n]*", lambda m: blank(m.group(0)), css, flags=re.M)
        css = re.sub(r"[#@]\{[^{}]*\}", lambda m: blank(m.group(0)), css)  # #{$x} in SCSS, @{x} in Less
    line = lambda pos: line_offset + line_of(css, pos)
    rules, stack, start = [], [], 0
    for i, c in enumerate(css):
        if c == "{":
            stack.append((css[start:i].strip(), i + 1, start, []))
            start = i + 1
        elif c == "}":
            if stack:
                selector, body_start, head_start, children = stack.pop()
                if stack:
                    stack[-1][3].append((head_start, i + 1))
                body = list(css[body_start:i])
                for a, b in children:  # nested blocks, selector included, so only direct declarations remain
                    body[a - body_start:b - body_start] = " " * (b - a)
                body = "".join(body)
                decls = []
                for m in re.finditer(r"([$@]?[-\w]+)\s*:\s*([^;]+)", body):
                    prop = m.group(1)  # custom properties are case-sensitive
                    if prop[0] in "$@":
                        continue  # a Sass or Less variable, like a custom property
                    decls.append((prop if prop.startswith("--") else prop.lower(), m.group(2).strip(),
                                  line(body_start + m.start()), None))
                for m in re.finditer(r"@apply\s+([^;]+)", body):
                    decls.append(("@apply", m.group(1).strip(), line(body_start + m.start()), None))
                rules.append(([s for s, *_ in stack] + [selector], decls))
            start = i + 1
        elif c == ";":
            start = i + 1
    return rules, css


def wrapped(selector, text, start, end, dialect="css"):
    """Rules from declarations between start and end, under one selector."""
    rules, _ = read_css(selector + "{" + text[start:end] + "}", dialect, line_of(text, start) - 1)
    return rules


# ---------------------------------------------------------------- attributes

STYLE_ATTR = re.compile(r"""(?<![\w:.\[-])style\s*=\s*(?:"([^"]*)"|'([^']*)')""")
SVELTE_STYLE = re.compile(r"""(?<![\w-])style:([\w-]+)(?:\|important)?\s*=\s*(?:"([^"]*)"|'([^']*)'|\{\s*(["'])([^"'{}]*)\4\s*\})""")
ANGULAR_STYLE = re.compile(r"""\[style\.([-\w]+)(?:\.([a-z]+|%))?\]\s*=\s*"([^"]*)\"""")


def read_attributes(text):
    """style="…" in any template, Svelte style:prop and Angular [style.prop]."""
    rules = []
    for m in STYLE_ATTR.finditer(text):
        g = 1 if m.group(1) is not None else 2
        start, end = m.start(g), m.end(g)
        values = r"\$?\{[^{}]*\}"  # {x}, {{x}}, ${x}: values filled in by the template
        body = text[:start] + re.sub(values, lambda b: blank(b.group(0)),
                                     re.sub(values, lambda b: blank(b.group(0)), text[start:end]))
        rules += wrapped(tag_at(text, m.start()), body, start, end)
    for m in SVELTE_STYLE.finditer(text):
        value = next((v for v in (m.group(2), m.group(3), m.group(5)) if v is not None), "")
        if "{" not in value:
            rules.append(([tag_at(text, m.start())], [(m.group(1), value.strip(), line_of(text, m.start()), None)]))
    for m in ANGULAR_STYLE.finditer(text):
        prop, unit, expr = m.group(1), m.group(2), m.group(3).strip()
        if re.fullmatch(r"'[^']*'", expr):
            value = expr[1:-1]
        elif unit and re.fullmatch(r"-?\d*\.?\d+", expr):
            value = expr + unit
        else:
            continue  # a variable: its value is not in the file
        rules.append(([tag_at(text, m.start())], [(prop, value, line_of(text, m.start()), None)]))
    return rules


# ---------------------------------------------------------------- template literals

TAGGED = re.compile(
    r"(?<![\w$.])(styled(?:\.[\w$]+|\s*\((?:[^()]|\([^()]*\))*\))"
    r"(?:\s*\.\s*(?:attrs|withConfig)\s*\((?:[^()]|\([^()]*\))*\))*"
    r"|css|createGlobalStyle|injectGlobal|keyframes)\s*(?:<[^`<>]*(?:<[^`<>]*>[^`<>]*)*>)?\s*`")
ANGULAR_STYLES = re.compile(r"(?<![\w$.])styles\s*:\s*(?=[\[`])")


def read_templates(text):
    """Rules and text from CSS written in template literals."""
    rules, clean = [], ""
    sources = []
    for m in TAGGED.finditer(text):
        tag = re.sub(r"\s+", "", m.group(1)).lower()
        selector = "@keyframes" if tag == "keyframes" else None if tag in ("createglobalstyle", "injectglobal") else tag
        sources.append((m.end() - 1, selector))
    for m in ANGULAR_STYLES.finditer(text):
        if text[m.end()] == "`":
            sources.append((m.end(), None))
        else:
            for offset, _ in string_literals(text, m.end(), closing(text, m.end())):
                if text[offset - 1] == "`":
                    sources.append((offset - 1, None))
    for tick, selector in sources:
        body = without_interpolations(text[tick + 1:string_end(text, tick) - 1])
        source = selector + "{" + body + "}" if selector else body  # the selector sits on the body's first line
        found, css = read_css(source, "scss", line_of(text, tick + 1) - 1)
        rules += found
        clean += css + "\n"
    return rules, clean


# ---------------------------------------------------------------- object styles

JSX_OBJECT = re.compile(r"(?<![\w$.-])(style|sx)\s*=\s*\{")
BOUND_OBJECT = re.compile(r"""(?<![\w-])((?::|v-bind:)style|\[ngStyle\])\s*=\s*\"""")
SELECTOR_KEY = re.compile(r"[&:@.#>\[\s*+~]")
SX_SHORTHANDS = {"m": "margin", "mt": "margin-top", "mr": "margin-right", "mb": "margin-bottom",
                 "ml": "margin-left", "mx": "margin-inline", "my": "margin-block",
                 "p": "padding", "pt": "padding-top", "pr": "padding-right", "pb": "padding-bottom",
                 "pl": "padding-left", "px": "padding-inline", "py": "padding-block",
                 "bgcolor": "background-color"}
SX_THEME_SCALE = re.compile(r"^(margin|padding|gap|row-gap|column-gap|border-radius)")  # numbers are theme units
SIZING = re.compile(r"^(min-|max-)?(width|height)$")
UNITLESS = {"animation-iteration-count", "aspect-ratio", "column-count", "columns", "flex", "flex-grow",
            "flex-shrink", "font-weight", "grid-area", "grid-row", "grid-row-end", "grid-row-start",
            "grid-column", "grid-column-end", "grid-column-start", "line-clamp", "line-height", "opacity",
            "order", "orphans", "scale", "tab-size", "widows", "z-index", "zoom", "fill-opacity",
            "flood-opacity", "stop-opacity", "stroke-dasharray", "stroke-dashoffset", "stroke-miterlimit",
            "stroke-opacity", "stroke-width"}
NUMBER = re.compile(r"-?\d*\.?\d+")


def css_name(key, kind):
    """CSS property and unit for an object key: camelCase, sx shorthands, Angular 'prop.px'."""
    unit = None
    if kind == "angular" and re.search(r"\.([a-z]+|%)$", key):
        key, unit = key.rsplit(".", 1)
    if key.startswith("--"):
        return key, unit
    if kind == "sx" and key in SX_SHORTHANDS:
        return SX_SHORTHANDS[key], unit
    name = re.sub(r"[A-Z]", lambda m: "-" + m.group(0).lower(), key)
    return ("-" + name if name.startswith("ms-") else name), unit


def literal_values(text, v, end):
    """Values written as literals at v: a string, a number, or each value of a
    responsive object or array. Anything else is a variable and is skipped."""
    c = text[v] if v < end else ""
    if c in "{[":
        close = closing(text, v)
        values = []
        for a, b in entries(text, v, close):
            item = a + len(text[a:b]) - len(text[a:b].lstrip())
            if c == "{":
                m = re.compile(r"(?:[\w$-]+|'[^']*'|\"[^\"]*\")\s*:\s*").match(text, item, b)
                if not m:
                    continue
                item = m.end()
            values += literal_values(text, item, b)
        return values
    if c in QUOTES:
        stop = string_end(text, v)
        if text[stop:end].strip():
            return []  # an expression that starts with a string
        body = text[v + 1:stop - 1]
        return [(without_interpolations(body) if c == "`" else body, False)]
    m = NUMBER.match(text, v)
    if m and not text[m.end():end].strip():
        return [(m.group(0), True)]
    return []


def with_unit(prop, value, number, unit, kind):
    """The CSS value of a number, as the framework writes it."""
    if not number:
        return value
    if unit:
        return value + unit
    if kind == "sx":
        if SX_THEME_SCALE.match(prop) or (SIZING.match(prop) and abs(float(value)) <= 1):
            return None  # theme spacing and radius units, fractions of the parent
    if kind in ("react", "sx") and prop not in UNITLESS and float(value) != 0:
        return value + "px"
    return value


def walk(text, open_i, chain, kind, rules):
    decls = []
    for a, b in entries(text, open_i, closing(text, open_i)):
        a += len(text[a:b]) - len(text[a:b].lstrip())
        if a >= b:
            continue
        if text[a] in "\"'":
            stop = string_end(text, a)
            key, rest = text[a + 1:stop - 1], stop
        else:
            m = re.compile(r"[\w$-]+").match(text, a, b)
            if not m:
                continue  # a spread or a computed key
            key, rest = m.group(0), m.end()
        m = re.compile(r"\s*:\s*").match(text, rest, b)
        if not m:
            continue
        v, line = m.end(), line_of(text, a)
        if text[v:v + 1] == "{" and SELECTOR_KEY.search(key):
            walk(text, v, chain + [key], kind, rules)
            continue
        prop, unit = css_name(key, kind)
        for value, number in literal_values(text, v, b):
            value = with_unit(prop, value, number, unit, kind)
            if value is not None:
                decls.append((prop, value.strip(), line, None))
    rules.append((chain, decls))


def objects(text, start, end, chain, kind, rules):
    """Object literals at the top of an expression: one object or an array of them."""
    start += len(text[start:end]) - len(text[start:end].lstrip())
    if start >= end:
        return
    if text[start] == "{":
        walk(text, start, chain, kind, rules)
    elif text[start] == "[":
        for a, b in entries(text, start, closing(text, start)):
            objects(text, a, b, chain, kind, rules)


def read_objects(text):
    """style={{…}} and sx={{…}} in JSX, Vue :style="{…}", Angular [ngStyle]="{…}"."""
    rules = []
    for m in JSX_OBJECT.finditer(text):
        close = closing(text, m.end() - 1)
        objects(text, m.end(), close, [tag_at(text, m.start())], "sx" if m.group(1) == "sx" else "react", rules)
    for m in BOUND_OBJECT.finditer(text):
        end = text.find('"', m.end())
        kind = "angular" if m.group(1) == "[ngStyle]" else "vue"
        objects(text, m.end(), end if end != -1 else len(text), [tag_at(text, m.start())], kind, rules)
    return rules


# ---------------------------------------------------------------- Tailwind

CLASS_ATTR = re.compile(r"""(?<![\w:.\[-])(?:class|className)\s*=\s*(?:"([^"]*)"|'([^']*)'|(\{))""")
BOUND_CLASS = re.compile(r"""(?:(?<![\w-])(?::|v-bind:)class|\[(?:ngClass|class)\]|class:list)\s*=\s*(?:"([^"]*)"|(\{))""")
CLASS_CALL = re.compile(r"(?<![\w$.])(?:cn|cx|clsx|classnames|classNames|cva|tv|twMerge|twJoin)\s*\(")
VARIANTS = {"hover": ":hover", "group-hover": ":hover", "peer-hover": ":hover", "focus": ":focus",
            "focus-visible": ":focus-visible", "focus-within": ":focus-within", "active": ":active",
            "selection": "::selection", "motion-reduce": "@media (prefers-reduced-motion: reduce)",
            "motion-safe": "@media (prefers-reduced-motion: no-preference)"}
PALETTE = re.compile(r"(slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan"
                     r"|sky|blue|indigo|violet|purple|fuchsia|pink|rose|mauve|olive|mist|taupe)-(50|[1-9]00|950)")
# Tailwind's defaults, used only for a name the project's theme does not map.
FONT_SIZES = {"xs": ".75rem", "sm": ".875rem", "base": "1rem", "lg": "1.125rem", "xl": "1.25rem",
              "2xl": "1.5rem", "3xl": "1.875rem", "4xl": "2.25rem", "5xl": "3rem", "6xl": "3.75rem",
              "7xl": "4.5rem", "8xl": "6rem", "9xl": "8rem"}
RADII = {"": "4px", "xs": "2px", "sm": "4px", "md": "6px", "lg": "8px", "xl": "12px", "2xl": "16px",
         "3xl": "24px", "4xl": "32px", "none": "0", "full": "9999px"}
WEIGHTS = {"thin": "100", "extralight": "200", "light": "300", "normal": "400", "medium": "500",
           "semibold": "600", "bold": "700", "extrabold": "800", "black": "900"}
TRACKING = {"tighter": "-0.05em", "tight": "-0.025em", "normal": "0em", "wide": "0.025em",
            "wider": "0.05em", "widest": "0.1em"}
EASINGS = {"in": "cubic-bezier(0.4, 0, 1, 1)", "out": "cubic-bezier(0, 0, 0.2, 1)",
           "in-out": "cubic-bezier(0.4, 0, 0.2, 1)", "linear": "linear"}
SHADOWS = {"2xs", "xs", "sm", "", "md", "lg", "xl", "2xl"}
BLURS = {"xs": "4px", "sm": "8px", "": "8px", "md": "12px", "lg": "16px", "xl": "24px", "2xl": "40px", "3xl": "64px"}
SIDES = {"": "", "x": "-inline", "y": "-block", "t": "-top", "r": "-right", "b": "-bottom", "l": "-left",
         "s": "-inline-start", "e": "-inline-end"}
SPACING_ROOTS = {**{"p" + k: "padding" + v for k, v in SIDES.items()},
                 **{"m" + k: "margin" + v for k, v in SIDES.items()},
                 "gap": "gap", "gap-x": "column-gap", "gap-y": "row-gap",
                 "space-x": "margin-inline-start", "space-y": "margin-block-start",
                 "inset": "inset", "inset-x": "inset-inline", "inset-y": "inset-block", "top": "top",
                 "right": "right", "bottom": "bottom", "left": "left", "start": "inset-inline-start",
                 "end": "inset-inline-end", "translate-x": "translate", "translate-y": "translate",
                 "scroll-m": "scroll-margin", "scroll-p": "scroll-padding"}
SIZE_ROOTS = {"w": "width", "h": "height", "size": "width", "min-w": "min-width", "min-h": "min-height",
              "max-w": "max-width", "max-h": "max-height", "basis": "flex-basis"}
BORDER_ROOTS = {"border" + ("-" + k if k else ""): "border" + v for k, v in SIDES.items()}
RADIUS_ROOTS = {"rounded" + ("-" + k if k else ""): "border-radius"
                for k in ("", "t", "r", "b", "l", "s", "e", "tl", "tr", "br", "bl", "ss", "se", "es", "ee")}
COLOR_ROOTS = {"caret": "caret-color", "accent": "accent-color", "fill": "fill", "from": "background-image",
               "via": "background-image", "to": "background-image", "placeholder": "color"}
OTHER_ROOTS = {"text", "bg", "font", "leading", "tracking", "z", "duration", "delay", "ease", "shadow",
               "outline", "outline-offset", "ring", "decoration", "underline-offset", "stroke", "blur",
               "backdrop-blur", "transition", "float", "divide-x", "divide-y", "opacity", "aspect",
               "grid-cols", "grid-rows", "columns", "animate"}
ROOTS = sorted({*SPACING_ROOTS, *SIZE_ROOTS, *BORDER_ROOTS, *RADIUS_ROOTS, *COLOR_ROOTS, *OTHER_ROOTS},
               key=len, reverse=True)
ARBITRARY_PROPS = {"opacity": "opacity", "aspect": "aspect-ratio", "grid-cols": "grid-template-columns",
                   "grid-rows": "grid-template-rows", "columns": "columns", "animate": "animation",
                   "transition": "transition-property", "delay": "transition-delay",
                   "duration": "transition-duration", "ease": "transition-timing-function", "z": "z-index",
                   "leading": "line-height", "tracking": "letter-spacing", "outline-offset": "outline-offset",
                   "underline-offset": "text-underline-offset", "blur": "filter", "backdrop-blur": "backdrop-filter"}
LENGTHISH = re.compile(r"^-?\d|^calc\(|^(min|max|clamp)\(|^var\(--(space|spacing|rounded|radius|text)")
TYPE_HINT = re.compile(r"^(length|color|number|percentage|url|image|position|size|line-width|family-name|"
                       r"absolute-size|relative-size|shadow|integer|ratio|any|bg-size|vector):")


class Tailwind:
    def __init__(self, names, space_tokens):
        """names: the custom properties the theme defines, and v3 config keys;
        space_tokens: {px: "--space-N"}, Kore's spacing scale."""
        self.names, self.space = names, space_tokens

    def themed(self, namespace, name):
        if f"--{namespace}-{name}" in self.names or (name and name in self.names):
            return f"var(--{namespace}-{name})"
        return None

    def color(self, name):
        name = name.split("/")[0]
        if name in ("transparent", "current", "inherit", "currentColor"):
            return None
        return self.themed("color", name) or ("#000000" if PALETTE.fullmatch(name) or name in ("white", "black") else None)

    def translate(self, cls):
        """(variants, property, value) Tailwind generates for a class, or None."""
        parts, depth, start = [], 0, 0
        for i, c in enumerate(cls):
            depth += c in "[(" and 1 or c in "])" and -1 or 0
            if c == ":" and depth == 0:
                parts.append(cls[start:i])
                start = i + 1
        utility, variants = cls[start:].strip("!"), parts
        if utility.startswith("[") and utility.endswith("]") and ":" in utility:
            prop, value = utility[1:-1].split(":", 1)
            return variants, prop, value.replace("_", " ")
        sign = "-" if utility.startswith("-") else ""
        utility = utility.lstrip("-")
        root = next((r for r in ROOTS if utility == r or utility.startswith(r + "-")), None)
        if root is None:
            return None
        rest = utility[len(root) + 1:]
        arbitrary = None
        if rest[:1] == "[" and "]" in rest:
            arbitrary = TYPE_HINT.sub("", rest[1:rest.rindex("]")]).replace("_", " ")
        elif rest[:1] == "(" and rest.endswith(")"):
            inner = TYPE_HINT.sub("", rest[1:-1])
            arbitrary = f"var({inner})" if inner.startswith("--") else inner
        found = self.value(root, rest, arbitrary)
        if not found:
            return None
        prop, value = found
        if sign and value and value[0] not in "-0":
            value = sign + value
        return variants, prop, value

    def value(self, root, rest, arbitrary):
        number = re.fullmatch(r"\d+(\.\d+)?", rest)
        if root in SPACING_ROOTS:
            prop = SPACING_ROOTS[root]
            if arbitrary:
                return prop, arbitrary
            if rest == "px":
                return prop, "1px"
            if number:
                px = float(rest) * 4
                return prop, f"var({self.space[px]})" if px in self.space else "0" if px == 0 else f"{px:g}px"
            return (prop, self.themed("spacing", rest)) if self.themed("spacing", rest) else None
        if root in SIZE_ROOTS:
            prop = SIZE_ROOTS[root]
            if arbitrary:
                return prop, arbitrary
            if number:
                return prop, f"{float(rest) * 4:g}px"
            if rest == "screen" and "height" in prop:
                return prop, "100vh"
            named = self.themed("spacing", rest) or (self.themed("container", rest) if root == "max-w" else None)
            return (prop, named) if named else None
        if root in RADIUS_ROOTS:
            if arbitrary:
                return "border-radius", arbitrary
            named = self.themed("radius", rest) if rest else ("var(--radius)" if "--radius" in self.names else None)
            return "border-radius", named or RADII.get(rest)
        if root in BORDER_ROOTS or root in ("divide-x", "divide-y"):
            prop = BORDER_ROOTS.get(root, "border")
            if arbitrary:
                return (prop + "-width", arbitrary) if LENGTHISH.match(arbitrary) else (prop + "-color", arbitrary)
            if rest == "" or number:
                return prop + "-width", f"{rest or 1}px"
            return (prop + "-color", self.color(rest)) if self.color(rest) else None
        if root in COLOR_ROOTS:
            value = arbitrary or self.color(rest)
            return (COLOR_ROOTS[root], value) if value else None
        if root == "text":
            if arbitrary:
                return ("font-size", arbitrary) if LENGTHISH.match(arbitrary) else ("color", arbitrary)
            if rest in ("left", "right", "center", "justify", "start", "end"):
                return "text-align", rest
            if rest.split("/")[0] in FONT_SIZES:
                return "font-size", self.themed("text", rest.split("/")[0]) or FONT_SIZES[rest.split("/")[0]]
            return ("color", self.color(rest)) if self.color(rest) else None
        if root == "bg":
            if arbitrary:
                image = re.match(r"(url|[\w-]*gradient)\(", arbitrary)
                return ("background-image" if image else "background-color"), arbitrary
            return ("background-color", self.color(rest)) if self.color(rest) else None
        if root == "font":
            if arbitrary:
                return ("font-weight" if arbitrary.isdigit() else "font-family"), arbitrary
            if rest in WEIGHTS:
                return "font-weight", self.themed("font-weight", rest) or WEIGHTS[rest]
            return None
        if root == "leading" and number:
            return "line-height", f"{float(rest) * 4:g}px"
        if root == "tracking" and rest in TRACKING:
            return "letter-spacing", self.themed("tracking", rest) or TRACKING[rest]
        if root == "z" and number:
            return "z-index", rest
        if root in ("duration", "delay") and number:
            return "transition-" + root, rest + "ms"
        if root == "ease" and rest in EASINGS:
            return "transition-timing-function", self.themed("ease", rest) or EASINGS[rest]
        if root == "transition" and rest == "all":
            return "transition-property", "all"
        if root == "shadow":
            if arbitrary:
                return ("box-shadow", arbitrary) if re.search(r"\d", arbitrary) else None
            if rest in SHADOWS:
                named = self.themed("shadow", rest) if rest else ("var(--shadow)" if "--shadow" in self.names else None)
                return "box-shadow", named or "0 1px 3px 0 rgb(0 0 0 / 0.1)"
            return None
        if root in ("outline", "ring", "stroke", "decoration"):
            prop = {"outline": "outline", "ring": "box-shadow", "stroke": "stroke", "decoration": "text-decoration"}[root]
            width = {"outline": "outline-width", "ring": "box-shadow", "stroke": "stroke-width",
                     "decoration": "text-decoration-thickness"}[root]
            if arbitrary:
                return (width, arbitrary) if LENGTHISH.match(arbitrary) else (prop + "-color", arbitrary)
            if rest == "" or number:
                size = f"{rest or 1}" + ("" if root == "stroke" else "px")
                return width, f"0 0 0 {size}" if root == "ring" else size
            color = self.color(rest)
            return (("outline-color" if root == "ring" else prop + "-color"), color) if color else None
        if root in ("blur", "backdrop-blur"):
            prop = "filter" if root == "blur" else "backdrop-filter"
            if arbitrary:
                return prop, f"blur({arbitrary})"
            return (prop, f"blur({BLURS[rest]})") if rest in BLURS and not self.themed("blur", rest) else None
        if root == "float" and rest in ("left", "right"):
            return "float", rest
        if root in ("underline-offset", "outline-offset") and number:
            return ARBITRARY_PROPS[root], rest + "px"
        if arbitrary and root in ARBITRARY_PROPS:
            return ARBITRARY_PROPS[root], arbitrary
        return None

    def rule(self, cls, chain, line):
        found = self.translate(cls)
        if not found:
            return None
        variants, prop, value = found
        return (chain + [VARIANTS.get(v, v + ":") for v in variants], [(prop, value, line, cls)])

    def read_classes(self, text):
        """A rule for every class whose declaration a check can measure."""
        spans = []
        for m in CLASS_ATTR.finditer(text):
            if m.group(3):
                spans.append((tag_at(text, m.start()), "expr", m.end() - 1, closing(text, m.end() - 1)))
            else:
                g = 1 if m.group(1) is not None else 2
                spans.append((tag_at(text, m.start()), "plain", m.start(g), m.end(g)))
        for m in BOUND_CLASS.finditer(text):
            if m.group(2):
                spans.append((tag_at(text, m.start()), "expr", m.end() - 1, closing(text, m.end() - 1)))
            else:
                spans.append((tag_at(text, m.start()), "expr", m.start(1), m.end(1)))
        for m in CLASS_CALL.finditer(text):
            spans.append(("element", "expr", m.end() - 1, closing(text, m.end() - 1)))
        rules, seen = [], set()
        for tag, kind, start, end in spans:
            chain = [tag]
            if kind == "plain":
                body = re.sub(r"\{[^{}]*\}", lambda b: blank(b.group(0)), text[start:end])
                literals = [(start, re.sub(r"\{[^{}]*\}", lambda b: blank(b.group(0)), body))]
            else:
                literals = string_literals(text, start, end)
            for offset, body in literals:
                for m in re.finditer(r"\S+", body):
                    if offset + m.start() in seen:
                        continue
                    seen.add(offset + m.start())
                    rule = self.rule(m.group(0), chain, line_of(text, offset + m.start()))
                    if rule:
                        rules.append(rule)
        return rules

    def expand_apply(self, rules):
        """@apply in CSS, replaced by the declarations of its classes."""
        out = []
        for chain, decls in rules:
            kept = [d for d in decls if d[0] != "@apply"]
            out.append((chain, kept))
            for prop, value, line, _ in decls:
                if prop == "@apply":
                    out += [r for cls in value.split() if (r := self.rule(cls, chain, line))]
        return out


def tailwind_config(text):
    """Keys and copied values of a Tailwind v3 config: (keys, [(line, literal)])."""
    keys = set(re.findall(r"""['"]?([\w-]+)['"]?\s*:""", text))
    for m in re.finditer(r"\bscreens\s*:\s*\{", text):  # media queries cannot read var()
        end = closing(text, m.end() - 1)
        text = text[:m.end()] + blank(text[m.end():end]) + text[end:]
    copies = [(line_of(text, offset), body) for offset, body in string_literals(text, 0, len(text))
              if "var(" not in body and re.search(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch)\(|\d(px|rem|em)\b", body)]
    return keys, copies
