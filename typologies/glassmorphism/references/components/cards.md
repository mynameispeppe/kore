# Cards

- **Card:** Replaces: `cards.card`. As in `references/components/cards.md`, with the Glass recipe (1 · surface). A card that Glass keeps solid, such as a plan card of Pricing or a card that holds a Table, a chart or a Figure, stays as the default.
- **Clickable hover:** Replaces: `cards.clickable-hover`. On mouse hover (hover: hover): box-shadow `glass-shadow`; transform translateY(−`space-1`).
- **Clickable pressed:** Replaces: `cards.clickable-pressed`. transform none; box-shadow `glass-shadow`; transition-duration `duration-instant`.
- **Icon circle:** Replaces: `cards.icon-circle`. As in the default, with the inner glass of Glass inside glass under a layer of `surface-elevated`: background linear-gradient(color-mix(in srgb, `surface-elevated` `mix-tint`, transparent)), `glass-inner-background`; box-shadow `glass-inner-shadow`.
- **Cover veil:** Replaces: `cards.cover-veil`. A dark glass over the photo, as in the default with: top −(2 × `space-12` + `space-6`); background rgb(0 0 0 / .41); backdrop-filter blur(22px) saturate(1.8); mask-image linear-gradient(to bottom, transparent, #000 2 × `space-12`), so the glass fades in over its first 2 × `space-12`. Black at 41% is the lowest at which `on-photo-mute` reaches 4.5:1 over the lightest color of the placeholder file after the saturate(). The cover title and subtitle keep `on-photo` and `on-photo-mute`.
- **Arrow circle:** Replaces: `cards.arrow-circle`. As in the default, with the inner glass of Glass inside glass: background `glass-inner-background`; box-shadow `glass-inner-shadow`; color `on-photo`.
