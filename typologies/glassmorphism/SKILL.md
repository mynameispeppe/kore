# Glassmorphism

## Definition

Glassmorphism builds depth from translucent layers: panels of frosted glass float above a vivid background and blur it.

Four traits define it: translucent panels that blur what lies behind them, several layers floating above the page, vivid colors behind the glass that make the blur visible, a thin light border on every glass panel.

## Where to use

- **Fits:** a page where a few surfaces float above the content (Glass).

## Replaces

### Material

- **Glass:** Replaces: `elevation.glass`. Glass covers the Top bar and its navigation panel, Menu, Popover, Dialog, Sheet, Command palette, the Cookie banner's box, Cards and the Accordion's items. These keep their default solid recipe: the Top bar's menus; a surface that holds a Table, a chart (Charts), a Figure, Form fields or the body of an article; the plan cards of Pricing. Glass surfaces keep space between them. The Top bar, its navigation panel and the Sheet reach the screen's edge; cards sit in the page with space around them. Glass that a component's file prescribes, such as the Hero's veil, stays as written.
- **Glass recipe:** background `glass-background`; backdrop-filter `glass-backdrop`; box-shadow `glass-shadow`. A glass surface over the page takes this one recipe, in each theme; a glass surface inside another takes Glass inside glass.
- **Glass inside glass:** A glass surface that lies inside another glass surface, such as the Accordion in a card or a menu in a dialog, takes the inner glass: background `glass-inner-background`; backdrop-filter none; box-shadow `glass-inner-shadow`. The outer surface keeps the Glass recipe. Text on the inner glass keeps the tokens of Text on glass, since the inner glass only adds the theme's tint.
- **Text on glass:** `glass-background` keeps its value; the text moves. Each token that fails its minimum (Contrast) on the glass moves its tone away from the glass, as in Custom palette step 3, until it passes on the worst point behind the glass. The points behind the glass are `canvas` and the five stops of Page background, each after the saturate() of `glass-backdrop`. The moved value replaces the token on the whole page. `typologies/glassmorphism/references/tokens.yaml` holds the result for Kore's palette; a Custom palette computes its own with `kore_palette.py --typology glassmorphism`.
- **Depth:** Replaces: `elevation.depth`. Glass layers separate from what lies behind them by blur and the edge of `glass-shadow`. Solid layers separate with a surface step and a 1px `hairline`; only interactive solid elements cast a shadow, and the inset bevel of `gradient-raised` and `shadow-raised-sm` counts as part of the surface. In dark, a solid layer that sits higher is lighter.
- **Page background:** Replaces: `elevation.0-flat`. `glass-gradient`, fixed to the window behind every layer, painted as the background of `html`: background `glass-gradient` fixed. In light it runs from the dark theme's `primary` to its `accent`, in dark from the light theme's, in CIE LCH, 5 stops. Full-width sections are transparent, so the gradient shows through; a section with a photo shows its photo.
- **Glow level:** Replaces: `elevation.glow`. The gradient of Page background is the only color behind the layers; it takes the place of every `*-glow` wash.
- **1 · surface:** Replaces: `elevation.1-surface`. Static cards and panels on glass: Glass recipe. Solid ones keep `surface-card` + `hairline`.
- **3 · floating:** Replaces: `elevation.3-floating`. Popovers and menus on glass: Glass recipe; active items use `surface-float-active`. Solid ones keep `surface-float` + `hairline`.
- **4 · overlay:** Replaces: `elevation.4-overlay`. Dialogs and sheets on glass, over a `scrim`: Glass recipe. Solid ones keep `surface-float` + `hairline`.
- **Interactive level:** Replaces: `elevation.interactive`. Buttons and solid clickable cards as the default. A clickable glass card: as Hover.
- **The Hairline Rule:** Replaces: `elevation.the-hairline-rule`. Glass surfaces take `glass-shadow`, clickable or not. On solid surfaces only interactive elements cast a shadow; every other solid element, containers of clickable items included, uses only a 1px `hairline` border.
- **Identity:** Replaces: `identity.identity`. The Hairline Rule of this typology (The Hairline Rule), The Radius-Padding Rule, The Concentric Rule.
- **Barely perceptible:** Replaces: `elevation.barely-perceptible`. On solid surfaces, `shadow-rest` hints that an element is clickable and `shadow-hover` suggests a lift; the only stacked solid shadows are the `shadow-raised` tokens, on filled and elevated Buttons (Button). `glass-shadow` draws the glass edge: a white line along the top, a 1px white ring and, in light, a soft drop shadow in black.

### Color

- **The One Primary Rule:** Replaces: `color.the-one-primary-rule`. The default rule (The One Primary Rule), and `primary` also colors the gradient of Page background.
- **The accent is rare:** Replaces: `color.the-accent-is-rare`. The default rule (The accent is rare), and `accent` also colors the gradient of Page background, outside the count of the page's 4 elements in `accent`. Text on glass takes any text token other than `accent`.
- **Glows:** Replaces: `color.glows`. As Glow level.

### Interaction and motion

- **Hover:** Replaces: `elevation.hover`. A clickable glass card keeps `glass-shadow` and lifts by `space-1`, with `duration-fast` and `ease-out`. Other clickable elements: `shadow-rest` → `shadow-hover`, `shadow-raised` → `shadow-raised-hover` on filled and elevated Buttons, and the same lift. **Pressed:** back to rest in `duration-instant`.
- **Stay light:** Replaces: `motion.stay-light`. Blur is the material of every glass surface (Glass), the large ones included: the Top bar, sheets and dialogs. Keep the other expensive effects, filters and shaders, in small isolated areas, apply `will-change` only during the animation, and test on a mid-range phone. Verify against two measurable bars: 60fps or better while the animation runs (DevTools Performance panel), and zero layout shift caused by it (CLS 0, Lighthouse). A failure on either means the effect is too heavy for its purpose.

### Dark theme and fallback

- **Dark theme shadows:** Replaces: `elevation.dark-theme-shadows`. Solid surfaces: denser, black at 24–32%. `glass-shadow` keeps the value of its token.
- **Without glass:** with `prefers-reduced-transparency: reduce`, or where `backdrop-filter` is not supported, every glass surface takes its default solid recipe.

**Composition:** material only: no source gives a rule on composition, so grid, type and spacing stay the default.

## Files

- `typologies/glassmorphism/references/tokens.yaml`: the keys of `references/tokens.yaml` glassmorphism replaces, and its new keys.
- `typologies/glassmorphism/references/components/`: one file per component whose material glassmorphism replaces, named as in `references/components/`.
