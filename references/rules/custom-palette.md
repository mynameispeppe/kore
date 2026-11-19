# Custom palette

**Own palette.** A project may replace Kore's colors with its own. Every token comes from one Palette with fixed rules, so the result keeps Kore's contrast and surface steps without choosing each token by hand.

**The four base colors:** `canvas` (the page background), `primary` (the main action), `accent` (emphasis) and `ink` (the text). Every other token is derived from them or keeps Kore's value, and everything above the `canvas` meets WCAG 2.1 and 2.2 (Contrast).

**Three ways to a Palette.** The user gives one color or none; a user who offers two or more colors picks one of them as the source of way 3.

| Way | What to do |
|---|---|
| 1. Kore's palette | Propose it first, as the recommended one. Method step 2 uses it as it is |
| 2. A palette of `references/candidates.md` | Propose the palettes after Kore's. The palette's four colors are the base colors as written: `background` is `canvas`, `primary`, `accent`, `text` is `ink`. The script derives every other token |
| 3. One color | The user's color is the source: the script derives the four base colors and every other token from it |

**The script.** `scripts/kore_palette.py` does every computation of this section, with `--themes` set to the themes chosen at question 9. Way 2: `--canvas`, `--primary`, `--accent` and `--ink`, each `light=<hex>,dark=<hex>`. Way 3: `--primary <hex>`. It prints every token with its contrast, and one line for each case below; act on each line as its case says.

**MCU.** The script derives with Material Color Utilities, scheme `SchemeFidelity`: way 3 runs it on the user's color, way 2 on each theme's `primary`. Tone is HCT tone (0–100, equal to CIELAB L\*).

**A color that fails.**
- **Canvas that fails.** A `canvas` fails when a text, border or icon token cannot reach its minimum in Contrast on a surface derived from it. Say so and propose both options, the second recommended because it keeps the palette's color: another palette, or the value the script's line gives (same hue and chroma, tone 98 in light and 3 in dark). If the user has no other palette, use that value.
- **Pure white or black canvas.** A `canvas` at tone 100 or 0 leaves no room for the surfaces above or below it: the script moves its tone to 98 in light and 3 in dark, keeping its hue and chroma. Tell the user.
- **Any other color** that cannot reach its minimum even at tone 0 or 100: ask the user for another palette or color.

**Themes.** Every way gives both themes: way 2 takes each theme's colors from the palette; way 3 derives both from the one color. A project that ships one theme uses that theme only. Every other token follows the table.

**Derived tokens.** Each row names the MCU role the token takes, or its rule.

| Token | Rule, light | Rule, dark | Check |
|---|---|---|---|
| `ink` | Way 2: the palette's `text`. Way 3: `onSurface` | same | 4.5:1 on every surface |
| `surface-card` | `surfaceContainerLowest` | `surfaceContainerLow` | — |
| `surface-elevated` | `surfaceContainer` | `surfaceContainer` | — |
| `surface-deep` | `surfaceContainerLowest` | `surfaceContainerLowest` | — |
| `surface-float` | `surfaceContainerLowest` | `surfaceContainerHigh` | Floating layers must be lighter than `canvas` and `surface-card` in dark |
| `surface-float-active` | `surfaceContainer` | `surfaceContainerHighest` | — |
| `surface-hover` | `ink` at 8% over `canvas`, mixed in sRGB: Material 3's hover state layer | same | — |
| `surface-pressed` | `ink` at 10% over `canvas`, mixed in sRGB: Material 3's pressed state layer | same | — |
| `body` | `ink` at 86% opacity | same | 4.5:1 |
| `mute` | `onSurfaceVariant` | same | 4.5:1; moves along MCU's neutral variant palette |
| `hairline-medium` | `outlineVariant` | same | — (below 3:1 by choice) |
| `hairline-strong` | `outline` | same | 3:1; moves along MCU's neutral variant palette |
| `stone` | `ink` at 38% over `canvas`, mixed in sRGB: Material 3's disabled state layer | same | exempt only where Contrast says so |
| `hairline` | `ink` at 6% opacity | same | none, meant to be barely visible |
| `primary-on` | `onPrimaryContainer` | same | 4.5:1 on `primary`; moves along MCU's primary palette, away from `primary` |
| `primary-pressed` | `primary-on` at 10% over `primary`, mixed in sRGB | same | `primary-on` still 4.5:1; if not, it moves as a fill, as Method step 3 says |
| `danger`, `warning`, `success`, `info` | Kore's values | same | 4.5:1 |
| `danger-on` | White or black, whichever contrasts more with `danger` | same | 4.5:1 |
| `danger-pressed` | `danger-on` at 10% over `danger`, mixed in sRGB | same | `danger-on` still 4.5:1; if not, it moves as a fill, as Method step 3 says |
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

1. **Base colors.** Take the base colors from the project or from the user, following Three ways to a Palette and Themes.
2. **Derive.** Derive every token with the table. Kore's own palette is not derived: it is `references/tokens.yaml` as it is.
3. **Measure.** Measure every color token drawn over a surface (text, icons, borders, focus marks, on-colors, chart marks) on every derived surface, in each theme the project ships; the lowest ratio decides. `danger`, `warning`, `success` and `info` are measured as text, at 4.5:1; `accent` as large text, at 3:1 (The accent is rare). Surfaces, `scrim` and `veil-*` have no contrast of their own and are not measured; `on-photo` and `on-photo-mute` are not measured, because the photo is not known; `*-glow` and `selection` follow their row. `chart-1` … `chart-8` are measured too, but a failing one keeps its value and follows Contrast (legend or direct labels), because the set is validated together for color blindness. A token that fails moves its tone away from the surface it sits on: down in light, up in dark. It moves one tone at a time and stops at the first value that passes on its worst surface (Contrast), keeping hue and chroma: the hue and chroma of the MCU palette its row names, otherwise its own. `danger-on` always passes on its fill: the better of white and black reaches at least 4.58:1 on any solid color. A pressed fill (`primary-pressed`, `danger-pressed`) that fails keeps its on-color and moves its tone away from it, one tone at a time, until the on-color passes. A token that reaches tone 0 or 100 without passing cannot be used (A color that fails).
4. **Approve.** Show one table: token, value, contrast and, for every value that is not the palette's or that moved, where it comes from: derived, Kore's value or moved to pass Contrast. Wait for the user's OK, then write the project's tokens.
