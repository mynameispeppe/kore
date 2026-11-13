# Checkbox and radio

**Uses:** Form fields.

**Purpose:** a checkbox lets the user pick several options; a radio, one option from a group.

- **Hierarchy:** the row reads as one unit, the control before its label. A checked control is the focal point of the row (The One Winner Rule): `primary` fill against the `surface-deep` of the controls left empty; the label in `body-md` `ink`.
- **Elements:** the Checkbox and radio's own: row, input, control, radio control, mark, check icon, minus icon, dot, icon. Other components: the group's fieldset, its legend and its error message (Form fields). Checkbox, radio, error and disabled are variants of the row, not elements.
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Indeterminate `references/components/checkbox-radio/indeterminate.md`.
- **Row:** the whole row (control and label) is clickable; rows touch, with no space between them. position relative; display flex; align-items center; gap `space-3`; min-height calc(`space-10` + `space-1`); cursor pointer; color `ink`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Input:** the native input, invisible over the control, so the browser keeps its keyboard and its accessible name. position absolute; opacity 0; width `checkbox`; height `checkbox`; margin 0; cursor pointer.
- **Control:** the checkbox's square. position relative; flex none; display grid; place-items center; width `checkbox`; height `checkbox`; border-radius `rounded-checkbox`; background `surface-deep`; box-shadow inset 0 0 0 `line-thin` `hairline-strong`; color `primary-on`; transition background-color `duration-base` `ease-in-out`.
- **Radio control:** a circle. border-radius `rounded-full`; corner-shape round; its focus marks follow a radius of `checkbox` / 2.
- **Mark:** the check icon, the minus icon and the dot share the control's one cell. grid-area 1/1.
- **Check icon:** the Hugeicons `Tick02`, `icon-xs`. Hidden: clip-path inset(0 100% 0 0); transition clip-path `duration-fast` `ease-in`, so unchecking hides it from right to left.
- **Dot:** width `space-2`; height `space-2`; border-radius `rounded-full`; corner-shape round; background `primary-on`; scale 0; transition scale `duration-fast` `ease-in`.
- **Icon:** flex none; display block.
- **Checked control:** checked or indeterminate. background `primary`; box-shadow none.
- **Checked icon:** the check icon of a checked control and the minus icon of an indeterminate one, revealed from left to right by a clip, never by editing the icon: clip-path inset(0); transition clip-path `duration-base` `ease-out` `duration-instant`, so it starts after `duration-instant`.
- **Checked dot:** scale 1; transition scale `duration-base` `ease-out`.
- **Hover:** box-shadow inset 0 0 0 `line-thin` `mute` on the control of an unchecked row, changed in 0s. The control never scales on hover or press.
- **Checked hover:** background `primary-pressed`, in the control's transition (`duration-base`, `ease-in-out`).
- **Reduced motion:** transition 0s !important on the control and its marks.
- **Focus:** on :focus-visible of the input the control takes the four-corner marks of States, following `rounded-checkbox`, changed in 0s: content ""; position absolute; inset −(`line-thick` + the mark's width); pointer-events none; border the mark's width solid `focus-ring`; border-radius the control's radius + `line-thick` + the mark's width; mask linear-gradient, one square per corner.
- **Groups:** a group sits in a `fieldset` with a `legend` styled as a field label (Form fields); an error message sits right under the last row.
- **Error:** box-shadow inset 0 0 0 `line-thin` `danger` on the control; a message in `danger` under the control or the group, linked (`aria-invalid`, `aria-describedby`), as in Form fields.
- **Disabled:** color `stone`; cursor not-allowed.
- **Disabled control:** background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; on hover the same.
- **Disabled checked control:** background `stone`.
