# Features

**Uses:** Hero.

A section of the page (site.md Features): what the product does, with no order to learn. With an order, the section is How it works.

**Which variant,** the first yes wins:

1. One visual shows every feature → Large visual under the title.
2. No visual → Icon grid.
3. Several visuals, one per feature → ask the user which feature is the main one (Never invent values): it becomes a Large visual section of its own and the others an Icon grid, their visuals left out. When no feature is the main one, Icon grid only.

**All variants**

- **At most four features** (site.md Sections); the others go on their own page, reached by a "See all" link at the end of the section.
- **Title of the section:** `headline-md` `ink`, `space-12` over what follows (The Distance Ratio Rule).
- **Images:** outside a card, so the Images of Hero (`references/components/hero.md`): as wide as their slot, `object-fit: cover`, radius `xl`, a 1px `hairline` drawn inside the edge, `surface-elevated` behind while they load.

**Variants**

1. **Large visual under the title:** Centred column (`references/components/hero.md`): the title and, `space-1` under it, the section's text in `body-lg` `body`; the block at most 60ch of `body-lg` wide, centred with `margin-inline: auto`, its text centred. No call to action. The visual 16:9, as wide as the section, `space-12` under the text. On a page whose hero is Centred, visual below, this variant is that hero's shape again: the section takes Icon grid instead (site.md Sections, Each shape once per page).
2. **Icon grid:** the same Centred column above the features, `space-12` over them; a `ul` with one `li` per feature.
   - **Feature:** three zones in this order, `space-4` apart: the icon, the title in `headline-sm` `ink`, the text in `body-lg` `body` `space-1` under the title.
   - **Icon:** 24px in `mute`, `aria-hidden` (Icons): the title already names the feature. Never in a box or on a tinted square, which would be a surface in the accent (Color rules, The accent is rare).
   - **Row or column:** all the features on one row, one column each, when the section is at least `n × 320px` plus `(n − 1) × space-8` (32px) wide — 320px is the column of 45 characters of `body-lg`. Below that they stack, all of them: never some side by side and the rest below. `space-12` between the rows; between the columns `space-8`, `space-6` below `lg` and `space-4` below `md`.
   - **Zones aligned:** on a row the three zones start at the same height in every column (subgrid), whatever the length of the titles and the texts.
