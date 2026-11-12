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

**How the script picks.** The candidate is the one that passes Contrast with the colors already set, a `canvas` on the tokens derived from it alone, and whose hue is closest to the derived value. The derived values follow the Material Color Utilities scheme `TONAL_SPOT`, file `dynamic_scheme.ts`, for `canvas` and `primary`, and the palettable.dev cell Analogous, row 0, column 8 for `accent`; a gray color, below HCT chroma 5, gives Kore's value for its role.

**A color that fails.**
- **Canvas that fails.** A `canvas` fails when a text, border or icon token cannot reach its minimum in Contrast on a surface derived from it. Say so and propose both ways, the second recommended because it keeps the user's color: another `canvas`, or the value the script's line gives (same hue and chroma, tone 98 in light and 3 in dark). If the user has no other `canvas`, use that value.
- **Pure white or black canvas.** A `canvas` at tone 100 or 0 leaves no room for the surfaces above or below it: the script moves its tone to 98 in light and 3 in dark, keeping its hue and chroma. Tell the user.
- **Any other color** that cannot reach its minimum even at tone 0 or 100: ask the user for another.

**Themes.** Colors are counted once per project, by role. A given color is used as it is in the theme it was given for, unless A color that fails or Method step 3 moves it; for the other shipped theme the script keeps its hue and chroma and moves its tone. A project that ships one theme derives nothing for the other. Every other token follows the table.

**Derived tokens.** Tone is HCT tone (0–100, equal to CIELAB L\*). Neutral tokens, the rows below that take `canvas` hue and chroma (the surfaces, `ink`, `mute`, `hairline-*` and `stone`), take at most HCT chroma 6.

| Token | Rule, light | Rule, dark | Check |
|---|---|---|---|
| `ink` | `canvas` hue and chroma; from tone 17 away from the surfaces, the first tone that passes | same hue and chroma; from tone 96, the first tone that passes | 4.5:1 on every surface |
| `surface-card` | `canvas` tone +1 | `canvas` tone +3 | — |
| `surface-elevated` | `canvas` tone −1.5 | `canvas` tone +9 | — |
| `surface-deep` | `canvas` tone +1 | `canvas` tone −1 | — |
| `surface-float` | `canvas` tone +1 | `canvas` tone +8 | Floating layers must be lighter than `canvas` and `surface-card` in dark |
| `surface-float-active` | `canvas` tone −1.5 | `surface-float` tone +7 | — |
| `surface-hover` | `canvas` tone −3.5 | `canvas` tone +9.5 | — |
| `surface-pressed` | `canvas` tone −6 | `canvas` tone +12 | — |
| `body` | `ink` at 86% opacity | same | 4.5:1 |
| `mute` | From `ink` toward `canvas`, one tone at a time, keeping hue and chroma; the last tone that still passes on the worst derived surface | same | 4.5:1 |
| `hairline-medium` | Solid, `canvas` tone −9.5 | Solid, `canvas` tone +16.5 | — (below 3:1 by choice) |
| `hairline-strong` | Solid, from `ink` toward `canvas`, one tone at a time, keeping hue and chroma; the last tone that still passes on the worst derived surface | same | 3:1 |
| `stone` | Halfway between `canvas` and `mute` in tone | same | exempt only where Contrast says so |
| `hairline` | `ink` at 6% opacity | same | none, meant to be barely visible |
| `primary-on` | White or black, whichever contrasts more with `primary` | same | 4.5:1 |
| `primary-pressed` | `primary` moved 6 tones toward `canvas` | same | `primary-on` still 4.5:1; if not, it moves as a fill, as Method step 3 says |
| `danger-on`, `danger-pressed` | As `primary-on` and `primary-pressed`, from `danger` | same | 4.5:1 |
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
2. **Derive.** Derive every token with the table. Kore's own values follow these rules within about 1 tone.
3. **Measure.** Measure every color token drawn over a surface (text, icons, borders, focus marks, on-colors, chart marks) on every derived surface, in each theme the project ships; the lowest ratio decides. `danger`, `warning`, `success` and `info` are measured as text, at 4.5:1; `accent` as large text, at 3:1 (The accent is rare). Surfaces, `scrim` and `veil-*` have no contrast of their own and are not measured; `on-photo` and `on-photo-mute` are not measured, because the photo is not known; `*-glow` and `selection` follow their row. `chart-1` … `chart-8` are measured too, but a failing one keeps its value and follows Contrast (legend or direct labels), because the set is validated together for color blindness. Any other token that fails moves its tone away from the surface it sits on: down in light, up in dark. It moves one tone at a time and stops at the first value that passes on its worst surface (Contrast), keeping hue and chroma. `primary-on` and `danger-on` always pass on their fill (the better of white and black reaches at least 4.58:1 on any solid color); a pressed fill (`primary-pressed`, `danger-pressed`) that fails keeps its on-color and moves its tone away from it, one tone at a time, until the on-color passes. A token that reaches tone 0 or 100 without passing cannot be used: ask the user for another color.
4. **Approve.** Show one table: token, value, contrast and, for every value that is not the user's or that moved, where it comes from: derived, candidate, Kore's value or moved to pass Contrast. Wait for the user's OK, then write the project's tokens.
