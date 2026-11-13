# Password

**Uses:** Form fields, Tooltip.

**Purpose:** a text field for a password, with a toggle that shows or hides it and, when the user sets a new password, the requirements it must meet.

- **Hierarchy:** the label comes first (Form fields), then the box with the value, then the requirements. The label stays the focal point (The One Winner Rule); the requirements in `body-md` `mute` only guide, and a met one turns `ink`.
- **Elements:** the Password's own: show/hide toggle, requirements, requirement, requirement icon, requirement state. Other components: the label, the box and the input (Form fields), the toggle's tooltip (Tooltip).
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Requirements `references/components/password/requirements.md`.
- **Field:** `autocomplete="current-password"` on sign in, `autocomplete="new-password"` on sign up and change, so password managers fill it. It starts empty and paste is never blocked.
- **Box with the toggle:** the input stops `space-2` before the toggle: padding-inline-end `space-2`.
- **Show/hide toggle:** an inline button of the box (Inline buttons). The icon switches between view and view-off; the accessible label and the Tooltip say "Show password" or "Hide password", with no `aria-pressed` (the label gives the state). position relative. On :focus-visible: outline none, changed in 0s; the corner marks of States, following `rounded-xs`.
- **Error:** when the user leaves the field (moving to the toggle does not count) with a requirement unmet, the box takes its error ring (Form fields, Box in error) and the input `aria-invalid="true"`. The list is the error message, so no other text is added. An empty field errs only on submit or once a value was cleared (Form fields, Validation). The error disappears as soon as every requirement is met.
