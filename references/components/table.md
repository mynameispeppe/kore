# Table

**Uses:** Cards, Form fields, Checkbox and radio, Badge, Button, Tooltip, Menu, Pagination, Progress, Toast, Empty state.

**Purpose:** it compares the same facts across many items.

- **Always drawn:** the card, the header, the rows, sorting, the Columns menu, the loading and the no-rows states.
- **On request only:** filters, selection, the action column, the add button, export, the total row and pagination appear only when the user asks for them ("let me filter workouts", "delete several workouts", "show the total"); never added on their own.
- **Hierarchy:** the toolbar comes first, then the header, then the rows, then the selection count and the pagination. The first column is the focal point (The One Winner Rule): the item's name, the only cell text in `title-sm` `ink`, the column the eye reads first (F pattern); the numbers in `ink` follow; the other cells in `body` follow them; the header in `label-md` `mute` only names the columns.
- **Elements:** the Table's own: toolbar, end group, menu wrapper, scroll container, table, caption, header cell, sort button, sort arrows, filter field, row cell, name cell, value, unit, selection column, action column, total row, selection count, no-rows cell. Other components: the card (Cards), the filter field (Form fields), the row checkboxes and the export radios (Checkbox and radio), the statuses (Badge), the toolbar buttons and the action button (Button), the tooltips (Tooltip), the Columns, Export and row menus (Menu), the pagination (Pagination), the loading rows (Progress, Skeleton), the confirmations (Toast), the no-rows content (Empty state).

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
- **Add button:** a primary Button with a verb and an object ("Add invoice"), text only. With no data it moves into the Empty state and the toolbar is not shown; focus that was in the toolbar or in the rows moves to it.
- **Export:** a secondary Button "Export" opens a Menu, built when it opens so its counts are current, placed at the end edge of its trigger. With no row passing the filters and none selected the button is disabled.
- **Export rows:** on top of the Export menu, a group (`role="group"`, `aria-label="Rows"`) of two `menuitemradio` items with the Radio circle (Checkbox and radio) at the start: "All rows" with the count of the rows that pass the filters, and "Selected" with the count of the selected rows. It starts on "Selected" while rows are selected, otherwise on "All rows"; picking a radio leaves the menu open. The checked circle: background `primary`; its dot at scale 1. An item with 0 rows has `aria-disabled="true"`; its circle: background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`.
- **Export formats:** after a group separator (Menu), the formats the user asked for, one `menuitem` each with its 16px icon at the start: "CSV" (`Csv01`), "Excel (.xlsx)" (`Xls01`), "JSON" (`FileCode`). The icon sits in a slot as wide as the radio circle, so every label starts on the same line: margin-inline calc((`checkbox` − `icon-sm`) / 2). A format exports the chosen rows with the visible columns, as shown on screen, closes the menu and confirms in a success Toast with the count and the format ("as Excel" for the spreadsheet).

**Header and rows**

- **Header cell:** a `<th scope="col">`. height `space-10`; color `mute`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`; border-bottom `line-thin` solid `hairline`; white-space nowrap.
- **Sorted header cell:** the header with `aria-sort`: color `ink`.
- **Row cell:** each td in the body. height `space-12`; vertical-align middle; color `body`; border-bottom `line-thin` solid `hairline`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`. A table is read across columns, so the line guides the eye (The Separation Ladder). A row whose cells hold their own links or buttons takes no background on hover; only a row that is one link as a whole does.
- **Last row:** its cells: border-bottom 0.
- **Name cell:** the first data column, the item's name. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Value:** a number carries the emphasis (Text hierarchy), alone or before its unit ("**55** min"). color `ink`; font-variant-numeric tabular-nums.
- **Unit:** after its value, separated by a space. color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Alignment:** text, counts ("6") and numbers with a unit ("55 min") at the start: text-align start. Amounts with their currency ("$1,250.00") at the end, so the digits line up: text-align end. Statuses and buttons centred: text-align center. A header follows its column.
- **Status:** a Badge.
- **Action:** a tertiary icon Button, small, with a 20px icon (`MoreHorizontal`), an accessible label and a Tooltip that name the row ("More options for Leg day"). When the row offers several commands, that button opens a Menu, with the destructive command last. The scroll container never clips it: the menu is placed on the screen (position fixed), min-width calc(`space-48` + `space-8`), its end edge on the trigger's end edge, `space-2` below the trigger, or above it when there is no room below; it closes when the page or the container scrolls, and focus inside it returns to the trigger.
- **Action column:** the last one: its header "Actions", centred. width calc(`space-12` + `space-8`).

**Sort order**

- **Sorting:** on columns where sorting helps to compare (numbers, dates, names), never on statuses or actions. One column is sorted at a time: a click on the active column alternates ascending and descending (there is no unsorted state); a click on another column sorts it ascending. Numbers sort by value, text in the language's alphabetical order. The table starts sorted by the first column, ascending. The active header has `aria-sort`; the other sortable headers have no `aria-sort`. A new order returns to the first page.
- **Sort button:** in the header cell, the title then the sort arrows. position relative; display inline-flex; align-items center; gap `space-1`; color inherit; font inherit; letter-spacing inherit; border-radius `rounded-sm`.
- **Sort hit area:** the sort button's ::before, 44px tall (Touch targets). content ""; position absolute; inset calc((`icon-sm` − (`space-10` + `space-1`)) / 2) calc(`space-1` × −1).
- **Sort arrows:** after the title, a slot with two chevrons, up and down, overlapped. The slot: position relative; display inline-flex; width `icon-xs`; height `icon-xs`. Each chevron: position absolute; inset 0; width 100%; height 100%; color `hairline-strong`; transition color `duration-fast` `ease-out`. The up one: transform translateY(calc(`icon-xs` / −4)). The down one: transform translateY(calc(`icon-xs` / 4)).
- **Active arrow:** the chevron of the active direction: color `ink`.

**Column filters**

- **Filters:** a filter field (Form fields) under the title of each sortable column, not shown while the table has no data. It is labelled by its column title and a visually hidden "filter" (`aria-labelledby`), so it reads "Name filter". It filters while the user types, and focus and caret stay in it: a row passes when the column's cell, as shown on screen, contains the text, ignoring case and accents; filters combine; the table returns to the first page.
- **Fixed layout:** with filters, the columns share the width equally (selection and actions aside) and never move while the rows change. The table: table-layout fixed.
- **Filter field:** width `space-32`; max-width 100%; margin-top `space-2`.
- **Filter box:** height `button-sm`; align-items flex-start. Its overlay (::before): inset 0 0 calc(`button-sm` − `button-lg`).
- **Filter input:** `type="search"`, placeholder "Filter…"; its hit area on the box's top, its text centred in the box. height `button-lg`; padding-block 0 calc(`button-lg` − `button-sm`); padding-inline `space-2`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Filter clear:** a field with text shows the inline button of Shapes at the end, with the X and a Tooltip, label "Clear Name filter"; it empties its field and focus stays in it. width `space-4`; height `space-4`. Its hit area (::before): inset calc((`space-4` − (`space-10` + `space-1`)) / 2). Its wrapper: align-self center; display flex.
- **Header with filters:** each title sits where it sits in a header without filters, and the field's hit area stays inside the header. Every header cell: vertical-align top; padding-block calc((`space-10` − `icon-sm`) / 2) calc(`button-lg` − `button-sm`).
- **Header cell without a filter:** on the filter's line. vertical-align bottom; line-height `button-sm`. The select-all box: min-height `button-sm`.
- **Sort hit area with filters:** it runs up and only into the `space-2` gap below, so it never overlaps the field's. inset calc(`icon-sm` + `space-2` − `button-lg`) calc(`space-1` × −1) calc(`space-2` × −1).

**Row selection**

- **Selection:** the first column holds a checkbox per row (Checkbox and radio) with a label that names the row ("Select Leg day"). A selected row keeps its background: the checked box shows the state. Selection is kept by item through sorting, filtering and pages. One visually hidden `role="status"` says the count after each change ("2 selected", "1 selected", "No rows selected").
- **Select all:** in the header, one more checkbox. With nothing selected it selects the rows of the current page ("Select all on this page"); with any row selected, on any page, it clears the whole selection ("Clear selection"), checked when the whole page is selected, otherwise indeterminate; disabled while the page shows no rows.
- **Delete:** acts at once and offers "Undo" in a Toast (Usability 3); focus then moves to the select-all checkbox.
- **Selection column:** its cells: width calc(`space-10` + `space-1`); padding-inline-end 0. The checkbox in a row: min-height calc(`space-10` + `space-1`); width calc(`space-10` + `space-1`); justify-content flex-start.
- **Select-all box:** min-height `space-10`; width calc(`space-10` + `space-1`); justify-content flex-start. Its hit area (::before), centred: content ""; position absolute; inset-inline 0; top 50%; height calc(`space-10` + `space-1`); transform translateY(−50%).
- **Selection count:** while a row is selected, a line under the card, `space-3` away, lined up with the pagination: "2 of 24 selected"; the total counts every row, filtered or not. margin-top calc(`space-3` − `space-6`); padding-inline `space-6`; color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; font-variant-numeric tabular-nums.

**Total, states and height**

- **Total row:** a `<tfoot>` row under the rows. It is not sorted with the rows and sums every row that passes the filters. With its column hidden there is no total row; with the first column hidden, "Total" stays in its place. Each cell: height `space-12`; border-top `line-thin` solid `hairline`; vertical-align middle; color `ink`.
- **Total label:** "Total", a `<th scope="row">` under the first data column. font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Sum:** under its column, with its alignment. font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; font-variant-numeric tabular-nums. The other cells, selection and actions included, are empty.
- **Loading:** skeleton rows in the shape of the table (Progress, Skeleton) under the real header, and the skeleton of the pagination (Pagination); the card has `aria-busy="true"`.
- **No rows:** the card keeps the header and, in place of the rows, one cell across every column holding the Empty state (Empty state), with no pagination; the header titles are plain text (nothing to sort). text-align center; color `mute`.
- **First use:** with no data, the Empty state names the missing items and what adding the first one gives ("No invoices yet", "Add your first one to start getting paid."), with the add button, if any, as its primary.
- **No match:** when the filters match nothing, in a `role="status"` region: "No workouts match these filters", "Check the spelling or try another word.", a tertiary Button "Clear filters" that empties every field and moves the focus to the first one.
- **Pagination:** when asked for, it shows whenever at least one row passes the filters, even on a single page ("1–1 of 1", "Page 1 of 1", both buttons disabled), so it never comes and goes while the user filters (Pagination). With no rows it gives way to the Empty state (No rows).
- **Height:** while the rows that pass the filters are more than the rows per page, the rows area is as tall as the header plus 5 rows, plus the total row when there is one; with 5 rows or fewer it is as tall as its rows, so a filter that leaves fewer rows shortens the table. The last page keeps the same height, so nothing below moves.
- **Fixed height:** with more rows per page than 5, they scroll inside the scroll container between a header that stays at the top and a total row that stays at the bottom. The scroll container: overflow-y auto.
- **Sticky header:** its cells: position sticky; top 0; z-index `zIndex-raised`; background `surface-card`; border-bottom 0.
- **Sticky total row:** its cells: position sticky; bottom 0; z-index `zIndex-raised`; background `surface-card`; border-top 0.
- **Sticky lines:** each sticky cell draws its line with ::after, so a hidden column keeps its piece of the line. content ""; position absolute; inset-inline 0; border-bottom `line-thin` solid `hairline`; visibility visible; bottom 0 in the header; top 0 and bottom auto in the total row.
