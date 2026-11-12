# Hero

**Uses:** Button.

The first section of a page: the title, the subtitle, the calls to action (site.md Hero) and, in seven of the eight variants, a visual.

**Choosing the variant.** From PRODUCT.md (what the page presents and its images); the first yes wins:
1. The product is a phone app → Phone with notifications.
2. 7 or more images, all portrait → Arc.
3. 10 or more images → Scattered gallery.
4. No image, and PRODUCT.md names 5 layers of the product → Isometric.
5. No image → Text only.
6. 1 to 9 images: the hero keeps the one that shows what the page presents as a whole (if none clearly does, ask); the others go in the sections below. Then:
   - a photo of a place, people or an object → Full-bleed photo;
   - portrait or square → Text and visual side by side;
   - landscape → Centred, visual below.

- A video counts as an image: its format decides.
- A form takes the place of the calls to action, under the subtitle; its button is the `primary` (Form fields). The variant does not change.

**All variants**

- **Section:** at least `100dvh` tall, from the top of the page: the hero is the only section that runs under the Top bar. Its content centred on both axes (`display: grid`, `place-items: center`); padding above the bar's height (`space-8` × 2 + `env(safe-area-inset-top)`) + `space-12`, so the content stays centred in the screen under the bar, `space-12` below, and the page's side margin at the sides (`space-4`, `space-8` from `md`, as the Top bar); the content `width: 100%`, `max-width: 1200px` (`max-content`). The section carries `isolation: isolate`, so its layers stay under the Top bar. From `lg`, every variant but Centred, visual below fits in one screen: its visual is at most `100dvh` minus the section's padding high, keeping its ratio.
- **Text:** the title in `display-lg` `ink`; the subtitle in `body-lg` `body`, `space-1` under it; the calls to action `space-6` under the subtitle, `space-2` apart, wrapping. The text block is at most 60ch of `body-lg` wide (its `font-size` is `body-lg`).
- **Centred column:** the text block centred with `margin-inline: auto`, its text and its calls to action centred (Layout primitives 4); a visual sits `space-12` under the text.
- **Side by side:** from `lg`, two equal halves `space-8` apart, the text at the start and the visual at the end, centred vertically; below `lg`, the text first and the visual `space-12` under it.
- **Images:** as wide as their slot, `object-fit: cover`, radius `xl`, a 1px `hairline` inside the edge, `surface-elevated` behind while they load.

**Variants**

1. **Text only:** Centred column; the two glows (`references/rules/color.md`, Glows, Form) inside the text block, on its corners.
2. **Centred, visual below:** Centred column; the visual 16:9, as wide as the section.
3. **Text and visual side by side:** Side by side; the visual 4:5.
4. **Full-bleed photo:** the section's only padding is the bar's height above. The photo fills it: `position: absolute`, `inset: 0`, 100% wide and high, `object-fit: cover`, empty `alt`. Over the photo a layer in `veil-photo`, `position: absolute`, `inset: 0`. The Centred column sits over the veil (`position: relative`), padding `space-12` above and below and `space-6` at the sides; title and subtitle in `on-photo`; the second call to action is `elevated`.
5. **Arc:** Centred column; `space-12` under it, a list of seven portrait 3:4 images on one line (3:4 also for photos of people): `display: flex`, centred on both axes, `padding-inline` 10% (it keeps the fan inside the section), no list style.
   - **Image:** `flex: 0 1 space-48` (it shrinks to fit), `min-width: 0`, `transform-origin: 50% 100%`; the 4th, the centre, `flex-basis: space-48 × 1.25` and flat.
   - **Fan:** d is an image's distance from the centre (3, 2, 1, 0, 1, 2, 3). The 1st to 3rd `rotate(−fan × d)`, the 5th to 7th `rotate(fan × d)`; in RTL the signs swap.
   - **Overlap:** each image after the first `margin-inline-start: −space-48 × 0.5`; `z-index: raised − d`, so inner images cover outer ones.
   - **Smaller screens:** from `md` to below `lg` the 1st and 7th are hidden and the 2nd has no overlap margin; below `md` the 1st, 2nd, 6th and 7th are hidden and the 3rd has no overlap margin.
