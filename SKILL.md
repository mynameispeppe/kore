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
  spacing and sizing sit on an 8-point grid (4px half-steps).
  There is no decorative chrome — just type, content, and atmospheric depth.
colors:
  light:
    canvas: "#F8FAFB"
    surface-card: "#fcfdfd"
    surface-elevated: "#f4f6f7"
    surface-deep: "#fcfdfd"
    surface-float: "#fcfdfd"
    surface-float-active: "#f4f6f7"
    hairline: "rgba(33, 33, 33, 0.06)"
    hairline-strong: "#8a8e92"
    ink: "#2a2a2a"
    body: "rgba(42, 42, 42, 0.86)"
    charcoal: "rgba(42, 42, 42, 0.72)"
    mute: "#6a6e72"
    stone: "#a9adb1"
    on-light-mute: "rgba(42, 42, 42, 0.72)"
    primary: "#212121"
    primary-on: "#ffffff"
    primary-pressed: "#2e2e2e"
    surface-hover: "#f4f4f5"
    accent: "#904E55"
    accent-glow: "rgba(144, 78, 85, 0.20)"
    warning: "#92400e"
    info: "#386580"
    info-glow: "rgba(56, 101, 128, 0.20)"
    success: "#047857"
    success-glow: "rgba(4, 120, 87, 0.20)"
    danger: "#c53030"
    danger-glow: "rgba(197, 48, 48, 0.20)"
    danger-on: "#ffffff"
    danger-pressed: "#b91c1c"
    link: "#386580"
    focus-ring: "#6a6e72"
    selection: "rgba(144, 78, 85, 0.20)"
    scrim: "rgba(12, 9, 10, 0.32)"
  dark:
    canvas: "#0C090A"
    surface-card: "#121212"
    surface-elevated: "#1f1f1f"
    surface-deep: "#060606"
    surface-float: "#1c1c1c"
    surface-float-active: "#2a2a2a"
    hairline: "rgba(255, 255, 255, 0.04)"
    hairline-strong: "#6e6a6a"
    ink: "#f5f3f3"
    body: "rgba(245, 243, 243, 0.86)"
    charcoal: "rgba(245, 243, 243, 0.72)"
    mute: "#918d8d"
    stone: "#464a4d"
    on-light-mute: "rgba(42, 42, 42, 0.72)"
    primary: "#fcfdff"
    primary-on: "#000000"
    primary-pressed: "#ebecee"
    surface-hover: "#1c1c1c"
    accent: "#F8F1FF"
    accent-glow: "rgba(248, 241, 255, 0.22)"
    warning: "#ffc53d"
    info: "#5b94b7"
    info-glow: "rgba(91, 148, 183, 0.34)"
    success: "#6ee7b7"
    success-glow: "rgba(110, 231, 183, 0.18)"
    danger: "#ef4444"
    danger-glow: "rgba(239, 68, 68, 0.34)"
    danger-on: "#000000"
    danger-pressed: "#f87171"
    link: "#5b94b7"
    focus-ring: "#918d8d"
    selection: "rgba(248, 241, 255, 0.22)"
    scrim: "rgba(0, 0, 0, 0.60)"
fonts:
  display: Outfit
  sans: Figtree
  mono: Geist Mono
typography:
  display-lg:
    fontFamily: Outfit
    fontSize: 57px
    fontWeight: 400
    lineHeight: 64px
    letterSpacing: -0.25px
  display-md:
    fontFamily: Outfit
    fontSize: 45px
    fontWeight: 400
    lineHeight: 52px
  display-sm:
    fontFamily: Outfit
    fontSize: 36px
    fontWeight: 400
    lineHeight: 44px
  headline-lg:
    fontFamily: Figtree
    fontSize: 32px
    fontWeight: 400
    lineHeight: 40px
  headline-md:
    fontFamily: Figtree
    fontSize: 28px
    fontWeight: 400
    lineHeight: 36px
  headline-sm:
    fontFamily: Figtree
    fontSize: 24px
    fontWeight: 400
    lineHeight: 32px
  title-lg:
    fontFamily: Figtree
    fontSize: 22px
    fontWeight: 400
    lineHeight: 28px
  title-md:
    fontFamily: Figtree
    fontSize: 16px
    fontWeight: 500
    lineHeight: 24px
    letterSpacing: 0.15px
  title-sm:
    fontFamily: Figtree
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0.1px
  body-lg:
    fontFamily: Figtree
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
    letterSpacing: 0.5px
  body-md:
    fontFamily: Figtree
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
    letterSpacing: 0.25px
  body-sm:
    fontFamily: Figtree
    fontSize: 12px
    fontWeight: 400
    lineHeight: 16px
    letterSpacing: 0.4px
  label-lg:
    fontFamily: Figtree
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
    letterSpacing: 0.1px
  label-md:
    fontFamily: Figtree
    fontSize: 12px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.5px
  label-sm:
    fontFamily: Figtree
    fontSize: 11px
    fontWeight: 500
    lineHeight: 16px
    letterSpacing: 0.5px
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
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-pressed:
    backgroundColor: "{colors.primary-pressed}"
    textColor: "{colors.primary-on}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-elevated:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-elevated-pressed:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
  button-fab:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-on}"
    rounded: "{rounded.md}"
    padding: 12px
    size: 44px
  button-destructive:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.danger-on}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-destructive-pressed:
    backgroundColor: "{colors.danger-pressed}"
    textColor: "{colors.danger-on}"
  button-disabled:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.stone}"
  button-compact:
    typography: "{typography.label-lg}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 36px
  button-small:
    typography: "{typography.label-lg}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 32px
  text-input:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.md}"
    padding: 0 12px
    height: 40px
  text-input-error:
    borderColor: "{colors.danger}"
  text-input-disabled:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.stone}"
  field-label:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  field-help:
    textColor: "{colors.mute}"
    typography: "{typography.body-md}"
  field-error:
    textColor: "{colors.danger}"
    typography: "{typography.body-md}"
  textarea:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.body-lg}"
    rounded: "{rounded.md}"
    padding: 12px
  select-menu:
    backgroundColor: "{colors.surface-float}"
    rounded: "{rounded.md}"
    padding: 4px
  select-option:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 0 8px
    height: 44px
  select-option-active:
    backgroundColor: "{colors.surface-float-active}"
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
    rounded: "{rounded.md}"
    padding: 8px
    gap: 8px
    height: 48px
  segmented-item:
    textColor: "{colors.mute}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.xs}"
    padding: 0 16px
    height: 32px
  segmented-item-selected:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
  inline-button:
    rounded: "{rounded.xs}"
    offset: 8px
    size: container height − 16px
  corner-action:
    size: 32px
    rounded: "{rounded.sm}"
    offset: container radius − 8px
  password-toggle:
    size: 24px
    rounded: "{rounded.xs}"
    offset: 8px
  stepper:
    backgroundColor: "{colors.surface-deep}"
    rounded: "{rounded.md}"
    padding: 8px
    height: 48px
    width: 160px
  stepper-button:
    rounded: "{rounded.xs}"
    size: 32px
  slider-track:
    backgroundColor: "{colors.hairline-strong}"
    height: 4px
  slider-fill:
    backgroundColor: "{colors.primary}"
  slider-thumb:
    backgroundColor: "{colors.primary}"
    size: 20px
    height: 44px
  card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-compact:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 16px
  card-media-image:
    aspectRatio: 16 / 9
  card-actions:
    gapAbove: 32px
    gap: 8px
    offset: card radius − button radius
  menu:
    backgroundColor: "{colors.surface-float}"
    rounded: "{rounded.md}"
    padding: 4px
    groupGap: 8px
  menu-item:
    rounded: "{rounded.sm}"
    padding: 0 8px
    height: 44px
  menu-item-active:
    backgroundColor: "{colors.surface-float-active}"
  popover:
    backgroundColor: "{colors.surface-float}"
    rounded: "{rounded.md}"
    padding: 12px
  dialog:
    backgroundColor: "{colors.surface-float}"
    rounded: "{rounded.xl}"
    padding: 24px
    maxWidth: 480px
  sheet:
    backgroundColor: "{colors.surface-float}"
    rounded: "{rounded.xl}"
    padding: 24px
    sideWidth: 400px
    sideOffset: 8px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
    offset: 8px
  card-title:
    textColor: "{colors.ink}"
    typography: "{typography.title-lg}"
  card-subtitle:
    textColor: "{colors.mute}"
    typography: "{typography.body-md}"
  card-key-figure:
    textColor: "{colors.accent}"
    typography: "{typography.display-sm}"
  card-clickable:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  list-row:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 8px 12px
    height: 56px
    gap: 8px
  list-row-hover:
    backgroundColor: "{colors.surface-hover}"
  list-row-icon:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    size: 40px
