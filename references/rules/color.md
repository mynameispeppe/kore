# Color rules

**Roles.** Colors are roles, not a bag of swatches. Every token has one job; a color with no relationship to hierarchy, state or content is decoration and does not ship.

## Contrast (binding)

| Content | Minimum |
|---|---|
| Body text, placeholders, labels | 4.5:1 |
| Large text (24px+, or 19px+ bold) | 3:1 |
| Icons, control borders, focus indicators, chart marks | 3:1; a chart palette color below it (in light: `chart-3`, `chart-4`, `chart-5`) needs the legend or visible direct labels (Charts) |
| `stone` on disabled elements and where a component's file declares it exempt | exempt; any other use of `stone` meets the minimum of its content |

- **Worst surface.** Measure every text, border and icon token on its worst surface, the one where its ratio is lowest: `surface-pressed` in light, `surface-float-active` in dark. A token that passes there passes on every surface. A token that fails there moves its tone until it passes, as Method step 3 says (Custom palette). A state with its own fill (primary, danger, pressed) is measured as its on-color against that fill.
- **Translucent text.** The translucent text token (`body`) changes contrast with the surface below. Re-check it on every new surface; if it fails, use a solid color for that pair.
- **Text on a photo.** Text over a photo, a video or a background image is measured on the pixels under it, the lowest ratio deciding (Worst surface); `kore_check` measures it. When it fails, ask the user for another photo, darker under the text, and keep the veil and the text color.
- **Control borders.** A control that is recognised only by its outline (checkbox, radio, switch track, slider track) uses `hairline-strong`, which reaches 3:1 on every surface. Labelled controls (form fields, number stepper, secondary buttons, chips) use `hairline-medium`, below 3:1 by choice, because their label identifies them. `hairline` is for static containers only.

**Contrast ratio** = (L1 + 0.05) / (L2 + 0.05), where L1 and L2 are the WCAG relative luminance of the lighter and the darker color. Composite translucent colors over the surface before measuring. Never round up: 4.49 fails 4.5.

## Meaning

- **Never color alone.** Error, success, warning and info always carry a text label or an icon too, so they work for color-blind users and in grayscale.
- **Semantic roles stay fixed:** `danger` = error and destructive, `success` = success, `warning` = warning, `info` = information, `link` = links. Never swap them for decoration.
- **The accent is rare.** `accent` marks the primary moment of a screen (key data, emphasis). Scattered everywhere, it stops meaning anything. A page holds at most 4 elements in `accent`, the Hero's plate and icon among them (Hero). Buttons take `primary`, the brand color; the only surface in `accent` is the Hero's visual (Hero). As text, only at `display-sm` or larger (large text, 3:1 in Contrast); smaller text in `accent` would fail Contrast. (replaced in: glassmorphism)

**The One Primary Rule.** `primary` is spent on the main action of its decision and nothing else: at most one solid primary button per decision, never on decoration. A decision is the set of actions that act on the same content (Action order): the fields of a form, a dialog, a section of a page, the screen for a floating action button. A repeated, independent unit (a card in a product grid, a row in a list) is its own decision: each may have its own primary; the rule counts per decision, not per page. A decision whose choices must weigh the same has no main action, so it has no primary: in the Cookie banner, Reject and Accept are two `secondary` (Cookie banner). (replaced in: glassmorphism)

## States

**All states.** Every interactive element defines all its states: default, hover, focus, active/pressed, disabled, selected, loading, error. A component with half of them does not ship.

- **Focus, one style everywhere:** four corner marks drawn outside the control, one per corner, concentric with it: the outer edge of a mark has the control's radius plus 3px (a field or a button of radius 12 has marks of radius 15). A mark is the curve of the corner only, at least 10px long (the control's radius + 2px), 1px thick, in `focus-ring` (`hairline-strong`), 2px away from the edge. Filled and outlined controls take the same marks. They show on keyboard focus only, and they must reach 3:1 against the surface behind them. Links (text links and every element that works as a link) show focus with the link focus underline instead of marks: the text turns `ink` and is underlined with 2px at a 4px offset; text on a fill (a link with the look of a button) keeps its on-color and takes only the underline. Another focus holds only where a component's file prescribes it. Never remove focus without a replacement.
- **Pressed, no browser highlight:** the browser's own tap highlight is turned off (`-webkit-tap-highlight-color: transparent`); the pressed state of each component is the only feedback to a touch.
- **Selection:** selected text uses `selection`. Selected rows and items use `surface-elevated` plus their own mark (a check), never a color that suggests an action.
- **Disabled:** foreground `stone`, no hover, cursor not-allowed; keep the element's size so the layout does not shift.

## Themes

- **Designed separately.** Light and dark are each designed, never produced by inverting the other. Check surface steps, borders and contrast separately in each.
- **Which theme shows:**
  1. **Light and dark, no switch** (proposed at question 9): the theme follows the system.
  2. **Light and dark, with a switch** (a control in the project's navigation, chosen at question 9): two options, Light and Dark. Until the person chooses, the theme follows the system. The choice is saved across visits and applied before the page is first drawn, so it never shows in the wrong theme.
  3. **One theme only** (chosen at question 9): that theme always shows, with no switch, whatever the system.
- **Forced colors** (`@media (forced-colors: active)`, Windows high contrast): the browser replaces Kore's colors with the system's. Never block it: no `forced-color-adjust: none`.
  - **Transparent border:** every element told apart only by background or shadow has a 1px `transparent` border. It is invisible normally and becomes its outline in forced colors.
  - **States:** selected, active and current use `Highlight` as background and `HighlightText` as text; disabled uses `GrayText`.
  - **Focus:** the corner marks use `Highlight`, so they stay visible; the link focus underline stays.
  - **Icons:** with `currentColor` they already follow the system colors.
- **Glows** (`*-glow`): the default behind text that stands alone on a wide area with no photo or visual: the form of a sign-in or sign-up page with neither a photo nor a review beside it, a text-only hero, a CTA band without a visual, the review beside a form, the featured plan's card (Pricing) and the Dashboard's leading card (Dashboard), clipped by the card. A quote alone in its section has none (Testimonials). Anywhere else only on the user's request. Never on dense task screens: lists, tables, and forms of more than 4 fields. (replaced in: glassmorphism, minimalism)
  - **Form:** two glows inside the text block, before its other parts, which paint over them: each `glow` wide and high, `position: absolute`, `pointer-events: none`, `aria-hidden`. The start glow is `radial-gradient(circle closest-side, accent-glow 40%, transparent 100%)`, centred on the block's top start corner (`inset-block-start: 0`, `inset-inline-start: 0`, `translate: -50% -50%`); the end glow the same in `info-glow`, centred on its bottom end corner (`translate: 50% 50%`). In RTL the x translate flips. The section clips them (`overflow: clip`), or the featured plan's card in Pricing.
