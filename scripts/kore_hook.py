#!/usr/bin/env python3
"""Kore hook for Claude Code, called by hooks/hooks.json with the hook's
JSON on stdin. Exit code 2 sends stderr to Claude; every other case exits 0
and stays silent, or adds a note to Claude's context (additionalContext).
Like impeccable on Claude Code, the hook never blocks a write.

PostToolUse on Edit, Write and MultiEdit:
- KORE-DECISIONS.md: checks its form (heading with files, Shape, the seven
  columns, Level, rule names that exist in Kore) and shows Claude every
  error. A valid table that changed waits for the next user message.
  Values are checked against the tokens of its Typology: line (minimalism without one).
- an interface file: runs kore_check on the project's changed files and
  shows Claude the ✗ of the files just written and of the whole project,
  each finding once per session (as impeccable: older code, such as a
  framework's template, is not this edit's work). Silent for another kind of file, a project without
  Kore's token file, only ? findings, or kore_check itself failing. In a
  Kore project the edit also leaves a mark for the session, and a file no
  table of KORE-DECISIONS.md names, or whose table the user has not seen
  yet, gets a note once per session; plain script files (.js, .ts) stay
  quiet unless kore_check finds something, as in impeccable. The token
  file never gets the note (question 2).

PostToolUse on Bash: the files the command changed (newer than the hook's
last look) get the same checks as an Edit or Write of them; a kore_check
run with --url that prints 0 ✗ and opened the browser clears the mark.

SessionStart: the tables already in KORE-DECISIONS.md count as seen.

UserPromptSubmit: the tables written since the last user message count as
seen; the user's messages are counted.

PostToolUse on Skill: the Kore skill started. On AskUserQuestion: the agent
asked, and the answer counts as a user message for the tables. PRODUCT.md or interface
code written before any answer (one user message, no question tool) gets a
note once per session: the open questions come first.

Stop: when the mark is there, Claude is stopped once with the reminder to
run references/checks.md and kore_check with --url before delivering. The
mark goes either way, so the reminder comes once per edit and never loops.
"""
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from check_references import tokens_for
from kore_check import (MARKUP_FILES, SCRIPT_FILES, SKIP_DIRS, STYLE_FILES, UNCHECKED_STYLES, typology_line,
                        typology_names)

UI_FILES = {*STYLE_FILES, *UNCHECKED_STYLES, *MARKUP_FILES, *SCRIPT_FILES}
KORE = Path(__file__).resolve().parent.parent
CHECK = KORE / "scripts" / "kore_check.py"
DECISIONS = "KORE-DECISIONS.md"
COLUMNS = ["Element", "Question", "Group", "Level", "Style", "Space", "Rule"]
LEVELS = {"Primary", "Secondary", "Tertiary", "—"}
PRIMITIVES = {"Stack", "Inline", "Sidebar", "Grid"}
SCRIPTS = {".js", ".ts", ".mjs", ".cjs", ".mts", ".cts"}  # no markup of their own
TOKENS = re.compile(r"--canvas\s*:")


def data_file(event, name):
    """A file of this session in the plugin's data folder."""
    folder = Path(os.environ.get("CLAUDE_PLUGIN_DATA") or tempfile.gettempdir())
    session = re.sub(r"[^\w-]", "", str(event.get("session_id") or "session"))
    return folder / f"kore-{name}-{session}"


def mark(event):
    """The file that says interface files were edited in this session."""
    return data_file(event, "edited")


# ---------------------------------------------------------------- decisions

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
    """Type roles ({role: (size, weight)}), color names and space names of
    references/tokens.yaml, the typology's tokens.yaml replacing and adding keys."""
    roles, colors, spaces = {}, set(), set()
    for name, entries in tokens_for(kore, typology).items():
        for path, value in entries:
            if path[0] == "typography" and path[-1] in ("fontSize", "fontWeight"):
                roles.setdefault(path[1], [0, 0])[path[-1] == "fontWeight"] = int(re.sub(r"\D", "", value))
            elif path[0] == "colors":
                colors.add(name)
            elif path[0] == "spacing":
                spaces.add(name)
    return {r: tuple(v) for r, v in roles.items()}, colors, spaces


