---
version: 0.1.0
name: Kore
description: |
  A dual-theme minimal design system, light and dark with equal weight: a
  high-contrast canvas (a cool off-white in light, a soft near-black in
  dark), an oversized round geometric sans for headlines, a friendly
  geometric sans for body and UI, and a monospace for code. Surfaces rely on
  subtle low-opacity gradient glows, hairline 1px borders, and a strict
  rounded-24px container vocabulary with concentric nested corners. All
  spacing, sizing and line-heights sit on an 8-point grid (4px half-steps).
  There is no decorative chrome — just type, content, and atmospheric depth.
colors:
  light:
    canvas: "#F8FAFB"
    surface-card: "#fcfdfd"
    surface-elevated: "#f4f6f7"
    surface-deep: "#fcfdfd"
    hairline: "rgba(33, 33, 33, 0.06)"
    hairline-strong: "#8a8e92"
    divider-soft: "#efeff1"
    ink: "#2a2a2a"
    body: "rgba(42, 42, 42, 0.86)"
    charcoal: "rgba(42, 42, 42, 0.72)"
    mute: "#6a6e72"
    stone: "#a9adb1"
    on-light: "#2a2a2a"
    on-light-mute: "rgba(42, 42, 42, 0.72)"
    primary: "#212121"
    primary-on: "#ffffff"
    primary-pressed: "#2e2e2e"
    secondary: "#f4f6f7"
    accent: "#f4f4f5"
    signature: "#904E55"
    signature-glow: "rgba(144, 78, 85, 0.20)"
    accent-yellow: "#92400e"
    accent-blue: "#386580"
    accent-blue-glow: "rgba(56, 101, 128, 0.20)"
    accent-green: "#047857"
    accent-green-glow: "rgba(4, 120, 87, 0.20)"
    accent-red: "#c53030"
    accent-red-glow: "rgba(197, 48, 48, 0.20)"
    accent-red-on: "#ffffff"
    accent-red-pressed: "#b91c1c"
    link: "#386580"
    info: "#386580"
    focus-ring: "#2a2a2a"
    selection: "rgba(144, 78, 85, 0.20)"
    scrim: "rgba(12, 9, 10, 0.32)"
  dark:
    canvas: "#0C090A"
    surface-card: "#121212"
    surface-elevated: "#1f1f1f"
    surface-deep: "#060606"
    hairline: "rgba(255, 255, 255, 0.04)"
    hairline-strong: "#6e6a6a"
    divider-soft: "rgba(255, 255, 255, 0.04)"
    ink: "#f5f3f3"
    body: "rgba(245, 243, 243, 0.86)"
    charcoal: "rgba(245, 243, 243, 0.72)"
    mute: "#918d8d"
    stone: "#464a4d"
    on-light: "#2a2a2a"
    on-light-mute: "rgba(42, 42, 42, 0.72)"
    primary: "#fcfdff"
    primary-on: "#000000"
    primary-pressed: "#ebecee"
    secondary: "#1c1c1c"
    accent: "#1c1c1c"
    signature: "#F8F1FF"
    signature-glow: "rgba(248, 241, 255, 0.22)"
    accent-yellow: "#ffc53d"
    accent-blue: "#5b94b7"
    accent-blue-glow: "rgba(91, 148, 183, 0.34)"
    accent-green: "#6ee7b7"
    accent-green-glow: "rgba(110, 231, 183, 0.18)"
    accent-red: "#ef4444"
    accent-red-glow: "rgba(239, 68, 68, 0.34)"
    accent-red-on: "#000000"
    accent-red-pressed: "#f87171"
    link: "#5b94b7"
    info: "#5b94b7"
    focus-ring: "#f5f3f3"
    selection: "rgba(248, 241, 255, 0.22)"
    scrim: "rgba(0, 0, 0, 0.60)"
fonts:
  display: Outfit
  sans: Figtree
  mono: Geist Mono
typography:
  display-xxl:
    fontFamily: Outfit
    fontSize: 64px
    fontWeight: 500
    lineHeight: 64px
    letterSpacing: -0.02em
  display-xl:
    fontFamily: Outfit
    fontSize: 48px
    fontWeight: 500
    lineHeight: 48px
    letterSpacing: -0.02em
  display-lg:
    fontFamily: Outfit
    fontSize: 40px
    fontWeight: 500
    lineHeight: 40px
    letterSpacing: -0.02em
  heading-md:
    fontFamily: Figtree
    fontSize: 24px
    fontWeight: 600
    lineHeight: 32px
    letterSpacing: -0.01em
  heading-sm:
    fontFamily: Figtree
    fontSize: 20px
    fontWeight: 600
    lineHeight: 28px
    letterSpacing: -0.01em
  subtitle:
    fontFamily: Figtree
    fontSize: 20px
    fontWeight: 400
    lineHeight: 28px
  body-lg:
    fontFamily: Figtree
    fontSize: 18px
    fontWeight: 400
    lineHeight: 28px
  body-md:
    fontFamily: Figtree
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-sm:
    fontFamily: Figtree
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  button-md:
    fontFamily: Figtree
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
  button-sm:
    fontFamily: Figtree
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.01em
  caption:
    fontFamily: Figtree
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
  caption-emph:
    fontFamily: Figtree
    fontSize: 12px
    fontWeight: 600
    lineHeight: 16px
  code-md:
    fontFamily: Geist Mono
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  full: 9999px
spacing:
  space-1: 4px
  space-2: 8px
  space-3: 12px
  space-4: 16px
  space-5: 20px
  space-6: 24px
  space-8: 32px
  space-10: 40px
  space-12: 48px
shadows:
  light:
    shadow-rest: "0 1px 2px rgba(33, 33, 33, 0.04)"
    shadow-hover: "0 4px 12px rgba(33, 33, 33, 0.06)"
  dark:
    shadow-rest: "0 1px 2px rgba(0, 0, 0, 0.24)"
    shadow-hover: "0 4px 12px rgba(0, 0, 0, 0.32)"
zIndex:
  base: 0
  raised: 10
  dropdown: 100
  overlay: 200
  modal: 300
  toast: 400
breakpoints:
  sm: 640px
  md: 768px
  lg: 1024px
  max-content: 1200px
motion:
  duration-instant: 100ms
  duration-fast: 150ms
  duration-base: 250ms
  duration-slow: 400ms
  duration-focal: 700ms
  ease-out: "cubic-bezier(0.16, 1, 0.3, 1)"
  ease-in: "cubic-bezier(0.4, 0, 1, 1)"
  ease-in-out: "cubic-bezier(0.65, 0, 0.35, 1)"
  spring: "stiffness 500, damping 40, mass 1"
icons:
  library: Hugeicons
  style: Stroke Rounded
  stroke: 1.5
  sizes: [16, 20, 24]
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-on}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 0 24px
    height: 48px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.primary-on}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 0 24px
    height: 48px
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 0 24px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 0 24px
    height: 48px
  button-destructive:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.accent-red-on}"
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 0 24px
    height: 48px
  button-destructive-pressed:
    backgroundColor: "{colors.accent-red-pressed}"
    textColor: "{colors.accent-red-on}"
  button-disabled:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.stone}"
  button-compact:
    typography: "{typography.button-md}"
    rounded: "{rounded.lg}"
    padding: 0 16px
    height: 40px
  button-small:
    typography: "{typography.button-sm}"
    rounded: "{rounded.md}"
    padding: 0 12px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 0 16px
    height: 48px
  text-input-compact:
    height: 40px
  text-input-focus:
    borderColor: "{colors.ink}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.accent-red}"
  text-input-disabled:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.stone}"
  field-label:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  field-help:
    textColor: "{colors.mute}"
    typography: "{typography.body-sm}"
  field-error:
    textColor: "{colors.accent-red}"
    typography: "{typography.body-sm}"
  textarea:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 12px 16px
  select-menu:
    backgroundColor: "{colors.surface-deep}"
    rounded: "{rounded.lg}"
    padding: 8px
  select-option:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    height: 44px
  select-option-active:
    backgroundColor: "{colors.surface-elevated}"
  checkbox:
    backgroundColor: "{colors.surface-deep}"
    rounded: "{rounded.xs}"
    size: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-on}"
  radio:
    backgroundColor: "{colors.surface-deep}"
    rounded: "{rounded.full}"
    size: 20px
  radio-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-on}"
  switch:
    backgroundColor: "{colors.surface-elevated}"
    rounded: "{rounded.full}"
    width: 40px
    height: 24px
  switch-on:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-on}"
  segmented:
    backgroundColor: "{colors.surface-elevated}"
    rounded: "{rounded.lg}"
    padding: 4px
    height: 48px
  segmented-item:
    textColor: "{colors.mute}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 0 16px
    height: 40px
  segmented-item-selected:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
  card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-compact:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 16px
  card-inner-block:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 12px 16px
  card-title:
    textColor: "{colors.ink}"
    typography: "{typography.heading-sm}"
  card-subtitle:
    textColor: "{colors.mute}"
    typography: "{typography.body-sm}"
  card-key-figure:
    textColor: "{colors.signature}"
    typography: "{typography.display-lg}"
  card-clickable:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  list-row:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 8px 12px
    height: 56px
  list-row-hover:
    backgroundColor: "{colors.accent}"
  list-row-icon:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 40px
---

## Overview

Guiding principle: *Calm Clarity*. When a choice is not covered by a rule, pick the option that keeps the screen calmer and clearer.

Kore aims for a screen that feels quiet and reads at a glance. Its forms are round and friendly, laid on a strict 8-point grid. Surfaces are subdued, a cool off-white by day and a warm near-black by night. Space, a change of tone or a 1px border is enough to separate them, and only elements you can click carry a shadow. Color is used sparingly. One signature color marks the moment that matters and semantic colors mark state, while everything else stays neutral so the content comes first. Every screen has a single point of entry, and the interface answers every action, prevents errors and uses the words of the people who use it.

