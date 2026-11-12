# Cards

**Uses:** Avatar, Button, Segmented control, Tooltip.

**Purpose:** it groups the content and the actions about one subject.

**Card Anatomy: The Fixed Zone Rule.** A card follows a fixed order of zones, never reordered, the convention of Material Design and other systems: media, header, body, actions. Every zone is optional; the zones present keep this order. The Plan card has its own anatomy (Plan card): its order, line, action and width replace the rules below.

- **Hierarchy:** the zones read in their fixed order. The title is the focal point (The One Winner Rule): `title-md` in `ink`, before the subtitle and the body in `body-md`. A card that exists to show one number has the number as its focal point (Key figure); a plan card has the price (Plan card).
- **Elements:** the Cards' own: card, header, title, subtitle, paragraph, body, key figure row, figure, unit, action row, media slot, media image, media body, summary, read more link, clickable card, clickable top, icon circle, cover card, cover image, cover text, cover veil, arrow circle, arrow, header row, card grid, clickable grid. Other components: the buttons of the action row (Button); the header action (Button, tertiary icon, small, with a Tooltip), the Segmented control and the Avatar in the header row. Standard, media, with actions, clickable, cover and plan are variants of the card, not elements.
- **Card:** position relative; display flex; flex-direction column; min-width 0; background `surface-card`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; border-radius `rounded-xl`; color `ink`.
- **Card padding:** padding `space-6`, the same on all four sides.
- **Card with a table:** `space-3` above and below the table; the sides stay `space-6` (Table).
- **No line between zones:** space separates them (The Separation Ladder); lines belong to containers whose body scrolls (Sheet).
- **Never nest cards.** Inner content uses rows separated by space; a rounded block with a background appears only when each item is its own unit (a clickable row).
- **Header:** title and subtitle, read as one block. display flex; flex-direction column; gap `space-1`.
- **Title:** font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; color `ink`.
- **Subtitle:** font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`. A description of one sentence; more sentences make a paragraph.
- **Paragraph:** margin-top `space-6`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `body` (From role to style).
- **Body:** the content and data under the header, `space-6` below it; its rows separated by space only, `space-3` apart; Affinity Grouping decides its groups, `space-6` apart.
- **Height:** each card is as tall as its content. Cards in one row of a layout grid share one height; a group of cards in one cell (a grid inside the cell) counts as one cell: the group sets the row's height, and its cards keep their own; the space left goes to the card's last zone: its actions move to the bottom, a chart grows.
- **Width:** max-width calc(`measure` + 2 × `space-6`) on a card with a paragraph: a `measure` paragraph plus its padding, so its lines stay within 75 characters (Typography rules), as in Carousel.
- **Titles of cards side by side** take the same number of lines at every width where the cards share a row; stacked cards are exempt (`kore_check --url` measures it). A title from the user stays as given; when the user's titles break it, the report proposes titles that hold it, through humanizer when installed, in every language of the project. The agent writes its own titles within 5 characters of each other, through humanizer when installed; when no humanizer version holds it, the agent picks one that does.
- **Key figure:** when a card exists to show one number, the number is its focal point, in one of two forms. In the header, the key figure row under the title and subtitle (Key figure row, Figure, Unit); `ink` instead of `accent` in a Dashboard's key figures but the leading one (`references/components/dashboard.md`). Or, when the card is one figure of a Stats section (`references/components/stats.md`), the figure first in `headline-lg` `ink` with tabular figures, its label `space-2` under it in `title-md` `ink`, and the explanation `space-4` below the label in `body-md` `mute`.
- **Key figure row:** display flex; flex-wrap wrap; align-items baseline; gap `space-1` `space-2`; margin-top `space-2`.
- **Figure:** font-family `display-sm`; font-size `display-sm`; font-weight `display-sm`; line-height `display-sm`; letter-spacing `display-sm`; font-variant-numeric tabular-nums; color `accent`.
- **Unit:** its unit and context, on the figure's baseline. font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Actions:** at the bottom of the card, at the end of the row, confirm last with cancel or back before it (Action order in Hierarchy), aligned with the actions of every other card of a set. At most one `primary` per card (The One Primary Rule): a repeated card keeps its own primary when it has a clear main action (buying a product); use secondary and tertiary instead when the card's actions are all lower-emphasis, with none of them the point of the card. A card with actions is at least `space-48` + `space-32` wide, as the Carousel's cards. It has no shadow, since it is not clickable as a whole.
- **Action row:** margin-top `space-8`; margin-inline-end −`space-3`; margin-bottom −`space-3`; display flex; justify-content flex-end; gap `space-2`. The buttons (`button-md`, `rounded-md`) sit `space-3` from the card's bottom and end edges (The Concentric Rule).
- **Action row button:** flex-shrink 0.
- **Stacked action row:** when the buttons do not fit the row's width: flex-direction column; align-items stretch. The confirming action at the bottom, never in a staircase.
- **Header row:** the header with an avatar before it, or a header action or a Segmented control at its end, `space-2` apart. The header takes the room left and breaks a long word inside the card. Its first line sits on the centre of a `button-sm` action: moved down by half the difference between `button-sm` and the `title-md` line-height. The avatar is centred on the title and subtitle block. A Segmented control sits at the row's end, aligned to the top, under the title and subtitle when the two do not fit on one row.
- **Header action:** only when the card has rare actions to gather (edit, duplicate, delete: Grouping actions), a "More" button (Button, tertiary icon, small) as a corner action (Shapes), `space-4` from the card's top and end edges, with the title centred on it; accessible label and tooltip "More options for <card title>".
- **Media card:** an image above the text. padding 0; overflow hidden.
- **Media slot:** position relative; aspect-ratio 16/9; margin `space-2` `space-2` 0; border-radius `rounded-lg` (The Concentric Rule); overflow hidden; background `surface-elevated`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`.
- **Media image:** with alt text. position absolute; inset 0; width 100%; height 100%; object-fit cover; border-radius inherit.
- **Media body:** padding `space-6`; display flex; flex-direction column.
- **Media body zones:** every zone after the first: margin-top `space-6`.
- **Summary:** one sentence. font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Read more link:** a "Read more" text link. justify-self start; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `link`; text-decoration underline `line-thin`; text-underline-offset `space-1`.
- **Read more focus:** on :focus-visible: outline none, changed in 0s, and the corner marks of States.
- **Card grid:** cards side by side. display grid; grid-template-columns 1fr; gap `space-8`.
- **Card grid below sm:** gap `space-6`.
- **Card grid from md:** grid-template-columns repeat(2, minmax(0, 1fr)).
- **Card grid from lg:** grid-template-columns repeat(3, minmax(0, 1fr)).
- **Zones in a row:** the zones of the cards in one row line up: titles, bodies, links and action rows each start on the same line in every card. Each card spans one grid row per zone: display grid; grid-template-rows subgrid; align-items start; row-gap 0; a media card spans 4 rows (the media slot and the 3 rows of its media body, itself a subgrid), a card with actions 3, a card with a paragraph 2.
- **Media card in a row:** overflow-wrap anywhere.
- **Clickable card:** the whole card is one link or button, a square, with its icon at the top and the title and subtitle at the bottom. It never contains other buttons or links. Several items that each open something are List rows inside one card; they become clickable cards only when the user asks for cards. An item without its own icon is a List row. aspect-ratio 1; justify-content space-between; gap `space-4`; text-decoration none; box-shadow `shadow-rest`; transition box-shadow `duration-fast` `ease-out`, transform `duration-fast` `ease-out`.
- **Clickable hover:** on mouse hover (hover: hover): box-shadow `shadow-hover`; transform translateY(−`space-1`). (replaced in: minimalism)
- **Clickable pressed:** transform none; box-shadow `shadow-rest`; transition-duration `duration-instant`.
- **Clickable focus:** on :focus-visible: outline none, changed in 0s; the title takes the underline of Clickable focus title.
- **Clickable focus title:** text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s (the link focus underline, States).
- **Clickable reduced motion:** transform none.
- **Clickable top:** display flex; color `mute`.
- **Icon circle:** holds one `icon-md` icon. flex none; display grid; place-items center; width `space-10`; height `space-10`; border-radius `rounded-full`; corner-shape round; background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; color `mute`.
- **Clickable grid:** columns that never stretch, as many as fit, the space left at the end of a row empty; a row of cards shares one height, so a card whose text needs more room makes its row taller instead of clipping. display grid; grid-template-columns repeat(auto-fill, calc(`space-32` + `space-8`)); gap `space-8`.
- **Clickable grid below sm:** gap `space-6`.
- **Cover card:** the whole card is one link, one column of the card grid, its photo filling the card, the title and subtitle over it. display grid; grid-template-columns minmax(0, 1fr); aspect-ratio auto; justify-content normal; padding 0; color `ink`; text-decoration none. Hover, pressed and reduced motion as the Clickable card. (replaced in: minimalism)
- **Cover image:** grid-area 1/1; overflow hidden; border-radius `rounded-xl`. Its image, with alt text: width 100%; aspect-ratio 1/1; object-fit cover.
- **Cover text:** grid-area 1/1; align-self end; position relative; z-index `zIndex-raised`; display grid; grid-template-columns minmax(0, 1fr) auto; column-gap `space-4`; row-gap `space-1`; padding 0 `space-6` `space-6`; overflow-wrap anywhere.
- **Cover title:** font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; color `on-photo`.
- **Cover subtitle:** font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `on-photo-mute`.
- **Cover veil:** the cover text's ::before: content ""; position absolute; z-index −1, behind the text; top −2 × `space-12`; inset-inline 0; bottom 0; border-radius 0 0 `rounded-xl` `rounded-xl`; background `veil-fade`: `veil-cover` faded in from transparent over its first 2 × `space-12`, then solid to the card's bottom.
- **Arrow circle:** hidden from assistive technology (the card is already the link). grid-column 2; grid-row 1 / span 2; align-self center; display grid; place-items center; width `space-10`; height `space-10`; border-radius `rounded-full`; background `surface-card`; color `ink`.
- **Arrow:** the Hugeicons `ArrowRight02`, `icon-md`.
- **Arrow in RTL:** transform scaleX(−1).
- **Plan card:** one plan of a Pricing section (`references/components/pricing.md`), compared with the cards beside it, so what decides comes before what details. Its zones in this order: the header (name in `title-lg` `ink`, one line in `body-md` `mute` `space-1` under it); the price `space-2` under the header, the figure with its currency symbol in `display-sm` `ink` with tabular figures, its period in `body-md` `mute` on the same baseline (not a Key figure: the accent marks the featured plan); one `primary` button `space-6` under the price, as wide as the card; a `line-thin` `hairline` line `space-6` under the button, which closes the part that decides; the list `space-6` under the line: each item in `body-md` `body`, the Hugeicons `Tick02` (`icon-sm`) in `mute` `space-2` before it (`Cancel01` for an item the plan does not hold, Pricing, Rows), its centre on the centre of the item's first line; the entries `space-3` apart. The card is never narrower than `plan-min`, since the one full-width button needs no room for a second, and never wider than (`max-content` − 2 × `space-8`) / 3.
- **Focus:** a button inside the card's image takes no focus marks: the card holds the focus.
- **Cards side by side:** a Card grid; their zones line up (Zones in a row).
