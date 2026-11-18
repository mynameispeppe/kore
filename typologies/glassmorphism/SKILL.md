# Glassmorphism

## Definition

Glassmorphism builds depth from translucent layers: panels of frosted glass float above a vivid background and blur it.

Four traits define it: translucent panels that blur what lies behind them, several layers floating above the page, vivid colors behind the glass that make the blur visible, a thin light border on every glass panel.

## Where to use

- **Fits:** a page where a few surfaces float above the content (Glass).

## Replaces

### Material

- **Glass:** Replaces: `elevation.glass`. Glass covers the Top bar and its navigation panel, Menu, Popover, Dialog, Sheet, Command palette, the Cookie banner's box and Cards. These keep their default solid recipe: a surface opened from inside a glass surface, such as a menu in a dialog, a popover in a card or the Top bar's menus; a surface that holds a Table, a chart (Charts), a Figure, Form fields or the body of an article; the plan cards of Pricing. Glass surfaces keep space between them. The Top bar, its navigation panel and the Sheet reach the screen's edge; cards sit in the page with space around them. Glass that a component's file prescribes, such as the Hero's veil, stays as written.
- **Glass recipe:** background `glass-fill`, or `glass-fill-strong` where a photo or page text can lie behind the glass; backdrop-filter blur(the surface's blur) saturate(`glass-saturate`); outline `line-thin` solid `glass-border`; outline-offset −`line-thin`; box-shadow of the surface. 1 · surface, 3 · floating, 4 · overlay and the Top bar's file give each surface its blur and its shadow.
- **Glass fill:** `glass-fill` and `glass-fill-strong` take the lowest alpha at which every token on them meets its minimum (Contrast), measured on the worst point behind the glass after saturate(`glass-saturate`). Behind `glass-fill`: the glows of Page background. Behind `glass-fill-strong`: the same glows, black in light and white in dark. The tint is white in light and `#202020` in dark. `typologies/glassmorphism/references/tokens.yaml` holds the result for Kore's palette; a Custom palette computes its own.
- **Depth:** Replaces: `elevation.depth`. Glass layers separate from what lies behind them by blur, a `glass-border` edge and a glass shadow. Solid layers separate with a surface step and a 1px `hairline`; only interactive solid elements cast a shadow, and the inset bevel of `gradient-raised` and `shadow-raised-sm`, like the inset highlight of the glass shadows, counts as part of the surface. In dark, a solid layer that sits higher is lighter.
- **Page background:** Replaces: `elevation.0-flat`. `canvas` and two glows fixed to the window behind every layer, painted as the background of `html`: background-color `canvas`; background-image `radial-gradient(circle closest-side, color-mix(in srgb, accent 60%, transparent) 40%, transparent 100%)`, then the same in `primary`; background-size `glow` `glow`; background-repeat no-repeat; background-attachment fixed; background-position calc(`glow` / −2) calc(`glow` / −2), then right calc(`glow` / −2) bottom calc(`glow` / −2). So the start glow is centred on the window's top start corner and the end glow on its bottom end corner; in RTL the two positions swap sides. Where the browser ignores background-attachment fixed, as Safari on iPhone does, the glows scroll with the page. Full-width sections are transparent, so the glows show through; a section with a photo shows its photo.
- **Glow level:** Replaces: `elevation.glow`. As the default, and the two glows of Page background on every page, dense task screens included.
- **1 · surface:** Replaces: `elevation.1-surface`. Static cards and panels on glass: Glass recipe, blur `glass-blur-card`, box-shadow `shadow-glass`; `glass-fill` on the page background, `glass-fill-strong` on a photo. Solid ones keep `surface-card` + `hairline`.
- **3 · floating:** Replaces: `elevation.3-floating`. Popovers and menus on glass: Glass recipe with `glass-fill-strong`, blur `glass-blur-float`, box-shadow `shadow-glass`; active items use `surface-float-active`. Solid ones keep `surface-float` + `hairline`.
- **4 · overlay:** Replaces: `elevation.4-overlay`. Dialogs and sheets on glass, over a `scrim`: Glass recipe with `glass-fill-strong`, blur `glass-blur-float`, box-shadow `shadow-glass-layered`. Solid ones keep `surface-float` + `hairline`.
- **Interactive level:** Replaces: `elevation.interactive`. Buttons and solid clickable cards as the default. A clickable glass card: `shadow-glass`, and `shadow-glass-layered` on hover (Hover).
- **The Hairline Rule:** Replaces: `elevation.the-hairline-rule`. Glass surfaces cast their glass shadow, clickable or not. On solid surfaces only interactive elements cast a shadow; every other solid element, containers of clickable items included, uses only a 1px `hairline` border.
- **Identity:** Replaces: `identity.identity`. The Hairline Rule of this typology (The Hairline Rule), The Radius-Padding Rule, The Concentric Rule.
- **Barely perceptible:** Replaces: `elevation.barely-perceptible`. On solid surfaces, `shadow-rest` hints that an element is clickable and `shadow-hover` suggests a lift; the only stacked solid shadows are the `shadow-raised` tokens, on filled and elevated Buttons (Button). Glass shadows show the layer floating, in `primary`, each with an inset highlight in white at 50% along the top edge: `shadow-glass` is one shadow, 0 20px 50px −12px at 45%; `shadow-glass-layered` stacks four, at 14, 12, 20 and 32%, on dialogs, sheets and the hover of a clickable glass card.

### Color

- **The One Primary Rule:** Replaces: `color.the-one-primary-rule`. The default rule (The One Primary Rule), and `primary` also colors the end glow of Page background and the glass shadows.
- **The accent is rare:** Replaces: `color.the-accent-is-rare`. The default rule (The accent is rare), and `accent` also colors the start glow of Page background, outside the count of the page's 4 elements in `accent`. Text on glass takes any text token other than `accent`.
- **Glows:** Replaces: `color.glows`. As the default (Glows), and the two glows of Page background on every page, dense task screens included.

### Interaction and motion

- **Hover:** Replaces: `elevation.hover`. A clickable glass card: `shadow-glass` → `shadow-glass-layered` and a lift of `space-1`, with `duration-fast` and `ease-out`. Other clickable elements: `shadow-rest` → `shadow-hover`, `shadow-raised` → `shadow-raised-hover` on filled and elevated Buttons, and the same lift. **Pressed:** back to rest in `duration-instant`.
- **Stay light:** Replaces: `motion.stay-light`. Blur is the material of every glass surface (Glass), the large ones included: the Top bar, sheets and dialogs. Keep the other expensive effects, filters and shaders, in small isolated areas, apply `will-change` only during the animation, and test on a mid-range phone. Verify against two measurable bars: 60fps or better while the animation runs (DevTools Performance panel), and zero layout shift caused by it (CLS 0, Lighthouse). A failure on either means the effect is too heavy for its purpose.

### Dark theme and fallback

- **Dark theme shadows:** Replaces: `elevation.dark-theme-shadows`. Solid surfaces: denser, black at 24–32%. Glass shadows stay in `primary`, at the alpha of their token.
- **Without glass:** with `prefers-reduced-transparency: reduce`, or where `backdrop-filter` is not supported, every glass surface takes its default solid recipe.

**Composition:** material only: no source gives a rule on composition, so grid, type and spacing stay the default.

## Files

- `typologies/glassmorphism/references/tokens.yaml`: the keys of `references/tokens.yaml` glassmorphism replaces, and its new keys.
- `typologies/glassmorphism/references/components/`: one file per component whose material glassmorphism replaces, named as in `references/components/`.
