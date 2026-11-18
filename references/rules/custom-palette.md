# Custom palette

**Own palette.** A project may replace Kore's colors with its own. The user gives a few base colors; every other token is derived with fixed rules, so the result keeps Kore's contrast and surface steps without choosing each token by hand.

**The three base colors:** `canvas` (the page background), `primary` (the main action) and `accent` (emphasis). Every other token is derived from them or keeps Kore's value, and everything above the `canvas` meets WCAG 2.1 and 2.2 (Contrast).

**How many colors the user gives.** The user may give any number.

| Colors given | What to do |
|---|---|
| 0 | Propose, in this order, Kore's own palette (recommended) and the palettes of `references/candidates.md`. The user picks one. Kore's palette is used as it is; a palette of `references/candidates.md` gives the three base colors, and the script derives every other token |
| 1 | Ask which role it has: `canvas`, `primary` or `accent`. Then ask for the other two. Each one the user does not have follows Missing colors |
| 2 | Ask which is `canvas` and which is `primary`, and whether the user has an `accent`. If not, Missing colors |
| 3 | Ask which is `canvas`, which is `primary` and which is `accent` |
| 4 or more | Ask the user to choose a `canvas`, a `primary` and an `accent` among them, and say why three: `canvas` carries every surface, `primary` the main action, `accent` the rare emphasis, and every other token is derived from these three (Derived tokens); a fourth color would be a second emphasis, which The accent is rare forbids, so the other colors are not used. If the user picks no `accent`, Missing colors |

**The script.** `scripts/kore_palette.py` does every computation of this section: run it with the colors already set, each as `--<role> <theme>=<hex>` (the theme it was given for), and `--themes` with the themes chosen at question 9. It prints every token with its contrast, and one line for each case below; act on each line as its case says.

**Missing colors.** One color at a time, in the order `canvas`, `primary`, `accent`:
1. **Ask** the user for it.
2. **Candidate.** If the user has none, run the script. Its line "Missing colors, step (2)" names a candidate of `references/candidates.md`: propose it and wait for the OK. If the user declines, use the derived value that line gives. If the line says no candidate passes, use the derived value it gives.
3. **Next.** Run the script again with the color just set, for the next missing one.

**How the script picks.** The candidate is the one that passes Contrast with the colors already set, a `canvas` on the tokens derived from it alone, and whose hue is closest to the derived value (for a `canvas`, closest to `primary`'s hue). The derived values come from Huecode (github.com/larisabarabas/huecode, commit `68b88c9`), run on `primary`: `canvas` is Huecode's `--bg`; `accent` is the step of Huecode's accent scale (`primary`'s hue +180°) whose HSL lightness is nearest 50 in light and 65 in dark, among all 11 steps. A missing `primary` takes `canvas` hue, HCT chroma 36 and tone 40 in light, 80 in dark. A gray color, below HCT chroma 5, gives Kore's value: a gray `primary` for `accent`, a gray `canvas` for `primary` and `accent`.

**A color that fails.**
- **Canvas that fails.** A `canvas` fails when a text, border or icon token cannot reach its minimum in Contrast on a surface derived from it. Say so and propose both ways, the second recommended because it keeps the user's color: another `canvas`, or the value the script's line gives (same hue and chroma, tone 98 in light and 3 in dark). If the user has no other `canvas`, use that value.
- **Pure white or black canvas.** A `canvas` at tone 100 or 0 leaves no room for the surfaces above or below it: the script moves its tone to 98 in light and 3 in dark, keeping its hue and chroma. Tell the user.
- **Any other color** that cannot reach its minimum even at tone 0 or 100: ask the user for another.

**Themes.** Colors are counted once per project, by role. A given color is used as it is in the theme it was given for, unless A color that fails or Method step 3 moves it; for the other shipped theme the script takes it from Huecode: `canvas` is Huecode's `--bg`; `primary` is the step of Huecode's primary scale whose HSL lightness is nearest 50 among steps 500, 600, 700 in light, nearest 65 among 300, 400, 500 in dark; `accent` is the step of Huecode's shade scale of the given `accent` nearest the same lightness, among all 11 steps. A project that ships one theme derives nothing for the other. Every other token follows the table.

**Derived tokens.** The tokens come from Huecode's palette of `primary`: its CSS variables (`--surface`, `--text`, ...) and the steps of its scales (neutral 100, ...), as `kore_palette.py` computes them. Tone is HCT tone (0–100, equal to CIELAB L\*).

