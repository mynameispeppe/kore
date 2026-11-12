# Combobox

**Uses:** Form fields, Menu, Tooltip, Button.

**Purpose:** a text field that filters a long list of options while the user types, and fills the field with the one they pick.

- **Hierarchy:** the label comes first (Form fields), then the box with the typed text, then the menu while it is open. The label stays the focal point (The One Winner Rule); the typed text follows in `body-lg` `ink`; the search icon, the placeholder and the clear button in `mute` only guide; in the menu the matched text is in `title-sm` (Menu).
- **Elements:** the Combobox's own: typed text, loading note, retry row. Other components: the label, the box, the input, the leading icon, the clear button (an inline button of the box), the combobox status and the combobox wrapper (Form fields), the clear button's tooltip (Tooltip), the menu, its options, the matched text and the no-match note (Menu), the spinner and the Try again button (Button).
- **Field:** a Form field with the search icon as its leading icon (Leading icon). The input: `type="text"`; `autocomplete="off"`.
- **Filter:** the options whose label contains the typed text, ignoring case and accents: "cafe" finds "Café". The list updates on every keystroke.
- **Matched text:** in each option, the part that matches the typed text (Matched text in Menu).
- **Clear button:** with a value in the field, an inline button at the end of the box (Inline buttons in Shapes): the Hugeicons `Cancel01` at `icon-sm`, the accessible label and the Tooltip "Clear search". It empties the field, keeps focus in it and leaves the menu open.
- **Menu:** the standard Menu under the field, as wide as it (Combobox wrapper in Form fields). It opens when the field takes focus.
- **Empty field:** a local list shows all its options; the menu scrolls past its max-height (Menu).
- **No match:** the no-match note (Menu) with two lines: what found nothing, with the typed text, then what to do (for example "No cities match “rmoe”" and "Check the spelling or add it as a new city.").
- **Typed text:** the typed text inside the no-match line. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Async hint:** with options from a server, on an empty field the note holds one line, what to type (for example "Type to search cities.").
- **Loading note:** as soon as the user types, the note shows the Spinner (Button) and "Searching…", side by side. display inline-flex; align-items center; justify-content center; gap `space-2`.
- **Request:** it leaves after a pause in typing of `delay-input`; only the latest request's answer is shown, as options or as the no-match note.
- **Failed request:** the note with two lines, what failed and what to do (for example "Couldn't load the cities." and "Try again in a moment."), then the retry row.
- **Retry row:** a small tertiary Button "Try again", `space-2` below the two lines: the note's gap `space-1` plus margin-top `space-1`. It moves focus to the field and repeats the request.
- **Keyboard:** focus stays in the field. ↓ and ↑ open the menu and move, stopping at the first and the last option; Enter picks; Escape and a click outside close. The menu closes when focus leaves the field, its clear button and the menu; Tab reaches the Try again button. After a pick the menu stays closed.
- **Roles:** the input is a `combobox` with `aria-expanded`, `aria-controls` on the `listbox`, `aria-autocomplete="list"` and `aria-activedescendant` on the highlighted option, which has `aria-selected="true"`. The `listbox` holds only `option` and `group` (a group with `aria-labelledby` on its title).
- **Status:** the combobox status (Form fields) announces the number of results ("1 city", "12 cities"), the two no-match lines, "Searching…" or the two error lines.
