# Number stepper

**Uses:** Form fields, Tooltip.

**Purpose:** a field for an exact number that the user types or changes one step at a time with − and +.

- **Hierarchy:** the field's label comes first (Form fields), then the stepper, then the help. Inside the stepper the value is the focal point (The One Winner Rule): `body-lg` `ink` with tabular figures; the − and + icons in `mute` only act.
- **Elements:** the Number stepper's own: stepper, step button, hit area, icon, value. Other components: the label and the help (Form fields), the step buttons' tooltips (Tooltip).
- **Stepper:** the box, with − on the left, the value, + on the right. The focus marks of States go around it while the value has focus, following `rounded-md`. position relative; display flex; align-items center; width calc(`space-32` + `space-8`); height `space-12`; padding `space-2`; border-radius `rounded-md`; background `surface-deep`; box-shadow inset 0 0 0 `line-thin` `hairline-medium`; transition box-shadow `duration-fast` `ease-out`.
- **Stepper hover:** box-shadow inset 0 0 0 `line-thin` `mute`.
- **Step button:** − and +, out of the Tab order (`tabindex="-1"`), each with an accessible label and a Tooltip naming the action and the step with its unit. A press keeps the focus in the value. position relative; width `button-sm`; height `button-sm`; border-radius `rounded-xs`; display grid; place-items center; color `mute`.
- **Step button hover:** color `ink`, changed in 0s.
- **Step button disabled:** − at the minimum, + at the maximum. color `stone`; cursor not-allowed.
- **Hit area:** the step button's ::before, calc(`space-10` + `space-1`) square, centred on the button. content ""; position absolute; inset calc((`button-sm` − (`space-10` + `space-1`)) / 2).
- **Icon:** the − and + icons, `icon-sm`. flex none; display block.
- **Value:** a text input (`type="text"`, `inputmode="numeric"`) as tall as the stepper, so a click on the stepper's body puts the caret in it. position relative; flex 1; min-width 0; align-self stretch; height auto; margin-block calc(−`space-2`); border 0; background none; padding 0; outline none; text-align center; color `ink`; font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`; font-variant-numeric tabular-nums.
- **Unit and limits:** the label names the unit and the help states the step and the limits with the unit, before use.
- **Typed value:** on Enter or when the value loses focus it snaps to the step and the limits. Only the digits count, so a thousands separator in either form is ignored; an empty value keeps the previous one. The value shows the page language's thousands separator.
- **Keyboard:** ↑ and ↓ change the value by one step; Home and End go to the limits.
- **Roles:** the value is a `spinbutton` with `aria-valuemin`, `aria-valuemax`, `aria-valuenow` and an `aria-valuetext` made of the value, a space and its unit.
