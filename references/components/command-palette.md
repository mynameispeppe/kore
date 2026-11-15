# Command palette

**Uses:** Menu, Overlay rules, Toast.

**Purpose:** a search over the product's actions and pages, opened from the keyboard (Usability 7).

- **Hierarchy:** the search comes first, then the results, then the key hints. The search input is the focal point (The One Winner Rule): `body-lg` in `ink`, the largest type of the palette. The highlighted result follows, the only one with a fill; the group titles, shortcuts and key hints, in `label-md` and `mute`, only guide.
- **Elements:** the Command palette's own: opening hint, palette, search, search input, separator, results, group, status, no-results note, no-results text, search term, key hints, hint, key. Other components: the opening button (Button, tertiary), the results' items, group titles and separators (Menu), the search icon (the Hugeicons `Search01`, `icon-sm`, `mute`) and the toast (Toast).
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Shortcuts `references/components/command-palette/shortcuts.md`.
- **Opening:** ⌘K on Mac, Ctrl+K elsewhere, and a button that says so, showing only the current platform's keys. The same keys close it again.
- **Opening hint:** beside the opening button, "or press" and the keys in a key. font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Palette:** a modal `<dialog>` with an accessible label. position fixed; inset `space-12` 0 auto 0; margin 0 auto; width min(`dialog`, 100vw − `space-8`); padding 0; border 0; border-radius `rounded-md`; background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; color `ink`.
- **Scrim:** the palette's ::backdrop: background `scrim`.
- **Palette below sm:** below `sm`: top `space-4`.
- **Search:** display flex; align-items center; gap `space-2`; height calc(`space-12` + `space-2`); padding 0 `space-5`; color `mute`. The icon starts `space-5` from the palette's edge and the text `space-5` + `icon-sm` + `space-2`, the same as the results' icons and labels.
- **Search input:** a `combobox` with `aria-expanded`, `aria-controls` and `aria-activedescendant`; focus stays in it. flex 1; min-width 0; height 100%; border 0; background none; outline none; color `ink`; font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`.
- **Search placeholder:** color `mute`.
- **Separator:** under the search. height 0; border-top `line-thin` solid `hairline`.
- **Results:** a `listbox` holding the Menu's items, group titles and separators; it scrolls past its max-height. position static; padding `space-1` `space-2`; animation 0s; outline 0; border-radius 0 0 `rounded-md` `rounded-md`; max-height calc(`space-48` + `space-32`); min-width 0; width auto.
- **Group:** a `group` with `aria-labelledby` pointing to its title. display flex; flex-direction column.
- **Group title:** padding-top `space-2`; padding-inline `space-3`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Result:** padding 0 `space-3`. One result is highlighted at a time: the first, then the one the arrows or a moving mouse reach. Enter runs it.
- **Result hover:** a result not highlighted: background none, changed in 0s, so hover adds no second highlight.
- **Empty search:** only the actions show; the pages show once the user types.
- **Key hints:** under the results: "↑↓ to navigate", "↵ to select", "esc to close". Hidden from screen readers. display flex; flex-wrap wrap; gap `space-4`; padding `space-2` `space-5`; border-top `line-thin` solid `hairline`; color `mute`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Key hints without hover:** on devices without hover (hover: none): display none.
- **Hint:** a key, then its words. display inline-flex; align-items center; gap `space-2`.
- **Status:** a visually hidden `role="status"` that says how many results there are: "<count> results". position absolute; width `line-thin`; height `line-thin`; overflow hidden; clip-path inset(50%); white-space nowrap.
- **No-results note:** outside the `listbox`, shown when nothing matches. padding `space-4` `space-2`; text-align center.
- **No-results text:** "No command for “…”", then "Try another word.". font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Search term:** the typed text inside the quotes. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Running a command:** closes the palette, then does its work. A page goes to its title, which takes focus. An action whose result is not visible on screen confirms with a toast that names the result in the past tense.
- **Closing:** Escape and a click on the scrim close the palette and return focus where it was.
- **Palette open:** opacity from 0 and scale from 0.98 to 1: animation `duration-base` `ease-out`.
- **Palette closing:** it fades to 0 and scales to 0.98 in `duration-fast` with `ease-in`, and stays so until it is hidden.
- **Reduced motion:** the palette only fades: animation opacity `duration-base` `ease-out` on open, `duration-fast` `ease-in` forwards on close.
