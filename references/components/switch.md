# Switch

**Uses:** Button.

**Purpose:** turns a setting on or off and applies the change at once.

- **Use:** a switch always sits next to its visible label and applies the change immediately; use a checkbox when the change waits for a Save.
- **Hierarchy:** the label comes first, the switch after it. An on switch is the focal point of the row (The One Winner Rule): the `primary` track against the `surface-elevated` of the switches left off; the label in `body-md` `ink` names it.
- **Elements:** the Switch's own: row, label, track, hit area, knob. Other components: the spinner in the knob while saving (Button, Loading).
- **Row:** the label, then the switch right after it; rows touch, with no space between them; the label is not clickable. display flex; align-items center; gap `space-4`; min-height calc(`space-10` + `space-1`); max-width `field-max`; color `ink`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Label:** a text element tied to the switch with `aria-labelledby`; the switch is a `<button role="switch">` with `aria-checked`.
- **Track:** position relative; flex none; width `space-10`; height `space-6`; border-radius `rounded-full`; corner-shape round; padding `space-1`; background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline-strong`; display flex; align-items center; transition background-color `duration-fast` `ease-out`, box-shadow `duration-fast` `ease-out`.
- **Hit area:** the track's ::before, 44px tall and wide. content ""; position absolute; inset calc((`space-6` − (`space-10` + `space-1`)) / 2) calc((`space-10` − (`space-10` + `space-1`)) / 2).
- **Knob:** width `space-4`; height `space-4`; border-radius `rounded-full`; corner-shape round; background `ink`; display grid; place-items center; transition transform `duration-fast` `ease-out`.
- **Off hover:** box-shadow inset 0 0 0 `line-thin` `mute`.
- **On:** never green: green means success. The track: background `primary`; box-shadow none. The knob: transform translateX(`space-4`); background `primary-on`.
- **On hover:** the track: background `primary-pressed`.
- **Focus:** the corner marks of States around the whole track. On :focus-visible: outline none, changed in 0s.
- **Disabled:** the track: background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; cursor not-allowed. The knob: background `stone`. The row: color `stone`.
- **Disabled on:** the track: background `stone`; box-shadow none. The knob: background `surface-elevated`.
- **Loading:** while the change is saved, the switch has `aria-busy="true"` and ignores further clicks; the knob holds the 16px spinner (Button, Loading), turning in `duration-spin`: background none; color `ink`, or `primary-on` when on. If saving fails, the switch returns to its previous position with an error message.
- **Reduced motion:** the knob: transition 0s.