Key characteristics (values reflect the active tokens; update them when a project picks different candidates):

- Two themes designed with the same care, Ice (`#F8FAFB`) and Night (`#0C090A`), each built on its own instead of as the inverse of the other.
- Headlines from 40px up in Outfit, everything else in Figtree, code and data in Geist Mono.
- A single signature color used rarely: `#904E55` in light, `#F8F1FF` in dark.
- Depth comes from surface steps and 1px borders. Only clickable elements have a shadow, and it is barely visible.
- Cards have 24px corners and controls 16px; nested radii follow the Half-Padding Rule.
- Every space, size and line-height comes from a token on the 8-point grid.
- One focal point per screen. Groups separate with the lightest step that works: space, then background, then line, then card.
- Motion explains what is happening. It is quick in apps, and a landing page gets one carefully built moment.
- Every action gets a response within 100ms, a deletion offers "Undo" instead of a confirmation, and errors are prevented and explained in plain words.
- Text at 4.5:1, controls at 3:1, 44px touch targets, and respect for people who reduce motion.

## Color rules

Colors are roles, not a bag of swatches. Every token has one job; a color with no relationship to hierarchy, state or content is decoration and does not ship.

### Contrast (binding)

| Content | Minimum |
|---|---|
| Body text, placeholders, labels | 4.5:1 |
| Large text (24px+, or 19px+ bold) | 3:1 |
| Icons, control borders, focus indicators, chart marks | 3:1 |
| Disabled elements (`stone`) | exempt |

- Check every pair against every surface it can sit on (`canvas`, `surface-card`, `surface-elevated`, `surface-deep`), in both themes, including hover, pressed, error and disabled states.
- Translucent text tokens (`body`, `charcoal`, `on-light-mute`) change contrast with the surface below. Re-check them on every new surface; if one fails, use a solid color for that pair.
- A control that is recognised only by its outline (text input, select, checkbox) uses `hairline-strong`, which reaches 3:1 on every surface. `hairline` is for static containers only.

### Meaning

- **Never color alone.** Error, success, warning and info always carry a text label or an icon too, so they work for color-blind users and in grayscale.
- **Semantic roles stay fixed:** `accent-red` = error and destructive, `accent-green` = success, `accent-yellow` = warning, `info` = information, `link` = links. Never swap them for decoration.
- **The accent is rare.** `signature` marks the primary moment of a screen (key data, emphasis). Scattered everywhere, it stops meaning anything.

**The One Primary Rule.** `primary` is spent on the main action of the view and nothing else: at most one solid primary button per view, never on decoration.

### States

Every interactive element defines all its states: default, hover, focus, active/pressed, disabled, selected, loading, error. A component with half of them does not ship.

- **Focus:** form fields (text input, textarea, select) thicken their border to 2px `ink`, with no outer ring. Every other control (buttons, checkbox, radio, switch, segments) gets a 2px `focus-ring` outline at a 2px offset. Never remove focus without a replacement.
- **Selection:** selected items and selected text use `selection`.
- **Disabled:** foreground `stone`, no hover, cursor not-allowed; keep the element's size so the layout does not shift.

### Themes

- Light and dark are each designed, never produced by inverting the other. Check surface steps, borders and contrast separately in each.
- **Glows** (`*-glow`) are atmosphere with a purpose: at most one per screen, anchored at the top of a section, and never on dense task screens (lists, forms, tables).

## Typography rules

- **Roles, not sizes.** Use the scale tokens (`display-*`, `heading-*`, `body-*`, `caption*`, `button-*`, `code-md`); never a free font size.
- **Display font only for display.** The display family (`display-*`, 40px and up) never appears in labels, buttons, navigation, form fields or data. Everything else uses the sans.
- **Form fields at 16px.** Text inside inputs, textareas and selects uses `body-md` (16px) so mobile Safari does not zoom the page on focus.
- **Reading floor.** Running text is at least 16px (`body-md`). 14px (`body-sm`) is for metadata and dense UI, 12px (`caption`) only for short labels.
- **Measure.** Paragraphs stay between 45 and 75 characters per line; cap text containers with a `ch` max-width.
- **Heading spacing.** More space above a heading than below it, so the heading belongs to the text it introduces.
- **Paragraph rhythm.** Separate paragraphs with space or with a first-line indent, never both.
- **Numbers.** Columns of numbers use tabular figures (`font-variant-numeric: tabular-nums`) so digits line up.
- **Dark theme compensation.** Light text on dark surfaces reads thinner: when a role looks weak in dark, add a touch of letter-spacing or one weight step for that role; never shrink contrast to compensate.
- **Fixed scale in apps.** Product screens use the fixed rem scale. Fluid sizes (clamp) are reserved for display type on marketing pages.
- **Font loading.** Load only the weights in use, with `font-display: swap` and a metric-compatible fallback, so text is never invisible and the layout does not jump.
- **Zoom and user settings.** Never block browser zoom, user font size, Dynamic Type or platform text scaling.

## Hierarchy

Hierarchy is the architecture of attention: it tells the eye what to look at first, what next, and what to ignore. A correct hierarchy lets a user understand a screen in under five seconds without reading a word.

### Visual weight

Six tools set how strongly an element pulls the eye. Use them on purpose, and mostly to take weight away from secondary elements.

| Tool | Rule |
|---|---|
| Size | The bigger element is read first. Headings are clearly larger than their subheadings; the primary button is larger than secondary actions; functional icons are larger than decorative ones. |
| Contrast | Primary text uses full contrast (`ink`); metadata steps down (`charcoal`, `mute`), always within the 4.5:1 minimum. |
| Color | One accent family for primary actions. Saturated beats desaturated; color never carries meaning alone. |
| Shape | A shape that breaks the pattern stands out (a round badge on a square icon). Kore keeps one corner language, so shape contrast comes from form (pill, circle, dot), never from mixing corner styles. |
| Position | Top-left is read first in left-to-right layouts; an element surrounded by space weighs more than the same element in a crowd. |
| Density | A dense area weighs more but can confuse. Reduce density of secondary areas; an isolated element gains weight from the empty space around it. Never the same density everywhere. |

**The One Winner Rule.** Every screen, and every zone of a screen, has one focal point. It beats everything else on at least two of the six tools (for example: largest, full contrast, top-left). Three is overdesign. Two elements with similar weight compete and neither wins.

### Three levels

- **Primary:** one element, the focal point. Caught first.
- **Secondary:** two or three elements that support it and add context.
- **Tertiary:** everything else; present, never distracting.

If the primary element cannot be named within three seconds of looking at the design, there is no focal point.

| Context | Focal point | Typical mistake |
|---|---|---|
| Landing page | Hero headline or main image | Three elements of similar size in the hero |
| Dashboard | The most important metric | A grid of identical cards with no leader |
| Form | The first field to fill | Label and input with the same weight |
| Product or content card | Image or title | Price, title and badge at the same weight |
| Error page | The error message | A decorative illustration heavier than the message |
| Dialog | Title and primary action | Three equivalent buttons |

### Typographic levels

- At most **three or four type levels** visible on one screen.
- Adjacent levels differ clearly in size and/or weight; if two roles look almost the same, drop one.
- Weight can compensate size: a semibold `heading-sm` can outrank a regular larger line.
- Bold only for headings and key terms; if everything is bold, nothing is.
- No all caps on long text.

### Grouping and separation

Elements close together are read as one group (proximity); distance between groups says how related they are.

**The Separation Ladder.** Separate with the lightest step that works, and never skip steps:

1. **Space only**: the gap does the work, zero graphic noise. The default.
2. **Background change**: a surface step (`surface-card`, `surface-elevated`) for wide sections.
3. **Line**: a 1px `hairline`, only between sections of equal importance, never on every row.
4. **Card** (surface + border): maximum separation and weight.

- **Rows in a list separate with space**, not with a divider on every row; a divider on each row makes every item look like its own section.
- **Containers only when needed:** the group changes context sharply (data vs. actions vs. navigation), proximity is not enough because the layout is dense, or the group is clickable as one unit. A border added "to tidy up" means the grouping is wrong.
- Other ways to group without containers: alignment on a shared axis, the same background tone, the same type style for the same category.

### Scanning patterns

- **F pattern** (dense content: feeds, tables, search results, dashboards): the left column and the first two lines of each block are always read. Put titles, status and key actions on the left; the first column of a table carries the most important data.
- **Z pattern** (sparse content: landing pages, cards, simple forms): brand top-left, primary action top-right, key message at the centre-left turn of the Z, final action bottom-right.
- A perfectly symmetric layout follows no pattern and guides nothing: break symmetry on purpose for the focal point (wider, taller, isolated).
- Critical information never lives only at the bottom right of an F layout.

### Three-second check

- [ ] Without reading, I know where to look first
- [ ] One primary element per zone
- [ ] Weight scales primary > secondary > tertiary
- [ ] Groups are clear without borders or backgrounds
- [ ] At least three type levels, clearly distinct
- [ ] Color appears only where it means something

## Spacing

The goal is not "8px everywhere": it is consistent spacing. Every margin, padding, gap, offset and element size comes from one small scale, repeated across the whole project. Consistency beats improvisation.

### Scale

Base unit 8px, with 4px half-steps for fine adjustments. Token names count 4px units: `space-N` = N × 4px, so the name tells the value.

