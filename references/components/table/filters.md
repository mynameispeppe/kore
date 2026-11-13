**Filters**

- **Filters:** a filter field (Form fields) under the title of each sortable column, not shown while the table has no data. It is labelled by its column title and a visually hidden "filter" (`aria-labelledby`), so it reads "Name filter". It filters while the user types, and focus and caret stay in it: a row passes when the column's cell, as shown on screen, contains the text, ignoring case and accents; filters combine; the table returns to the first page.
- **Fixed layout:** with filters, the columns share the width equally (selection and actions aside) and never move while the rows change. The table: table-layout fixed.
- **Filter field:** width `space-32`; max-width 100%; margin-top `space-2`.
- **Filter box:** height `button-sm`; align-items flex-start. Its overlay (::before): inset 0 0 calc(`button-sm` − `button-lg`).
- **Filter input:** `type="search"`, placeholder "Filter…"; its hit area on the box's top, its text centred in the box. height `button-lg`; padding-block 0 calc(`button-lg` − `button-sm`); padding-inline `space-2`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Filter clear:** a field with text shows the inline button of Shapes at the end, with the X and a Tooltip, label "Clear Name filter"; it empties its field and focus stays in it. width `space-4`; height `space-4`. Its hit area (::before): inset calc((`space-4` − (`space-10` + `space-1`)) / 2). Its wrapper: align-self center; display flex.
- **Header with filters:** each title sits where it sits in a header without filters, and the field's hit area stays inside the header. Every header cell: vertical-align top; padding-block calc((`space-10` − `icon-sm`) / 2) calc(`button-lg` − `button-sm`).
- **Header cell without a filter:** on the filter's line. vertical-align bottom; line-height `button-sm`. The select-all box: min-height `button-sm`.
- **Sort hit area with filters:** it runs up and only into the `space-2` gap below, so it never overlaps the field's. inset calc(`icon-sm` + `space-2` − `button-lg`) calc(`space-1` × −1) calc(`space-2` × −1).
- **No match:** when the filters match nothing, in a `role="status"` region: "No workouts match these filters", "Check the spelling or try another word.", a tertiary Button "Clear filters" that empties every field and moves the focus to the first one.