def component_names():
    return {(p.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ").strip().lower())
            for p in (KORE / "references" / "components").glob("*.md")}


def check_values(where, body, roles, colors, spaces, components):
    """The values of each row against the rules they come from: Roles and
    sizes, From role to style, Typographic levels, the space scale."""
    errors, groups = [], {}
    bodies = sorted((r for r in roles if r.startswith("body-")), key=lambda r: -roles[r][0])
    for row in body:
        name, group, level, style, space, rule = row[0], row[2], row[3], row[4], row[5], row[6].lower()
        words = style.split()
        role = next((w for w in words if w in roles), None)
        if level == "—" and not (re.search(r"\bh[1-6]\b|\b\d+:\d+\b", f"{name} {style}") or (role or "").startswith("label-")
                                 or any(re.search(rf"\b{re.escape(c)}\b", style.lower()) for c in components)):
            errors.append(f"{where}, {name}: Level — is only for a heading, a label, a whole component or an image; "
                          "this element takes Primary, Secondary or Tertiary (Semantic weight)")
        if space != "—":
            named = re.findall(r"space-\d+", space)
            if not named or set(named) - spaces:
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
        below = [b for b in bodies if roles[b][0] <= size]
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
    return errors


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
        if not shape:
            errors.append(f"{where}: no Shape line")
        else:
            used = re.findall(r"^\s*(\w+)|(\w+)\s*\(", shape.group(1))
            wrong = {a or b for a, b in used} - PRIMITIVES
            if wrong:
                errors.append(f"{where}: Shape uses {', '.join(sorted(wrong))}, not a Layout primitive "
                              f"({', '.join(sorted(PRIMITIVES))})")
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
        errors += check_values(where, full, roles, colors, spaces, components)
    return errors


EMPTY = {"seen": {}, "waiting": {}, "reminded": {}, "prompts": 0, "asked": False, "kore": False, "shown": []}


def load_state(event, project):
    """Tables seen by the user and tables waiting, user messages and whether
    the agent asked with its question tool. Without a state nothing is seen:
    only SessionStart counts the tables already there as seen."""
    path = data_file(event, "decisions")
    return {**EMPTY, **(json.loads(path.read_text()) if path.exists() else {})}


def before_session(event, project):
    """The tables in KORE-DECISIONS.md when the session starts come from an
    earlier session: they count as seen. A resumed or compacted session
    keeps its state."""
    if data_file(event, "decisions").exists():
        return 0
    file = Path(project) / DECISIONS
    text = file.read_text(encoding="utf-8") if file.exists() else ""
    save_state(event, {**EMPTY, "seen": {t["heading"]: t["hash"] for t in tables(text)}})
    stamp(event).parent.mkdir(parents=True, exist_ok=True)
    stamp(event).touch()
    return 0


def questions_note(event, project, written):
    """Once per session, after the Kore skill started: PRODUCT.md or interface
    code written while the user has sent only the request and the agent used
    no question tool."""
    if not any(p.name.lower() == "product.md" or p.suffix.lower() in UI_FILES for p in written):
        return ""
    state = load_state(event, project)
    if not state["kore"] or state["asked"] or state["prompts"] > 1 or state["reminded"].get("questions"):
        return ""
    state["reminded"]["questions"] = True
    save_state(event, state)
    return ("Kore: written before any answer from the user. Unless the request or the project answers every one, "
            "ask the open questions first (Before the first line of code): the language is never inferred, "
            "not even from the language the user writes in.")


def save_state(event, state):
    path = data_file(event, "decisions")
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f"{path.name}.{os.getpid()}")
    temp.write_text(json.dumps(state))
    os.replace(temp, path)  # one step: a hook running beside this one never reads a half-written file


def decisions_note(event, project, edited):
    """A reminder, once per file and session, when an interface file has no
    table in KORE-DECISIONS.md or its table is not yet seen by the user.
    It never blocks: like impeccable on Claude Code, the edit stays."""
    try:
        rel = edited.resolve().relative_to(Path(project).resolve()).as_posix()
        text = edited.read_text(encoding="utf-8", errors="ignore")
    except (ValueError, OSError):
        return ""
    if TOKENS.search(text) or edited.suffix.lower() in SCRIPTS:
        return ""
    state = load_state(event, project)
    file = Path(project) / DECISIONS
    named = [t for t in tables(file.read_text(encoding="utf-8") if file.exists() else "") if rel in t["files"]]
    if any(state["seen"].get(t["heading"]) == t["hash"] for t in named):
        return ""
    waiting = any(state["waiting"].get(t["heading"]) == t["hash"] for t in named)
    if named and not waiting:  # written where the hook did not see it: validate it now
        waiting = not any(e.startswith(f"## {t['heading']}") for t in named
                          for e in validate(file.read_text(encoding="utf-8")))
    if waiting:
        reason = "waiting"
        note = (f"Kore: the table for {rel} in {DECISIONS} is not yet seen by the user. Show them the summary "
                "and wait for the OK before more code (Building anything, step 3).")
    elif named:
        reason = "invalid"
        note = (f"Kore: the table for {rel} in {DECISIONS} has errors. Fix them, show the user the summary "
                "and wait for the OK (Building anything, step 3; Decisions file).")
    else:
        reason = "missing"
        note = (f"Kore: {rel} has no table in {DECISIONS}. Write the Order of decisions for it, with the file "
                "in the table's heading, show the user the summary and wait for the OK "
                "(Building anything, step 3; Decisions file).")
    if state["reminded"].get(rel) == reason:
        return ""
    state["reminded"][rel] = reason
    save_state(event, state)
    return note


def after_decisions(event, project, path, errors):
    """Adds the table's errors to errors; a valid table that changed waits
    for the next user message."""
    found = validate(path.read_text(encoding="utf-8"))
    if found:
        errors += [f"Kore: fix {DECISIONS} (Decisions file):", *found]
        return True
    state = load_state(event, project)
    for table in tables(path.read_text(encoding="utf-8")):
        if state["seen"].get(table["heading"]) != table["hash"]:
            state["waiting"][table["heading"]] = table["hash"]
    save_state(event, state)
    return False


