# List rows

**Uses:** Avatar, Button, Menu, Tooltip.

**Purpose:** items shown one under the other, each a row with an optional leading element, a title, an optional secondary line and an optional trailing element.

- **Hierarchy:** the leading element comes first, then the title and the secondary line, then the trailing element. The title is the focal point (The One Winner Rule): `title-sm` in `ink`, read before the secondary line in `body-sm` `mute`; the leading circle and the trailing element, in `mute`, only mark and serve.
- **Elements:** the List rows' own: list, row, leading circle, text, title, secondary line, trailing, value. Other components: the leading Avatar (Avatar, 40px), the row's action (Button, tertiary), the More options menu (Button, tertiary icon, `button-md`, with its Tooltip, opening a Menu).
- **List:** a `ul`, each row an `li`, so assistive technology announces how many there are. Rows separate with space only, never with a divider on every row, and two highlights never touch. The negative margin lines the text up with the content around it, the highlight `space-3` beyond the text; a page that sets the list's own width overrides max-width. list-style none; padding 0; margin-block 0; display flex; flex-direction column; gap `space-2`; margin-inline −`space-3`; max-width `list`.
- **Row:** the radius is the standard card's radius less the row padding (The Concentric Rule), so the text stays on the card curve's centre. display flex; align-items center; gap `space-4`; min-height calc(`space-12` + `space-2`); padding `space-2` `space-3`; border-radius `rounded-md`; color `ink`; text-decoration none.
- **Leading circle:** optional; a 20px icon, centred, or in its place a 40px Avatar. Without it the text starts at the row padding. All rows of a list have it or none do. flex none; width `space-10`; height `space-10`; border-radius `rounded-full`; corner-shape round; background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; display grid; place-items center; color `mute`.
- **Text:** the title, then the secondary line. flex 1; min-width 0; display flex; flex-direction column.
- **Title:** font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Secondary line:** one line. white-space nowrap; overflow hidden; text-overflow ellipsis; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Trailing:** one of: the Hugeicons `ArrowRight01` arrow at 16 on a link row; a value on a static row; one tertiary Button with a verb label when the row has one action; the More options menu when it has more. display flex; align-items center; gap `space-2`; color `mute`.
- **Value:** font-variant-numeric tabular-nums; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Link row:** a row that opens something is an `a` with the arrow. transition background-color `duration-instant` `ease-out`; under reduced motion, transition 0s.
- **Link row hover:** on mouse hover (hover: hover): background `surface-hover`.
- **Link row pressed:** background `surface-pressed`.
- **Link row focus:** on :focus-visible: outline none, changed in 0s; background `surface-hover`.
- **Link title focus:** the link focus underline on the title (States): text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s.
- **Rows with actions:** a row holding a button or a menu is never a link, because a link cannot contain a button: it is a static row with the action as its trailing element.
- **Static rows:** an `li` with no link; they do not react to hover or press.
