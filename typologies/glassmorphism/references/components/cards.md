# Cards

- **Card:** Replaces: `cards.card`. As in `references/components/cards.md`, with the Glass recipe (1 · surface).
- **Clickable hover:** Replaces: `cards.clickable-hover`. On mouse hover (hover: hover): box-shadow `glass-shadow`; transform translateY(−`space-1`).
- **Clickable pressed:** Replaces: `cards.clickable-pressed`. transform none; box-shadow `glass-shadow`; transition-duration `duration-instant`.
- **Cover veil:** Replaces: `cards.cover-veil`. A dark glass over the photo, as in the default with: top −(2 × `space-12` + `space-6`); background rgb(0 0 0 / .41); backdrop-filter blur(22px) saturate(1.8); mask-image linear-gradient(to bottom, transparent, #000 2 × `space-12`), so the glass fades in over its first 2 × `space-12`. Black at 41% is the lowest at which `on-photo-mute` reaches 4.5:1 over the lightest color of the placeholder file after the saturate(). The cover title and subtitle keep `on-photo` and `on-photo-mute`.