---

## Start here

Read this section before any design or UI work with Kore. Kore promotes a minimal, clear and clean interface that never confuses the people using it; every rule below serves that goal.

This file is never edited during a project. The values chosen for a project live in that project's tokens (CSS variables, theme file or config), written from this file and following its token names and roles.

### Before the first line of code

Read the project first: request, dependencies, existing components, styles and assets. Anything already answered there is not asked. Ask the open questions below all together, in one message; if none is open, ask nothing and start.

1. **Is it a landing page or a web app?** Asked only when neither the request nor the project makes it clear. It sets the mode: landing page (persuade) or web app (operate), which changes motion, density, glows and fluid type. A project with both is two jobs, each in its own mode.
2. **Which framework?** Asked only when the project is empty (plain HTML and CSS, React, Vue, Svelte…). It decides how the tokens are exposed and which Hugeicons package to use. An empty project has no UI library, so Kore's own components apply. In an existing project, read the framework, the UI library and the icon library from the code (The Library-First Rule).
3. **Is there a brand identity already: logo, palette, fonts?** In an existing project, show what was found and ask only to confirm it. If there is none, use Kore's active identity.
   - **Logo:** used as it is. Check it on `canvas` in both themes; if it disappears in one, ask for a variant. Never derive the palette from the logo.
   - **Palette:** apply it with the Custom palette method (Color rules).
   - **Font:** any font the user chooses, even one outside the Candidates. One font may cover both `display` and `sans`. The type scale does not change: sizes, weights, line-heights and letter-spacing stay Kore's. Before applying it, check weights 400 and 500 (if one is missing, propose the nearest), the glyphs of the UI language, tabular figures (`tnum`) and a web license. Sum up the checks in one message and wait for the OK. Then change only the project's font tokens. Never resize the scale for the new font; sizes change only when the user asks, and always on the grid.
   - **Code:** when the user wants one font only, code uses the system monospace stack (`ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace`), which loads nothing. If no code appears in the interface, the mono token is unused and nothing is loaded. A proportional font for code only on an explicit request, with a one-line warning that alignment breaks and characters like `0`/`O` and `1`/`l` get confused.

After the answers, sum up the choices in two or three lines and start.

### Building anything

1. Check for a UI library first (The Library-First Rule).
2. If Kore defines the component, use it. If not, compose it from Kore's components and tokens; never invent values.
3. Apply the rules of the sections involved.
4. If the request breaks a rule, follow the three steps in Behaviour rules.
5. Before delivering, run Checks by context, item by item, and report the result in two lines: what was built, which checks ran, what was fixed and any exception.

Existing code is not proof: a reused or previously approved component goes through the same checks as a new one.

### Checks by context

Check every rule that concerns what is being built, one by one; never assume a rule holds. Skip only the rows that do not apply.

**Always:**
- Only tokens: every color, space, size, radius, shadow and duration comes from this file (search for free values such as `\b(1[0-9]|2[0-9]|3[0-9])px` outside token definitions).
- Contrast: text 4.5:1, large text 3:1, control borders, icons and focus 3:1, measured on `surface-elevated` and, in dark, `surface-float-active`, in both themes. In dark, `danger` text never sits on `surface-elevated` (4.4:1); red icons can.
- Both themes checked, each on its own.

| Building | Check |
|---|---|
| **Container** (card, panel, list) | Hierarchy: one focal point that wins on two of the six tools, primary > secondary > tertiary, no inverted hierarchy (metadata never outweighs the title), groups clear without extra borders. Semantic weight: no value repeats without a new purpose, roles differ by at least one clear step in size or weight, no asymmetry left unquestioned against the component's stated priority. Spacing: uniform padding (`space-6`, compact `space-4`), The Distance Ratio Rule (between ≥ 2 × inside: title ↔ subtitle `space-1`, header ↔ content `space-6`, rows `space-3`, compact rows `space-2`, rows ↔ actions `space-8`), list items `space-2` apart, two highlights never touch. Shapes: horizontal padding = radius, nested radii concentric (outer − distance), no rounded blocks inside cards unless each is a clickable unit, no card inside a card. Actions: at the bottom, right-aligned, confirm last; each card as tall as its content (equal heights only in a grid of cards with the same structure). Elevation: `hairline` border, shadow only if the whole container is clickable. |
| **Control** (button, field, switch, slider…) | Every state: default, hover, focus, pressed, disabled, and selected, loading, error where they apply. Focus: see States. Button sizes 44 / 36 / 32px, field height 40px (inline buttons: container height − 16), touch target 44px, targets `space-2` apart. Accessible name, keyboard use, ARIA roles on custom controls. Labeled buttons without icons; labels are a verb and an object. Form text 16px. |
| **Overlay** (menu, popover, dialog, sheet, tooltip) | Floating level: `surface-float` + `hairline`, no shadow; hover inside uses `surface-float-active`; corner actions and action rows placed by The Concentric Rule. Opens and closes with the motion tokens. Escape and click outside close it; focus moves in on open and returns to the trigger on close. Options: radius 8, 4px from the menu edge, padding 8, so text sits on the menu curve's centre. |
| **Feedback** (toast, error, empty state, loading) | Response times: 100ms, 300ms, 1s, 3s (Usability 1). Messages say what, why and how, next to their cause, without codes. Semantic colors keep their meaning and never work alone. Announced to screen readers (`aria-live`). Motion tokens, reduced motion respected. |
| **Screen or page** | Without reading, the eye knows where to look first (three-second check). One focal point per zone, one `primary` per view, one `h1`, three or four type levels. Scanning pattern: F for dense content, Z for sparse. Sections `space-12` apart, page margins `space-4` / `space-8`. Responsive: works from 320px, holds at 200% zoom, touch without hover. Color only where it means something. |

**If the element is clickable,** add the Control row to its own row (a clickable card is a Container plus a Control).

### Ask later, when it matters

Everything else starts from a default and is asked only when the work reaches it.

| Topic | Default until asked | Ask when |
|---|---|---|
| Themes | Light and dark, following the system preference; no theme switch in the UI | The user wants one theme only or asks for a theme switch, or a custom palette covers one theme only |
| Language and formats | The language the user writes in; dates, currencies and units of their locale | The first text, date, price or measure goes on screen |
| Identity | The active values in the frontmatter | The user asks to change colors or fonts: offer the options in Candidates, or apply their palette with the Custom palette method |

### Behaviour rules

- **Never invent values.** Every color, size, radius, space, shadow and duration comes from this file or from the Custom palette method. When something is missing, propose a value that follows the rules and wait for approval.
- **When no rule covers a choice,** apply *Calm Clarity*: pick the option that keeps the screen calmer and clearer.
- **Binding rules change only on an explicit request.** They are: the 8-point grid, contrast, The Hairline Rule, The Radius-Padding Rule, The Concentric Rule, The Distance Ratio Rule, shadows only on interactive elements, no icons on labeled buttons. When the user asks for something that breaks one:
  1. name the rule and the consequence (for example: "this text drops to 3.1:1, below the 4.5:1 minimum");
  2. offer the closest option that follows the rule;
  3. only if the user confirms, apply the exception where it was asked, leave a note in the project (a code comment or the project notes), and never extend it anywhere else on your own.
- **Accessibility weighs more.** Contrast minimums, visible focus, 44px touch targets and reduced motion can be broken only on an explicit request, after a clear warning that the change shuts people out. Never break them silently, by default, or to make something look better. The accessibility rules live in Color rules (contrast, focus, meaning), Spacing (touch targets, zoom), Motion (reduced motion), Icons (accessible labels) and Responsive (input, safe areas).

## Overview

Guiding principle: *Calm Clarity*. When a choice is not covered by a rule, pick the option that keeps the screen calmer and clearer.

