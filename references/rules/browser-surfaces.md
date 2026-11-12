# Browser surfaces

**The parts the browser draws** still carry the design. Theme them from the palette instead of shipping browser defaults:

- **Text selection:** `selection` background, `ink` text.
- **Caret:** `ink` (or `accent` in inputs that deserve emphasis).
- **Focus:** see States, in `references/rules/color.md`.
- **Scrollbars:** thin, `hairline-strong` thumb on a transparent track, visible only while the content scrolls and hidden shortly after, where the platform allows it.
- **Links in running text:** `link` color, underline with a 4px offset, thickness 1px. Links in a list (Footer, Social links) follow their component.
- **Numerals:** tabular figures in tables and data.
