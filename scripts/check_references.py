#!/usr/bin/env python3
"""Check that Kore's files are consistent with each other.

Run from anywhere: python3 scripts/check_references.py [root]
The root is the repo by default. It reads SKILL.md, references/ and typologies/
under it, changes nothing, and prints every problem with its file and line, or OK.

Checks:
1. Every token written in backticks exists in references/tokens.yaml (in a typology's
   references/tokens.yaml too, for the files of that typology).
2. Every value written next to a token matches references/tokens.yaml, as in check 1.
3. Every references/ path exists.
4. The components index (references/components/index.md) and references/components/ match.
5. Every name in a Uses line is a component of the index.
6. Every reference in parentheses to a section, rule or component exists.
7. Every rule line has a name, and no id is at two rules of its group.
8. No line of a new file (references/start/, references/rules/, typologies/) is a rule line of another file.
9. Every id a typology replaces is the id of a default rule.
10. Every "replaced in" of a default rule lists the typologies that replace it, and only them.
11. Every typologies/ folder has the files and folders of typologies/_template.
12. Every typologies/ path, router table included, exists.
13. A typology's tokens.yaml repeats no default value and names no default token of another group.
"""

import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
TOKENS = ROOT / "references" / "tokens.yaml"
COMPONENTS = ROOT / "references" / "components"


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if not unicodedata.combining(c))


# Point 8, decided by the user 2026-10-23: a rule's id is <file>.<name>, its name the bold label that opens a
# line or the first cell of a table row; a line with neither is a finding until it gets a bold label.
BOLD = re.compile(r"^(?:- |\d+\. )?\*\*([^*]+?):?\*\*")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", fold(s.replace("`", ""))).strip("-")


def rule_ids(stem, md_text):
    """(n, id) of every rule of the .md, and the lines that are a rule with no name."""
    ids, unnamed, header, fenced = [], [], True, False
    for n, line in enumerate(md_text.splitlines(), 1):
        if line.startswith("```"):
            fenced = not fenced
        if fenced or line.startswith(("```", "#", " ")) or not line.strip():
            header = True
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not header and not set("".join(cells)) <= set("-: "):
                ids.append((n, f"{stem}.{slug(cells[0])}"))
            header = False
            continue
        header = True
        if m := BOLD.match(line):
            ids.append((n, f"{stem}.{slug(m.group(1))}"))
        else:
            unnamed.append(f"{n}: {line.strip()[:120]}")
    return ids, unnamed


# Names in parentheses that are not Kore's own: sources, tools, frameworks,
# languages, examples. A new one is added here when the check flags it.
EXTERNAL = {
    "Cowan 2001", "Material", "Apple", "WCAG 2.1.4", "MIT", "MIT license",
    "Bootstrap", "Bootstrap through Sass", "MUI", "Angular Material",
    "React", "React Native", "Vue", "Angular", "Svelte", "SolidJS", "Flutter",
    "Astro", "CSS", "FLIP", "DevTools Performance panel", "CLS", "CLS 0", "Lighthouse",
    "Arabic", "Hebrew", "Persian", "Urdu", "Italiano", "English",
    "Large", "Medium", "Small", "Uniform Connectedness",
}

REPLACES = re.compile(r"Replaces: ((?:`[\w.-]+`(?:, )?)+)")


def replaced_ids(text):
    """The ids the Replaces lines of a text name, in order."""
    return [rid for m in REPLACES.finditer(text) for rid in re.findall(r"`([\w.-]+)`", m.group(1))]


def read_tokens(block):
    """Return {token: value} from tokens.yaml, by indentation."""
    tokens = {}
    stack = []
    for raw in block.split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        key, _, value = raw.strip().partition(":")
        while stack and stack[-1][0] >= indent:
            stack.pop()
        value = value.strip().strip('"')
        path = [k for _, k in stack] + [key]
        if value:
            tokens.setdefault(key, []).append((path, value))
        else:
            stack.append((indent, key))
    return tokens