6. **Scattered gallery:** the text on the start edge. Ten images, a to j; with more than ten, the user picks which ten. Ratios: a 3:4, b 1:1, c 4:3, d 4:3, e 3:4, f 1:1, g 3:4, h 4:3, i 1:1, j 3:4.
   - **Grid:** one grid holds the title, a block with the subtitle and the calls to action, and the ten images; every column `minmax(0, 1fr)`. The title and the subtitle block sit at the bottom of their cell (`align-self: end`).
   - **Below `lg`:** two columns, `gap: space-4`, areas `"t t" "s s" "a b" "c d"`: the title, the subtitle block, then images a and b on one row and c and d on the next; the subtitle block `margin-top: space-1 − space-4` and `margin-bottom: space-12 − space-4`, so the subtitle sits `space-1` under the title and the images `space-12` under the text; e to j are hidden.
   - **From `lg`:** six columns and three rows `minmax(0, 1fr)`, the grid as high as `100dvh` minus the section's padding, `gap: space-8`, areas `"a . b c . d" ". e . f g ." "h . i . j ."`; each image at most `space-48` wide and `max-height: 100%` of its cell, keeping its ratio, placed in its cell (`align-self`, `justify-self`):

     | Row | Image, column, place in the cell |
     |---|---|
     | 1 | a, 1, top start · b, 3, bottom centre · c, 4, centre end · d, 6, top centre |
     | 2 | e, 2, centre start · f, 4, bottom end · g, 5, top centre |
     | 3 | h, 1, top end · i, 3, centre start · j, 5, top centre |

     The title (`grid-row: 3`, `grid-column: 1 / 4`) and the subtitle block (`grid-row: 3`, `grid-column: 4 / 7`) sit at the bottom of row 3, over the images (`position: relative`, `z-index: raised`).
   - **Veil behind the text (from `lg`):** one glass panel behind the title and the subtitle block, the title's `::before`: `position: absolute`, `z-index: -1` (inside the block: over the images, under the text), `pointer-events: none`. It runs from `space-12` × 2 above the title to the section's bottom (`space-12` under it), and from the screen's start edge to its end edge: with E = (`100vw` − `min(100vw − space-8 × 2, 1200px)`) / 2, `inset-inline-start: −E`, `inset-inline-end: −(100% + space-8 + E)` (the subtitle block is as wide as the title, `space-8` away). `canvas` at 15% with `backdrop-filter: blur(7px)`, faded in from the top with `mask-image: linear-gradient(to bottom, transparent, #000 space-12 × 2)`.
   - **Without glass** (`prefers-reduced-transparency` or no `backdrop-filter` support): instead, a `::before` behind each text block, `position: absolute`, `inset: −space-12 × 2 0 0 0`, `z-index: -1`, `pointer-events: none`, `opacity: 0.8`. Its background is `linear-gradient(to bottom, …)` with `canvas` mixed into transparent (`color-mix(in srgb, canvas N%, transparent)`) at these stops, from the veil's top (smoothstep t²(3 − 2t)):

     | Stop | 0 | `space-12` × 0.2 | × 0.4 | × 0.6 | × 0.8 | `space-12` | × 1.2 | × 1.4 | × 1.6 | × 1.8 | `space-12` × 2 |
     |---|---|---|---|---|---|---|---|---|---|---|---|
     | `canvas` | 0% | 2.8% | 10.4% | 21.6% | 35.2% | 50% | 64.8% | 78.4% | 89.6% | 97.2% | 100% |
7. **Isometric:** Side by side; the visual is five square plates, one per layer of the product, the first layer at the bottom. The visual is decorative (`aria-hidden`) and has no hover.
   - **Container:** `perspective: perspective`, `display: grid`, `place-items: center`, `padding-block-start: space-12 × 4` (room for the plates above).
   - **Stack** (in the container; it carries the whole rotation, once): `position: relative`, `space-48` × 1.25 wide, `max-width: 100% / 1.6`, `aspect-ratio: 1`, `transform-style: preserve-3d`, `transform: rotateX(tilt) rotateZ(−turn)` (`rotateZ(turn)` in RTL).
   - **Plate n** (n = 0 for the first layer, at the bottom, to 4): in the stack, `position: absolute`, `inset: 0`, `transform-style: preserve-3d`, `transform: translateZ(space-12 × n)` and nothing else. Radius `sm`, `space-6` padding, a 1px `hairline-medium` outline inside the edge, background `linear-gradient(to bottom right, accent-glow, info-glow), canvas` (`to bottom left` in RTL).
   - **Edge:** four copies of the plate's shape behind it (`position: absolute`, `inset: 0`, radius inherited, `preserve-3d`, `pointer-events: none`), at `translateZ` −¼, −½, −¾ and −1 times `space-2`, so its corners have no gap; the last one has the plate's 1px `hairline-medium` outline. They are painted with the plate's gradient over `hairline-medium`.
   - **Label:** the layer's name in `label-md` `mute`, `white-space: nowrap`, `position: absolute`, `inset-inline-start: space-6`, `inset-block-end: space-2`: in the strip the plate above leaves visible.
   - **Top plate:** the one accent point. It carries `data-theme="light"`; plate and edge in `linear-gradient(to bottom right, accent, info)` (`to bottom left` in RTL), so the light theme's values in both themes; its label in that theme's `primary-on`.
   - **Drawing colors:** `hairline-medium`, `canvas` and `primary-on` for the plates' outlines and drawings are read on the stack, in the page's theme (custom properties set on the stack), so the top plate's outline and drawing keep the page's theme.
   - **Drawing:** each plate carries a drawing of its layer, chosen by the agent, made of boxes in the page's theme: a 1px `hairline-medium` outline over `canvas`, radius `xs`, or `md` for a button or a field, sizes and gaps from the space tokens. Text lines are bars `space-1` or `space-2` high, radius `full`, in `canvas` with no outline. The top plate's drawing ends with one button: `space-12` × `space-4`, radius `md`, filled in `primary-on` with no outline. The drawings of Kore's own layers, as a reference:
     - Token: four `space-6` squares in a row, `space-2` apart.
     - Spacing: a three-column grid of six squares, `space-3` apart.
     - Text: three bars, `space-2`, `space-1` and `space-1` high, 100%, 75% and 50% wide, `space-2` apart.
     - Components: a button `space-12` × 2 by `space-8` and a field `field` high, radius `md`, `space-3` apart.
     - Page: a bar `space-4` high, a block `space-12` high and the button, `space-3` apart.
