# Glassmorphism

## Definition

Glassmorphism builds depth from translucent layers: panels of frosted glass float above a vivid background and blur it.

Four traits define it: translucent panels that blur what lies behind them, several layers floating above the page, vivid colors behind the glass that make the blur visible, a thin light border on every glass panel.

## Where to use

- **Fits:** a page where a few surfaces float above the content (Glass).

## Replaces

### Material

- **Glass:** Replaces: `elevation.glass`. Twelve components are glass: the Top bar and its navigation panel, the Sidebar at every width, Menu, Popover, the Select's open list (a Menu), the Date picker's open calendar (a Popover), Dialog, Sheet, Command palette, the Cookie banner's box, Toast, and Cards, the Carousel's slides and the plan cards of Pricing included. Read the markup and apply each check:
  1. A component in the list takes the Glass recipe.
  2. A component inside a listed one keeps its base recipe, and so does a Menu or Popover whose trigger sits inside one or inside a Panel (step 3). Dialog, Sheet and Command palette open in the top layer and take the Glass recipe wherever their trigger sits.
  3. A Table, a chart (Charts), List rows, Steps, a form or the body of an article outside every listed component sits in one Panel: the Glass recipe; border-radius `rounded-xl` = padding `space-6`. Below `sm`, the Panel reaches the screen's side edges: margin-inline calc(`space-4` × −1); border-radius 0; padding-inline `space-4`, the phone side margin (Breakpoints). The Table's Panel holds its toolbar, its card and its pagination. The components inside it keep their base recipe, a card included, as in a Popover. A form is Form fields, Switch, Slider and every component that uses Form fields; the components of one form share one Panel, and a form inside a step of Steps shares the Steps' Panel.
  4. Every other component keeps its base recipe.

  The parts of a glass component, its own elements and the components inside it, keep their base recipe. Three parts lie on their surface's glass with a transparent fill: the Command palette's results, a drilled Menu's sub-menu, and the Toast's icon circle. The Popover's arrow is part of the popover's glass (Popover). Glass surfaces keep space between them. The Top bar and its navigation panel reach the screen's edge; cards sit in the page with space around them. Glass that a component's file prescribes, such as the Hero's veil, stays as written.
- **Glass recipe:** background `glass-background`; backdrop-filter `glass-backdrop`; box-shadow `glass-shadow`. A glass surface over a `scrim`, the Dialog, the Sheet, the Command palette and the Cookie banner's box, takes background `glass-scrim-background`: the lowest fill at which text on glass keeps its contrast over the dimmed page. The rest of the recipe stays, in each theme.
- **Ledge recipe:** box-shadow `shadow-raised-rim`, inset 0 −`line-thick` 0 color-mix(in srgb, the ledge color `mix-ledge`, transparent). The component names its ledge color.
- **Text on glass:** `glass-background` keeps its value; the text moves. Each token that fails its minimum (Contrast) on the glass moves its tone away from the glass, as in Custom palette step 3, until it passes on the worst point behind the glass. The points behind the glass are `canvas` and the five stops of Page background, each after the saturate() of `glass-backdrop`, and the five stops of Page background under `glass-page-dim`, where text sits on the page with no glass under it. The moved value replaces the token on the whole page. `typologies/glassmorphism/references/tokens.yaml` holds the result for Kore's palette; a Custom palette computes its own with `kore_palette.py --typology glassmorphism`.
- **Destructive fill:** the fill of a Destructive button is `danger-fill`, the `danger` of `references/tokens.yaml` before Text on glass moves it; its text keeps `danger-on`. `typologies/glassmorphism/references/tokens.yaml` holds it for Kore's palette; a Custom palette takes its own `danger`.
- **Depth:** Replaces: `elevation.depth`. Glass layers separate from what lies behind them by blur and the edge of `glass-shadow`. Solid layers separate with a surface step and a 1px `hairline`; only interactive solid elements cast a shadow, and the inset bevel of `gradient-raised` and `shadow-raised-sm` counts as part of the surface. In dark, a solid layer that sits higher is lighter.
- **Page background:** Replaces: `elevation.0-flat`. `glass-gradient`, fixed to the window behind every layer, painted as the background of `html`: background linear-gradient(`glass-page-dim`) fixed, `glass-gradient` fixed. `glass-page-dim` is black at 35% in dark, Apple HIG's dark dimming layer, and transparent in light. In light it runs from the dark theme's `primary` to its `accent`, in dark from the light theme's, in CIE LCH, 5 stops. Full-width sections are transparent, so the gradient shows through; a section with a photo shows its photo.
- **Section on a photo:** Replaces: `images.section-on-a-photo`. Photo, veil and the section's text as the default rule (Section on a photo). The Panel takes the Glass recipe in the dark theme, whatever the page's theme: the section carries `data-theme="dark"`, so the Panel's glass and its text take the dark tokens. The page around the section keeps its theme.
- **Glow level:** Replaces: `elevation.glow`. The gradient of Page background is the only color behind the layers; it takes the place of every `*-glow` wash.
- **1 · surface:** Replaces: `elevation.1-surface`. Static cards and panels on glass: Glass recipe. Solid ones keep `surface-card` + `hairline`.
- **3 · floating:** Replaces: `elevation.3-floating`. Popovers and menus on glass: Glass recipe; active items use `surface-float-active`. Solid ones keep `surface-float` + `hairline`.
- **4 · overlay:** Replaces: `elevation.4-overlay`. Dialogs and sheets on glass, over a `scrim`: Glass recipe. Solid ones keep `surface-float` + `hairline`.
- **Interactive level:** Replaces: `elevation.interactive`. Buttons and every clickable element other than a card as the default. A clickable card: as Hover.
- **The Hairline Rule:** Replaces: `elevation.the-hairline-rule`. Glass surfaces take `glass-shadow`, clickable or not. On solid surfaces only interactive elements cast a shadow; every other solid element, containers of clickable items included, uses only a 1px `hairline` border.
- **Identity:** Replaces: `identity.identity`. The Hairline Rule of this typology (The Hairline Rule), The Radius-Padding Rule, The Concentric Rule.
- **Barely perceptible:** Replaces: `elevation.barely-perceptible`. On solid surfaces, `shadow-rest` hints that an element is clickable and `shadow-hover` suggests a lift; the only stacked solid shadows are the `shadow-raised` tokens, on filled and elevated Buttons (Button). `glass-shadow` draws the glass edge: a white line along the top, a 1px white ring and, in light, a soft drop shadow in black.

