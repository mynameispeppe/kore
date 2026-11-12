# Password

**Uses:** Form fields, Tooltip.

**Purpose:** a text field for a password, with a toggle that shows or hides it and, when the user sets a new password, the requirements it must meet.

- **Hierarchy:** the label comes first (Form fields), then the box with the value, then the requirements. The label stays the focal point (The One Winner Rule); the requirements in `body-md` `mute` only guide, and a met one turns `ink`.
- **Elements:** the Password's own: show/hide toggle, requirements, requirement, requirement icon, requirement state. Other components: the label, the box and the input (Form fields), the toggle's tooltip (Tooltip).
- **Field:** `autocomplete="current-password"` on sign in, `autocomplete="new-password"` on sign up and change, so password managers fill it. It starts empty and paste is never blocked.
- **Box with the toggle:** the input stops `space-2` before the toggle: padding-inline-end `space-2`.
- **Show/hide toggle:** an inline button of the box (Inline buttons). The icon switches between view and view-off; the accessible label and the Tooltip say "Show password" or "Hide password", with no `aria-pressed` (the label gives the state). position relative. On :focus-visible: outline none, changed in 0s; the corner marks of States, following `rounded-xs`.
- **Requirements:** only with `autocomplete="new-password"`, never on sign in, and visible from the start, before the user types. Under the box, linked to the input with `aria-describedby` and announced with `aria-live="polite"`. list-style none; margin 0; padding 0; padding-inline-start `space-2`; display flex; flex-direction column; gap `space-1`.
- **Requirement:** one rule of the password per row, updated while the user types. display flex; align-items center; gap `space-2`; color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Met requirement:** color `ink`.
- **Requirement icon:** an empty circle while unmet, a check circle once met, `icon-sm`; the shape changes, so the state never depends on color alone. flex none; display block; color `mute`.
- **Met requirement icon:** color `success`.
- **Requirement state:** visually hidden text after each row, "met" or "not met", changed with the icon. position absolute !important; width `line-thin`; height `line-thin`; overflow hidden; clip-path inset(50%); white-space nowrap.
- **Error:** when the user leaves the field (moving to the toggle does not count) with a requirement unmet, the box takes its error ring (Form fields, Box in error) and the input `aria-invalid="true"`. The list is the error message, so no other text is added. An empty field errs only on submit or once a value was cleared (Form fields, Validation). The error disappears as soon as every requirement is met.
- **Unmet requirement in error:** the row and its icon: color `danger`.