8. **Phone with notifications:** Side by side; the visual is a phone in a holder `space-48` × 1.25 wide, `max-width: 60%`, `margin-inline: auto`, `position: relative`, `container-type: inline-size`, with the start glow only (`references/rules/color.md`, Glows, Form). Its shape is iPhone 15 Pro's (71.6 × 146.6 mm body); every size below is in `cqw` of the holder's width. The body carries `data-theme="dark"`: its colors are the dark theme's tokens.
   - **Body:** `position: relative`, `aspect-ratio: 71.6 / 146.6`, radius 15cqw, padding 3cqw, `canvas`; its rings `box-shadow: inset 0 0 0 1.2cqw surface-float-active, inset 0 0 0 1.6cqw stone`.
   - **Side buttons:** `position: absolute`, 1.2cqw wide, radius `xs`, `surface-float-active`, outside the body (`inset-inline-start: −1.2cqw` on the start side, `inset-inline-end: −1.2cqw` on the end side). On the start side: action button at `top: 20%`, 4% high; volume up at 28%, 9% high; volume down at 39%, 9% high. On the end side: power at 31%, 12% high.
   - **Screen:** `position: relative`, 100% high, radius 12cqw, `surface-float`, `overflow: hidden`, padding 15cqw at the top and 4cqw on the other sides, `display: flex`, `flex-direction: column`, `justify-content: flex-end` (the notification at the bottom). The wallpaper covers it (`position: absolute`, `inset: 0`, `data-theme="light"`): `linear-gradient(to bottom right, accent, info)`, as the top Isometric plate.
   - **Dynamic Island:** `position: absolute`, 32cqw × 9.4cqw, centred (`inset-inline: 0`, `margin-inline: auto`), 3cqw from the top, radius `full`, `primary-on`; the camera a 3cqw dot in `hairline-medium`, 3cqw from its end, centred vertically.
   - **Notification:** the app's grouped notification, over the wallpaper (`position: relative`), as wide as the screen's content: a `surface-elevated` card, radius `md`, `space-3` padding, a 1px `hairline` inside the edge, `z-index: raised` over the strips. In it, `display: flex`, `space-2` apart and aligned at the top: the app icon, a `space-8` square (`flex: none`) with radius `sm` in `accent`, holding the app's icon (Icons) `icon-md` in `primary-on`, centred; then the text (`min-width: 0`, `flex: 1`): the app name and the time in `body-sm` `mute` on one line, at its two ends, `space-2` apart; the title in `title-sm` `ink`; one line of `body-sm` `body` cut with an ellipsis.
   - **Grouped notifications:** under the card two strips `space-2` high, radius `md` at the bottom corners only, `surface-elevated` with a 1px `hairline`: the first `space-3` in from each side, the second `space-6` in at 70% opacity.

**Motion**

- **One focal moment per page:** the hero enters once, built from the product. All its pieces enter together in `duration-focal`: opacity on `ease-linear`, a `space-6` (24px) shift on `ease-out`. The title comes from above. In the Hero variants Centred, visual below, Arc and every side-by-side one, the subtitle and the calls to action come from above too and the visual from below; in the others they come from below. From `lg`, in the side-by-side variants, the text comes from the start side and the visual from the end side. The Isometric plates add their own entry (Isometric entry). The entry holds its first state only before it starts (`animation-fill-mode: backwards`): once it ends the pieces carry no animation, so a glass inside them blurs what is behind.
- **Isometric entry:** plate n starts at `translateZ(space-12 × (n + 1))` with `visibility: hidden` and drops to its place, `duration-slow` with `ease-out`, delay `n × duration-slow`, so the bottom plate first. No opacity: it flattens the 3D. Under reduced motion the plates do not move.
