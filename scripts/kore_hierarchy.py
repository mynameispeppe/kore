#!/usr/bin/env python3
"""The checks of the Hierarchy rule group (references/rules/hierarchy.md), starting with the Decisions file table."""
import difflib
import hashlib
import os
import re
from pathlib import Path

from check_references import tokens_for
from kore_check import typology_line, typology_names

KORE = Path(__file__).resolve().parent.parent
COLUMNS = ["Element", "Question", "Group", "Level", "Style", "Space", "Rule"]
LEVELS = {"Primary", "Secondary", "Tertiary", "—"}
PRIMITIVES = {"Stack", "Inline", "Sidebar", "Grid"}
SCRIPTS = {".js", ".ts", ".mjs", ".cjs", ".mts", ".cts"}  # no markup of their own
TOKENS = re.compile(r"--canvas\s*:")


def needs_table(path, text):
    """Whether an interface file needs a table: not the token file, not a plain script."""
    return not (TOKENS.search(text) or Path(path).suffix.lower() in SCRIPTS)


def names_file(found, rel):
    """Whether one of the tables (from `tables`) names the file."""
    return any(rel in t["files"] for t in found)


def tables(text):
    """Each `## ` section of KORE-DECISIONS.md: heading, files, lines, hash."""
    found = []
    for section in re.split(r"(?m)^## ", text)[1:]:
        heading, _, body = section.partition("\n")
        files = heading.split(" · ", 1)[1] if " · " in heading else ""
        found.append({"heading": heading.strip(), "body": body,
                      "files": {f.strip().removeprefix("./") for f in files.split(",") if f.strip()},
                      "hash": hashlib.sha256(section.strip().encode()).hexdigest()})
    return found


def rule_names():
    """Every name a Rule cell may cite: headings, bold rule names and bold
    labels of SKILL.md and references/, outside code blocks."""
    names = set()
    for path in [KORE / "SKILL.md", *sorted((KORE / "references").rglob("*.md"))]:
        text = re.sub(r"(?ms)^\s*```.*?^\s*```", "", path.read_text(encoding="utf-8"))
        names |= set(re.findall(r"(?m)^#+\s+(.+?)\s*$", text))
        names |= set(re.findall(r"\*\*(The [^*]+? Rule)\*\*", text))
        names |= set(re.findall(r"(?m)^\s*(?:[-*]|\d+\.)?\s*\*\*([^*]+?)[.:]\*\*", text))
    names |= {re.sub(r"\s*\(.*?\)$", "", n) for n in names}  # "Contrast (binding)" is cited as Contrast
    return sorted({n.lower() for n in names if n}, key=len, reverse=True)


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def kore_tokens(typology, kore=KORE):
    """Type roles ({role: (size, weight)}), color names and spaces ({name: px}) of
    references/tokens.yaml, the typology's tokens.yaml replacing and adding keys."""
    roles, colors, spaces = {}, set(), {}
    for name, entries in tokens_for(kore, typology).items():
        for path, value in entries:
            if path[0] == "typography" and path[-1] in ("fontSize", "fontWeight"):
                roles.setdefault(path[1], [0, 0])[path[-1] == "fontWeight"] = int(re.sub(r"\D", "", value))
            elif path[0] == "colors":
                colors.add(name)
            elif path[0] == "spacing":
                spaces[name] = int(re.sub(r"\D", "", value))
    return {r: tuple(v) for r, v in roles.items()}, colors, spaces


