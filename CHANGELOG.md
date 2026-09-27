# Changelog

All notable changes to Kore are listed here. Versioning follows [semver](https://semver.org): **MAJOR** for breaking changes (renamed or removed tokens, changed scales), **MINOR** for compatible additions (new components or variants), **PATCH** for fixes that don't change usage.

## Unreleased

Working toward 1.0.0, the first public release.

- Start here: at most three questions before a project (landing page or web app, framework, brand identity), defaults for everything asked later, and behaviour rules, including how to handle an explicit request to break a binding or accessibility rule. This file is never edited during a project; chosen values live in the project's tokens.
- Start here: fonts outside the Candidates allowed, one font may cover `display` and `sans` with the type scale unchanged; checks for weights, glyphs, tabular figures and web license; system monospace stack for code in single-font projects.
- Color rules: Custom palette, a method to apply a project's own palette from four base colors per theme, with derivation rules and contrast checks for every other token, plus the WCAG contrast ratio formula.
- The Library-First Rule: library sizes and behaviours that break no binding rule stay as they are; typical overrides listed; theming through the library's API.
- Hierarchy: one `h1` per page, no inverted hierarchy (metadata never outweighs its title), focal point placed on a third of the layout.
- Start here: where the accessibility rules live; Building anything, the five steps for any component or screen.
- Colors: new `surface-float` (`#fcfdfd` / `#1c1c1c`) and `surface-float-active` (`#f4f6f7` / `#2a2a2a`) for floating layers. In dark, menus used `surface-deep`, darker than the canvas, and disappeared on some screens; floating layers are now lighter than the canvas and the cards.
- Elevation: floating and overlay levels use `surface-float`; in dark, a higher layer is always lighter.
- Focus: one style everywhere, a 2px border drawn inside the control with no outer ring; `ink` on empty controls, the foreground color on filled ones, `accent-red` on fields with an error.
- Components: password with live requirements, combobox, number stepper, file upload and slider.
- Start here: Checks by context replaces the separate checklists (Spacing pre-delivery checklist, Three-second check): three checks always, plus one row per kind of work (container, control, overlay, feedback, screen); results are reported at delivery; reused code goes through the same checks.
- List rows: `space-2` (8px) between rows, so two highlights never touch.
- Shapes: The Radius-Padding Rule (side-aligned content starts on the corner curve's centre: horizontal padding = radius, reduce the radius when the padding is smaller; centered content exempt).
- Shapes: The Concentric Rule replaces The Half-Padding Rule: inner radius = outer radius − distance, so nested curves share one centre. Menu options now radius 8, row highlights 12, compact card 16.
- Inline buttons: inside a control they sit 8px from every edge, size = container height − 16, radius = container radius − 8 (password toggle, stepper, segments, file row remove).
- Spacing: The Distance Ratio Rule replaces "one step apart": space between groups ≥ 2 × space inside. Card rows now 12 (compact 8), rows ↔ actions 32. Rules for alignment, density and grouping actions.
- Hierarchy: action order, right-aligned with the confirming action last and cancel or back to its left.
- Cards: compact cards drop inner blocks and separate rows with space; new media card and card with actions (actions at the bottom, placed by The Concentric Rule, at least 320px wide, stacking instead of wrapping); each card as tall as its content.
- Icons: Hugeicons always in the free set; the Pro set only on the user's request and license.

## 0.1.0

First draft, reviewed point by point. The full step-by-step history is in the git log.

- Colors: dual-theme palette (Ice light canvas `#F8FAFB`, Night dark canvas `#0C090A`) with surface, border, text, brand, signature and semantic tokens, all checked against WCAG contrast.
- Typography: Outfit for display, Figtree for body and UI, Geist Mono for code; a full type scale with line-heights on the 4px grid.
- Spacing: `space-N` = N × 4px on an 8-point grid, with binding rules, proximity guidance and a pre-delivery checklist.
- Shapes: rounded scale 0 / 4 / 8 / 12 / 16 / 24 / full and The Half-Padding Rule for nested corners.
- Elevation: shadows only on interactive elements, hairline borders elsewhere (The Hairline Rule), a fixed z-index scale.
- Responsive, Motion (app and landing modes), Browser surfaces, Icons (Hugeicons by default), Hierarchy and Usability (Nielsen's 10 heuristics) sections.
- Overview with the guiding principle *Calm Clarity*, and Do's and Don'ts.
- Components: The Library-First Rule; Button, form controls (text input, textarea, select, checkbox, radio, switch, segmented control), cards and list rows.
- Candidates: alternative values for colors, fonts, type sizes and radius sets.
