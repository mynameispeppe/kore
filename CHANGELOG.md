# Changelog

All notable changes to Kore are listed here. Versioning follows [semver](https://semver.org): **MAJOR** for breaking changes (renamed or removed tokens, changed scales), **MINOR** for compatible additions (new components or variants), **PATCH** for fixes that don't change usage.

## Unreleased

Working toward 1.0.0, the first public release. The list of changes will be written before the release; until then the history is in the git log.

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