| Token | Value | Role | When to use it |
|---|---|---|---|
| `space-1` | 4px | Micro adjustment | Icon ↔ text inside badges and chips, title ↔ subtitle, label ↔ helper text |
| `space-2` | 8px | Base unit | Tight groups: items in a compact list, buttons in a toolbar, label ↔ input |
| `space-3` | 12px | Half-step (8 + 4) | Only when 8 is visibly too tight and 16 too loose |
| `space-4` | 16px | Small gap | Compact card padding, icon spacing in lists and cards, gap between related items, page side margin on phones |
| `space-5` | 20px | Half-step (16 + 4) | Only when 16 is visibly too tight and 24 too loose |
| `space-6` | 24px | Medium gap | Default card padding, gap between sections inside a card, gap between fields in a form |
| `space-8` | 32px | Large gap | Card outer margin, gap between cards, layout gutters, page side margin from tablet up |
| `space-10` | 40px | Half-step (5 × 8) | Only when 32 is visibly too tight and 48 too loose |
| `space-12` | 48px | Section spacing | Space between page sections, main button and input height |

The primary scale is 4 / 8 / 16 / 24 / 32 / 48. The half-steps 12, 20 and 40 exist so they can be used as tokens, but only when the primary value next to them is visibly wrong. No other values.

### Rules (binding)

1. **The Token-Only Rule.** Every margin, padding, gap and offset (top, left, inset, translate) uses a `space-*` token. Never a free number, never an arbitrary value.
2. **No random values.** Never 10, 11, 13, 14, 19, 22, 23, 27, 31px. If a value is missing, round to the nearest token.
3. **Keep the scale small.** Never add a token for a single case. Repeat the existing ones.
4. **Uniform card padding.** The same value on all four sides and on every card of the same kind: `space-6` (24px) by default, `space-4` (16px) for compact cards.
5. **Everything that adds space follows the scale:** card padding, gaps between sections, text spacing, button sizes, layout margins, icon spacing.
6. **Element sizes are multiples of 8** (4 when needed): icons 16 / 20 / 24, avatars 24 / 32 / 40 / 48, controls 32 / 40 / 48, bars 56 / 64.
7. **Line-heights are multiples of 4** (see Typography), so vertical rhythm never breaks.
8. **Borders don't count.** A 1px border is not spacing: use border-box sizing and fixed heights so a border never forces off-grid padding (no `7px 15px` to compensate).
9. **Use relative units.** Implement tokens in `rem` (1rem = 16px) so spacing follows the user's text size and zoom.

### Proximity and hierarchy

Spacing tells the reader what belongs together.

- **Inside < between.** Space inside a group is always smaller than space between groups: label ↔ input `space-2`, field ↔ field `space-6`, section ↔ section `space-12`.
- **One step apart.** Two nested levels differ by at least one step of the primary scale. Never the same gap inside and outside a group.
- **Space the siblings from the parent.** Put the gap on the container (flex or grid gap, stack spacing) instead of margins on each child, so gaps never collapse or double.
- **Nested padding.** A block inside a card uses the same or a smaller step than the card: card `space-6`, inner block `space-4`.
- **Whitespace is structure.** Group with space first; add a divider only when space alone cannot separate the groups.

### Reference values

| Situation | Token | Value |
|---|---|---|
| Card outer margin, gap between cards | `space-8` | 32px |
| Card padding | `space-6` (compact `space-4`) | 24px (16px) |
| Gap between sections inside a card | `space-6` | 24px |
| Icon spacing in cards and lists | `space-4` | 16px |
| Icon ↔ text in badges and chips | `space-1` | 4px |
| Title ↔ subtitle | `space-1` | 4px |
| Label ↔ input | `space-2` | 8px |
| Gap between list items | `space-2` / `space-4` / `space-6` | 8 / 16 / 24px |
| Gap between page sections | `space-12` | 48px |
| Page side margin | `space-4` phone, `space-8` tablet and up | 16px / 32px |
| Main button and input height | `space-12` | 48px |
| Button horizontal padding | `space-6` (compact `space-4`) | 24px (16px) |

### Accessibility

Accessibility has the same priority as the grid. When the two conflict, usability wins.

- **Touch targets** are at least 44 × 44px, 48px preferred. A smaller control extends its hit area to 44px with padding or an invisible overlay.
- **Adjacent targets** are at least `space-2` (8px) apart, so a finger never hits the wrong one.
- **Never shrink spacing below the scale to fit content.** Change the layout instead: wrap, stack, scroll or cut content.
- **Zoom.** Layouts must hold at 200% text zoom without overlapping or cutting text.

### Common mistakes

- Random values everywhere (`padding: 13px 22px`).
- Too many spacing tokens.
- Different padding on cards of the same kind, or on different sides of one card.
- Mixing 10, 14, 23, 31px with no reason.
- No scale defined at all.

### Pre-delivery checklist

- [ ] Every margin, padding and gap uses a `space-*` token
- [ ] No free or arbitrary values (search for `\b(1[0-9]|2[0-9]|3[0-9])px` outside token definitions)
- [ ] Card padding is uniform on all sides and across cards of the same kind
- [ ] Half-steps (12, 20, 40) are used only where the primary step was visibly wrong
- [ ] Spacing inside groups is smaller than spacing between groups
- [ ] Controls are 32 / 40 / 48px tall and every touch target is at least 44px
- [ ] Line-heights are multiples of 4
- [ ] The layout holds at 200% text zoom

### Implementation

Kore is stack-agnostic. Expose the scale as tokens in whatever the project uses: CSS custom properties, a Tailwind theme, an SCSS map, Swift or Kotlin constants. Reference in CSS:

```css
:root {
  --space-1: 0.25rem;  /*  4 */
  --space-2: 0.5rem;   /*  8 */
  --space-3: 0.75rem;  /* 12, half-step */
  --space-4: 1rem;     /* 16 */
  --space-5: 1.25rem;  /* 20, half-step */
  --space-6: 1.5rem;   /* 24 */
  --space-8: 2rem;     /* 32 */
  --space-10: 2.5rem;  /* 40, half-step */
  --space-12: 3rem;    /* 48 */
}
```

## Shapes

Kore is round: corners use circular arcs from the `rounded` scale, never squircle or cut corners, so they look the same in every browser and nest cleanly.

### Radius by role

| Role | Token | Value |
|---|---|---|
| Cards, sheets, dialogs | `xl` | 24px |
| Controls (buttons, inputs, selects), inner blocks, menus | `lg` | 16px |
| Menu items, segments, small chips inside a container | from the nested rule | — |
| Pills, badges, avatars, status dots | `full` | 9999px |
| Full-width sections, page edges | `none` | 0 |

### Nested radius (binding)

**The Half-Padding Rule.** When a rounded element sits inside another, its radius comes from the outer one:

```
inner radius = outer radius − (padding ÷ 2)
rounded down to the nearest step of the scale (multiples of 4)
```

The pure geometric formula (outer − padding) gives exactly concentric curves, but with generous padding it makes inner corners look too square next to a round container. Subtracting half the padding keeps the two curves related and compensates optically.

| Case | Outer | Padding | Inner |
|---|---|---|---|
| Rows inside a compact card | 24 | 16 | 16 |
| Items inside a menu | 16 | 8 | 12 |
| Segments inside a segmented control | 16 | 4 | 12 |
| Rows inside a standard card | 24 | 24 | no rounded block: rows separate with space only |

- **Standard cards** (padding `space-6`) never contain rounded blocks with their own background: their rows separate with space only (see The Separation Ladder). Rounded inner blocks live only in compact cards (padding `space-4`).
- **Never the same radius inside and outside.** Equal radii make the gap look thicker at the corners.
- **Deeper nesting** applies the rule again from the parent, not from the outermost container.

### Borders inside the edge

A border must not change the measurements the nested rule relies on. Draw the 1px `hairline` inside the element's edge without taking layout space (in CSS: `outline: 1px solid; outline-offset: -1px`, or an inset ring), so the gap between two nested edges is exactly the padding.

## Elevation

Depth tells the reader what sits on what. Static layers separate with a surface step and a 1px `hairline`; only interactive elements get a shadow.

### Levels

| Level | Recipe | Use |
|---|---|---|
| 0 · flat | `canvas`, no border, no shadow | Page background, full-width sections |
| glow | one `*-glow` wash at the top of a section | Atmosphere; at most one per screen, never on dense task screens |
| 1 · surface | `surface-card` + `hairline` | Static cards and panels |
| 2 · inset | `surface-elevated` + `hairline` | Rows and icon wells inside a card; never a card inside a card |
| 3 · floating | `surface-deep` + `hairline` | Popovers, menus, code blocks |
| 4 · overlay | `surface-deep` + `hairline` over a `scrim` | Dialogs and sheets |
| interactive | its surface + `shadow-rest`, `shadow-hover` on hover | Buttons and clickable cards only |

### Shadows

**The Hairline Rule.** Shadows only on interactive elements: things the user clicks or taps. Everything else, including containers of clickable items such as popovers, menus and sheets, uses a 1px `hairline` border and no shadow.

- **Barely perceptible.** `shadow-rest` is a hint that the element is clickable; `shadow-hover` suggests a lift, nothing more. Never stack several shadows or raise the opacity to make a point.
- A shadow always has a vertical offset and a soft blur. A zero-offset colored halo is decoration; a hard shadow with no blur (`4px 4px 0`) is a costume.
- Dark theme shadows are denser (black at 24–32%) because a light shadow disappears on a near-black canvas.

### Interaction

- **Hover** on a clickable element: `shadow-rest` → `shadow-hover` and a lift of `space-1` (4px), with `duration-fast` and `ease-out`. **Pressed:** back to rest in `duration-instant`.
- **Reduced motion:** no lift; only the shadow changes, without animation.
- Touch devices have no hover: the pressed state carries the feedback.

### Stacking order