| Token | Rule, light | Rule, dark | Check |
|---|---|---|---|
| `ink` | Huecode's `--text` | same | 4.5:1 on every surface; moves along the neutral scale |
| `surface-card` | `--surface` | `--surface` | — |
| `surface-elevated` | `--surface-2` | `--surface-2` | — |
| `surface-deep` | `--surface` | neutral 950 | — |
| `surface-float` | `--surface` | `--surface-2` | Floating layers must be lighter than `canvas` and `surface-card` in dark |
| `surface-float-active` | `--surface-2` | `--surface-2` | — |
| `surface-hover` | `--surface-2` | `--surface-2` | — |
| `surface-pressed` | neutral 100 | `--surface-2` | — |
| `body` | `ink` at 86% opacity | same | 4.5:1 |
| `mute` | The step of the neutral scale nearest `canvas` that passes on every surface | same | 4.5:1 |
| `hairline-medium` | `--border` | `--border` | — (below 3:1 by choice) |
| `hairline-strong` | `--border-strong` | `--border-strong` | 3:1; moves along the neutral scale |
| `stone` | neutral 400 | neutral 500 | exempt only where Contrast says so |
| `hairline` | `ink` at 6% opacity | same | none, meant to be barely visible |
| `primary-on` | Huecode's `--accent-fg`: white or black, whichever contrasts more | same | 4.5:1 |
| `primary-pressed` | Huecode's `--accent-hover` | same | `primary-on` still 4.5:1; if not, it moves along the primary scale |
| `danger`, `warning`, `success`, `info` | Kore's values | same | 4.5:1 |
| `danger-on` | White or black, whichever contrasts more with `danger` | same | 4.5:1 |
| `danger-pressed` | `danger` moved 6 tones toward `canvas` | same | `danger-on` still 4.5:1; if not, it moves as a fill, as Method step 3 says |
| `primary-edge`, `danger-edge`, `surface-card-edge` | The raised button's outside border: its fill (`primary`, `danger`, `surface-card`) mixed in sRGB, 80% with 20% black | same | — (below 3:1 by choice: the label identifies the button) |
| `link` | `info` | same | 4.5:1 |
| `focus-ring` | `hairline-strong` | same | 3:1 |
| `*-glow`, `selection` | The color (for `selection`, `accent`) at 20% opacity | The color at the lowest opacity, raised 1% at a time, at which it reaches 1.5:1 against the worst derived surface; if the text over it fails 4.5:1 there, the glow is not used | `ink` and `body` over a glow, and `ink` over `selection`, 4.5:1 |
| `scrim` | Kore's value | Kore's value | — |
| `veil-photo`, `veil-cover`, `on-photo`, `on-photo-mute` | Kore's values: the veils over a photo and the text on it | same | — |
| `vivid-info`, `vivid-success`, `vivid-warning`, `vivid-danger` | The dark theme's `info`, `success`, `warning`, `danger`, or in a project with no dark theme Kore's dark values: a kind's vivid value, behind its icon (Alert) | same | — |
| `on-vivid` | The dark theme's `canvas`, or in a project with no dark theme `canvas` hue and chroma at tone 3: the icon on a kind's vivid value (Alert) | same | 3:1 on each `vivid-*`; if not, it moves its tone away from them, one tone at a time |
| `chart-1` … `chart-8` | Kore's values, never derived: the dataviz reference palette, validated as a set for color blindness | same | adjacent pairs ΔE ≥ 8 under color blindness (Charts) |

**Method:**

1. **Base colors.** Take the base colors from the project or from the user, following How many colors the user gives and Themes.
2. **Derive.** Derive every token with the table. Kore's own palette is not derived: it is `references/tokens.yaml` as it is.
3. **Measure.** Measure every color token drawn over a surface (text, icons, borders, focus marks, on-colors, chart marks) on every derived surface, in each theme the project ships; the lowest ratio decides. `danger`, `warning`, `success` and `info` are measured as text, at 4.5:1; `accent` as large text, at 3:1 (The accent is rare). Surfaces, `scrim` and `veil-*` have no contrast of their own and are not measured; `on-photo` and `on-photo-mute` are not measured, because the photo is not known; `*-glow` and `selection` follow their row. `chart-1` … `chart-8` are measured too, but a failing one keeps its value and follows Contrast (legend or direct labels), because the set is validated together for color blindness. A token whose row names a scale (`ink`, `hairline-strong`, `primary-pressed`) takes the next step of that scale toward more contrast, the first that passes; at the end of the scale it cannot be used. Any other token that fails moves its tone away from the surface it sits on: down in light, up in dark. It moves one tone at a time and stops at the first value that passes on its worst surface (Contrast), keeping hue and chroma. `primary-on` and `danger-on` always pass on their fill (the better of white and black reaches at least 4.58:1 on any solid color); a pressed fill (`primary-pressed`, `danger-pressed`) that fails keeps its on-color and moves its tone away from it, one tone at a time, until the on-color passes. A token that reaches tone 0 or 100 without passing cannot be used: ask the user for another color.
4. **Approve.** Show one table: token, value, contrast and, for every value that is not the user's or that moved, where it comes from: derived, candidate, Kore's value or moved to pass Contrast. Wait for the user's OK, then write the project's tokens.