def tokens_for(root, t):
    """Default tokens, with the typology's tokens.yaml replacing the entries of the same path."""
    default_tokens = read_tokens((Path(root) / "references" / "tokens.yaml").read_text(encoding="utf-8"))
    own = Path(root) / "typologies" / t / "references" / "tokens.yaml"
    if not own.exists():
        return default_tokens
    own_tokens = read_tokens(own.read_text(encoding="utf-8"))
    own_paths = {tuple(p) for entries in own_tokens.values() for p, _ in entries}
    merged = {key: [e for e in entries if tuple(e[0]) not in own_paths]
              for key, entries in default_tokens.items()}
    for key, entries in own_tokens.items():
        merged[key] = merged.get(key, []) + entries
    return merged


def token_values(tokens, name):
    """Comparable values of a token: its value, or its fontSize."""
    values = set()
    for path, value in tokens.get(name, []):
        values.add(value)
    for path, value in tokens.get("fontSize", []):
        if path[-2] == name:
            values.add(value)
    return values


def is_token(tokens, name):
    if name in tokens and any(path[0] != "typography" or len(path) == 2
                              for path, _ in tokens[name]):
        return True
    return any(path[-2] == name for path, _ in tokens.get("fontSize", []))


def walk(root, pattern):
    """Files matching pattern under root, names starting with "." left out."""
    return sorted(p for p in root.glob(pattern) if p.is_file()
                  and not any(part.startswith(".") for part in p.relative_to(root).parts))


def tree(base):
    """Relative paths of the files and folders under base, names starting with "." left out."""
    return sorted(p.relative_to(base) for p in base.rglob("*")
                  if not any(part.startswith(".") for part in p.relative_to(base).parts))


def typology_of(root, path):
    """The typology folder a file sits in, None outside typologies/<t>/."""
    parts = path.relative_to(root).parts
    return parts[1] if parts[0] == "typologies" and len(parts) > 2 else None


def group_of(root, path):
    """The group ids must be unique in: references/rules together, each typology's references alone."""
    parts = path.relative_to(root).parts
    return "rules" if parts[0] == "references" else parts[1]


def mask(text):
    """The text with its frontmatter and its lines of dashes blanked, line numbers kept."""
    lines = text.splitlines()
    top = lines.index("---", 1) + 1 if lines[:1] == ["---"] and "---" in lines[1:] else 0
    return "\n".join("" if n < top or re.fullmatch(r"-+", line) else line
                     for n, line in enumerate(lines))


def rule_lines(path, text):
    """(line, id or None, text) of each rule line of a file, in line order; None when the line has no name."""
    lines = text.splitlines()
    # a variant's file (components/cards/cover.md) holds rules of its component: cards.cover-card
    stem = path.parent.name if path.parent.parent.name == "components" else path.stem
    ids, unnamed = rule_ids(stem, mask(text))
    found = ids + [(int(u.split(": ", 1)[0]), None) for u in unnamed]
    return sorted((n, rid, lines[n - 1]) for n, rid in found)


def identity(path):
    """(group, name) of a token: the role for typography, the color name for colors."""
    group = path[0]
    name = path[2] if group == "colors" else path[1] if group == "typography" else path[-1]
    return group, name


