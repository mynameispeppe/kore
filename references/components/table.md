# Table

**Uses:** Cards, Form fields, Checkbox and radio, Badge, Button, Tooltip, Menu, Pagination, Progress, Toast, Empty state.

**Purpose:** it compares the same facts across many items.

- **Always drawn:** the card, the header, the rows, sorting, the Columns menu, the loading and the no-rows states.
- **On request only:** filters, selection, the action column, the add button, export, the total row and pagination appear only when the user asks for them ("let me filter workouts", "delete several workouts", "show the total"); never added on their own.
- **Hierarchy:** the toolbar comes first, then the header, then the rows, then the selection count and the pagination. The first column is the focal point (The One Winner Rule): the item's name, the only cell text in `title-sm` `ink`, the column the eye reads first (F pattern); the numbers in `ink` follow; the other cells in `body` follow them; the header in `label-md` `mute` only names the columns.
- **Elements:** the Table's own: toolbar, end group, menu wrapper, scroll container, table, caption, header cell, sort button, sort arrows, filter field, row cell, name cell, value, unit, selection column, action column, total row, selection count, no-rows cell. Other components: the card (Cards), the filter field (Form fields), the row checkboxes and the export radios (Checkbox and radio), the statuses (Badge), the toolbar buttons and the action button (Button), the tooltips (Tooltip), the Columns, Export and row menus (Menu), the pagination (Pagination), the loading rows (Progress, Skeleton), the confirmations (Toast), the no-rows content (Empty state).
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Filters `references/components/table/filters.md`, Selection `references/components/table/selection.md`, Action column `references/components/table/action-column.md`, Add button `references/components/table/add-button.md`, Export `references/components/table/export.md`, Total row `references/components/table/total-row.md`, Pagination `references/components/table/pagination.md`.

**Layout**

- **Container:** a Card (Cards) with padding-block `space-3` instead of `space-6`; the sides keep `space-6`.
- **Scroll container:** the table runs `space-3` into the card's side padding. overflow-x auto; margin-inline calc(`space-3` × −1).
- **Table:** border-collapse collapse; width 100%; min-width `table-min`.
- **Caption:** visible or visually hidden. text-align start.
- **Cells:** every th and td: padding 0 `space-3`; text-align start; so the first column's text lines up with the card's content.
- **Phones:** the table keeps its min-width and scrolls sideways inside its scroll container; the page never scrolls sideways.

**Above the card**

- **Toolbar:** a row above the card, `space-4` away, never inside it. display flex; justify-content space-between. The Columns button at the start; the end group at the end.
- **End group:** export, then the add button last. display flex; gap `space-2`.
- **Menu wrapper:** each menu trigger sits with its menu in it. position relative; display inline-flex.
- **Columns:** a secondary Button "Columns" opens a Menu with one `menuitemcheckbox` per data column, its 16px check as the trailing element. Picking an item leaves the menu open. The last visible column cannot be hidden: its item has `aria-disabled="true"`. A hidden column has visibility hidden, so it keeps its place and width and the other columns never move; its filter empties, the table returns to the first page, and if the table was sorted by it, the sort moves to the first visible sortable column.
- **Checked column item:** the check shows the state; the text stays as in a normal item: font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.

**Header and rows**

- **Header cell:** a `<th scope="col">`. height `space-10`; color `mute`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`; border-bottom `line-thin` solid `hairline`; white-space nowrap.
- **Sorted header cell:** the header with `aria-sort`: color `ink`.
- **Row cell:** each td in the body. height `space-12`; vertical-align middle; color `body`; border-bottom `line-thin` solid `hairline`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`. A table is read across columns, so the line guides the eye (The Separation Ladder). A row whose cells hold their own links or buttons takes no background on hover; only a row that is one link as a whole does.
- **Last row:** its cells: border-bottom 0.
- **Name cell:** the first data column, the item's name. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Value:** a figure carries the emphasis (Text hierarchy), alone or before its unit ("**55** min"). color `ink`; font-variant-numeric tabular-nums.
- **Unit:** after its value, separated by a space. color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Alignment:** text, counts ("6") and figures with a unit ("55 min") at the start: text-align start. Amounts with their currency ("$1,250.00") at the end, so the digits line up: text-align end. Statuses and buttons centred: text-align center. A header follows its column.
- **Status:** a status Badge (Badge, Status badge).

**Sort order**

- **Sorting:** on columns where sorting helps to compare (numbers, dates, names), never on statuses or actions. One column is sorted at a time: a click on the active column alternates ascending and descending (there is no unsorted state); a click on another column sorts it ascending. Numbers sort by value, text in the language's alphabetical order. The table starts sorted by the first column, ascending. The active header has `aria-sort`; the other sortable headers have no `aria-sort`. A new order returns to the first page.
- **Sort button:** in the header cell, the title then the sort arrows. position relative; display inline-flex; align-items center; gap `space-1`; color inherit; font inherit; letter-spacing inherit; border-radius `rounded-sm`.
- **Sort hit area:** the sort button's ::before, 44px tall (Touch targets). content ""; position absolute; inset calc((`icon-sm` − (`space-10` + `space-1`)) / 2) calc(`space-1` × −1).
- **Sort arrows:** after the title, a slot with two chevrons, up and down, overlapped. The slot: position relative; display inline-flex; width `icon-xs`; height `icon-xs`. Each chevron: position absolute; inset 0; width 100%; height 100%; color `hairline-strong`; transition color `duration-fast` `ease-out`. The up one: transform translateY(calc(`icon-xs` / −4)). The down one: transform translateY(calc(`icon-xs` / 4)).
- **Active arrow:** the chevron of the active direction: color `ink`.

**Total, states and height**

- **Loading:** skeleton rows in the shape of the table (Progress, Skeleton) under the real header, and the skeleton of the pagination (Pagination); the card has `aria-busy="true"`.
- **No rows:** the card keeps the header and, in place of the rows, one cell across every column holding the Empty state (Empty state), with no pagination; the header titles are plain text (nothing to sort). text-align center; color `mute`.
- **First use:** with no data, the Empty state names the missing items and what adding the first one gives ("No invoices yet", "Add your first one to start getting paid."), with the add button, if any, as its primary.
- **Height:** while the rows that pass the filters are more than the rows per page, the rows area is as tall as the header plus 5 rows, plus the total row when there is one; with 5 rows or fewer it is as tall as its rows, so a filter that leaves fewer rows shortens the table. The last page keeps the same height, so nothing below moves.
- **Fixed height:** with more rows per page than 5, they scroll inside the scroll container between a header that stays at the top and a total row that stays at the bottom. The scroll container: overflow-y auto.
- **Sticky header:** its cells: position sticky; top 0; z-index `zIndex-raised`; background `surface-card`; border-bottom 0.
- **Sticky lines:** each sticky cell draws its line with ::after, so a hidden column keeps its piece of the line. content ""; position absolute; inset-inline 0; border-bottom `line-thin` solid `hairline`; visibility visible; bottom 0 in the header; top 0 and bottom auto in the total row.