Kore aims for a screen that feels quiet and reads at a glance. Its forms are round and friendly, laid on a strict 8-point grid. Surfaces are subdued, a cool off-white by day and a warm near-black by night. Space, a change of tone or a 1px border is enough to separate them, and only elements you can click carry a shadow. Color is used sparingly. One accent color marks the moment that matters and semantic colors mark state, while everything else stays neutral so the content comes first. Every screen has a single point of entry, and the interface answers every action, prevents errors and uses the words of the people who use it.

Key characteristics (values reflect the active tokens; update them when a project picks different candidates):

- Two themes designed with the same care, Ice (`#F8FAFB`) and Night (`#0C090A`), each built on its own instead of as the inverse of the other.
- Display roles in Outfit, everything else in Figtree, code and data in Geist Mono.
- A single accent color used rarely: `#904E55` in light, `#F8F1FF` in dark.
- Depth comes from surface steps and 1px borders. Only clickable elements have a shadow, and it is barely visible.
- Cards have 24px corners and controls 12px; content starts on the corner's centre and nested radii are concentric.
- Every space and size comes from a token on the 8-point grid.
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

- Check every pair against every surface it can sit on (`canvas`, `surface-card`, `surface-elevated`, `surface-deep`, `surface-float`), in both themes, including hover, pressed, error and disabled states.
- Translucent text tokens (`body`, `charcoal`, `on-light-mute`) change contrast with the surface below. Re-check them on every new surface; if one fails, use a solid color for that pair.
- A control that is recognised only by its outline (text input, select, checkbox) uses `hairline-strong`, which reaches 3:1 on every surface. `hairline` is for static containers only.

### Meaning

- **Never color alone.** Error, success, warning and info always carry a text label or an icon too, so they work for color-blind users and in grayscale.
- **Semantic roles stay fixed:** `danger` = error and destructive, `success` = success, `warning` = warning, `info` = information, `link` = links. Never swap them for decoration.
- **The accent is rare.** `accent` marks the primary moment of a screen (key data, emphasis). Scattered everywhere, it stops meaning anything. Never as a button or a surface, and never a second brand color alongside it.

**The One Primary Rule.** `primary` is spent on the main action of its decision and nothing else: at most one solid primary button per decision, never on decoration. A repeated, independent unit (a card in a product grid, a row in a list) is its own decision — each may have its own primary; the rule counts per decision, not per page.

### States

Every interactive element defines all its states: default, hover, focus, active/pressed, disabled, selected, loading, error. A component with half of them does not ship.

- **Focus, one style everywhere:** four corner marks drawn outside the control, one per corner, each following the control's radius. A mark is the curve of the corner only, at least 10px long (radius + 2px), 2px thick, in `focus-ring` (`mute`), 2px away from the edge and concentric with it. Filled and outlined controls take the same marks. They show on keyboard focus only, and they must reach 3:1 against the surface behind them, a photo or a colored surface included. Exceptions: links (text links and clickable rows) take no marks, and menu items and select options show the active item with `surface-float-active`. Apart from links, never remove focus without a replacement.
- **Selection:** selected items and selected text use `selection`.
- **Disabled:** foreground `stone`, no hover, cursor not-allowed; keep the element's size so the layout does not shift.

### Themes

- Light and dark are each designed, never produced by inverting the other. Check surface steps, borders and contrast separately in each. Pick the default from the use scene (who, where, what light), never by habit.
- **Glows** (`*-glow`) are atmosphere with a purpose: at most one per screen, anchored at the top of a section, and never on dense task screens (lists, forms, tables).

### Custom palette

A project may replace Kore's colors with its own. The user gives a few base colors; every other token is derived with fixed rules, so the result keeps Kore's contrast and surface steps without choosing each token by hand.

**Base colors, per theme:** `canvas`, `ink`, `primary`, `accent`. Optional: `danger`, `success`, `warning`, `info`; any missing one keeps Kore's value, so its meaning stays recognisable.

**Derived tokens.** L is OKLCH lightness (0–100). Neutral tokens take the hue of `canvas` with chroma at most 0.01.

| Token | Rule, light | Rule, dark | Check |
|---|---|---|---|
| `surface-card` | `canvas` L +1 | `canvas` L +4 | — |
| `surface-elevated` | `canvas` L −1 | `canvas` L +10 | — |
| `surface-deep` | `canvas` L +1 | `canvas` L −2 | — |
| `surface-float` | `canvas` L +1 | `canvas` L +8 | Floating layers must be lighter than `canvas` and `surface-card` in dark |
| `surface-float-active` | `canvas` L −1 | `surface-float` L +6 | — |
| `surface-hover` | `canvas` L −2 | `canvas` L +8 | — |
| `body`, `charcoal` | `ink` at 86% and 72% opacity | same | 4.5:1 |
| `mute` | From `ink` toward `canvas`, stopping at the last value that passes | same | 4.5:1 |
| `hairline-strong` | Solid, from `ink` toward `canvas`, stopping at the last value that passes | same | 3:1 |
| `stone` | Halfway between `canvas` and `mute` in L | same | exempt |
| `hairline` | `ink` at 6% opacity | `ink` at 4% opacity | none, meant to be barely visible |
| `primary-on` | White or black, whichever contrasts more with `primary` | same | 4.5:1 |
| `primary-pressed` | `primary` L +5 toward `canvas` | same | `primary-on` still 4.5:1 |
| `danger-on`, `danger-pressed` | As `primary-on` and `primary-pressed`, from `danger` | same | 4.5:1 |
| `link` | `info` | same | 4.5:1 |
| `focus-ring` | `mute` | same | 3:1 |
| `*-glow`, `selection` | The color at 20% opacity | The color at 18–34%, raised until visible on `canvas` | none |
| `on-light-mute` | Light `charcoal` | same as light | 4.5:1 on white |
| `scrim` | Kore's value | Kore's value | — |

**Method:**

1. Take the base colors from the project or from the user. If they cover one theme only, ask whether to derive the other theme or ship one theme.
2. Derive every token with the table. Kore's own values follow these rules within about 1 L point.
3. Check contrast on the worst surfaces: `surface-elevated` and, in dark, `surface-float-active`. A text or border that passes there passes on every surface. For `danger`, `success`, `warning` or `info` used as text, if one fails, move its L until it passes and keep its hue.
4. Show one table: token, value, contrast. Wait for the user's OK, then write the project's tokens.

**Contrast ratio** = (L1 + 0.05) / (L2 + 0.05), where L1 and L2 are the WCAG relative luminance of the lighter and the darker color. Composite translucent colors over the surface before measuring. Never round up: 4.49 fails 4.5.

## Typography rules

- **Roles, not sizes.** Use the scale tokens (`display-*`, `headline-*`, `title-*`, `body-*`, `label-*`, `code-md`); never a free font size.
- **Display font only for display.** The display family (the `display-*` roles) never appears in labels, buttons, navigation, form fields or data. Everything else uses the sans. Monospace is for code, data and tabular numbers, never a costume for "technical".
- **Form fields at 16px.** Text inside inputs, textareas and selects uses `body-lg` (16px) so mobile Safari does not zoom the page on focus.
- **Reading floor.** Running text is `body-md` (14px), the default for most app text. `body-lg` (16px) is for introductory paragraphs and primary reading text; `body-sm` (12px) for supporting notes, legal text and secondary descriptions in dense layouts.
- **Measure.** Paragraphs stay between 45 and 75 characters per line; cap text containers with a `ch` max-width.
- **Heading spacing.** More space above a heading than below it, so the heading belongs to the text it introduces.
- **Paragraph rhythm.** Separate paragraphs with space or with a first-line indent, never both.
- **Numbers.** Columns of numbers use tabular figures (`font-variant-numeric: tabular-nums`) so digits line up.
- **Dark theme compensation.** Light text on dark surfaces reads thinner: when a role looks weak in dark, add a touch of letter-spacing or one weight step for that role; never shrink contrast to compensate.
- **Fixed scale in apps.** Product screens use the fixed rem scale. Fluid sizes (clamp) are reserved for display type on marketing pages.
- **Font loading.** Load only the weights in use, with `font-display: swap` and a metric-compatible fallback, so text is never invisible and the layout does not jump.
- **Zoom and user settings.** Never block browser zoom, user font size, Dynamic Type or platform text scaling.
- **Line-height per script.** The scale's line-heights are set for Latin, Greek, Cyrillic and Hebrew. Arabic, Chinese, Japanese and Korean add 10% to the line-height; Devanagari, Thai and Khmer add up to 20%. Sizes do not change, and the result is not rounded to the grid.

