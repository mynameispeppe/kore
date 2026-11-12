# Select

**Uses:** Form fields, Menu.

**Purpose:** a field that opens a list of options and shows the one the user picks.

**Native:** a custom menu, never the browser's native dropdown.

- **Hierarchy:** the label comes first (Form fields), then the trigger with the value, then the menu while it is open. The label stays the focal point (The One Winner Rule); the value follows in `body-lg` `ink`; the placeholder and the arrow in `mute` only guide; in the open menu the selected option is in `title-sm` (Menu).
- **Elements:** the Select's own: wrapper, trigger, value, placeholder, arrow, placeholder option. Other components: the label, the box, the help and the error (Form fields), the menu, its options and their check (Menu).
- **Wrapper:** the Menu's wrapper around the trigger and its menu. position relative; display inline-flex. Inside a field it takes the field's width: display flex; the trigger: flex 1.
- **Trigger:** a Form fields box that is a button, so it takes every state of Form fields (hover, error with its message). position relative; width 100%; cursor pointer; text-align start. On :focus-visible: outline none, changed in 0s; the corner marks of States, following `rounded-md`.
- **Value:** the chosen option's text, as the input of Form fields (Input). display flex; align-items center.
- **Placeholder:** the value until an option is chosen, with the placeholder option's text. color `mute`.
- **Arrow:** the `icon-sm` Hugeicons down arrow on the end side of the trigger. flex none; display block; margin-inline-end `space-3`; color `mute`; transition transform `duration-base` `ease-out`.
- **Open arrow:** while the menu is open: transform rotate(`flip`).
- **Disabled:** the trigger has the disabled attribute. background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; cursor not-allowed.
- **Disabled value and arrow:** color `stone`.
- **Read-only:** a read-only Form field (Box read-only) with the chosen value and no arrow; the menu never opens.
- **Menu:** the standard Menu, under the trigger and never narrower than it. The selected option has the check on the right (Selected option in Menu).
- **Placeholder option:** the first option, with the trigger's placeholder text. color `mute`. Choosing it clears the value; a required select then shows its error.
- **Validation:** a required select shows its error when the menu closes without a pick (Validation in Form fields).
- **Keyboard:** focus stays on the trigger. Closed: Enter, Space, ↓ or ↑ open the menu on the selected option. Open: ↑ ↓ Home End move, Enter or Space selects, Escape, Tab and a click outside close. Typing a letter moves to the next option that starts with it.
- **Roles:** the trigger is a select-only `combobox` with `aria-haspopup="listbox"`, `aria-expanded` and `aria-activedescendant`; the menu is a `listbox` of `option` rows.
