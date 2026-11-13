**Child list**

- **Trailing:** on a row that opens in place, an `icon-sm` chevron at the end, pointing down when closed and up when open. display flex; color `mute`.
- **Child list:** the children of a row, and the options of a Settings row, open in place under it and start closed; their text lines up with the parent's label. They open and close as the Accordion's answer: display grid; grid-template-rows 0fr; transition grid-template-rows `duration-base` `ease-in`; open: grid-template-rows 1fr; transition-timing-function `ease-out`. position relative; margin-block-start calc(−`space-2`), which takes back the group's gap while closed; margin-inline-start calc(`space-3` + `icon-md` / 2), the centre of the row icon; border-inline-start `line-thin` solid transparent.
- **Guide:** the child list's ::after: a vertical `hairline` line at its start side, from the top of the first child's text to the bottom of the last one's. content ""; position absolute; inset-inline-start −`line-thin`; width `line-thin`; inset-block calc(`space-2` + (`space-10` − the line-height of `body-md`) / 2) calc((`space-10` − the line-height of `body-md`) / 2); background `hairline`.
- **Child list inner:** min-height 0; overflow hidden; opacity 0; transition opacity `duration-fast` `ease-in`; open: opacity 1; transition-timing-function `ease-out`. display flex; flex-direction column; gap `space-2`; padding-inline-start `space-3`. Its ::before gives back the group's gap when open: content "".
- **Child row:** padding-inline `space-3`.
- **Child list reduced motion:** the child list: transition 0s; its inner only fades.
- **Rail child lists:** display none. A row with children or options, and the More row, expand the panel; a row with children or options also opens in place, with the focus on it.
