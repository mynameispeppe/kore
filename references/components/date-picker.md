# Date picker

**Uses:** Form fields, Popover, Button, Tooltip.

**Purpose:** a text field for a date, or a range of two dates, with a calendar in a popover.

- **Hierarchy:** the field comes first; in the calendar, the header, then the weekdays, then the days. The selected day is the focal point (The One Winner Rule): the only mark in `primary`, among days in `body-md` `ink`. The weekdays and the days of other months, in `mute`, only guide.
- **Elements:** the Date picker's own: date field, field wrap, calendar, header, view switch, view separator, corner arrow, year row, year range, day grid, weekday, day, day mark, cell grid, cell. Other components: the text field and its help and error (Form fields), the calendar button (Form fields, inline button, with a Tooltip), the popover (Popover), the month and year arrows (Button, tertiary icon, medium, with a Tooltip) and the month and year buttons (Button, tertiary, small).
- **Typing:** the field has the locale's date format as its placeholder. Typing always works: the field accepts spaces, dashes and dots and normalises the value when the user leaves it (Accept variants, keep one format). A typed date moves the calendar to its month while the user types; in a range, the start date's month when the user leaves the field. The help text states the limits.
- **Calendar button:** a calendar icon at `icon-sm` in the field's inline button, with the label "Choose from calendar", a tooltip, `aria-haspopup="dialog"` and `aria-expanded`.
- **Date field:** as wide as the calendar: max-width calc(7 × (`space-10` + `space-1`)).
- **Field wrap:** it holds the field's box and the calendar, which is placed against it. position relative; display inline-flex; inside a field, display flex.
- **Field box:** flex 1.
- **Calendar:** a Popover with the role `dialog` and a label, `space-2` under the field; seven days wide and no padding at the sides, so the corner arrows sit over the first and last weekday columns. width calc(7 × (`space-10` + `space-1`)); max-width calc(100vw − `space-8`); padding `space-3` 0; gap `space-2`.
- **Header:** the month arrows at the edges, the view switch centred between them; they change the month in every view. It rises into the padding, so the arrows sit `space-1` from the top and side edges. display flex; align-items center; justify-content space-between; margin-top calc(`space-2` × −1); padding-inline `space-1`.
- **Corner arrow:** "Previous month" and "Next month", and the arrows of the year row. border-radius `rounded-sm`: the calendar's `rounded-md` less the `space-1` gap.
- **View switch:** with `aria-live="polite"`: the month's long name ("Choose month") and the year ("Choose year"), each a button with `aria-expanded`. display flex; align-items center; gap `space-1`.
- **View switch open:** the button whose view is shown: background `surface-float-active`; pressing it again returns to the days.
- **View separator:** between the two buttons. width `line-thin`; height `space-4`; background `hairline`.
- **Day grid:** a group labelled with the month and year. On a narrow screen the days narrow to fill the calendar, at least `button-md` wide, and keep their height. display grid; grid-template-columns repeat(7, minmax(`button-md`, `space-10` + `space-1`)); justify-content space-between.
- **Weekday:** the locale's narrow names, starting on the locale's first day, Monday for `it-IT` and `en-GB`; hidden from screen readers. height `space-8`; display grid; place-items center; color `mute`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Day:** a button labelled with the full date, with no space between days: each is already a full target. The first and last weeks hold the days of the months before and after; they work as the other days. position relative; isolation isolate; width 100%; height calc(`space-10` + `space-1`); border-radius `rounded-sm`; display grid; place-items center; color `ink`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; font-variant-numeric tabular-nums.
- **Other month's day:** color `mute`.
- **Day mark:** the day's ::before, a `button-md` square centred in the day, that draws hover, today and selected. content ""; position absolute; inset-block `space-1`; inset-inline max(0, (100% − `button-md`) / 2); border-radius `rounded-sm`; z-index calc(`zIndex-raised` × −1).
- **Day hover:** with a mouse (hover: hover): the mark's background `surface-float-active`, changed in 0s.
- **Today:** `aria-current="date"`, drawn on the day's mark.
- **Today mark:** box-shadow inset 0 0 0 `line-thin` `hairline-strong`.
- **Selected:** `aria-pressed="true"`, also on hover: color `primary-on`, changed in 0s; the mark's background `primary`.
- **Inside a range:** one band between the two ends: background `surface-elevated`; border-radius 0.
- **Outside the limits:** `aria-disabled="true"`, so it still takes focus but cannot be picked; color `stone`; cursor not-allowed; no hover.
- **Cell grid:** the months and the years: three columns and four rows, in a group with a label. display grid; grid-template-columns repeat(3, 1fr).
- **Cell:** a day of the cell grid, labelled with the full month and year, or the year; its mark is the cell less `space-1` on each side. height calc(`space-10` + `space-1`); the mark's inset `space-1`.
- **Months:** the locale's short names, three letters. The month shown is selected, the current month has the today ring. Picking a month shows its days.
- **Year row:** "Previous years" and "Next years", 12 years each, with the year range centred between them. display flex; align-items center; justify-content space-between; padding-inline `space-1`.
- **Year range:** the first and the last of the 12 years. color `mute`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Years:** 12 years, starting five years before the year shown. The year shown is selected, the current year has the today ring. Picking a year shows the days of the same month in that year.
- **Picking:** a day of the month before or after also moves the calendar to its month. A single date fills the field, closes the calendar and returns focus to the field. A range takes two clicks: the first sets the start (the field shows "start – "), the second the end and closes; a day before the start starts again.
- **Focus on open:** the selected day, else today, else the first of the month. Only that day of the month shown has `tabindex="0"`; opening the month or year grid moves the focus to the selected cell.
- **Keyboard:** arrows move by a day and a week; Home and End go to the start and end of the week; Page Up and Page Down change the month; Enter and Space pick; Escape closes and returns focus to the calendar button. In the month and year grids, Left and Right move by one cell, Up and Down by three (in the years, past the edge the grid moves by 12 years); Escape returns to the days and the focus to the header button of that grid.
- **Limits:** days outside them cannot be picked. A typed date outside them shows the Form fields error when the user leaves the field, saying which limit it passes. The same error shows for a value that is not a date, with the format and an example, and for a range whose last day comes first.
