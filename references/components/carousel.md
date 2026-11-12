# Carousel

**Uses:** Button, Cards, Tooltip.

**Purpose:** items of the same kind that scroll sideways. It never moves on its own.

- **Hierarchy:** the item in view is the focal point (The One Winner Rule): the centre photo, the card at the start of the row, the card in view, the current feature photo, the current story. The neighbours step back (scaled, grey or cut by the edge); the arrows, the indicator and the position only move and tell where the user is.
- **Elements:** the Carousel's own: viewport, photo track, photo slide, photo, photo frame, arrow slot, indicator, indicator mark, header, section title, navigation, position, card track, card slide, offer link, offer photo, offer text, label row, offer title, offer subtitle, bottom row, code, end arrow, snap card, snap title, snap subtitle, snap position, footer, arrow group, features, feature list, feature panel, feature description, editorial, editorial grid, story text, story stack, story, story position, story title, place, paragraph, story arrows, story list, story tab, tab line, status. Other components: the arrows (Button, icon, with a Tooltip), the feature tabs (Button, tertiary and secondary), the cards of the Card and Snap variants (Cards, Clickable card and Standard). Photo, Card, Snap, Features and Editorial are variants of the carousel, not elements.
- **Variant files:** read only the file of each variant that the part being built or checked contains: Photo `references/components/carousel/photo.md`, Card `references/components/carousel/card.md`, Snap `references/components/carousel/snap.md` with `references/components/carousel/photo.md`, Features `references/components/carousel/features.md`, Editorial `references/components/carousel/editorial.md`.

**Every variant**

- **Structure:** a `section` with `aria-roledescription="carousel"` and a name; each item is a `group` with `aria-roledescription="slide"` and the name "<position> of <total>".
- **Finger:** the content follows the finger; on release the `spring` settles it on the nearest item, the gesture's speed included. Past the first and the last item the movement follows at 30% of the finger (this file's value). An interrupted gesture continues from where it is.
- **Trackpad:** a sideways scroll moves the items like the finger and stops at the first and the last item; when it stops for `duration-fast`, the `spring` settles on the nearest item. A vertical scroll scrolls the page.
- **Keyboard:** the area takes focus with Tab, and its name says the keys: "<what the items are>, use the arrow keys to move". ← and → move by one item, Home and End go to the first and the last. The focus marks sit on the item in view, concentric with it; the area keeps `space-1` around the items so the marks are never clipped.
- **Keyboard area focus:** on :focus-visible: outline none, changed in 0s; the item in view takes the corner marks of States.
- **Arrows:** icon-only buttons (Hugeicons `ArrowLeft01`, `ArrowRight01`, `icon-md`) with a label and a tooltip, disabled at the ends; when the focused one becomes disabled, focus moves to the other.
- **Arrow timing:** arrows, keys and clicks move in `duration-base` with `ease-out` in the Photo and Card variants, in `duration-focal` with `ease-in-out` in the Snap and Features variants.
- **Announcement:** one `role="status"` says the position: "<item> <position> of <total>"; it is visually hidden in the Photo, Snap, Features and Editorial variants; the Card variant shows it (Position).
- **Status:** position absolute; width `line-thin`; height `line-thin`; overflow hidden; clip-path inset(50%); white-space nowrap.
- **Reduced motion:** the item changes at once, with no scale, no slide and no fade.
- **No text on a photo;** a caption goes under it.
- **Icon:** flex none; display block.