def main(root=ROOT):
    root = Path(root)
    skill = root / "SKILL.md"
    comp_dir = root / "references" / "components"
    problems = []

    def report(path, line, message):
        problems.append(f"{path.relative_to(root)}:{line}: {message}")

    skill_text = skill.read_text(encoding="utf-8")
    default_tokens = read_tokens((root / "references" / "tokens.yaml").read_text(encoding="utf-8"))
    body_start = skill_text.split("\n---", 1)[0].count("\n") + 2

    files = [skill] + walk(root, "references/**/*.md")
    typology_files = walk(root, "typologies/**/*.md")
    checked = files + typology_files
    texts = {f: f.read_text(encoding="utf-8") for f in checked}
    rules = {f: rule_lines(f, texts[f]) for f in checked}
    rule_files = walk(root, "references/rules/**/*.md") + walk(root, "typologies/*/references/**/*.md")
    default_rule_files = walk(root, "references/rules/**/*.md") + walk(root, "references/components/**/*.md")
    new_files = walk(root, "references/start/**/*.md") + walk(root, "references/rules/**/*.md") + typology_files

    # Known names: headings, bold labels (named rules included), components.
    names = set()
    for text in texts.values():
        names |= {m.group(1).strip() for m in re.finditer(r"^ *#+ (.+)$", text, re.M)}
        names |= set(re.findall(r"\*\*[^*]*\(([A-Z]+)\)[^*]*\*\*", text))
        names |= {m.group(1).strip() for m in re.finditer(r"\*\*([^*]+?)[.:]?\*\*", text)}
    names = {re.sub(r"^\d+\. ", "", n).rstrip(".:") for n in names}
    names = {re.sub(r" \(binding\)$", "", n) for n in names}
    names |= {n.split(",")[0] for n in names}
    names |= {p for n in names for p in n.split(": ")}

    index_file = comp_dir / "index.md"
    index_text = index_file.read_text(encoding="utf-8") if index_file.exists() else ""
    index = dict(re.findall(r"^\| ([^|]+?) \| `references/components/([\w-]+\.md)` \|$",
                            index_text, re.M))
    components = set(index)

    # Families that are always tokens, so a typo in them is caught.
    families = re.compile(
        r"^(space-\w+|(display|headline|title|body|label|code)-\w+|duration-\w+|"
        r"ease-[\w-]+|shadow-\w+|surface-[\w-]+|hairline[\w-]*|"
        r"(primary|danger|success|warning|info|accent)-[\w-]+)$")
    colors = {k for k, v in default_tokens.items() if any(p[0] == "colors" for p, _ in v)}

    for path, text in texts.items():
        t = typology_of(root, path)
        tokens = tokens_for(root, t) if t else default_tokens
        offset = body_start if path == skill else 1
        lines = text.split("\n")
        if path == skill:
            lines = lines[body_start - 1:]
        for n, line in enumerate(lines, offset):
            # 1. Tokens in backticks.
            for m in re.finditer(r"`([a-z][\w-]*)`", line):
                name = m.group(1)
                if families.match(name) and name[-1] != "N" and not is_token(tokens, name):
                    report(path, n, f"unknown token `{name}`")
            # 2. Values next to tokens: `space-4` (16px), `md` (12px).
            for m in re.finditer(r"`([a-z][\w-]*)` \((\d+(?:px|ms))", line):
                name, value = m.groups()
                values = token_values(tokens, name)
                if values and value not in values:
                    report(path, n, f"`{name}` ({value}) but tokens.yaml says "
                                    f"{', '.join(sorted(values))}")
            # 3. Paths.
            for m in re.finditer(r"`((?:references|typologies)/[\w/<>.-]+)`", line):
                ref = m.group(1)
                if "<" not in ref and not (root / ref).exists():
                    report(path, n, f"missing file {ref}")
            # 5. Uses lines.
            m = re.match(r"\*\*Uses:\*\* (.+)\.$", line)
            if m:
                for name in m.group(1).split(", "):
                    if name not in components:
                        report(path, n, f"Uses names {name}, not in the index")
            # 6. References in parentheses.
            for m in re.finditer(r"\(([A-Z][^()]*?)\)", line):
                whole = m.group(1)
                if whole in names or whole in EXTERNAL:
                    continue
                pieces = whole.split(", ")  # a name holding " and " (Grouping and separation) stays whole
                for part in [q for piece in pieces for q in ([piece] if piece in names else piece.split(" and "))]:
                    part = re.sub(r"^(see |as in )", "", part.strip())
                    part = re.sub(r"\s#?\d+$", "", part)
                    part = re.sub(r"^.+ in ([A-Z].+)$", r"\1", part)
                    if not re.fullmatch(r"[A-Z][\w-]*(?: [\w-]+){0,4}", part):
                        continue
                    if re.fullmatch(r"(Usability|question) \d+", part, re.I):
                        continue
                    if part in names or part in components or part in EXTERNAL:
                        continue
                    report(path, n, f"reference ({part}) not found")

    # 4. Index and folder.
    on_disk = {p.name for p in comp_dir.glob("*.md")} - {"index.md"}
    for name, file in index.items():
        if file not in on_disk:
            report(index_file, 1, f"index lists {file} for {name}, the file is missing")
    for file in sorted(on_disk - set(index.values())):
        report(comp_dir / file, 1, "not in the components index")
    for name, file in index.items():
        if file in on_disk:
            title = (comp_dir / file).read_text(encoding="utf-8").split("\n", 1)[0]
            if title != f"# {name}":
                report(comp_dir / file, 1, f"title '{title}', the index says {name}")

    # 7. Rule names and ids.
    ids_at = defaultdict(list)  # (group, id) -> [(file, line)]
    for path in rule_files:
        for n, rid, _ in rules[path]:
            if rid:
                ids_at[(group_of(root, path), rid)].append((path, n))
    for path in rule_files:
        for n, rid, _ in rules[path]:
            if rid is None:
                report(path, n, "rule line with no name")
                continue
            again = [(p, m) for p, m in ids_at[(group_of(root, path), rid)] if (p, m) != (path, n)]
            if again:
                other, line = again[0]
                report(path, n, f"id {rid} also at {other.relative_to(root)}:{line}")

    # 8. Lines of new files repeated from another rule line.
    same = defaultdict(list)  # stripped line -> [(file, line)]
    for path in checked:
        for n, _, line in rules[path]:
            same[line.strip()].append((path, n))
    for path in new_files:
        for n, _, line in rules[path]:
            other = [(p, m) for p, m in same[line.strip()] if (p, m) != (path, n)]
            if other:
                report(path, n, f"same line as {other[0][0].relative_to(root)}:{other[0][1]}")

    # 9. Replaces, and the typologies that replace each id (for 10).
    default_ids = {rid for f in default_rule_files for _, rid, _ in rules[f] if rid}
    replaced_in = defaultdict(set)  # id -> typologies whose files replace it
    for path in typology_files:
        t = typology_of(root, path)
        if t == "_template":
            continue
        for n, line in enumerate(texts[path].splitlines(), 1):
            for rid in replaced_ids(line):
                if t:
                    replaced_in[rid].add(t)
                if rid not in default_ids:
                    report(path, n, f"Replaces: {rid}, no default rule has this id")

    # 10. "replaced in" of default rules against the Replaces of typologies.
    for path in default_rule_files:
        for n, rid, line in rules[path]:
            m = re.search(r"\(replaced in: ([^)]+)\)", line)
            listed = sorted(m.group(1).split(", ")) if m else []
            found = sorted(replaced_in[rid]) if rid else []
            if listed != found:
                report(path, n, f"replaced in: {', '.join(listed) or 'none'}, "
                                f"Replaces in: {', '.join(found) or 'none'}")

    # 11. Typologies have the files and folders of _template.
    typologies = root / "typologies"
    folders = sorted(p.name for p in typologies.iterdir()
                     if p.is_dir() and not p.name.startswith(".")) if typologies.is_dir() else []
    if folders:
        template = typologies / "_template"
        if not template.is_dir():
            report(template, 1, "missing")
        else:
            for t in folders:
                base = typologies / t
                if t == "_template":
                    continue
                for p in tree(template):
                    if not (base / p).exists():
                        report(base / p, 1, "missing, _template has it")
                for p in tree(base):
                    if (template / p).exists():
                        continue
                    if (base / p).is_file() and (template / p.parent).is_dir():
                        continue
                    report(base / p, 1, "not in _template")

    # 13. A typology's tokens repeat no default value and name no default token of another group.
    default_entries = [(p, v) for entries in default_tokens.values() for p, v in entries]
    default_at = {tuple(p): v for p, v in default_entries}
    default_names = {identity(p) for p, _ in default_entries}
    for t in folders:
        own_file = typologies / t / "references" / "tokens.yaml"
        if t == "_template" or not own_file.exists():
            continue
        for entries in read_tokens(own_file.read_text(encoding="utf-8")).values():
            for path, value in entries:
                group, name = identity(path)
                dotted = ".".join(path)
                if default_at.get(tuple(path)) == value:
                    report(own_file, 1, f"{dotted} has the default's value")
                elif (group, name) not in default_names and \
                        name in {n for g, n in default_names if g != group}:
                    report(own_file, 1, f"new key {dotted} has the name of a default token")

    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problems")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT))