Layers use the fixed `zIndex` scale, never a free number: `base` 0, `raised` 10 (sticky headers, raised items), `dropdown` 100 (menus, popovers), `overlay` 200 (scrim), `modal` 300 (dialogs, sheets), `toast` 400 (notifications). Floating layers render outside clipping containers (popover API, dialog, portal) so they are never cut off.

## Responsive

Adapting is rethinking the experience for each context, not scaling pixels down. A phone gets phone patterns; a desktop uses its space.

### Principles

- **Mobile-first.** Base styles are for the smallest screen; larger screens add layout with `min-width` queries.
- **Same structure everywhere.** The information architecture and naming never change between screen sizes; only the layout does.
- **Nothing important hidden on mobile.** If a function matters, it works on a phone.
- **Content decides the breakpoints.** Stretch the layout until it breaks and add a breakpoint there; never target a device model.

### Breakpoints

| Token | From | What changes |
|---|---|---|
| base | 0 | Phone: one column, side margin `space-4`, bottom navigation, bottom sheets instead of dropdowns, primary controls within thumb reach |
| `sm` | 640px | Large phones and landscape: card grids up to 2 columns |
| `md` | 768px | Tablet: 2 columns, list + detail views, side margin `space-8` |
| `lg` | 1024px | Desktop: multi-column layouts, side navigation always visible, extra information on hover, keyboard shortcuts |
| `max-content` | 1200px | Content stops growing; wider screens add margin, never stretch text or cards |

### Grids

- Columns step 1 → 2 → 3 as space allows; gutters step `space-4` → `space-6` → `space-8`.
- Prefer layouts that reflow on their own (flex wrap, auto-fit grids) and container-based rules for components used in different widths.

### Typography

- Below `sm`, display roles step down one level: `display-xxl` 64 → 48, `display-xl` 48 → 40. Line-height stays equal to the size.
- Product screens keep the fixed scale at every width (see Typography rules).

### Input

- Detect the input, not the screen size: `(hover: hover)` and `(pointer: fine)` for mouse and trackpad, `(hover: none)` and `(pointer: coarse)` for touch.
- Hover is an enhancement only, never the only way to reach a function. The hover lift from Elevation applies only where hover exists; on touch, the pressed state carries the feedback.
- Touch targets stay at least 44 × 44px at every width, desktop included (many laptops have touch screens).

### Safe areas

- Fixed bars and full-bleed content respect the notch, rounded corners and home indicator with `env(safe-area-inset-*)`, and the viewport uses `viewport-fit=cover`.
- A bar fixed to the bottom adds `env(safe-area-inset-bottom)` to its own padding, so its content never sits under the home indicator.

### Extremes

- Layouts work from 320px wide to 4K, in portrait and landscape on phones and tablets, and at 200% text zoom.
- The page never scrolls horizontally. Only tables and code blocks may be wider, each inside its own scroll container.
- Long names, long translations and empty states never break the layout.

### Tables and media

- **Tables** on phones become stacked cards (one card per row, label + value) or scroll inside their own container.
- **Images** ship several resolutions (`srcset` + `sizes`), use art-directed crops when a different framing reads better on small screens (`picture`), keep a fixed `aspect-ratio` so the layout doesn't jump, and never exceed their container.

### Testing

Test on at least one real iPhone and one real Android phone, in Safari, Chrome and Firefox, with a throttled network. Browser device emulation is useful for layout but misses real touch, performance and keyboards.

## Motion

Motion explains feedback, state and relationship, or creates one authored moment the page has earned. Removing an animation should lose meaning, not just decoration.

### Tokens

