# Pagination

**Uses:** Button, Progress.

It goes under a table or a long list, after a 1px `hairline` line placed right under the last row, as wide as the table, with `space-3` (12px) of space below it.

- **Left:** the range ("1–4 of 12") in `body-md` `mute` with tabular figures, in a region with `aria-live="polite"`. It counts the rows that pass the filter, and the number of pages follows it.
- **Rows per page:** 5, with no control to change them. Another number only when the user asks for it ("show 10 workouts per page").
- **Right:** the previous and next buttons (`tertiary`, small, icon only, 20px arrow, accessible label and tooltip) with "Page 2 of 3" between them in `body-md` `ink` with tabular figures, `space-2` (8px) apart.
- **Limits:** a button is disabled on the first and the last page; when the button that has the focus becomes disabled, the focus moves to the other one.
- **No list of page numbers.** For long sets, filter and search instead of offering more pages.
- **Loading:** blocks in the same shape (Progress, Skeleton).
