# Cards

**Uses:** Avatar, Button, Segmented control, Tooltip.

**Purpose:** it groups the content and the actions about one subject.

**Card Anatomy: The Fixed Zone Rule.** A card follows a fixed order of zones, never reordered, the convention of Material Design and other systems: media, header, body, actions. Every zone is optional; the zones present keep this order. The Plan card has its own anatomy (Plan card): its order, line, action and width replace the rules below.

- **Hierarchy:** the zones read in their fixed order. The title is the focal point (The One Winner Rule): `title-md` in `ink`, before the subtitle and the body in `body-md`. A card that exists to show one number has the number as its focal point (Key figure); a plan card has the price (Plan card).
- **Elements:** the Cards' own: card, header, title, subtitle, paragraph, body, key figure row, figure, unit, action row, media slot, media image, media body, summary, read more link, clickable card, clickable top, icon circle, cover card, cover image, cover text, cover veil, arrow circle, arrow, header row, card grid, clickable grid. Other components: the buttons of the action row (Button); the header action (Button, tertiary icon, small, with a Tooltip), the Segmented control and the Avatar in the header row. Standard, media, with actions, clickable, cover and plan are variants of the card, not elements.
- **Variant files:** read only the file of each variant that the part being built or checked contains: Clickable `references/components/cards/clickable.md`, Cover `references/components/cards/cover.md` with `references/components/cards/clickable.md`, Plan `references/components/cards/plan.md`.
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Media `references/components/cards/media.md`, With actions `references/components/cards/actions.md`.
- **Card:** position relative; display flex; flex-direction column; min-width 0; background `surface-card`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; border-radius `rounded-xl`; color `ink`. (replaced in: glassmorphism)
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
- **Header row:** the header with an avatar before it, or a header action or a Segmented control at its end, `space-2` apart. The header takes the room left and breaks a long word inside the card. Its first line sits on the centre of a `button-sm` action: moved down by half the difference between `button-sm` and the `title-md` line-height. The avatar is centred on the title and subtitle block. A Segmented control sits at the row's end, aligned to the top, under the title and subtitle when the two do not fit on one row.
- **Header action:** only when the card has rare actions to gather (edit, duplicate, delete: Grouping actions), a "More" button (Button, tertiary icon, small) as a corner action (Shapes), `space-4` from the card's top and end edges, with the title centred on it; accessible label and tooltip "More options for <card title>".
- **Card grid:** cards side by side. display grid; grid-template-columns 1fr; gap `space-8`.
- **Card grid below sm:** gap `space-6`.
- **Card grid from md:** grid-template-columns repeat(2, minmax(0, 1fr)).
- **Card grid from lg:** grid-template-columns repeat(3, minmax(0, 1fr)).
- **Zones in a row:** the zones of the cards in one row line up: titles, bodies, links and action rows each start on the same line in every card. Each card spans one grid row per zone: display grid; grid-template-rows subgrid; align-items start; row-gap 0; a media card spans 4 rows (the media slot and the 3 rows of its media body, itself a subgrid), a card with actions 3, a card with a paragraph 2.
- **Focus:** a button inside the card's image takes no focus marks: the card holds the focus.
- **Cards side by side:** a Card grid; their zones line up (Zones in a row).