| Token | Value | Use |
|---|---|---|
| `duration-instant` | 100ms | Immediate feedback: press, toggle |
| `duration-fast` | 150ms | Hover, focus, small state changes, exits of small elements |
| `duration-base` | 250ms | Routine state changes, opening menus and popovers |
| `duration-slow` | 400ms | Layout changes, overlays, sheets, view transitions |
| `duration-focal` | 700ms | Only the authored focal moment of a landing page |
| `ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Entrances and responses: natural deceleration |
| `ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | Exits |
| `ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Moving from one place to another |
| `spring` | stiffness 500, damping 40, mass 1 | Gestures: toggles, drag, swipe; no bounce |

### Rules (all modes)

- **A reason to move.** Motion only acknowledges an action, makes a state change or spatial relationship legible, keeps continuity through a change, or directs attention to a meaningful moment.
- **Exit faster than entrance.** An element leaves one step faster than it arrived (menu: in `duration-base`, out `duration-fast`; sheet: in `duration-slow`, out `duration-base`).
- **No bounce by reflex.** No elastic or bouncy curves unless the project's world asks for them; `spring` is tuned without overshoot.
- **Springs for gestures.** Toggles, drag and swipe use `spring`, so an interrupted gesture continues naturally. Timed transitions use the duration tokens.
- **Transform and opacity.** Never animate properties that recalculate layout (width, height, top, left, margins); use transforms, and layout techniques (FLIP, view transitions) for size and position changes.
- **Visible by default.** Content is visible in its resting state; an entrance animation starts from a class added by script, so nothing stays hidden if the script fails.
- **Loops stop.** Non-essential loops pause when off screen or hidden. No autoplay with sound.
- **Reduced motion.** `prefers-reduced-motion` keeps fades, color and state changes that carry meaning, and removes spatial movement (slides, lifts, scale). Never a global kill that removes feedback. Nothing flashes more than three times per second.
- **Stay light.** Keep expensive effects (blur, filters, shaders) in small isolated areas, apply `will-change` only during the animation, and test on a mid-range phone.

### App mode

- Feedback with `duration-instant` and `duration-fast`; state changes with `duration-base`; overlays and sheets with `duration-slow`.
- **No page-load choreography.** The app opens straight into the task.
- View transitions only when they explain where the user went (list → detail and back).
- Loading shows content skeletons; motion never makes the user wait.

### Landing mode

- **One focal moment per page**, built from the product, not a generic fade-and-rise repeated on every section. It uses `duration-focal` and `ease-out`.
- **Stagger** only for real lists, with a total delay of about 300ms at most.
- **Scroll-driven motion** only when the scroll itself carries meaning (a progress, a sequence), with a static fallback.
- Supporting elements (subtitle, call to action) fade in after the focal element with `duration-slow`.

### Implementation

Kore is stack-agnostic: expose the tokens as CSS custom properties and use CSS transitions and keyframes for timed states. Use the Web Animations API or a motion library (for example Motion.dev) when you need springs, interruption, sequencing or exit animations. Never add a dependency for an effect CSS already handles.

## Browser surfaces

The parts the browser draws still carry the design. Theme them from the palette instead of shipping browser defaults:

- **Text selection:** `selection` background, `ink` text.
- **Caret:** `ink` (or `signature` in inputs that deserve emphasis).
- **Focus:** 2px `ink` border on form fields; 2px `focus-ring` at a 2px offset on every other control.
- **Scrollbars:** thin, `hairline-strong` thumb on a transparent track, where the platform allows it.
- **Links:** `link` color, underline with a 4px offset, thickness 1px.
- **Numerals:** tabular figures in tables and data.

## Icons

**Library first.** If the project already uses an icon library, keep it and apply the rules below. Otherwise use Kore's default.

**Default: Hugeicons**, free set, *Stroke Rounded* style (MIT license). Its round stroke ends match Kore's round type and corners, and it has official packages for every major stack: React, Vue, Angular, Svelte, SolidJS, React Native and Flutter, plus plain SVG for anything else.

### Rules

- **One library per project**, one style, one stroke width (1.5 on a 24px grid). Never mix libraries or filled and outlined styles.
- **Sizes from the grid:** 16px next to 12–14px text, 20px in buttons and inputs, 24px for standalone and navigation icons.
- **Color from text:** icons use `currentColor`, so they follow the text or state color of their container.
- **Spacing:** icon ↔ text `space-2` (8px) in rows and fields, `space-1` (4px) in badges and chips. Buttons with a label carry no icon (see Button).
- **Accessibility:** an icon-only button always has an accessible label (`aria-label` or visually hidden text) and a tooltip; decorative icons are hidden from screen readers (`aria-hidden="true"`).
- **Clear meaning:** one icon means one thing across the product (pencil = edit, trash = delete). When an icon is not obvious, add the word.
- **No stand-ins:** never emoji or Unicode symbols instead of icons.

### Candidates

| Library | Style that fits Kore | Stacks |
|---|---|---|
| Hugeicons | Stroke Rounded (free) | active |
| Lucide | default (round caps) | React, Vue, Angular, Svelte, Solid, React Native, vanilla |
| Phosphor | Regular or Light | React, Vue, web components, Flutter, Swift |
| Tabler Icons | outline | React, Vue, Svelte, Solid, vanilla SVG, web font |
| Material Symbols | Rounded | web font and SVG, any stack |

## Usability

Based on Nielsen's 10 usability heuristics. They are principles, applied in the context of each product; the values below are Kore's defaults.

### 1. System status is always visible

No user action stays without a visible response.

| Wait | Feedback |
|---|---|
| Under 100ms | Immediate response: pressed state, hover, focus |
| Over 300ms | A loading indicator: skeleton for content, spinner inside the button that started the action |
| Over 1s | A progress bar with percentage when progress is measurable |
| Over 3s | A time estimate and a way to cancel |

- A submitting button becomes disabled, shows a spinner and a label ("Saving…"). Completion shows a toast ("Saved") that disappears after about 3 seconds.
- Page and view changes show a skeleton or a thin progress bar at the top, never a silent swap.

### 2. Speak the user's language

- Use the words people use for the task, not database or code terms: `FULFILLMENT_PENDING` → "Being prepared", `Error 401` → "Wrong password".
- Map raw API values to plain language before showing them.
- Avoid metaphors that need explaining; when an icon is not obvious, add the word.

### 3. Control and freedom

- **Undo over confirmation.** A destructive action runs, then a toast offers "Undo" for 5 seconds. Confirm first only when the action truly cannot be undone.
- Leaving a form with unsaved changes asks before discarding them.
- Dialogs and sheets always have a visible close control and close on click outside and on Escape.
- In multi-step flows, completed steps stay clickable.
- Applied filters always show a visible "Clear filters".
- When a flow must be sequential (payment, signing), say so clearly.

### 4. Consistency and standards

- The same action has the same name, icon and position everywhere ("Save" is always "Save"; a pencil always means edit).
- Semantic colors keep one meaning: red only for errors and destructive actions.
- One format for dates, currencies and units across the product, produced by shared helpers.
- Centralise what varies: design tokens in one place, recurring labels as shared constants.
- Consistency is not uniformity: a primary and a secondary button look different on purpose.

### 5. Prevent errors

- If many users make the same mistake, the design is wrong, not the users.
- Constrain input to valid values: date pickers with invalid ranges blocked, numeric inputs with min, max and step.
- Show limits and formats before the action ("Max 5 MB", `DD/MM/YYYY` as a format hint), not after it fails.
- Validate when the user leaves a field and suggest corrections; do not wait for submit.
- Disable an action whose preconditions are not met, and explain why in a tooltip or helper text.
- Keep advanced or risky options behind progressive disclosure.

### 6. Recognition rather than recall

- Show what the user needs where they need it: password requirements live under the field and update as they type; an order summary stays visible during checkout; completed steps stay summarised in a wizard.
- Offer recent items, suggestions and autocomplete instead of asking people to type from memory.
- Show a preview before publishing or confirming.
- Always show where the user is (active navigation, title, breadcrumb).

### 7. Flexibility and efficiency

- Design for the first-time user, then add accelerators for experts; the two paths never conflict.
- Keyboard shortcuts for frequent actions, listed where users can find them.
- A command palette (Cmd/Ctrl + K) or global search when the product has many actions.
- Bulk actions for repeated work; presets and templates for repetitive setups.

### 8. Minimal by design

- For every element ask: would the user miss it? If not, remove it.
- Minimal is not fewer features: show what is needed now and reveal the rest when it is needed (progressive disclosure).
- One sentence of context, then the action.
- Notify only what needs attention now.

### 9. Help users recover from errors

- An error message says **what** went wrong, **why** when useful, and **how** to fix it. Missing one of the three makes it incomplete.
- Never show error codes to users; log them instead.
- Neutral, solution-oriented language; the user is never blamed.
- Show the message inline next to the field that caused it, not in a generic toast at the top.
- Empty states are silent errors: explain why nothing is shown and what to do next ("No projects yet. Create one").

### 10. Help and documentation

Help comes in layers, from best to last resort:

1. The interface explains itself.
2. Inline help: tooltips on non-obvious icons, helper text under fields with requirements.
3. Contextual onboarding for complex first-time flows (a short tour of the essential gestures).
4. Searchable, task-oriented documentation with numbered steps (at most five per task).

If many users look up the docs to do one thing, the interface is the problem.

## Components

**The Library-First Rule.** Before building any component, check whether the project already uses a UI library (for example shadcn/ui, Radix, MUI, Headless UI, a native component kit). Look at the dependencies and the existing components; if it is not clear, ask the project owner before writing anything.

- **A library is in use:** never rewrite its components. Keep the library and adapt it to Kore: map Kore's tokens (colors, typography, rounded, spacing, shadows, motion) onto the library's theme, and override a component's styles only where the library's defaults break a Kore rule.
- **No library:** use the Kore components defined below, built on Kore's tokens and following every rule in this file.

> **To do (as of 2026-09-26).** Components still to define, in this order:
> 1. Overlay: menu/popover (same look as the select menu), dialog, sheet, tooltip.
> 2. Feedback: toast (including the 5-second "Undo"), skeleton, progress bar, empty state. Spinner and inline errors already exist in Button and Form fields.
> 3. Data and identity: badge/pill, avatar, status dot.
> 4. Navigation: top bar, bottom nav (mobile), side nav (desktop), tabs (navigation between sections, not the segmented control).
>
> After the components: bump Kore to version 1.0.0, then apply Kore to Vitae starting from `globals.css` (Vitae uses shadcn/ui with Base UI, so The Library-First Rule applies).
>
> **Also to review (draft, not yet approved):** a "Start here" section at the top of this file, telling the AI what to ask the user before starting a project with Kore:
> 1. Project type: app, landing/marketing, or both (sets Operate vs Persuade: motion, fluid type, glows, density).
> 2. Platforms and stack: web, iOS, Android; which framework (how tokens are exposed, which icon package).
> 3. Existing UI library? (The Library-First Rule.)
> 4. Existing icon library? Otherwise Hugeicons.
> 5. Keep the active identity or pick candidates: canvas, `signature`, display and sans fonts. If changed: move the choice to the frontmatter, log it in the Changelog, re-check every dependent contrast.
> 6. Themes: both or one, and which is the default (chosen from the use scene).
> 7. Language and formats: UI language, dates, currencies, units (metric or imperial).
> 8. Brand constraints already decided (logo, mandatory color, licensed font): they win over active values but stay subject to contrast and accessibility rules.
>
> Behaviour rules in the draft: ask once, grouped, at the start; never invent values outside the file (propose, and add to candidates and Changelog if approved); apply *Calm Clarity* where no rule covers a choice; binding rules (8-point grid, contrast, Hairline, Half-Padding, no icons on labeled buttons) change only with the user's explicit consent.

### Button

Five variants, three sizes, one shape. Every button has all its states.

| Variant | Background | Text | Border | Shadow | Hover | Pressed | Use |
|---|---|---|---|---|---|---|---|
| primary | `primary` | `primary-on` | none | `shadow-rest` | `shadow-hover` + 4px lift | `primary-pressed` | The main action of the view (The One Primary Rule) |
| secondary | `secondary` | `ink` | 1px `hairline-strong` | `shadow-rest` | `shadow-hover` + 4px lift | `surface-elevated` | Other important actions |
| outline | transparent | `ink` | 1px `hairline-strong` | none | `accent` background | `surface-elevated` | Tertiary actions, next to a primary |
| ghost | transparent | `ink` | none | none | `accent` background | `surface-elevated` | Low-emphasis actions, toolbars |
| destructive | `accent-red` | `accent-red-on` | none | `shadow-rest` | `shadow-hover` + 4px lift | `accent-red-pressed` | Delete and other destructive actions |

| Size | Height | Horizontal padding | Radius | Type |
|---|---|---|---|---|
| default | 48px | `space-6` (24px) | `lg` (16px) | `button-md` |
| compact | 40px | `space-4` (16px) | `lg` (16px) | `button-md` |
| small | 32px | `space-3` (12px) | `md` (12px), so it never turns into a pill | `button-sm`, hit area extended to 44px |

- **Icon buttons** are square in the same three sizes and always carry an accessible label and a tooltip.
- **No icons on labeled buttons.** A button with a label shows only text. The one exception is the loading spinner, placed before the label with `space-2` (8px).
- **Focus:** 2px `focus-ring` at a 2px offset, on every variant.
- **Disabled:** `surface-elevated` background, `stone` text, no shadow, not-allowed cursor; outline keeps a `hairline` border. Explain why it is disabled when it is not obvious.
- **Loading:** a spinner plus the running action ("Saving…"); the button keeps its width and ignores further clicks.
- **Timing:** press in `duration-instant`; shadow and lift in `duration-fast` with `ease-out`; no lift under reduced motion or on touch.
- **Shadows** only on filled buttons (primary, secondary, destructive); outline and ghost show hover with a background change.
- **Destructive in dark** uses black text: white on `#ef4444` is only 3.76:1, black is 5.58:1.
- **Borders** are drawn inside the edge (inset ring), so they never change the button's size.
- **Labels** are a verb and an object ("Save meal", "Delete workout"), never "OK", "Yes" or "Submit".

### Form fields

Text input, textarea and select share one look.

| Part | Spec |
|---|---|
| Field | Height 48px (compact 40px); padding `space-4` (16px), textarea `space-3` × `space-4`; radius `lg` (16px); background `surface-deep`; 1px `hairline-strong` border drawn inside |
| Text | `body-md` (16px) in `ink`; placeholder in `mute`, only as an example, never as the label |
| Label | `body-sm` medium in `ink`, above the field, `space-2` (8px) away; "(optional)" in `mute` when the field is optional |
| Help text | `body-sm` in `mute`, below the field, `space-1` (4px) away |
| Error | Red `accent-red` border plus a message in `accent-red` **with the alert icon**, linked to the field (`aria-invalid`, `aria-describedby`) |

- **States:** hover turns the border `mute`; **focus thickens the border to 2px `ink`, with no outer ring**; disabled uses `surface-elevated`, `stone` text and a `hairline` border; read-only uses `surface-elevated` with no border and stays selectable.
- **Adornments:** a 20px icon on the left (search) with the text starting at 44px; a unit on the right ("kg", "g") in `mute`.
- **Textarea:** minimum height 96px, resizable vertically only.
- **Validation** runs when the user leaves the field, and the error disappears as soon as the value is valid.

### Select

A custom menu, never the browser's native dropdown.

- **Trigger:** looks like a text field, with the Hugeicons down arrow on the right that rotates when open. Placeholder in `mute` until a value is chosen.
- **Menu:** `surface-deep`, 1px `hairline`, radius `lg` (16px), padding `space-2` (8px), opening under the trigger at `space-2`. Opens in `duration-base` with `ease-out`, closes in `duration-fast` with `ease-in`; no border shadow (see The Hairline Rule).
- **Options:** 44px tall, radius `md` (12px, from the Half-Padding Rule), `body-md`; the active option has `surface-elevated`; the selected one is medium weight with a check icon on the right.
- **Keyboard and screen readers:** arrows move, Enter or Space selects, Escape and click outside close; focus returns to the trigger. Uses `listbox` / `option` roles and `aria-activedescendant`.