### Color

- **The One Primary Rule:** Replaces: `color.the-one-primary-rule`. The default rule (The One Primary Rule), and `primary` also colors the gradient of Page background.
- **The accent is rare:** Replaces: `color.the-accent-is-rare`. The default rule (The accent is rare), and `accent` also colors the gradient of Page background, outside the count of the page's 4 elements in `accent`. Text on glass takes any text token other than `accent`.
- **Glows:** Replaces: `color.glows`. As Glow level.
- **Disabled:** a disabled element changes two things of its component file. Its fill `surface-elevated`, and the Slider's track `hairline-medium`, becomes `disabled-background` with no shadow; the `hairline` ring of its base recipe stays as its edge. Its text and icons in `stone` take color-mix(in srgb, `ink` `mix-disabled`, transparent). The parts that show the state keep their default: the checked box of Checkbox and radio, the Switch's knob and its track when on, the Slider's thumb.

### Interaction and motion

- **Hover:** Replaces: `elevation.hover`. A clickable card keeps `glass-shadow` and lifts by `space-1`, with `duration-fast` and `ease-out`. Every other clickable element, Buttons included, as the default (Hover). **Pressed:** back to rest in `duration-instant`.
- **Stay light:** Replaces: `motion.stay-light`. Blur is the material of every glass surface (Glass), the large ones included: the Top bar, sheets and dialogs. Keep the other expensive effects, filters and shaders, in small isolated areas, apply `will-change` only during the animation, and test on a mid-range phone. Verify against two measurable bars: 60fps or better while the animation runs (DevTools Performance panel), and zero layout shift caused by it (CLS 0, Lighthouse). A failure on either means the effect is too heavy for its purpose.

### Dark theme and fallback

- **Dark theme shadows:** Replaces: `elevation.dark-theme-shadows`. Solid surfaces: denser, black at 24–32%. `glass-shadow` keeps the value of its token.
- **Without glass:** with `prefers-reduced-transparency: reduce`, or where `backdrop-filter` is not supported, every glass surface takes its default solid recipe.

**Composition:** material only: no source gives a rule on composition, so grid, type and spacing stay the default.

## Files

- `typologies/glassmorphism/references/tokens.yaml`: the keys of `references/tokens.yaml` glassmorphism replaces, and its new keys.
- `typologies/glassmorphism/references/components/`: one file per component whose material glassmorphism replaces, named as in `references/components/`.