def component_names():
    return {(p.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ").strip().lower())
            for p in (KORE / "references" / "components").glob("*.md")}


# Rule cited by a label row: (what it is, its style, the rule's name).
LABELS = {"value labels are a last resort": ("a value label", "body-md 400 mute", "Value labels are a last resort"),
          "specs lead with the label": ("a spec label", "body-md 400 ink", "Specs lead with the label")}


def check_values(where, body, roles, colors, spaces, components, primary_group=None, shape_items=()):
    """The values of each row against the rules they come from: Roles and
    sizes, From role to style, Typographic levels, the space scale."""
    errors, groups = [], {}
    styles = {row[0]: row[4] for row in body}
    bodies = sorted((r for r in roles if r.startswith("body-")), key=lambda r: -roles[r][0])
    for row in body:
        name, group, level, style, space, rule = row[0], row[2], row[3], row[4], row[5], row[6].lower()
        words = style.split()
        role = next((w for w in words if w in roles), None)
        if "consequences are never quiet" in rule:
            if level != "—":
                errors.append(f"{where}, {name}: a consequence has Level —, not {level} (Consequences are never quiet)")
            if not role or roles[role][1] != 500 or "danger" not in words:
                errors.append(f"{where}, {name}: a consequence is a 500 role in danger, not {style} (Consequences are never quiet)")
        elif label := next((v for k, v in LABELS.items() if k in rule), None):
            kind, want, cite = label
            if level != "—":
                errors.append(f"{where}, {name}: {kind} has Level —, not {level} ({cite})")
            if words != want.split():
                errors.append(f"{where}, {name}: {kind} is {want}, not {style} ({cite})")
            if space.strip() == "—":
                errors.append(f"{where}, {name}: {kind} has a Space to its value, not — ({cite})")
            value = re.match(r"space-\d+ to (.+)$", space.strip())
            if cite == "Specs lead with the label" and value and styles.get(value.group(1), "body-md 400 body").split() != ["body-md", "400", "body"]:
                errors.append(f"{where}, {name}: its value {value.group(1)} is body-md 400 body, not {styles[value.group(1)]} ({cite})")
        elif level == "—" and not (re.search(r"\bh[1-6]\b|\b\d+:\d+\b", f"{name} {style}") or (role or "").startswith("label-")
                                 or any(re.search(rf"\b{re.escape(c)}\b", style.lower()) for c in components)):
            errors.append(f"{where}, {name}: Level — is only for a heading, a label, a whole component or an image; "
                          "this element takes Primary, Secondary or Tertiary (Semantic weight)")
        if space != "—":
            named = re.findall(r"space-\d+", space)
            if not named or set(named) - set(spaces):
                errors.append(f"{where}, {name}: Space is {space}; it names a space token "
                              f"({', '.join(sorted(spaces, key=lambda s: int(s[6:])))}) or —")
        if not role:
            if level in ("Primary", "Secondary", "Tertiary"):
                groups.setdefault(group, []).append((name, level, None, None))  # an image, a component
            wrong = re.search(r"\b(?:display|headline|title|body|label)-\S*", style)
            if level in ("Primary", "Secondary", "Tertiary") and wrong:
                errors.append(f"{where}, {name}: Style names {wrong.group()}, not a type role "
                              f"({', '.join(sorted(roles))}) (Roles and sizes)")
            continue
        weight = next((int(w) for w in words if re.fullmatch(r"[1-9]00", w)), None)
        color = next((w for w in words if w in colors), None)
        if weight != roles[role][1]:
            errors.append(f"{where}, {name}: {role} has weight {roles[role][1]}, not {weight or 'none'} "
                          "(Roles and sizes, Emphasis)")
        if not color:
            errors.append(f"{where}, {name}: Style names no color token ({', '.join(sorted(colors))})")
        heading = re.search(r"\bh([23])\b", f"{name} {style}")  # the tag may sit in Element or Style
        expected = {"2": "headline-md", "3": "headline-sm"}.get(heading.group(1)) if heading else None
        if expected and role != expected and not any(c in rule for c in components):
            errors.append(f"{where}, {name}: an h{heading.group(1)} of a page section is {expected}, not {role} "
                          "(Typographic levels)")
        if level in ("Primary", "Secondary", "Tertiary"):
            if role.startswith("label-"):
                errors.append(f"{where}, {name}: {role} follows its component, so its Level is — (From role to style)")
            groups.setdefault(group, []).append((name, level, role, color))
    by_group, by_question = {}, {}  # Relatedness Test: rows of every Level, — included
    for row in body:
        question, group = row[1].strip(), row[2].strip()
        by_group.setdefault(group.casefold(), (group, {}))[1].setdefault(question.casefold(), question)
        by_question.setdefault(question.casefold(), (question, {}))[1].setdefault(group.casefold(), group)
    for group, questions in by_group.values():
        if len(questions) > 1:
            errors.append(f"{where}, group {group} answers {len(questions)} questions: "
                          f"{', '.join(questions.values())} (The Relatedness Test)")
    for question, found in by_question.values():
        if len(found) > 1:
            errors.append(f"{where}, question {question} is answered by {len(found)} groups: "
                          f"{', '.join(found.values())} (The Relatedness Test)")
    elements = {r[0].strip().casefold(): r[2].strip() for r in body}
    links = []  # (row's Element, space token, target Element, row's group, target's group)
    for row in body:
        link = re.match(r"(space-\d+) to (.+)$", row[5])
        if not link:
            if row[5].strip() != "—":
                errors.append(f"{where}, {row[0]}: Space is {row[5]}; it reads space-N to [Element] or — (Decisions file)")
            continue
        target = link.group(2).strip()
        if target.casefold() not in elements or target.casefold() == row[0].strip().casefold():
            errors.append(f"{where}, {row[0]}: Space goes to {target}, no Element of the table (Decisions file)")
        elif link.group(1) in spaces:
            links.append((row[0], link.group(1), target, row[2].strip(), elements[target.casefold()]))
    for name, token, target, a, b in links:
        if a.casefold() == b.casefold():
            continue
        inside = [(spaces[t], t) for _, t, _, x, y in links if x.casefold() == y.casefold() and x.casefold() in (a.casefold(), b.casefold())]
        if inside and spaces[token] < 2 * max(inside)[0]:
            errors.append(f"{where}, {name}: {token} to {target} joins groups {a} and {b}; it is at least twice "
                          f"{max(inside)[1]}, their largest inside space (The Distance Ratio Rule)")
    sizes = sorted({roles[i[2]][0] for items in groups.values() for i in items if i[2]}, reverse=True)
    if len(sizes) > 3:
        errors.append(f"{where}: {len(sizes)} font sizes on the text rows with a Level "
                      f"({', '.join(f'{s:g}px' for s in sizes)}); at most three (Text hierarchy)")
    for group, items in groups.items():
        primaries = [i for i in items if i[1] == "Primary"]
        if len(primaries) > 1:
            errors.append(f"{where}, group {group}: {len(primaries)} Primary elements; one answers the main "
                          "question (Semantic weight)")
        if not primaries:
            errors.append(f"{where}, group {group}: no Primary (Semantic weight)")
            continue
        if not primaries[0][2]:
            continue  # the Primary is not text: no size to step down from
        size = roles[primaries[0][2]][0]
        below = [b for b in bodies if roles[b][0] < size or (roles[b][0] == size and roles[primaries[0][2]][1] > 400)]
        secondary = next((i[2] for i in items if i[1] == "Secondary" and i[2]), below[0] if below else None)
        for name, level, role, color in items:
            if not role:
                continue
            if level == "Primary" and color != "ink":
                errors.append(f"{where}, {name}: a Primary is ink, not {color} (From role to style)")
            if level == "Secondary":
                if role != (below[0] if below else None):
                    errors.append(f"{where}, {name}: a Secondary under {primaries[0][2]} is "
                                  f"{below[0] if below else 'no Body role'}, not {role} (From role to style)")
                if color != "body":
                    errors.append(f"{where}, {name}: a Secondary is body, not {color} (From role to style)")
            if level == "Tertiary":
                lower = bodies[bodies.index(secondary) + 1] if secondary in bodies[:-1] else None
                if role != lower:
                    errors.append(f"{where}, {name}: a Tertiary under a Secondary of {secondary} is "
                                  f"{lower or 'no Body role'}, not {role} (From role to style)")
                if color != "mute":
                    errors.append(f"{where}, {name}: a Tertiary is mute, not {color} (From role to style)")
    text_rows = [(r[0], next((w for w in r[4].split() if w in roles), None), r[3]) for r in body]
    text_rows = [(n, role, lvl) for n, role, lvl in text_rows if role and lvl in ("Primary", "Secondary", "Tertiary")]
    focal = next((r[0] for r in body if r[3] == "Primary" and r[2] == primary_group), None)
    focal_role = next((role for n, role, _ in text_rows if n == focal), None)
    for name, role, _ in text_rows if focal_role else ():
        if name != focal and (roles[role][0], roles[role][1]) > (roles[focal_role][0], roles[focal_role][1]):
            errors.append(f"{where}, {name}: {role} outweighs the focal point {focal} in {focal_role} (The One Winner Rule)")
    typed = {n.casefold(): n for n, _, _ in text_rows}
    first = next((typed[i.casefold()] for i in shape_items if i.casefold() in typed), None)
    if focal_role and first and first.casefold() != focal.casefold():
        errors.append(f"{where}: {first} comes before the focal point {focal} in the Shape (The One Winner Rule)")
    return errors


def type_rows(text):
    """[(table name, [(Element, role, weight, color, space token, target, focal, inline, label, text)])] for every row; role, weight and color are None when Style names no type role, token and target when Space is —, focal True on the Primary of the Primary group, inline True when the Rule column names Inline emphasis, label True when it names Value labels are a last resort, text True on a text row (The One Winner Rule)."""
    roles, colors, _ = kore_tokens(typology_line(text))
    found = []
    for table in tables(text):
        rows = [cells(l) for l in table["body"].splitlines() if l.strip().startswith("|")][2:]
        typed = []
        group = re.search(r"(?m)^Primary group:\s*(.+?)\s*$", table["body"])
        for row in (r for r in rows if len(r) == len(COLUMNS)):
            words = row[4].split()
            role = next((w for w in words if w in roles), None)
            link = re.match(r"(space-\d+) to (.+)$", row[5])
            typed.append((row[0], role, next((w for w in words if re.fullmatch(r"[1-9]00", w)), None) if role else None,
                          next((w for w in words if w in colors), None) if role else None,
                          link and link.group(1), link and link.group(2),
                          row[3] == "Primary" and bool(group) and row[2] == group.group(1),
                          "inline emphasis" in row[6].lower(),
                          "value labels are a last resort" in row[6].lower(),
                          row[3] in ("Primary", "Secondary", "Tertiary")))
        found.append((table["heading"].split(" · ")[0], typed))
    return found


def validate(text):
    errors, names = [], rule_names()
    typology, typologies = typology_line(text), typology_names()
    if typology not in typologies:
        errors.append(f"Typology: {typology} is not a folder of typologies/ ({', '.join(typologies)})")
        typology = "minimalism"
    roles, colors, spaces = kore_tokens(typology)
    components = component_names()
    for table in tables(text):
        where = f"## {table['heading']}"
        if not table["files"]:
            errors.append(f"{where}: the heading names no file (name · file, file)")
        shape = re.search(r"(?m)^Shape:\s*(.+)$", table["body"])
        items = re.findall(r"(?:^|[(,])\s*([^(),]+?)\s*(?=[,)]|$)", shape.group(1)) if shape else []  # the text between brackets and commas
        if not shape:
            errors.append(f"{where}: no Shape line")
        else:
            used = re.findall(r"^\s*(\w+)|(\w+)\s*\(", shape.group(1))
            wrong = {a or b for a, b in used} - PRIMITIVES
            if wrong:
                errors.append(f"{where}: Shape uses {', '.join(sorted(wrong))}, not a Layout primitive "
                              f"({', '.join(sorted(PRIMITIVES))})")
            names_in = {cells(l)[0].casefold() for l in table["body"].splitlines() if l.strip().startswith("|")}
            for item in items:
                if item.casefold() not in names_in:
                    errors.append(f"{where}: Shape item {item} is no Element of the table (Decisions file)")
            lowered = [i.casefold() for i in items]
            for l in table["body"].splitlines():
                if l.strip().startswith("|") and (element := cells(l)[0]).casefold() in names_in - {"element", "---"} and not set(element) <= set("-: "):
                    if lowered.count(element.casefold()) != 1:
                        errors.append(f"{where}: Element {element} is not in the Shape (Decisions file)" if not lowered.count(element.casefold())
                                      else f"{where}: {element} is twice in the Shape (Decisions file)")
            stack, count, paths = [], 0, {}
            for word, opens, close in re.findall(r"([^(),]+)(\()?|(\))", shape.group(1)):
                if opens == "(":
                    count += 1
                    stack.append(count)
                elif close:
                    stack.pop()
                elif word.strip():
                    paths.setdefault(word.strip().casefold(), tuple(stack))
            groups = {}
            for l in table["body"].splitlines():
                row = cells(l) if l.strip().startswith("|") else []
                if len(row) == len(COLUMNS) and row[0].casefold() in paths:
                    groups.setdefault(row[2], []).append(row[0])
            for group, members in groups.items():
                if len(members) < 2 or group == "—":  # items of no group are only ever foreign
                    continue
                prefix = os.path.commonprefix([paths[m.casefold()] for m in members])
                for other, mates in groups.items():
                    for m in mates if other != group else []:
                        if paths[m.casefold()][:len(prefix)] == prefix:
                            errors.append(f"{where}: group {group} shares its primitive with {m} of group {other} (Layout primitives)")
        rows = [cells(l) for l in table["body"].splitlines() if l.strip().startswith("|")]
        if not rows or rows[0] != COLUMNS:
            errors.append(f"{where}: the table must start with | {' | '.join(COLUMNS)} |")
            continue
        body = rows[2:]
        if not body:
            errors.append(f"{where}: the table has no row")
        for row in body:
            name = row[0] if row else "?"
            if len(row) != len(COLUMNS):
                errors.append(f"{where}, {name}: {len(row)} cells instead of {len(COLUMNS)}")
                continue
            empty = [c for c, v in zip(COLUMNS, row) if not v]
            if empty:
                errors.append(f"{where}, {name}: empty {', '.join(empty)}")
            if row[3] and row[3] not in LEVELS:
                errors.append(f"{where}, {name}: Level is {row[3]}, not Primary, Secondary, Tertiary or —")
            rest = row[6].lower()
            for rule in names:
                rest = re.sub(rf"(?<![\w-]){re.escape(rule)}(?![\w-])", ",", rest)
            unknown = [p.strip() for p in rest.split(",") if p.strip(" ;·")]
            if unknown:
                near = [f"{u} → {', '.join(m)}" for u in unknown if (m := difflib.get_close_matches(u, names, 3, 0.6))]
                errors.append(f"{where}, {name}: Rule cites {', '.join(unknown)}, not a heading or bold rule name "
                              f"of SKILL.md or references/ (never a file name)"
                              + (f"; nearest: {'; '.join(near)}" if near else "")
                              + "; a value with no rule behind it is a question for the user")
        full = [r for r in body if len(r) == len(COLUMNS)]
        named = re.search(r"(?m)^Primary group:\s*(.+?)\s*$", table["body"])
        if not named:
            errors.append(f"{where}: no Primary group line (Primary group: [group])")
        elif named.group(1) not in {r[2] for r in full}:
            errors.append(f"{where}: Primary group {named.group(1)} is not a group of the table")
        errors += check_values(where, full, roles, colors, spaces, components, named and named.group(1), items)
    return errors