### Checkbox and radio

- **Checkbox:** 20px, radius `xs` (4px), `surface-deep` with a `hairline-strong` border. Checked: `primary` fill with a `primary-on` check icon. Indeterminate: `primary` fill with a minus icon.
- **Radio:** 20px circle; checked: `primary` fill with an 8px `primary-on` dot.
- **Rows:** the whole row (control + label) is clickable and at least 44px tall; label in `body-md`, `space-3` (12px) from the control.
- **Groups** sit in a `fieldset` with a `legend` as the group label.
- **Disabled:** `surface-elevated` with a `hairline` border and `stone` label; a checked disabled control uses a `stone` fill.
- **Focus:** 2px `focus-ring` at a 2px offset around the box or circle.

### Switch

- 40 × 24px track, 16px knob, padding `space-1` (4px); hit area extended to 44px with an invisible overlay.
- **Off:** `surface-elevated` track with a `hairline-strong` border, `ink` knob. **On:** `primary` track, `primary-on` knob. Never green: green means success.
- The knob moves with `spring` (or `duration-fast` with `ease-out`); under reduced motion it changes without sliding.
- A switch always sits next to its visible label and applies the change immediately; use a checkbox when the change waits for a Save.

### Segmented control

- **Container:** 48px tall, radius `lg` (16px), padding `space-1` (4px), `surface-elevated` with a `hairline` border. It hugs its segments, never stretches to full width.
- **Segments:** 40px tall, radius `md` (12px, from the Half-Padding Rule), padding `space-4` (16px), `button-md`, `mute` text. Selected: `surface-card` with a `hairline` border and `ink` text.
- For two to five short, mutually exclusive options that switch a view; for more options, use a select.

### Cards

| Card | Padding | Inside | Shadow |
|---|---|---|---|
| Standard | `space-6` (24px) | Rows separated by space only (`space-4`, 16px); no rounded inner blocks | none |
| Compact | `space-4` (16px) | The only card that may hold rounded inner blocks: `surface-elevated`, radius `lg` (16px, from the Half-Padding Rule), padding `space-3` × `space-4`, gap `space-2` | none |
| Clickable | `space-6` (24px) | Title, subtitle and a Hugeicons arrow on the right | `shadow-rest`, `shadow-hover` + 4px lift on hover |

- **Shape and surface:** `surface-card`, 1px `hairline` drawn inside, radius `xl` (24px), the same padding on all four sides.
- **Header:** title in `heading-sm`, subtitle in `body-sm` `mute`, `space-1` (4px) apart; `space-6` (24px) between the header and the content (`space-4` in compact cards).
- **Key figure:** when a card exists to show one number, the number is its focal point: `display-lg` in `signature`, with its unit and context in `body-sm` `mute` on the same baseline.
- **Clickable card:** the whole card is one link or button. It fills the full width of its container, with the arrow anchored to the right edge. Focus uses the 2px `focus-ring`; pressed returns to rest. It never contains other buttons or links.
- **Spacing between cards:** `space-8` (32px); on phones `space-4` to `space-6`.
- **Never nest cards.** Inner content uses rows (standard card) or inner blocks (compact card).

### List rows

- **Row:** at least 56px tall, padding `space-2` × `space-3`; leading element, text and trailing element separated by `space-4` (16px).
- **Leading:** a 40px circle in `surface-elevated` with a 20px icon, or an avatar.
- **Text:** title in `body-md` medium `ink`; secondary line in `body-sm` `mute`, one line, truncated with an ellipsis.
- **Trailing:** a value in `body-sm` `mute` with tabular figures, and/or the Hugeicons arrow when the row opens something.
- **Clickable rows** are links: hover gives the `accent` background, pressed `surface-elevated`, focus the 2px `focus-ring`. The highlight extends `space-3` (12px) beyond the text, and its radius comes from the container with the Half-Padding Rule (inside a standard card: 24 − 12 ÷ 2 = 18, rounded down to `lg` 16px).
- **Static rows** do not react to hover.
- Rows separate with space only, never with a divider on every row.

## Do's and Don'ts

### Do

- **Do** spend `primary` on one main action per view (The One Primary Rule).
- **Do** separate static layers with a surface step and a 1px `hairline`; give `shadow-rest` / `shadow-hover` only to clickable elements (The Hairline Rule).
- **Do** take every margin, padding and gap from the `space-*` scale, and give cards the same padding on all four sides: `space-6` (24px), compact `space-4` (16px) (The Token-Only Rule).
- **Do** compute nested radii as outer − padding ÷ 2, rounded down to the scale (The Half-Padding Rule).
- **Do** use the display font only for `display-*` roles (40px and up), the sans for everything else, and the mono only for code, data and measurements.
- **Do** keep running text at 16px (`body-md`) or larger, in lines of 45–75 characters.
- **Do** give every control all its states (default, hover, focus, active, disabled, selected, loading, error), with a visible focus (2px `ink` border on fields, 2px `focus-ring` on other controls).
- **Do** pair every status color with a text label or an icon.
- **Do** size controls at 48px, compact 40px, minimum 32px with a 44 × 44px hit area.
- **Do** label actions with a verb and an object ("Save meal", "Delete workout"); name the object and the consequence on destructive actions; prefer undo over a confirmation when recovery is safe.
- **Do** write errors that say what failed and how to recover, without blaming the user or showing internal codes.
- **Do** keep form labels visible at all times; a placeholder is an example, never the label.
- **Do** make empty states explain the situation and offer the next useful action; show loading with content skeletons, not a spinner in the middle of the page.
- **Do** give every screen and zone one focal point that wins on at least two weight tools (The One Winner Rule).
- **Do** separate with the lightest step that works: space, then background, then line, then card (The Separation Ladder).
- **Do** answer every action within 100ms, show loading after 300ms and progress after 1s.
- **Do** offer "Undo" for 5 seconds after a destructive action instead of asking first, when the action can be undone.
- **Do** show limits, formats and requirements before the user acts, and validate when they leave a field.
- **Do** check both themes, every width from 320px to 4K, and 200% text zoom before shipping.

### Don't

- **Don't** use gradient text. Emphasis comes from weight or size.
- **Don't** put a colored border thicker than 1px on the left or right side of cards, list items, callouts or alerts.
- **Don't** put an eyebrow or kicker label above a heading. The heading carries its own weight.
- **Don't** number sections (01 / 02 / 03) unless the order itself is information the reader needs.
- **Don't** nest cards. Inner blocks use `surface-elevated` as rows or wells, never as cards.
- **Don't** use glass or blur as decoration.
- **Don't** use hard offset shadows with no blur.
- **Don't** use monospace as a costume for "technical".
- **Don't** use emoji or Unicode symbols instead of icons. Icons come from one real library or authored SVG, with one stroke and weight.
- **Don't** build a whole page out of same-size icon + heading + text cards.
- **Don't** open a modal for a task that needs neither interruption nor protected focus; try inline or progressive alternatives first.
- **Don't** pick the light or dark default by habit; choose it from the use scene (who, where, what light).
- **Don't** use `signature` or any `*-glow` as a button or a surface, or on dense task screens.
- **Don't** introduce a second brand color.
- **Don't** add a spacing, color or radius token for a single case.
- **Don't** put translucent text (`body`, `charcoal`, `on-light-mute`) on a new surface without re-checking its contrast.
- **Don't** mix corner shapes: no squircle, no cut corners.
- **Don't** hide a function behind hover.
- **Don't** use "Yes", "No", "OK" or "Submit" on confirmations; the button names the action.
- **Don't** put three primary actions, or three equally weighted elements, in the same zone.
- **Don't** put a divider on every row of a list; rows separate with space.
- **Don't** add a container or border just to tidy up; fix the grouping instead.
- **Don't** show error codes, database values or internal terms to users.
- **Don't** let users discover a limit only after they submit.
- **Don't** use different names, icons or formats for the same thing in different places.

## Candidates

Alternative values for each token. The frontmatter holds the active value for the current project; to change it in a new project, pick a candidate from here. Every alternative we evaluate for a token is added to its list.

### canvas — light

| Name | Hex | |
|---|---|---|
| Ice | `#F8FAFB` | active |
| Ghost White | `#F8F8FF` |  |
| Snow Drift | `#F8FBF8` |  |
| Vista White | `#FDFCFA` |  |
| White Smoke | `#F5F5F5` |  |
| Vivid White | `#F8F8F4` |  |

### canvas — dark

| Name | Hex | |
|---|---|---|
| Night | `#0C090A` | active |
| Crow | `#0D0907` |  |
| Spider | `#040200` |  |
| Sable | `#060606` |  |
| True Black | `#0A0B0B` |  |

### surface-card — light

| Hex | |
|---|---|
| `#fcfdfd` | active |
| `#ffffff` |  |
| `#f1f4f5` |  |
| `#eceff1` |  |

### surface-card — dark

| Hex | |
|---|---|
| `#121212` | active |
| `#151213` |  |
| `#1a1718` |  |
| `#1f1c1d` |  |

### surface-elevated — light

| Hex | |
|---|---|
| `#f4f6f7` | active |
| `#f0f3f5` |  |
| `#ebeef0` |  |
| `#e5e9ec` |  |

### surface-elevated — dark

| Hex | |
|---|---|
| `#1f1f1f` | active |
| `#181818` |  |
| `#242424` |  |
| `#2a2a2a` |  |

### surface-deep — light

| Hex | |
|---|---|
| `#fcfdfd` | active |
| `#f1f4f5` |  |
| `#ebeef0` |  |
| `#e6eaed` |  |

