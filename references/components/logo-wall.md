# Logo wall

**Uses:** Button.

A section of the page (site.md Logo wall): the logos of clients, partners, press or integrations on one row.

**Choosing the variant.** From PRODUCT.md: integrations (tools the product connects to) → Title and text; clients, partners and press → Logos only.

**All variants**

- **Logos:** no label under each one; the brand name goes in `alt`. Every logo is one color, `currentColor` set to `mute`, so it works in both themes. Each logo is `space-8` (32px) tall, `space-12` apart.
- **Row:** one row, centred. When the logos do not fit, the row loops: the list repeated once with `aria-hidden="true"`, moving toward the start, one loop every `duration-loop` with `ease-linear`; the edges fade over `space-12`. It stops on hover and on focus on the logos, and off screen.
- **Pause:** an icon-only `tertiary` button (Pause/Resume), hidden until focused, as the Skip link; focused, it shows over the faded end edge of the row.
- **Reduced motion:** the row does not move, shows each logo once and scrolls by hand; no button.
- **Text above:** centred, `space-12` above the row (The Distance Ratio Rule).

**Variants**

1. **Logos only:** One line in `body-md` `mute` above the row, when the user gives it.
2. **Title and text:** The title in `headline-md` `ink`, the text in `body-lg` `body` `space-1` under it, at most 60ch of `body-lg` wide.
