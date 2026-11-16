#!/usr/bin/env python3
"""Kore hook for Claude Code, called by hooks/hooks.json with the hook's
JSON on stdin. Exit code 2 sends stderr to Claude; every other case exits 0
and stays silent, or adds a note to Claude's context (additionalContext).
The hook never blocks a write.

PostToolUse on Edit, Write and MultiEdit:
- KORE-DECISIONS.md: checks its form (heading with files, Shape, the seven
  columns, Level, rule names that exist in Kore) and shows Claude every
  error. A valid table that changed waits for the next user message.
  Values are checked against the tokens of its Typology: line (minimalism without one).
- an interface file: runs kore_check on the project's changed files and
  shows Claude the ✗ of the files just written and of the whole project,
  each finding once per session (older code, such as a
  framework's template, is not this edit's work). Silent for another kind of file, a project without
  Kore's token file, only ? findings, or kore_check itself failing. In a
  Kore project the edit also leaves a mark for the session, and a file no
  table of KORE-DECISIONS.md names, or whose table the user has not seen
  yet, gets a note once per session; plain script files (.js, .ts) stay
  quiet unless kore_check finds something. The token
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
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from kore_check import (MARKUP_FILES, SCRIPT_FILES, STYLE_FILES, UNCHECKED_STYLES, skipped)
from kore_hierarchy import needs_table, tables, validate

UI_FILES = {*STYLE_FILES, *UNCHECKED_STYLES, *MARKUP_FILES, *SCRIPT_FILES}
KORE = Path(__file__).resolve().parent.parent
CHECK = KORE / "scripts" / "kore_check.py"
DECISIONS = "KORE-DECISIONS.md"


def data_file(event, name):
    """A file of this session in the plugin's data folder."""
    folder = Path(os.environ.get("CLAUDE_PLUGIN_DATA") or tempfile.gettempdir())
    session = re.sub(r"[^\w-]", "", str(event.get("session_id") or "session"))
    return folder / f"kore-{name}-{session}"


def mark(event):
    """The file that says interface files were edited in this session."""
    return data_file(event, "edited")


# ---------------------------------------------------------------- decisions

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
    """A reminder, once per file and session, when an interface file's table in
    KORE-DECISIONS.md is not yet seen by the user or has errors.
    It never blocks: the edit stays."""
    try:
        rel = edited.resolve().relative_to(Path(project).resolve()).as_posix()
        text = edited.read_text(encoding="utf-8", errors="ignore")
    except (ValueError, OSError):
        return ""
    if not needs_table(edited, text):
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
    else:  # no table names the file: kore_check reports it
        return ""
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
        dirs[:] = [d for d in dirs if not skipped(d)]
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
    # Only what this write is responsible for (the files just written and the
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