### surface-deep — dark

| Hex | |
|---|---|
| `#060606` | active |
| `#080607` |  |
| `#040404` |  |
| `#000000` |  |

### hairline — light

| Value | |
|---|---|
| `rgba(33, 33, 33, 0.06)` | active |
| `rgba(33, 33, 33, 0.04)` |  |
| `rgba(33, 33, 33, 0.08)` |  |
| `rgba(33, 33, 33, 0.10)` |  |

### hairline — dark

| Value | |
|---|---|
| `rgba(255, 255, 255, 0.04)` | active |
| `rgba(255, 255, 255, 0.08)` |  |
| `rgba(255, 255, 255, 0.10)` |  |
| `rgba(255, 255, 255, 0.12)` |  |

### hairline-strong — light

| Value | |
|---|---|
| `#8a8e92` | active |
| `rgba(33, 33, 33, 0.12)` | below 3:1 for control borders |
| `rgba(33, 33, 33, 0.16)` |  |
| `rgba(33, 33, 33, 0.20)` |  |
| `rgba(33, 33, 33, 0.24)` |  |

### hairline-strong — dark

| Value | |
|---|---|
| `#6e6a6a` | active |
| `rgba(255, 255, 255, 0.12)` | below 3:1 for control borders |
| `rgba(255, 255, 255, 0.16)` |  |
| `rgba(255, 255, 255, 0.24)` |  |
| `rgba(255, 255, 255, 0.28)` |  |

### divider-soft — light

| Value | |
|---|---|
| `#efeff1` | active |
| `rgba(33, 33, 33, 0.03)` |  |
| `rgba(33, 33, 33, 0.04)` |  |
| `rgba(33, 33, 33, 0.05)` |  |

### divider-soft — dark

| Value | |
|---|---|
| `rgba(255, 255, 255, 0.04)` | active |
| `rgba(255, 255, 255, 0.02)` |  |
| `rgba(255, 255, 255, 0.03)` |  |

### ink — light

| Hex | |
|---|---|
| `#2a2a2a` | active |
| `#18181b` |  |
| `#1b1d1f` |  |
| `#111111` |  |

### ink — dark

| Hex | |
|---|---|
| `#f5f3f3` | active |
| `#f5f5f5` |  |
| `#ededed` |  |
| `#e8e6e6` |  |

### body — light

| Value | |
|---|---|
| `rgba(42, 42, 42, 0.86)` | active |
| `rgba(42, 42, 42, 0.92)` |  |
| `rgba(42, 42, 42, 0.80)` |  |
| `rgba(42, 42, 42, 0.74)` |  |

### body — dark

| Value | |
|---|---|
| `rgba(245, 243, 243, 0.86)` | active |
| `rgba(245, 243, 243, 0.92)` |  |
| `rgba(245, 243, 243, 0.80)` |  |
| `rgba(245, 243, 243, 0.74)` |  |

### charcoal — light

| Value | |
|---|---|
| `rgba(42, 42, 42, 0.72)` | active |
| `rgba(42, 42, 42, 0.80)` |  |
| `rgba(42, 42, 42, 0.76)` |  |
| `rgba(42, 42, 42, 0.68)` |  |

### charcoal — dark

| Value | |
|---|---|
| `rgba(245, 243, 243, 0.72)` | active |
| `rgba(245, 243, 243, 0.80)` |  |
| `rgba(245, 243, 243, 0.76)` |  |
| `rgba(245, 243, 243, 0.68)` |  |

### mute — light

| Hex | |
|---|---|
| `#6a6e72` | active |
| `#666666` |  |
| `#6b6b6b` |  |
| `#707070` |  |

### mute — dark

| Hex | |
|---|---|
| `#918d8d` | active |
| `#a39f9f` |  |
| `#9a9696` |  |
| `#8a8686` |  |

### stone — light

| Hex | |
|---|---|
| `#a9adb1` | active |
| `#b8bcc0` |  |
| `#c4c8cc` |  |
| `#cfd2d5` |  |

### stone — dark

| Hex | |
|---|---|
| `#464a4d` | active |
| `#5e5a5a` |  |
| `#524e4e` |  |
| `#4a4646` |  |
| `#3f3b3b` |  |

### on-light — light & dark

| Value | |
|---|---|
| `#2a2a2a` | active |
| `#000000` |  |

### on-light-mute — light & dark

| Value | |
|---|---|
| `rgba(42, 42, 42, 0.72)` | active |
| `#6a6e72` |  |

### primary-pressed — light

| Hex | |
|---|---|
| `#2e2e2e` | active |
| `#000000` |  |
| `#0a0a0a` |  |
| `#383838` |  |

### primary-pressed — dark

| Hex | |
|---|---|
| `#ebecee` | active |
| `#e6e7e9` |  |
| `#dcdee1` |  |
| `#d1d4d8` |  |

### secondary — light

| Hex | |
|---|---|
| `#f4f6f7` | active |
| `#f2f4f5` |  |
| `#f0f2f4` |  |
| `#eef0f2` |  |

### signature — light

| Hex | |
|---|---|
| `#904E55` | active |
| `#EB5E28` |  |
| `#F8F1FF` |  |

### signature — dark

| Hex | |
|---|---|
| `#F8F1FF` | active |
| `#EB5E28` |  |
| `#904E55` |  |

### accent-yellow — light

| Hex | |
|---|---|
| `#92400e` | active |
| `#b45309` |  |
| `#a16207` |  |
| `#d97706` |  |

### accent-yellow — dark

| Hex | |
|---|---|
| `#ffc53d` | active |
| `#facc15` |  |
| `#fbbf24` |  |
| `#f5b83d` |  |
| `#ffd166` |  |

### accent-blue — light

| Hex | |
|---|---|
| `#386580` | active |
| `#457B9D` |  |
| `#788AA3` |  |
| `#44799b` |  |
| `#407191` |  |

### accent-blue — dark

| Hex | |
|---|---|
| `#5b94b7` | active |
| `#457B9D` |  |
| `#788AA3` |  |
| `#477ea1` |  |
| `#4b86ab` |  |

### accent-green — light

| Hex | |
|---|---|
| `#047857` | active |
| `#15803d` |  |
| `#2f855a` |  |
| `#3a7d44` |  |

### accent-green — dark

| Hex | |
|---|---|
| `#6ee7b7` | active |
| `#4ade80` |  |
| `#34d399` |  |
| `#86efac` |  |

### accent-red — light

| Hex | |
|---|---|
| `#c53030` | active |
| `#b91c1c` |  |
| `#be123c` |  |
| `#9b2c2c` |  |

### accent-red — dark

| Hex | |
|---|---|
| `#ef4444` | active |
| `#f87171` |  |
| `#ff5a6e` |  |
| `#fb7185` |  |

### font — sans (body and UI)

| Font | |
|---|---|
| Figtree | active |
| Geist |  |
| Outfit |  |
| Urbanist |  |
| DM Sans |  |
| Manrope |  |
| Rubik |  |
| Nunito |  |
| Quicksand |  |
| Varela Round |  |

### font — display (large headlines)

| Font | |
|---|---|
| Outfit | active |
| Figtree |  |
| Fraunces |  |
| Urbanist |  |

### font — mono (code, tabular numbers)

| Font | |
|---|---|
| Geist Mono | active |
| DM Mono |  |
| Red Hat Mono |  |
| JetBrains Mono |  |
| IBM Plex Mono |  |
| Martian Mono |  |

### display-xxl — size / line-height

| Size / line-height | |
|---|---|
| 64 / 64 | active |
| 96 / 96 |  |
| 88 / 88 |  |
| 80 / 80 |  |
| 72 / 72 |  |

### display-xxl — weight

| Weight | |
|---|---|
| 500 | active |
| 300 |  |
| 400 |  |
| 600 |  |

### display-xl — size / line-height

| Size / line-height | |
|---|---|
| 48 / 48 | active |
| 56 / 56 |  |
| 52 / 52 |  |
| 44 / 44 |  |

### rounded — set

| Set | |
|---|---|
| B · Round — controls 16 · inner blocks 16 · cards 24 | active |
| Current — controls 8 · inner blocks 8 · cards 12 |  |
| A · Soft — controls 12 · inner blocks 12 · cards 16 |  |
| C · Pill — controls full · inner blocks 16 · cards 24 |  |

## Changelog