### Roles and sizes

Five roles, each in three sizes (Large, Medium, Small). The role says what the text does; the size says how prominent it is. Values are dimension / line-height.

| Role | Large | Medium | Small |
|---|---|---|---|
| **Display** (`display-*`, Outfit). The largest text: short text or key figures, best on large screens. | `display-lg` 57 / 64. The main text or figure of top prominence on very large screens, or a single isolated visual (a temperature, a big score). | `display-md` 45 / 52. Expressive text or prominent figures on medium screens, or primary regions. | `display-sm` 36 / 44. The compact display: impact on small screens or narrow layouts without much vertical space. |
| **Headline**. Short, high-impact text that marks the primary passages or main regions. | `headline-lg` 32 / 40. The main title of a screen or view ("Profile", "Your orders"). | `headline-md` 28 / 36. Headings of important sections and high-priority dialogs (the title inside a dialog). | `headline-sm` 24 / 32. Headings of secondary content regions or less prominent sections on the same page. |
| **Title**. Smaller than Headline, medium emphasis: divides secondary passages or regions. | `title-lg` 22 / 28. Titles of cards and articles, primary app bar headings (a contact's name). | `title-md` 16 / 24. Main categories and section dividers ("Top News"). | `title-sm` 14 / 20. Subcategory headings, items of complex lists, compact sub-headers inside components. |
| **Body**. Long passages, line-height about 1.5×, simple highly legible font. | `body-lg` 16 / 24. Introductory paragraphs or primary reading text (the opening of an article). | `body-md` 14 / 20. The default for most app text: article paragraphs, option descriptions in settings. | `body-sm` 12 / 16. Supporting text, secondary notes, legal text and disclaimers, secondary descriptions in dense layouts. |
| **Label**. Small functional styles for components and micro-text. | `label-lg` 14 / 20. Action elements: the text inside buttons. | `label-md` 12 / 16. Navigation components: text under navigation bar icons, tabs. | `label-sm` 11 / 16. Micro-text and captions: timecodes, badges, small tags. |

`code-md` (13 / 20, Geist Mono) covers code; Material has no role for it.

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
| `space-12` | 48px | Section spacing | Space between page sections |

The primary scale is 4 / 8 / 16 / 24 / 32 / 48. The half-steps 12, 20 and 40 exist so they can be used as tokens, but only when the primary value next to them is visibly wrong. No other values.

### Rules (binding)

1. **The Token-Only Rule.** Every margin, padding, gap and offset (top, left, inset, translate) uses a `space-*` token. Never a free number, never an arbitrary value.
2. **No random values.** Never 10, 11, 13, 14, 19, 22, 23, 27, 31px. If a value is missing, round to the nearest token.
3. **Keep the scale small.** Never add a token for a single case. Repeat the existing ones.
4. **Uniform card padding.** The same value on all four sides and on every card of the same kind: `space-6` (24px) by default, `space-4` (16px) for compact cards.
5. **Everything that adds space follows the scale:** card padding, gaps between sections, text spacing, button sizes, layout margins, icon spacing.
6. **Element sizes are multiples of 8** (4 when needed): icons 16 / 20 / 24, avatars 24 / 32 / 40 / 48, controls 32 / 36 / 40 / 44, bars 56 / 64.
7. **The grid applies to containers, not to text.** Element sizes, padding and gaps follow the scale. Line-heights come from the type scale and the script factor (Typography), and need not be multiples of 4.
8. **Borders don't count.** A 1px border is not spacing: use border-box sizing and fixed heights so a border never forces off-grid padding (no `7px 15px` to compensate).
9. **Use relative units.** Implement tokens in `rem` (1rem = 16px) so spacing follows the user's text size and zoom.

### Proximity and hierarchy

Spacing tells the reader what belongs together.

- **Inside < between.** Space inside a group is always smaller than space between groups: label ↔ input `space-2`, field ↔ field `space-6`, section ↔ section `space-12`.
- **The Distance Ratio Rule (binding).** The space between two groups is at least twice the space inside each group. Below that ratio the eye reads them as one group. Examples: label ↔ input 8, field ↔ field 24; card rows 12, header ↔ rows 24, rows ↔ actions 32.
- **Alignment confirms the group.** Grouped elements share an axis (left edge, baseline or grid column); proximity without alignment looks accidental.
- **Density never collapses groups.** When content must be dense, keep the ratio and reduce the elements (fewer, smaller), never the ratio.
- **Space the siblings from the parent.** Put the gap on the container (flex or grid gap, stack spacing) instead of margins on each child, so gaps never collapse or double.
- **Grouping actions.** Related actions sit `space-2` apart; different groups at least `space-4`; a destructive action is always its own group. Rare actions go in a "More" menu, grouped by category with space or a label, destructive last.
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
| Button height | — | 44px |
| Input height | — | 40px |
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
| Compact cards | `lg` | 16px |
| Controls (buttons, inputs, selects), menus, popovers | `md` | 12px |
| Small buttons, items inside controls and menus, tooltips | `sm` | 8px |
| Anything nested inside another rounded shape | from The Concentric Rule | — |
| Pills, badges, avatars, status dots | `full` | 9999px |
| Full-width sections, page edges | `none` | 0 |

### Radius and padding (binding)

**The Radius-Padding Rule.** Content aligned to a side (text, icons, images, rows) starts at the centre of the corner curve: the horizontal padding equals the radius. If the padding is smaller than the radius, reduce the radius until they match. Centered content (a button label, a segment, the file drop area) never reaches the corners and is exempt.

| Element | Radius | Horizontal padding |
|---|---|---|
| Standard, media and clickable card | 24 | 24 |
| Compact card | 16 | 16 |
| Text input, select, textarea (48 and 40), popover | 12 | 12 |
| List row highlight | 12 | 12 |
| Menu option | 8 | 8 |

### Nested radius (binding)

**The Concentric Rule.** A rounded shape inside another shares the centre of its corner curve, so the two curves stay parallel:

```
inner radius = outer radius − distance between the two edges
```

The distance is the same on the sides and at the corner it faces. Combined with The Radius-Padding Rule, the inner shape sits halfway, and its own content lands exactly on the outer curve's centre, aligned with the rest of the container.

| Case | Outer | Distance | Inner |
|---|---|---|---|
| Option inside a menu | 12 | 4 | 8, text at 4 + 8 = 12 |
| Row highlight inside a standard card | 24 | 12 | 12, text at 12 + 12 = 24 |
| Buttons in an action row (36px, radius 12) in a card or dialog | 24 | 12 | 12 |
| Corner action (32px, radius 8) in a card, dialog or sheet | 24 | 16 | 8 |
| Inline button inside a 40px field, or a 48px stepper or segmented control | 12 | 8 | 4 |

- **Two kinds of nested shape.** The formula governs a shape anchored to the container's edge as its own functional unit: the cases in the table above, plus any button, menu item or control placed near a corner. An icon, avatar or badge that simply leads a padded block of content — not anchored to an edge on its own, just the first item in a stack — is not concentric: it keeps a constant radius from the `rounded` scale and sits at the container's own padding, exactly like the text beside it. (Apple's design system names these "concentric" and "fixed" shapes; a capsule, radius = half its height, is a third fixed case.)
- **Place a fixed-size element by its radius:** a button keeps its own size and radius, and its distance from the container's edge is outer radius − its radius.
- **Inline buttons** inside a control (the password toggle, stepper − and +, segments) sit 8px (`space-2`) from every edge, so the focus marks (States) never touch the container's border. Their radius is container radius − 8 (4px, `xs`, in a container with radius 12), and their size is container height − 16: in a 40px field, 24px buttons. They don't use the button sizes; their hit area extends to 44px. They have no background: the icon is 16px in `mute`, hover and pressed turn it `ink`, and the box shows only as the focus marks (States).
- **Corner actions** (a "More" or close button in the top-right corner of a card, dialog or sheet) are small icon buttons (32px, radius 8) placed with this rule: 24 − 8 = 16px from the top and the right. The header becomes a row that starts at the same 16px and is as tall as the button; the title is centred in that row, so it lines up with the button. The side padding stays 24.
- **No rounded blocks with a background inside cards** unless each one is its own unit (a clickable row); rows separate with space (see The Separation Ladder).
- **Never the same radius inside and outside.** Equal radii make the gap look thicker at the corners.
- **Deeper nesting** applies the rule again from the parent, not from the outermost container.

### Borders inside the edge

A border must not change the measurements the nested rule relies on. Draw the 1px `hairline` inside the element's edge without taking layout space (in CSS: `outline: 1px solid; outline-offset: -1px`, or an inset ring), so the gap between two nested edges is exactly the padding. Never a colored border thicker than 1px on one side of a card, list item, callout or alert to signal state — use a semantic color on an icon or text instead.

## Elevation

Depth tells the reader what sits on what. Static layers separate with a surface step and a 1px `hairline`; only interactive elements get a shadow. In dark, a layer that sits higher is lighter, never darker: without a shadow, the surface step is what separates it.

### Levels

| Level | Recipe | Use |
|---|---|---|
| 0 · flat | `canvas`, no border, no shadow | Page background, full-width sections |
| glow | one `*-glow` wash at the top of a section | Atmosphere; at most one per screen, never on dense task screens |
| 1 · surface | `surface-card` + `hairline` | Static cards and panels |
| 2 · inset | `surface-elevated` + `hairline` | Rows and icon wells inside a card; never a card inside a card |
| 3 · floating | `surface-float` + `hairline` | Popovers, menus; active items use `surface-float-active` |
| 4 · overlay | `surface-float` + `hairline` over a `scrim` | Dialogs and sheets |
| interactive | its surface + `shadow-rest`, `shadow-hover` on hover | Buttons and clickable cards only |

### Shadows

**The Hairline Rule.** Shadows only on interactive elements: things the user clicks or taps. Everything else, including containers of clickable items such as popovers, menus and sheets, uses a 1px `hairline` border and no shadow.

- **Barely perceptible.** `shadow-rest` is a hint that the element is clickable; `shadow-hover` suggests a lift, nothing more. Never stack several shadows or raise the opacity to make a point.
- A shadow always has a vertical offset and a soft blur. A zero-offset colored halo is decoration; a hard shadow with no blur (`4px 4px 0`) is a costume.
- Dark theme shadows are denser (black at 24–32%) because a light shadow disappears on a near-black canvas.
- No glass or blur as decoration.

### Interaction

- **Hover** on a clickable element: `shadow-rest` → `shadow-hover` and a lift of `space-1` (4px), with `duration-fast` and `ease-out`. **Pressed:** back to rest in `duration-instant`.
- **Reduced motion:** no lift; only the shadow changes, without animation.
- Touch devices have no hover: the pressed state carries the feedback.

### Stacking order

Layers use the fixed `zIndex` scale, never a free number: `base` 0, `raised` 10 (sticky headers, raised items), `dropdown` 100 (menus, popovers), `overlay` 200 (scrim), `modal` 300 (dialogs, sheets), `toast` 400 (notifications). Floating layers render outside clipping containers (popover API, dialog, portal) so they are never cut off.

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
- **Stay light.** Keep expensive effects (blur, filters, shaders) in small isolated areas, apply `will-change` only during the animation, and test on a mid-range phone. Verify against two measurable bars: 60fps or better while the animation runs (DevTools Performance panel), and zero layout shift caused by it (CLS 0, Lighthouse) — a failure on either means the animation is too heavy for its purpose, not just "feels off".

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

## Hierarchy

Hierarchy is the architecture of attention: it tells the eye what to look at first, what next, and what to ignore. A correct hierarchy lets a user understand a screen in under five seconds without reading a word.

### Visual weight

Six tools set how strongly an element pulls the eye. Use them on purpose, and mostly to take weight away from secondary elements.

| Tool | Rule |
|---|---|
| Size | The bigger element is read first. Headings are clearly larger than their subheadings; the primary button is larger than secondary actions; functional icons are larger than decorative ones. |
| Contrast | Primary text uses full contrast (`ink`); metadata steps down (`charcoal`, `mute`), always within the 4.5:1 minimum. |
| Color | One color family for primary actions. Saturated beats desaturated; color never carries meaning alone. |
| Shape | A shape that breaks the pattern stands out (a round badge on a square icon). Kore keeps one corner language, so shape contrast comes from form (pill, circle, dot), never from mixing corner styles. |
| Position | Top-left is read first in left-to-right layouts; an element surrounded by space weighs more than the same element in a crowd. |
| Density | A dense area weighs more but can confuse. Reduce density of secondary areas; an isolated element gains weight from the empty space around it. Never the same density everywhere. |

**The One Winner Rule.** Every screen, and every zone of a screen, has one focal point. It beats everything else on at least two of the six tools (for example: largest, full contrast, top-left). Three is overdesign. Two elements with similar weight compete and neither wins.

**Never invert the hierarchy:** metadata (date, author, category) never outweighs the title it belongs to.

### Three levels

- **Primary:** one element, the focal point. Caught first.
- **Secondary:** two or three elements that support it and add context.
- **Tertiary:** everything else; present, never distracting.

If the primary element cannot be named within three seconds of looking at the design, there is no focal point.

To isolate the focal point, surround it with space and place it on a third of the layout (the upper third, or the top-left crossing) rather than at the dead centre.

| Context | Focal point | Typical mistake |
|---|---|---|
| Landing page | Hero headline or main image | Three elements of similar size in the hero |
| Dashboard | The most important metric | A grid of identical cards with no leader, or a whole page of same-size icon + heading + text cards |
| Form | The first field to fill | Label and input with the same weight |
| Product or content card | Image or title | Price, title and badge at the same weight |
| Error page | The error message | A decorative illustration heavier than the message |
| Dialog | Title and primary action | Three equivalent buttons |

### Semantic weight

Before choosing how something looks (Visual weight), decide what it is: apply the same three roles as *Three levels* — Primary, Secondary, Tertiary — to a component, and again to everything nested inside it, and again to the group of components it belongs to.

1. **The reader's question.** At any level, ask: "if the user read only one element here, what would let them act or understand?" That element is Primary; the rest scales toward Secondary or Tertiary by how close it comes to answering the same question. Re-apply it at every level — the section holding several components, then each component, then each row, then each control — never assume the answer at one level carries to the next.
2. **One priority per repeating component.** For a component that repeats (cards in a grid, rows in a table), answer once: "what should the user perceive first across every instance?" That answer is the default for classifying every field in every instance, so the reasoning is not redone each time.
3. **State the default; never apply or flag it silently.** Building new content: apply the default and name it in one line ("gave the price more weight — it usually drives the decision here; say if the goal differs"). Reviewing existing content with an asymmetry (one card larger, one field bolder): don't assume it is a mistake — name it as an open question ("this card is bigger than its neighbors — is it the main offer, or should the row be even?"). Correct immediately once answered, and never ask the same question twice for the same component type.
4. **A weight the content doesn't earn is not fixed by adding a component.** If nothing in the request or the content confirms that one item outranks its peers, the default is equal weight, not an invented badge, tag or highlight to assert a priority no one confirmed (Behaviour rules, Never invent values). Ask, or wait until the priority is confirmed, before building the component that would express it.
5. Once roles are assigned, style them with *Text hierarchy*.

### Typographic levels

- **One `h1` per page;** it names the page.
- At most **three or four type levels** visible on one screen.
- Adjacent levels differ clearly in size and/or weight; if two roles look almost the same, drop one.
- Weight can compensate size: a medium `label-lg` (14px) can outrank a regular `body-lg` (16px).
- Bold only for key terms; if everything is bold, nothing is.
- No all caps on long text.
- No eyebrow or kicker label above a heading; the heading carries its own weight.

### Text hierarchy

Inside a component (a card, a popover, a dialog, a row), decide the order before the style.

1. **Order first.** Decide what the user needs now, the action that comes next, and the context that changes the decision. Say each idea once: if the title already says it, the text below adds something new or disappears.
2. **Emphasize by de-emphasizing.** The primary element stays `ink`; everything else steps down. Take weight away from the secondary text instead of making the primary louder.
3. **Labels are a last resort.** Drop a label when the format already says what the value is (a price, a date, an email). Merge label and value when possible ("148 g a day", "12 left in stock", not "Stock: 12"). When a label must stay, it is the quieter half: `body-md` in `mute`, with the value in `ink`. Emphasize the label instead only on dense reference pages where people scan for it (a spec sheet). Form fields always keep their visible labels.
4. **Limits.** At most three sizes and three levels in one component. Weights: 400 for text and titles, 500 for labels and buttons; never below 400. Text colors: `ink`, `body`, `mute`, and nothing else for plain text. No gradient text: emphasis comes from weight or size, never decoration.
5. **Numbers.** The number carries the emphasis; its unit is smaller and in `mute` ("148 g *a day*").
6. **Balance weight and contrast.** Heavy shapes (filled icons, large glyphs) take a softer color (`mute`); thin text keeps `ink`.
7. **Warnings are never quiet.** A consequence the user must not miss ("This can't be undone.") sits on its own line, in weight 500 and its semantic color, never in `mute`. The words carry the meaning, so no icon is needed; add one only when the text alone does not say it is a warning.
8. **Semantics follow hierarchy.** A destructive action in a list or menu is tertiary or secondary, with red limited to its icon; it becomes a filled `destructive` button only when it is the main action of the moment, as in the confirmation.
9. **No grey text on colored surfaces.** On a tinted or colored background, secondary text takes a tint of that color, not `mute`.
10. **Inline emphasis.** In a sentence, the words the user must check stand out in weight 500 and `ink`: figures with their unit (a quantity, a price, a date) and the name of the object an action affects ("**Next week's plan** and its **21 meals** will be removed."). At most two per sentence, never color, never whole phrases. It applies to explanations and messages (errors, confirmations); captions, subtitles and help text stay plain. It works because weight is noticed before reading (pre-attentive processing) and a lone different item stands out (the isolation effect).

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

**The Working Memory Rule.** A user holds at most four options, actions or facts in mind at once (Miller's Law, revised by Cowan 2001) — past that, they skip, misclick or give up instead of weighing all of them. Up to four in one group: no change needed. Five or more: group them into categories, or move the extra ones behind a "More" menu (Spacing, Grouping actions) rather than listing everything flat.

### Scanning patterns

- **F pattern** (dense content: feeds, tables, search results, dashboards): the left column and the first two lines of each block are always read. Put titles, status and key actions on the left; the first column of a table carries the most important data.
- **Z pattern** (sparse content: landing pages, cards, simple forms): brand top-left, primary action top-right, key message at the centre-left turn of the Z, final action bottom-right.
- **Action order.** Actions are right-aligned; the confirming action is last on the right, and cancel or back sits immediately to its left. The same in cards, dialogs and multi-step flows.
- A perfectly symmetric layout follows no pattern and guides nothing: break symmetry on purpose for the focal point (wider, taller, isolated).
- Critical information never lives only at the bottom right of an F layout.
- Number sections (01 / 02 / 03) only when the order itself is information the reader needs.

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
- Prefer layouts that reflow on their own (flex wrap, auto-fit grids) and container queries for a component used at different widths (a card in a sidebar and in a full-width page), so it adapts to its own box instead of the viewport.

### Typography

- Below `sm`, display roles step down one level: `display-lg` 57 → 45, `display-md` 45 → 36. Line-height steps with the role (64 → 52, 52 → 44).
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

## Browser surfaces

The parts the browser draws still carry the design. Theme them from the palette instead of shipping browser defaults:

- **Text selection:** `selection` background, `ink` text.
- **Caret:** `ink` (or `accent` in inputs that deserve emphasis).
- **Focus:** see States.
- **Scrollbars:** thin, `hairline-strong` thumb on a transparent track, where the platform allows it.
- **Links:** `link` color, underline with a 4px offset, thickness 1px.
- **Numerals:** tabular figures in tables and data.

## Icons

**Library first.** If the project already uses an icon library, keep it and apply the rules below. Otherwise use Kore's default.

**Default: Hugeicons**, always the free set (the paid Pro set only when the user asks for it and holds the license), *Stroke Rounded* style (MIT license). Its round stroke ends match Kore's round type and corners, and it has official packages for every major stack: React, Vue, Angular, Svelte, SolidJS, React Native and Flutter, plus plain SVG for anything else.

### Rules

- **One library per project**, one style, one stroke width (1.5 on a 24px grid). Never mix libraries or filled and outlined styles.
- **Sizes from the grid:** 16px inside controls and menus and next to 12–16px text (menu items, inline buttons, steppers, field adornments), 20px in icon-only buttons, 24px for navigation and standalone icons.
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

## Components

**The Library-First Rule.** Before building any component, check whether the project already uses a UI library (for example shadcn/ui, Radix, MUI, Headless UI, a native component kit). Look at the dependencies and the existing components; if it is not clear, ask the project owner before writing anything.

- **A library is in use:** never rewrite its components. Keep the library and adapt it to Kore: map Kore's tokens (colors, typography, rounded, spacing, shadows, motion) onto the library's theme, and override a component's styles only where the library's defaults break a Kore rule. Library sizes and behaviours that break no binding rule stay as they are: a 40px library button stays 40px, because 40 is on the grid. Typical overrides: shadows on menus, selects, popovers, dialogs and static cards (replaced by a `hairline` border), contrast, focus visibility, off-grid values, animations under reduced motion. Use the library's theming API (theme variables, token overrides) rather than rewriting its internal CSS. If the project uses the library's icon set, keep it; labeled buttons still carry no icon.
- **No library:** use the Kore components defined below, built on Kore's tokens and following every rule in this file.

### Button

Five variants, three sizes, one shape, plus the floating action button. Every button has all its states.

| Variant | Background | Text | Border | Shadow | Hover | Pressed | Use |
|---|---|---|---|---|---|---|---|
| primary | `primary` | `primary-on` | none | `shadow-rest` | `shadow-hover` + 4px lift | `primary-pressed` | The main action of its decision (The One Primary Rule) |
| destructive | `danger` | `danger-on` | none | `shadow-rest` | `shadow-hover` + 4px lift | `danger-pressed` | Delete and other destructive actions, at most one per decision |
| elevated | `surface-card` | `ink` | none | `shadow-rest` | `shadow-hover` + 4px lift | `surface-elevated` | Instead of secondary when the background is complex, colored or an image, where a transparent button would lose emphasis |
| secondary | transparent | `ink` | 1px `hairline-strong` | none | `surface-hover` background | `surface-elevated` | The standard supporting action next to a primary or a destructive ("Back", "View details"); never alone |
| tertiary | transparent | `ink` | none | none | `surface-hover` background | `surface-elevated` | Low-priority actions and secondary options ("Learn more"); the cancel action in a dialog; as many as needed |

| Size | Height | Horizontal padding | Vertical padding | Radius | Type |
|---|---|---|---|---|---|
| default | 44px | `space-6` (24px) | `space-3` (12px) | `md` (12px) | `label-lg` |
| compact | 36px | `space-4` (16px) | `space-2` (8px) | `md` (12px) | `label-lg` |
| small | 32px | `space-3` (12px) | `space-2` (8px) | `sm` (8px) | `label-lg`, hit area extended to 44px |

- **Icon buttons** are square in the same three sizes and always carry an accessible label and a tooltip.
- **No icons on labeled buttons.** A button with a label shows only text. The one exception is the loading spinner, placed before the label with `space-2` (8px).
- **Focus:** see States.
- **Disabled:** `surface-elevated` background, `stone` text, no shadow, not-allowed cursor; secondary keeps a `hairline` border. Explain why it is disabled when it is not obvious.
- **Loading:** a spinner plus the running action ("Saving…"); the button keeps its width and ignores further clicks.
- **Timing:** press in `duration-instant`; shadow and lift in `duration-fast` with `ease-out`; no lift under reduced motion or on touch.
- **Shadows** only on filled buttons (primary, destructive) and on elevated; secondary and tertiary show hover with a background change.
- **Destructive in dark** uses black text: white on `#ef4444` is only 3.76:1, black is 5.58:1.
- **Borders** are drawn inside the edge (inset ring), so they never change the button's size.
- **Labels** are a verb and an object ("Save meal", "Delete workout"), never "OK", "Yes" or "Submit". They use sentence case ("Create account"), never all caps.
- **Floating action button (FAB):** an icon-only button for the app's most frequent action, floating over the content; one per screen. 44px square, radius `md` (12px), 20px icon with 12px around it (equal to the radius), `primary` background, `primary-on` icon; states and shadows as primary. Placed bottom right, `space-4` from the edges on phones and `space-6` from `md` up. It carries an accessible label and a tooltip like any icon button.

### Form fields

Text input, textarea and select share one look.

| Part | Spec |
|---|---|
| Field | Height 40px; padding `space-3` (12px), equal to the radius; radius `md` (12px); background `surface-deep`; 1px `hairline-strong` border drawn inside |
| Text | `body-lg` (16px) in `ink`; placeholder in `mute`, only as an example, never as the label |
| Label | `label-lg` in `ink`, above the field, `space-2` (8px) away; "(optional)" in `mute` when the field is optional |
| Help text | `body-md` in `mute`, below the field, `space-1` (4px) away |
| Error | Red `danger` border plus a message in `danger`, linked to the field (`aria-invalid`, `aria-describedby`); an icon only when the message alone would not read as an error (Text hierarchy #7) |

- **States:** hover turns the border `mute`; focus follows States (an error keeps its `danger` border); disabled uses `surface-elevated`, `stone` text and a `hairline` border; read-only uses `surface-elevated` with no border and stays selectable.
- **Adornments:** a 20px icon on the left (search) at 12px, with the text starting at 40px; a unit on the right ("kg", "g") in `mute`, 12px from the edge.
- **Textarea:** minimum height 96px, resizable vertically only.
- **Validation** runs when the user leaves the field, and the error disappears as soon as the value is valid.

### Select

A custom menu, never the browser's native dropdown.

- **Trigger:** looks like a text field, with the Hugeicons down arrow on the right that rotates when open. Placeholder in `mute` until a value is chosen.
- **Menu:** `surface-float`, 1px `hairline`, radius `md` (12px), padding `space-1` (4px), opening under the trigger at `space-2`. Opens in `duration-base` with `ease-out`, closes in `duration-fast` with `ease-in`; no border shadow (see The Hairline Rule).
- **Options:** 44px tall, `space-1` (4px) apart so two highlights never touch, 4px from the menu edge, radius `sm` (12 − 4 = 8) and horizontal padding 8, so the text sits 12px from the menu edge; `body-md`; the active option has `surface-float-active`; the selected one is medium weight with a check icon on the right.
- **Keyboard and screen readers:** arrows move, Enter or Space selects, Escape and click outside close; focus returns to the trigger. Uses `listbox` / `option` roles and `aria-activedescendant`.

### Checkbox and radio

- **Checkbox:** 20px, radius `xs` (4px), `surface-deep` with a `hairline-strong` border. Checked: `primary` fill with a `primary-on` check icon. Indeterminate: `primary` fill with a minus icon.
- **Radio:** 20px circle; checked: `primary` fill with an 8px `primary-on` dot.
- **Rows:** the whole row (control + label) is clickable and at least 44px tall; label in `body-md`, `space-3` (12px) from the control.
- **Groups** sit in a `fieldset` with a `legend` as the group label.
- **Disabled:** `surface-elevated` with a `hairline` border and `stone` label; a checked disabled control uses a `stone` fill.
- **Focus:** see States.

### Switch

- 40 × 24px track, 16px knob, padding `space-1` (4px); hit area extended to 44px with an invisible overlay.
- **Off:** `surface-elevated` track with a `hairline-strong` border, `ink` knob. **On:** `primary` track, `primary-on` knob. Never green: green means success.
- The knob moves with `spring` (or `duration-fast` with `ease-out`); under reduced motion it changes without sliding.
- A switch always sits next to its visible label and applies the change immediately; use a checkbox when the change waits for a Save.

### Segmented control

- **Container:** 48px tall, radius `md` (12px), padding `space-2` (8px), `surface-elevated` with a `hairline` border. It hugs its segments, never stretches to full width.
- **Segments:** inline buttons, 32px tall, radius `xs` (12 − 8 = 4), padding `space-4` (16px), `space-2` apart, hit area 44px; `label-md`, `mute` text. Selected: `surface-card` with a `hairline` border and `ink` text.
- For two to four short, mutually exclusive options that switch a view (The Working Memory Rule); for more options, use a select.

### Password

- A text field with a show/hide toggle: an inline button (24px, radius 12 − 8 = 4, 8px from every edge; the text stops 40px from the right edge). Hover `surface-hover`; focus follows States. The icon switches between view and view-off; the accessible label and tooltip say "Show password" or "Hide password", with `aria-pressed`.
- Requirements sit under the field, `space-1` apart, in `body-md`, and update while the user types: unmet is a 16px empty circle and `mute` text; met is a 16px check circle in `success` and `ink` text. The icon changes shape, so the state never depends on color alone. The list is linked with `aria-describedby` and announced with `aria-live="polite"`.

### Combobox

- A text field with the search icon on the left and the select menu below (`listbox`, `surface-float`). It filters while the user types; the matching part of each option is weight 500.
- Empty field: show recent items under a `body-sm` label ("Recent"). No match: one line in `mute` saying what to do ("No foods match “rize”. Check the spelling or add it as a new food.").
- Keyboard: arrows move, Enter picks, Escape closes. Roles `combobox` and `listbox`, `aria-expanded`, `aria-activedescendant`, `aria-autocomplete="list"`.

### Number stepper

- 160 × 48px, padding `space-2` (8px), radius `md`, `surface-deep` with a `hairline-strong` border; − and + are inline buttons, 32px with radius 12 − 8 = 4, hit area extended to 44px. The value is centred, with tabular figures.
- Show the unit in the label and the limits in the help text before use ("Steps of 10 g, from 0 to 1,000 g"). − is disabled at the minimum and + at the maximum. Typed values snap to the step and the limits.
- Focus follows States, on the value or on a button. Role `spinbutton` with `aria-valuemin`, `aria-valuemax`, `aria-valuenow`; Arrow Up and Down change the value.

### Slider

- A 4px track: `hairline-strong` for the empty part, `primary` for the filled part. A 20px `primary` thumb with `shadow-rest` (`shadow-hover` on hover, `primary-pressed` while dragging), since it is dragged. The hit area is 44px tall.
- The label sits on the left and the current value on the right, in `label-lg` with tabular figures. A range uses two thumbs that never cross, with the fill between them.
- Focus: see States, around the thumb. Disabled: `surface-elevated` track and `stone` thumb, no shadow.
- Use a slider only when an approximate value is fine; for an exact value use the number stepper. Give each thumb a readable value (`aria-valuetext`, for example "€14").

### Menu

- **Surface:** `surface-float`, 1px `hairline`, no shadow, radius `md` (12px), padding `space-1` (4px), at least 224px wide, opening `space-2` below its trigger with its start edge aligned to the trigger's start edge (left in left-to-right languages); it flips to the end edge or above only when there is no room.
- **Items:** 44px tall, radius `sm` (8px), padding 8, so the text sits 12px from the menu edge, in `body-md`; optional 16px icon in `mute`, `space-2` from the label. Show a keyboard shortcut on the right (`body-sm`, `charcoal`) only when the product really has it. Active and hover: `surface-float-active`.
- **Spacing:** items `space-1` (4px) apart, so two highlights never touch; groups `space-2` (8px) apart (The Distance Ratio Rule).
- **Groups** by category, optionally with a `body-sm` label in `mute`. A destructive item comes last, alone, with a red icon and `ink` text (red text fails contrast on the active surface in dark).
- **Keyboard:** Enter, Space or ↓ opens and focuses the first item; ↑ ↓ Home End move; Escape closes and returns focus to the trigger; Tab closes. Roles `menu` and `menuitem`, `aria-haspopup`, `aria-expanded`.

### Popover

- `surface-float`, 1px `hairline`, radius `md` = padding `space-3` (12px), at most 288px wide, `space-2` from its trigger. Content follows Text hierarchy (label, value, explanation).
- No buttons in its corners: a small action is a link. Focus moves in on open; Escape or a click outside closes it and returns focus. Role `dialog` with a label.

### Dialog

- A modal over a `scrim`: `surface-float`, 1px `hairline`, radius `xl` = padding `space-6` (24px), at most 480px wide, 16px from the screen edges on phones.
- **Header:** title in `headline-md`, a statement that names the action with a verb and an object ("Delete this plan"), never a question; the close button is a corner action (Shapes), with the title centred on it. **Body:** the object and figures in inline emphasis ("**Next week's plan** and its **21 meals** will be removed."). A consequence that cannot be undone sits on its own line in `danger`, weight 500, `space-1` below the body: body and consequence are one message, centred between title and actions with `space-6` above and below it.
- **Actions:** `space-6` below the message, compact buttons 24 − 12 = 12px from the edges, right-aligned, confirm last, the cancel action tertiary; the buttons name the action ("Keep plan", "Delete plan"), never "Yes", "No", "OK" or "Submit". Initial focus goes to the safer action.
- Use a dialog only when the action cannot be undone or truly needs interruption and protected focus; otherwise act and offer "Undo" (Usability 3) or use an inline or progressive alternative. Focus stays inside; Escape, the close button and a click on the scrim close it; focus returns to the trigger. Use the platform's modal element where it exists (`<dialog>` on the web).
- Opens with a fade and a 0.98 → 1 scale in `duration-base` `ease-out`; only the fade under reduced motion.

### Sheet

- **Phones (below `md`):** from the bottom edge, full width, top corners `xl`, padding `space-6` plus the bottom safe area, at most 85% of the screen height.
- **From `md`:** from the right, 400px wide, `space-2` (8px) from the screen edges, all corners `xl`, full height minus 16px.
- Header with a corner close button, content, and actions at the bottom (right-aligned, confirm last). Same modal behaviour as the dialog; slides in with `duration-base` `ease-out`, fade only under reduced motion.

### Tooltip

- The one inverted overlay: `ink` background with `canvas` text, so it separates from anything below it without a shadow. `body-sm`, radius `sm` = padding 8 (4 × 8), `space-2` from its trigger, at most 240px wide.
- Appears after `duration-slow` (400ms) of hover and immediately on keyboard focus; Escape hides it. Plain text only, never links or buttons. Linked with `aria-describedby`, role `tooltip`. Every icon-only button has one.

### Overlay rules

- **Hover on floating surfaces:** tertiary and secondary buttons inside a menu, popover, dialog or sheet use `surface-float-active` for hover and pressed, because `surface-hover` equals `surface-float` in dark.
- On `surface-float-active`, secondary text uses `charcoal` (not `mute`) and links don't appear; in dark, `mute`, `link` and `hairline-strong` fall below their minimum there.

### Cards

| Card | Padding | Inside | Shadow |
|---|---|---|---|
| Standard | `space-6` (24px), radius 24 | Rows separated by space only (`space-3`, 12px) | none |
| Compact | `space-4` (16px), radius 16 | Rows separated by space only (`space-2`, 8px) | none |
| Media | image full-bleed at the top (16:9, clipped by the card radius, with `alt` text), then `space-6` padding | Title, subtitle, a detail line with 16px icons `space-2` from their text | none (or clickable) |
| With actions | `space-6` (24px) | Content, then the action row `space-8` (32px) below it | none |
| Clickable | `space-6` (24px) | Title, subtitle and a Hugeicons arrow on the right | `shadow-rest`, `shadow-hover` + 4px lift on hover |

- **Shape and surface:** `surface-card`, 1px `hairline` drawn inside, radius `xl` (24px), the same padding on all four sides.
- **Header:** title in `title-lg`, subtitle in `body-md` `mute`, `space-1` (4px) apart; `space-6` (24px) between the header and the content (`space-4` in compact cards).
- **Actions:** at the bottom of the card, right-aligned, confirm last with cancel or back to its left (Action order in Hierarchy); compact buttons (36px, radius 12) placed 24 − 12 = 12px from the card's bottom and right edges (The Concentric Rule), `space-2` apart. At most one `primary` per card (The One Primary Rule): a repeated card keeps its own primary when it has a clear main action (a product's "Buy"); use secondary and tertiary instead when the card's actions are all lower-emphasis, with none of them the point of the card. A card with actions is at least 320px wide; if the buttons still don't fit, they stack full-width with the confirming action at the bottom, never in a staircase. It has no shadow, since it is not clickable as a whole.
- **Header action:** an optional "More" button placed as a corner action (Shapes): 32px, radius 8, 16px from the corner, with the title centred on it; accessible label ("More options for Leg day") and tooltip.
- **Height:** each card is as tall as its content. Cards in a row share one height only in a grid of cards with the same structure.
- **Key figure:** when a card exists to show one number, the number is its focal point: `display-sm` in `accent`, with its unit and context in `body-md` `mute` on the same baseline.
- **Clickable card:** the whole card is one link or button. It fills the full width of its container, with the arrow anchored to the right edge. Focus follows States; pressed returns to rest. It never contains other buttons or links.
- **Spacing between cards:** `space-8` (32px); on phones `space-4` to `space-6`.
- **Never nest cards.** Inner content uses rows separated by space; a rounded block with a background appears only when each item is its own unit (a clickable row).

### List rows

- **Row:** at least 56px tall, padding `space-2` × `space-3`; leading element, text and trailing element separated by `space-4` (16px).
- **Leading:** a 40px circle in `surface-elevated` with a 20px icon, or an avatar.
- **Text:** title in `title-sm` `ink`; secondary line in `body-md` `mute`, one line, truncated with an ellipsis.
- **Trailing:** a value in `body-md` `mute` with tabular figures, and/or the Hugeicons arrow when the row opens something.
- **Clickable rows** are links: hover gives the `surface-hover` background, pressed `surface-elevated`, and no focus marks (States). The highlight extends `space-3` (12px) beyond the text, with radius 24 − 12 = 12 inside a standard card (The Concentric Rule), so the text stays on the card curve's centre.
- **Static rows** do not react to hover.
- Rows separate with space only, never with a divider on every row. Rows in a list are `space-2` (8px) apart, so two highlights never touch.

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
| `#868a8e` |  |
| `#7f8387` |  |
| `#767a7e` |  |

### hairline-strong — dark

| Value | |
|---|---|
| `#6e6a6a` | active |
| `#726e6e` |  |
| `#777373` |  |
| `#7d7979` |  |

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

### on-light-mute — light & dark

| Value | |
|---|---|
| `rgba(42, 42, 42, 0.72)` | active |
| `#6a6e72` |  |

### primary — light

| Hex | |
|---|---|
| `#212121` | active |
| `#000000` |  |
| `#1a1a1a` |  |
| `#2a2a2a` |  |

### primary — dark

| Hex | |
|---|---|
| `#fcfdff` | active |
| `#ffffff` |  |
| `#f5f3f3` |  |
| `#ebecee` |  |

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

### accent — light

| Hex | |
|---|---|
| `#904E55` | active |
| `#EB5E28` |  |
| `#F8F1FF` |  |

### accent — dark

| Hex | |
|---|---|
| `#F8F1FF` | active |
| `#EB5E28` |  |
| `#904E55` |  |

### warning — light

| Hex | |
|---|---|
| `#92400e` | active |
| `#b45309` |  |
| `#a16207` |  |
| `#d97706` |  |

### warning — dark

| Hex | |
|---|---|
| `#ffc53d` | active |
| `#facc15` |  |
| `#fbbf24` |  |
| `#f5b83d` |  |
| `#ffd166` |  |

### info — light

| Hex | |
|---|---|
| `#386580` | active |
| `#457B9D` |  |
| `#788AA3` |  |
| `#44799b` |  |
| `#407191` |  |

### info — dark

| Hex | |
|---|---|
| `#5b94b7` | active |
| `#457B9D` |  |
| `#788AA3` |  |
| `#477ea1` |  |
| `#4b86ab` |  |

### success — light

| Hex | |
|---|---|
| `#047857` | active |
| `#15803d` |  |
| `#2f855a` |  |
| `#3a7d44` |  |

### success — dark

| Hex | |
|---|---|
| `#6ee7b7` | active |
| `#4ade80` |  |
| `#34d399` |  |
| `#86efac` |  |

### danger — light

| Hex | |
|---|---|
| `#c53030` | active |
| `#b91c1c` |  |
| `#be123c` |  |
| `#9b2c2c` |  |

### danger — dark

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

### rounded — set

| Set | |
|---|---|
| Kore — cards 24 · compact cards 16 · controls 12 · inner items 8 | active |
| B · Round — controls 16 · inner blocks 16 · cards 24 |  |
| Current — controls 8 · inner blocks 8 · cards 12 |  |
| A · Soft — controls 12 · inner blocks 12 · cards 16 |  |
| C · Pill — controls full · inner blocks 16 · cards 24 |  |
