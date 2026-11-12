# Carousel

**Uses:** Button, Cards, Tooltip.

**Purpose:** items of the same kind that scroll sideways. It never moves on its own.

- **Hierarchy:** the item in view is the focal point (The One Winner Rule): the centre photo, the card at the start of the row, the card in view, the current feature photo, the current story. The neighbours step back (scaled, grey or cut by the edge); the arrows, the indicator and the position only move and tell where the user is.
- **Elements:** the Carousel's own: viewport, photo track, photo slide, photo, photo frame, arrow slot, indicator, indicator mark, header, section title, navigation, position, card track, card slide, offer link, offer photo, offer text, label row, offer title, offer subtitle, bottom row, code, end arrow, snap card, snap title, snap subtitle, snap position, footer, arrow group, features, feature list, feature panel, feature description, editorial, editorial grid, story text, story stack, story, story position, story title, place, paragraph, story arrows, story list, story tab, tab line, status. Other components: the arrows (Button, icon, with a Tooltip), the feature tabs (Button, tertiary and secondary), the cards of the Card and Snap variants (Cards, Clickable card and Standard). Photo, Card, Snap, Features and Editorial are variants of the carousel, not elements.

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

**Photo variant**

- **Viewport:** the centre photo is 40% of the carousel's width, 60% below `sm` (container query), proportions of this variant; a neighbour is scaled to 80%. position relative; overflow hidden; touch-action pan-y; height calc(the photo's width × 4 / 3 + 2 × `space-1`).
- **Photo track:** position absolute; inset 0.
- **Photo slide:** portrait 3:4. position absolute; top `space-1`; inset-inline-start calc(50% − the photo's width / 2); height calc(100% − 2 × `space-1`); border-radius `rounded-xl`; cursor pointer.
- **Photo slide place:** transform translateX(the slide's distance from the centre) scale(0.8); each slide sits (its index − the current index) steps from the centre, a step being 0.9 × the photo's width + `space-4`, so the neighbours sit `space-4` from the centre photo.
- **Centre photo:** scale 1; cursor default. A click on a neighbour makes it the centre photo. While dragging, the scale follows the position.
- **Photo:** with its alt text. width 100%; height 100%; border-radius inherit; object-fit cover.
- **Ends:** the first and the last photo never leave the carousel's edges (Material 3, Carousel). On the first photo the centre photo sits at the start edge, its neighbours after it; on the last, at the end edge, `space-1` from it; on every other photo it is centred. While dragging, its place follows the scroll between these places.
- **Start:** the carousel opens on the second photo, centred, the first one visible at its start side; with two photos, on the first.
- **Photo arrows:** elevated, medium. They show only with a fine pointer (pointer: fine); on touch they are visually hidden (Status) and stay for screen readers.
- **Arrow slot:** position absolute; top 50%; transform translateY(−50%); z-index `zIndex-raised`. The previous one inset-inline-start `space-4`, the next one inset-inline-end `space-4`.
- **Indicator:** decoration (`aria-hidden`): the status says the position. display flex; justify-content center; gap `space-2`; margin-top `space-4`.
- **Indicator mark:** one per photo. height `space-1`; width `space-2`; border-radius `rounded-full`; corner-shape round; background `hairline-strong`; transform-origin center; transition background-color `duration-base` `ease-out`.
- **Current mark:** width `space-6`; background `ink`. The change of width is animated with a transform (FLIP) in `duration-base`, never by animating the width (Motion).
- **Indicator reduced motion:** transition 0s.

**Card variant**

- **Header:** the section's title at the start, the navigation at the end. display flex; align-items center; justify-content space-between; gap `space-4`.
- **Section title:** font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`.
- **Navigation:** the position and the arrows, small tertiary buttons, shown on every device. display flex; align-items center; gap `space-2`.
- **Position:** the status, "<position> of <total>". font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; font-variant-numeric tabular-nums; color `mute`.
- **Card track:** cursor grab; display grid; grid-auto-flow column; grid-template-rows auto auto auto auto auto; grid-auto-columns min(calc(`space-48` + `space-32`), calc(100% − `space-4` − `space-8`)); column-gap `space-4`; row-gap 0; overflow-x auto; scroll-snap-type x mandatory; scroll-behavior smooth; scrollbar-width none; padding `space-1`; margin −`space-1`; scroll-padding-inline `space-1`. The scrollbar of WebKit: display none.
- **Card track from sm:** 2 cards in view. column-gap `space-8`; grid-auto-columns calc((100% − 2 × `space-8` − `space-8`) / 2).
- **Card track from lg:** 3 cards in view. grid-auto-columns calc((100% − 3 × `space-8` − `space-8`) / 3). Every card is wider than tall.
- **Card track reduced motion:** scroll-behavior auto.
- **Scrolling:** on touch, the native scroll snapping to the start of a card; with a mouse the row is dragged, at 30% of the pointer past the first and the last card, and the spring settles on a card. A drag that moved does not open the card's link.
- **Card slide:** position relative; isolation isolate; overflow-wrap anywhere; scroll-snap-align start; translate var(--ox, 0) 0, where --ox is the drag's offset set by the script; display grid; grid-row span 5; grid-template-rows subgrid; row-gap 0. Its focus marks follow `rounded-xl`.
- **Offer slide:** the slide of an offer has no look of its own: background none; outline 0.
- **Offer link:** the whole card is one link (Cards: Clickable card), as tall as its content. display grid; grid-row span 5; grid-template-rows subgrid; overflow-wrap anywhere.
- **Offer photo:** 16:9, optional, a Media slot (Cards). grid-row 1.
- **Offer text:** grid-row 2 / span 3; display grid; grid-template-rows subgrid; padding-inline `space-6`.
- **Label row:** optional, the Hugeicons `Tag01` before the label: `icon-sm`, in `mute`; grid-row 1; display flex; align-items center; gap `space-2`; margin-block `space-6` `space-2`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; color `mute`.
- **Offer title:** grid-row 2; margin-top `space-6`, 0 when a card of the row has a label row; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`.
- **Offer subtitle:** grid-row 3; margin-top `space-1`; margin-bottom `space-6`, 0 when a card of the row has a bottom row; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Bottom row:** optional: the code at the start, the end arrow at the end. grid-row 5; display flex; align-items center; justify-content space-between; gap `space-4`; margin `space-4` `space-6` `space-6`; padding-top `space-4`; border-top `line-thin` solid `hairline`.
- **Code:** font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; font-variant-numeric tabular-nums; color `mute`.
- **End arrow:** the Hugeicons `ArrowRight02`, `icon-md`, hidden from assistive technology. color `ink`.
- **End arrow in RTL:** transform scaleX(−1).
- **Aligned zones:** a card without an optional zone keeps its other zones aligned with the cards beside it; the cards share one height.

**Snap variant**

- **Snap track:** one card in view, as wide as a card with a paragraph (Cards, Width), or the row when it is narrower; no other card shows. column-gap `space-4`; max-width calc(`measure` + 2 × `space-6` + 2 × `space-1`); grid-template-rows auto; grid-auto-columns 100%.
- **Snap card:** a standard card (Cards). grid-row auto; grid-template-rows 1fr auto; row-gap `space-4`; justify-items center; text-align center; scroll-snap-stop always; scale `scale-enter`; transition scale `duration-slow` `ease-in-out`. On touch each swipe moves one card.
- **Snap card in view:** scale 1.
- **Snap card reduced motion:** scale 1; transition 0s.
- **Snap header:** align-self center; align-items center.
- **Snap title:** the card's title, font-family `title-lg`; font-size `title-lg`; font-weight `title-lg`; line-height `title-lg`; letter-spacing `title-lg`.
- **Snap subtitle:** under the title, font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Snap position:** "<position> of <total>" at the bottom end. justify-self end; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; font-variant-numeric tabular-nums; color `mute`.
- **Footer:** under the card, `space-4` below, the indicator of the Photo variant at its start edge, the arrow group at its end edge. display flex; align-items center; justify-content space-between; gap `space-4`; width min(calc(`measure` + 2 × `space-6`), 100%).
- **Footer indicator:** margin-top 0.
- **Arrow group:** small secondary buttons, shown on every device. display flex; gap `space-2`.

**Features variant**

- **Features:** the list and the photos, no fill; below `lg` one column, the list centred above the photos. display grid; gap `space-8`; align-items center.
- **Features from lg:** the list and the photos side by side, centred together: the list as wide as its longest feature, the photos' column as wide as the photo plus `space-8` on each side. grid-template-columns auto calc(`space-48` + `space-32` + 2 × `space-8`); justify-content center; column-gap `space-12`.
- **Feature list:** the features are tabs (`role="tablist"`, vertical): tertiary buttons with the feature's name, the selected one secondary. display flex; flex-direction column; align-items center; gap `space-2`. ↑ and ↓ move and select, Home and End go to the first and the last; focus follows the tab. The photos are the tab panel. No arrows.
- **Feature list from lg:** align-items flex-start.
- **Feature panel:** container-type inline-size.
- **Feature photos:** the current photo portrait 3:4, min(calc(`space-48` + `space-32`), calc(100cqw − 2 × `space-8`)) wide; the previous and the next sit behind it, so `space-8` of each shows past its sides; the photos further away hide behind them. A click on a side photo selects it. The change moves in `duration-focal` with `ease-in-out`.
- **Feature slide:** transform none; scale `scale-enter`; transition scale `duration-slow` `ease-in-out`.
- **Current feature slide:** scale 1.
- **Photo frame:** position absolute; inset 0; overflow hidden; border-radius inherit.
- **Feature photo frame:** filter grayscale(1); transition filter `duration-slow` `ease-in-out`.
- **Current feature photo frame:** filter none.
- **Feature reduced motion:** the slide: scale 1; transition 0s; the photo frame: transition 0s.
- **Feature description:** the selected feature's sentence. margin `space-4` auto 0; max-width 40ch; text-align center; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.

**Editorial variant**

- **Editorial:** display flex; flex-direction column; gap `space-8`.
- **Editorial grid:** one column as wide as a Snap card, centred, the photo above the text. display grid; gap `space-12`; align-items center; width min(calc(`measure` + 2 × `space-6`), 100%); margin-inline auto.
- **Editorial grid from lg:** two equal columns, the text at the start and the photo at the end. grid-template-columns repeat(2, minmax(0, 1fr)); width auto.
- **Story text from lg:** order −1.
- **Editorial viewport:** portrait 4:5. height auto; aspect-ratio 4/5; overflow visible. No swipe on the photo.
- **Editorial slide:** inset 0; width auto; height auto; transform none; cursor default.
- **Story fade:** the editorial slide and the story: opacity 0; visibility hidden; transition opacity `duration-slow` `ease-in-out`, visibility 0s linear `duration-slow`.
- **Current story:** opacity 1; visibility visible; transition opacity `duration-slow` `ease-in-out`.
- **Story stack:** the stories share one cell. display grid.
- **Story:** grid-area 1/1.
- **Story position:** "<position> of <total>"; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; font-variant-numeric tabular-nums; color `mute`.
- **Story title:** margin-top `space-2`; font-family `display-sm`; font-size `display-sm`; font-weight `display-sm`; line-height `display-sm`; letter-spacing `display-sm`.
- **Place:** margin-top `space-1`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Paragraph:** margin-top `space-4`; max-width `measure`; font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`; color `body`.
- **Story arrows:** secondary buttons, shown on every device. display flex; gap `space-2`; margin-top `space-6`.
- **Story list:** one tab per story (`role="tablist"`), `space-8` under the editorial grid. display grid; grid-auto-flow column; grid-auto-columns minmax(0, 1fr); gap `space-4`. ← and → move and select, Home and End go to the first and the last.
- **Story tab:** position relative; display block; min-height `button-lg`; padding-top `space-2`; border-top `line-thin` solid `hairline`; text-align start; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Story tab focus:** its focus marks follow `rounded-sm`.
- **Selected story tab:** color `ink`.
- **Tab line:** the story tab's ::before: content ""; position absolute; inset-inline 0; top −`line-thin`; height `line-thick`; background `ink`; transform scaleX(0); transform-origin left; transition transform `duration-base` `ease-out`, never by animating the width.
- **Selected tab line:** transform scaleX(1).
- **Tab line in RTL:** transform-origin right.
- **Editorial reduced motion:** the editorial slide, the story and the tab line: transition 0s.