Versioning follows [semver](https://semver.org): **MAJOR** for breaking changes (renamed or removed tokens, changed scales), **MINOR** for compatible additions (new components or variants), **PATCH** for fixes that don't change usage.

### 0.1.0
- Initial draft: name, versioning, description.
- Colors: brand group (`primary`, `primary-on`, `primary-pressed`) for light and dark themes. `surface-light` renamed to `primary-pressed`; light value fixed to `#3f3f46`.
- Colors: `canvas` for light (Ice `#F8FAFB`) and dark (Night `#0C090A`), placed before the brand group.
- New Candidates section: alternative values per token, starting with `canvas`.
- Colors: `primary-pressed` changed to `#2e2e2e` (light) and `#ebecee` (dark); new `secondary` token, `#f4f6f7` (light) and `#1c1c1c` (dark).
- Candidates: added `primary-pressed` and `secondary`.
- Colors: new `accent` token (hover surface), `#f4f4f5` (light) and `#1c1c1c` (dark).
- Description: canvas now described as a cool off-white (light) and a soft near-black (dark).
- Colors: new `surface-card` token (card background), `#fcfdfd` (light) and `#121212` (dark).
- Candidates: added `surface-card`.
- Colors: new `surface-elevated` token (second surface step), `#f4f6f7` (light) and `#1f1f1f` (dark).
- Candidates: added `surface-elevated`.
- Colors: new `surface-deep` token (popovers, menus, code wells), `#fcfdfd` (light) and `#060606` (dark).
- Candidates: added `surface-deep`.
- Colors: new `hairline` token (thin 1px border for non-interactive elements, row dividers), `rgba(33, 33, 33, 0.06)` (light) and `rgba(255, 255, 255, 0.04)` (dark).
- Candidates: added `hairline`.
- Colors: new `hairline-strong` token (1px border for controls: inputs, secondary and outline buttons), `rgba(33, 33, 33, 0.12)` (light) and `rgba(255, 255, 255, 0.12)` (dark).
- Candidates: added `hairline-strong`.
- Colors: new `divider-soft` token (faintest divider: footer columns, copyright row), `#efeff1` (light) and `rgba(255, 255, 255, 0.04)` (dark).
- Candidates: added `divider-soft`.
- Colors: new `ink` token (main text), `#2a2a2a` (light) and `#f5f3f3` (dark).
- Candidates: added `ink`.
- Colors: new `body` token (long-form text), `rgba(42, 42, 42, 0.86)` (light) and `rgba(245, 243, 243, 0.86)` (dark) — `ink` at 86%.
- Candidates: added `body`.
- Colors: new `charcoal` token (captions, secondary labels), `rgba(42, 42, 42, 0.72)` (light) and `rgba(245, 243, 243, 0.72)` (dark) — `ink` at 72%.
- Candidates: added `charcoal`.
- Colors: new `mute` token (supporting text, inactive labels), `#6a6e72` (light) and `#918d8d` (dark).
- Candidates: added `mute`.
- Colors: `ash` removed — tertiary and footer text use `mute`, since anything lighter than `mute` falls below the 4.5:1 text contrast minimum.
- Colors: new `stone` token (disabled foreground), `#a9adb1` (light) and `#464a4d` (dark).
- Candidates: added `stone`.
- Colors: new `on-light` (`#2a2a2a`) and `on-light-mute` (`rgba(42, 42, 42, 0.72)`) tokens for text inside the white light inset; same value in both themes.
- Candidates: added `on-light` and `on-light-mute`.
- Colors: `accent-orange` replaced by `signature` (Kore's distinctive colour: glows, chart data, emphasis), `#904E55` (light) and `#F8F1FF` (dark), with `signature-glow` at 20% (light) and 22% (dark).
- Candidates: added `signature`.
- Colors: new `accent-yellow` token (warning, highlight strokes), `#92400e` (light) and `#ffc53d` (dark).
- Candidates: added `accent-yellow`.
- Colors: new `accent-blue` token (inline links, cool glow), `#386580` (light) and `#5b94b7` (dark) — accessible variants of `#457B9D` — with `accent-blue-glow` at 20% (light) and 34% (dark).
- Candidates: added `accent-blue`.
- Colors: new `accent-green` token (success), `#047857` (light) and `#6ee7b7` (dark), with `accent-green-glow` at 20% (light) and 18% (dark).
- Candidates: added `accent-green`.
- Colors: new `accent-red` token (errors, destructive actions, attention), `#c53030` (light) and `#ef4444` (dark), with `accent-red-glow` at 20% (light) and 34% (dark).
- Candidates: added `accent-red`.
- Colors: new `link` token (inline links), `#386580` (light) and `#5b94b7` (dark) — same values as `accent-blue`, kept as a separate token.
- Typography: sans font (body and UI) set to Figtree.
- Candidates: added sans font options.
- Typography: display font (large headlines) set to Outfit.
- Candidates: added display font options.
- Typography: mono font (code, tabular numbers) set to Geist Mono.
- Candidates: added mono font options.
- Description: headline and body fonts now described as round geometric sans and friendly geometric sans.
- Description: "editorial" replaced by "minimal".
- Typography: `display-xxl` set to Outfit 64/64, weight 500, letter-spacing −0.02em.
- Candidates: added `display-xxl` sizes and weights.
- Typography: full scale added — `display-xl` 48/48 and `display-lg` 40/40 (Outfit 500), `heading-md` 24/32 and `heading-sm` 20/28 (Figtree 600), `subtitle` 20/28, `body-lg` 18/28, `body-md` 16/24, `body-sm` 14/20, `button-md` 14/20, `button-sm` 12/16, `caption` 12/16, `caption-emph` 12/16 (Figtree), `code-md` 13/20 (Geist Mono). All line-heights are multiples of 4.
- Candidates: added `display-xl` sizes.
- Shapes: `rounded` scale set to 0 / 4 / 8 / 12 / 16 / 24 / full (6px removed, off the 4px grid). Set B: controls and inner blocks 16px (`lg`), cards 24px (`xl`), pills and avatars full.
- Shapes: `cornerShape: squircle` as progressive enhancement — browsers without `corner-shape` support (Safari, iOS) fall back to round corners with the same radius.
- Candidates: added `rounded` sets.
- Description: container vocabulary now rounded-24px with squircle corners where supported.
- Spacing: scale `space-1` … `space-12` (name = N × 4px) — primary 4 / 8 / 16 / 24 / 32 / 48, half-steps 12 / 20 / 40 only when needed; no 96/128.
- New Spacing section: scale with when-to-use, binding rules, proximity and hierarchy, reference values, accessibility, common mistakes, checklist, stack-agnostic implementation.
- Italian version (KORE.it.md) dropped; Kore is maintained in English only.
- Colors: `hairline-strong` changed to solid `#8a8e92` (light) and `#6e6a6a` (dark) so control borders reach 3:1 (WCAG 1.4.11) on every surface; the old 12% values failed at ~1.3:1.
- Colors: new `info` (same values as `accent-blue`), `focus-ring` (`#2a2a2a` / `#f5f3f3`) and `selection` (signature at 20% / 22%) tokens.
- New sections from the Impeccable review: Color rules (contrast, meaning, states, themes, glows), Typography rules, Shadows, Motion, Browser surfaces, Never.
- New Elevation section (replaces Shadows): levels flat / surface / inset / floating / overlay / interactive, barely perceptible `shadow-rest` and `shadow-hover` tokens, hover lift of 4px, reduced-motion behaviour, `scrim` color and a fixed `zIndex` scale.
- Shapes: `cornerShape: squircle` removed — squircle corners cannot be concentric when nested, and Safari does not support them. Kore uses round corners everywhere.
- Description: "with squircle corners where supported" replaced by "with concentric nested corners".
- New Shapes section: radius by role, binding nested-radius rule (inner = outer − padding ÷ 2, rounded down to the scale), standard cards use hairline-divided rows instead of rounded inner blocks, borders drawn inside the edge.
- New Responsive section: mobile-first principles, breakpoints `sm` 640 / `md` 768 / `lg` 1024 and `max-content` 1200 (in the frontmatter), grids and gutters, display type stepping down on phones, input-based hover, safe areas, extremes, tables and media, testing.
- The Never section becomes Do's and Don'ts: 14 Do's with tokens and values (including UI copy, forms, empty and loading states) and 19 Don'ts (the previous 12 plus 7 new).
- Named rules: The One Primary Rule (Color rules), The Token-Only Rule (Spacing), The Half-Padding Rule (Shapes), The Hairline Rule (Elevation).
- Motion section rewritten: duration, easing and spring tokens (in the frontmatter), rules for all modes, app mode, landing mode with one focal moment, stack-agnostic implementation. Reviewed with Impeccable and the Motion.dev skill.
- Elevation: hover timing now uses the motion tokens (`duration-fast`, `ease-out`; pressed `duration-instant`) instead of a free 200ms.
- Components section added as a placeholder note: components are defined per project; with an existing UI library Kore only reskins it through its tokens and rules.
- New Hierarchy section: six visual-weight tools, The One Winner Rule, three levels with focal points per context, typographic levels, The Separation Ladder, scanning patterns (F and Z), three-second check.
- New Usability section based on Nielsen's 10 heuristics, with Kore's concrete values (feedback at 100ms / 300ms / 1s / 3s, 5-second undo, validation on blur, layered help).
- Shapes: rows inside a standard card now separate with space only (was `hairline` dividers).
- Do's and Don'ts: 5 Do's and 6 Don'ts added for hierarchy and usability.
- New Overview section: guiding principle *Calm Clarity*, intro paragraph and ten key characteristics, written with the humanizer skill.
- Overview: "Creative North Star" renamed to "Guiding principle", with a line on how to use it for choices the rules don't cover.
- Components: placeholder note replaced by The Library-First Rule (check for a UI library first, ask if unsure; with a library, map tokens and override only where needed; without one, use Kore's components).
- New Icons section: library-first, default Hugeicons (free, Stroke Rounded, MIT, official packages for all major stacks), rules for stroke, sizes, color, spacing, accessibility and meaning, plus library candidates. Icon settings also in the frontmatter.
- Components: Button added (five variants, three sizes, icon buttons, all states) in the frontmatter and the Components section; new color tokens `accent-red-on` and `accent-red-pressed`.
- Button: labeled buttons carry no icon; the only exception is the loading spinner. Icons section spacing updated accordingly.
- Components: form controls added (text input, textarea, custom select with its own menu, checkbox, radio, switch, segmented control) in the frontmatter and the Components section.
- Focus: form fields now thicken their border to 2px `ink` with no outer ring; other controls keep the 2px `focus-ring` at a 2px offset.
- Typography rules: form fields use `body-md` (16px) so mobile Safari doesn't zoom on focus.
- Switch: reduced from 52 × 32 to 40 × 24 (16px knob), hit area still 44px.
- Components: containers added (standard, compact and clickable cards, card header and key figure, list rows) in the frontmatter and the Components section.
- Components: to-do note added listing the components still to define (overlay, feedback, data and identity, navigation) and the next steps.
- To-do note: added the draft "Start here" questions and AI behaviour rules, pending review.