def before_prompt(event, project):
    stamp(event).parent.mkdir(parents=True, exist_ok=True)
    stamp(event).touch()
    state = load_state(event, project)
    state["prompts"] += 1
    state["seen"].update(state["waiting"])
    state["waiting"] = {}
    save_state(event, state)
    return 0


# ---------------------------------------------------------------- checks

def stamp(event):
    """When the hook last looked at the project: files changed after it were
    written by a tool the hook did not see edit them (Bash)."""
    return data_file(event, "stamp")


def changed_since(event, project):
    """Files of the project modified after the stamp; none without a stamp."""
    if not stamp(event).exists():
        return []
    since, found = stamp(event).stat().st_mtime, []
    for folder, dirs, files in os.walk(project):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = Path(folder) / name
            try:
                if path.stat().st_mtime > since:
                    found.append(path)
            except OSError:
                continue
    return found


def after_interface(event, project, edited):
    """kore_check on the changed files after interface files were written;
    the note of each file without a seen table. Returns (errors, notes)."""
    result = subprocess.run([sys.executable, str(CHECK), project, "--changed"],
                            capture_output=True, text=True)
    if result.returncode not in (0, 1) or "no token file defining --canvas" in result.stdout:
        return [], []
    mark(event).parent.mkdir(parents=True, exist_ok=True)
    mark(event).touch()
    notes = [n for n in (decisions_note(event, project, path) for path in edited) if n]
    # Like impeccable: only what this write is responsible for (the files just written and the
    # whole-project checks), and never a finding already shown in the session.
    files = set()
    for path in edited:
        try:
            files.add(path.resolve().relative_to(Path(project).resolve()).as_posix())
        except (ValueError, OSError):
            continue
    state = load_state(event, project)
    errors = []
    for line in result.stdout.splitlines():
        where = line[2:].split(" · ", 1)[0] if line.startswith("✗") else None
        if where is None or (where != "project" and where.rsplit(":", 1)[0] not in files):
            continue
        key = re.sub(r":\d+ · ", " · ", line)  # the same finding after lines moved
        if key not in state["shown"]:
            state["shown"].append(key)
            errors.append(line)
    save_state(event, state)
    if errors:
        errors.insert(0, "Kore check: triage every ✗ before going on (references/checks.md). A real problem: fix it. "
                         "A false positive you can prove: waive it with `kore-ignore-next-line <Rule>: <who decided: "
                         "evidence>` above the line, and say so in your reply. Unsure: ask the user in one line.")
    return errors, notes


def after_tool(event, project):
    """After Edit and Write, the file they name; after Bash, every file it
    changed (a heredoc or a script writes files the hook would not see)."""
    tool_input = event.get("tool_input") or {}
    if event.get("tool_name") in ("AskUserQuestion", "Skill"):
        state = load_state(event, project)
        if event.get("tool_name") == "AskUserQuestion":
            state["asked"] = True
            state["seen"].update(state["waiting"])  # an answer is a user message: the tables were seen
            state["waiting"] = {}
        elif tool_input.get("skill", "").split(":")[-1] == "kore":
            state["kore"] = True
        save_state(event, state)
        return 0
    if event.get("tool_name") == "Bash":
        written = changed_since(event, project)
    else:
        written = [Path(tool_input.get("file_path", ""))]
    stamp(event).parent.mkdir(parents=True, exist_ok=True)
    stamp(event).touch()
    errors, notes = [], []
    notes += [n for n in [questions_note(event, project, written)] if n]
    decisions = [p for p in written if p.name == DECISIONS and p.exists()]
    if decisions:
        after_decisions(event, project, decisions[0], errors)
    interface = [p for p in written if p.suffix.lower() in UI_FILES]
    if interface:
        found, more = after_interface(event, project, interface)
        errors += found
        notes += more
    if event.get("tool_name") == "Bash":
        command = tool_input.get("command", "")
        response = event.get("tool_response") or {}
        output = response.get("stdout", "") if isinstance(response, dict) else str(response)
        passed = re.search(r"(?m)^0 ✗", output) and "not checked in a browser" not in output
        if "kore_check" in command and "--url" in command and passed and mark(event).exists():
            mark(event).unlink()
    if errors:
        print("\n".join(errors + notes), file=sys.stderr)
        return 2
    if notes:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "\n".join(notes)}}))
    return 0


def before_stop(event, project):
    if not mark(event).exists():
        return 0
    mark(event).unlink()
    if event.get("stop_hook_active"):
        return 0
    print("Kore: interface files changed. Before delivering, go through references/checks.md box by box "
          f"and run python3 {CHECK} {project} --url <page> with one --url for each page built or changed "
          "(Measure); the work is finished only when it exits with 0.", file=sys.stderr)
    return 2


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    project = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or "."
    name = event.get("hook_event_name")
    if name == "Stop":
        return before_stop(event, project)
    if name == "UserPromptSubmit":
        return before_prompt(event, project)
    if name == "SessionStart":
        return before_session(event, project)
    return after_tool(event, project)


if __name__ == "__main__":
    sys.exit(main())
