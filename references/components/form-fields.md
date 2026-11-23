# Form fields

**Uses:** Button, Menu.

**Purpose:** text input, textarea and select share one box, with a label above it and a help text or an error below it.

- **Hierarchy:** the label comes first, then the box with the value, then the help or the error. The label is the focal point (The One Winner Rule): `label-lg` in `ink`, read before the value in `body-lg` `ink`; the help in `body-md` `mute` only explains; an error in `danger` takes the help's place.
- **Elements:** the Form fields' own: field, label, optional mark, required mark, box, hit area, input, placeholder, textarea box, textarea, leading icon, unit, help, error, combobox status, combobox wrapper. Other components: the Combobox's menu (Menu) and the password toggle (Button).
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Textarea `references/components/form-fields/textarea.md`, Leading icon `references/components/form-fields/leading-icon.md`, Unit `references/components/form-fields/unit.md`.
- **Field:** the label, the box, then the help text or the error. Every field has the same width inside and outside a form; a component that sets its own width overrides it, as File upload and the Table's search field do. display flex; flex-direction column; gap `space-2`; width 100%; max-width `field-max`.
- **Form:** a form is at most `panel` wide; a control outside a form (switch row, slider) at most `field-max`.
- **Label:** above the box, a `<label>` tied to the input. color `ink`; font-family `label-lg`; font-size `label-lg`; font-weight `label-lg`; line-height `label-lg`; letter-spacing `label-lg`.
- **Optional mark:** "(optional)" after the label when the field is optional. color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Required mark:** " *" after the label when the field is required, in the label's type and color, hidden from screen readers (`aria-hidden="true"`); the input has `aria-required="true"`. While the field is in error: color `danger`.
- **Box:** the field's edge (below 3:1 by choice: the visible label identifies the field). position relative; display flex; align-items center; height `field`; border-radius `rounded-md`; background `surface-deep`; box-shadow inset 0 0 0 `line-thin` `hairline-medium`; outline `line-thin` solid transparent, for forced colors; outline-offset −`line-thin`; transition box-shadow `duration-fast` `ease-out`.
- **Box hover:** box-shadow inset 0 0 0 `line-thin` `mute`.
- **Box focus:** the focus marks of States go on the box while its input has focus.
- **Box in error:** at rest and on hover: box-shadow inset 0 0 0 `line-thin` `danger`.
- **Box disabled:** background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; the ring stays on hover.
- **Box read-only:** background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline-medium`; the ring stays on hover. The value stays selectable.
- **Hit area:** the box's ::before, so the field's hit area reaches the Touch targets height. content ""; position absolute; inset calc(−`line-thick`) 0.
- **Input:** above the hit area, so it takes the click; centred by the box. position relative; flex 1; min-width 0; height `button-lg`; border 0; background none; outline none; padding 0 `space-3`; color `ink`; font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`.
- **Input disabled:** color `stone`; cursor not-allowed.
- **Disabled label:** color `stone`. The help keeps `mute`: it says why the field is disabled.
- **Placeholder:** only as an example, never as the label. color `mute`; opacity 1.
- **Help:** margin-top calc(`space-1` − `space-2`); color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`. Under the field's edge.
- **Error:** margin-top calc(`space-1` − `space-2`); color `danger`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`. In place of the help, linked to the input (`aria-invalid`, `aria-describedby`); an icon only when the message alone would not read as an error (Text hierarchy #7).
- **Combobox status:** a visually hidden `role="status"` that announces the results. position absolute; width `line-thin`; height `line-thin`; overflow hidden; clip-path inset(50%); white-space nowrap.
- **Combobox wrapper:** the menu's wrapper takes the field's width: display flex; its box: flex 1.
- **Validation:** runs when the user leaves the field, and the error disappears as soon as the value is valid. An empty required field shows its error only on submit, or when the user clears a value.
- **One column:** fields stack one per row, at every width. Only the parts of one value share a row (day, month and year of a date; month and year of an expiry).
- **Keyboard type:** each field uses the type of its value (`type="email"`, `type="tel"`, `type="url"`, `type="search"`). Values made of digits that are not quantities (card number, code, postal code) use `type="text"` with `inputmode="numeric"`; amounts use `inputmode="decimal"`.
- **Submitting with errors:** submitting validates every field. Each invalid field shows its error and focus moves to the first one, scrolled into view. A visually hidden `aria-live="assertive"` region announces the number of fields to fix, in the page's language. The submit button is never disabled while waiting for a valid form; it is disabled only while submitting (Button, Loading).
