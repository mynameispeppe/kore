"""Usability (references/rules/usability.md), Script errors: the page loads and scrolls through with no uncaught exception and no console.error."""


def listen(page, errors):
    """Appends to errors one line per script error of page, from now on."""
    page.on("pageerror", lambda error: errors.append(f"{error.name}: {error.message}".split("\n")[0]))
    # A message the browser writes itself (a file that fails to load, a CORS block) has no args; a console.error call has at least one.
    page.on("console", lambda message: errors.append(message.text.split("\n")[0]) if message.type == "error" and message.args else None)
