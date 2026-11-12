# Minimalism

## Definition

Minimalism simplifies the interface by removing the elements and content that do not serve the user's tasks, so content and functions come across simply and directly, with as few distractions from the main content as possible. It applies to content, look and functions together; used as a visual style only, it adds complexity.

Five traits define it: flat surfaces, a reduced or monochrome palette, fewer elements, as much empty space as possible, marked type.

**Fewer elements:** remove every element that serves neither the function nor the message (menu items, links, images, lines, captions, textures, colors, fonts, icons), until removing one more breaks a task.

Kore aims for a screen that feels quiet and reads at a glance. Its forms are round and friendly, laid on a strict 8-point grid. Surfaces are subdued, a cool off-white by day and a warm near-black by night. Space, a change of tone or a 1px border is enough to separate them. Color is used sparingly. One accent color marks the moment that matters and semantic colors mark state, while everything else stays neutral so the content comes first. Every screen has a single point of entry, and the interface answers every action, prevents errors and uses the words of the people who use it.

## Where to use

- **Fits:** simple sites, portfolios, pages with little content.
- **Complex sites:** remove only what no task needs; information that becomes hard to find means too much was removed.

## Replaces

### Material

- **Depth:** Replaces: `elevation.depth`. Static layers separate with a surface step and a 1px `hairline`; no element casts a shadow or carries the inset bevel of `gradient-raised`. In dark, a layer that sits higher is lighter, never darker.
- **Identity:** Replaces: `identity.identity`. The 8-point grid, The Hairline Rule (no shadow anywhere, a 1px border on static containers), The Radius-Padding Rule, The Concentric Rule, The Distance Ratio Rule, no icons on labeled buttons.
- **The Hairline Rule:** Replaces: `elevation.the-hairline-rule`. No element casts a shadow, clickable or not. Static containers, including containers of clickable items such as popovers, menus and sheets, use a 1px `hairline` border. A ring with no offset and no blur (`0 0 0 1px`) is a border, not a shadow, and stays.
- **Interactive level:** Replaces: `elevation.interactive`. Buttons and clickable cards: their surface, no shadow, no `gradient-raised`; on hover, the background of Hover.

### Color

- **Glow level:** Replaces: `elevation.glow`. A `*-glow` wash, only on the user's request; never on dense task screens.
- **Glows:** Replaces: `color.glows`. Only on the user's request, never by default. Never on dense task screens: lists, tables, and forms of more than 4 fields.

### Interaction and motion

- **Hover:** Replaces: `elevation.hover`. On a clickable element only the background changes, with `duration-fast` and `ease-out`, and nothing lifts: a transparent or neutral surface takes `surface-hover`; a filled one takes its fill mixed with `ink` at `mix-hover`. Text links keep the hover of their component (`ink` and underline). **Pressed:** back to rest in `duration-instant`.
- **Reduced motion:** Replaces: `elevation.reduced-motion`. The background changes without animation.

## Files

- `typologies/minimalism/references/tokens.yaml`: the keys of `references/tokens.yaml` minimalism replaces, and its new keys.
- `typologies/minimalism/references/components/`: one file per component whose material minimalism replaces, named as in `references/components/`.
