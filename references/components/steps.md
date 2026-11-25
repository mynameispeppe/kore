# Steps

**Uses:** Progress, Button, Toast.

**Purpose:** the steps of a flow: the open one and the ones done.

- **Hierarchy:** the row comes first, then the step's content, then its actions. The open step's label is the focal point (The One Winner Rule): the only label in `title-sm`; the done steps follow in `label-md` `ink` with a filled circle; the steps to do only guide, in `mute`.
- **Elements:** the Steps' own: flow, row, step, line, step button, circle, step label, step content, actions. Other components: the bar that replaces the row (Progress), Back, Continue and the last step's button (Button), the success message (Toast).
- **Variant files:** read only the file of each variant that the part being built or checked contains: Vertical `references/components/steps/vertical.md`.
- **Flow:** the row, the step content and the actions together, centred. width 100%; max-width `steps`; margin-inline auto.
- **Row:** a `nav` with a label ("Order steps") holding an `ol`, one `li` per step. list-style none; margin 0; padding 0; display flex; align-items center; gap `space-2`.
- **Step:** display flex; align-items center; gap `space-2`; flex none.
- **Line:** between two steps, it fills the space; `aria-hidden="true"`. flex 1 1 `space-4`; min-width `space-4`; height 0; border-top `line-thin` solid `hairline`.
- **Step button:** the circle and the label; its hit area is at least 44px tall. position relative; display inline-flex; align-items center; gap `space-2`; min-height calc(`space-10` + `space-1`); color `ink`.
- **Circle:** flex none; width `space-6`; height `space-6`; border-radius `rounded-full`; corner-shape round; display grid; place-items center; font-family `label-sm`; font-size `label-sm`; font-weight `label-sm`; line-height `label-sm`; letter-spacing `label-sm`; font-variant-numeric tabular-nums.
- **Step label:** font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Done:** a link that reopens the step; visually hidden text ", done". The step button: text-decoration none. The circle holds the 16px Hugeicons `Tick02`: background `ink`; color `canvas`.
- **Done hover:** on mouse hover (hover: hover), the label: text-decoration underline `line-thin`; text-underline-offset `space-1`.
- **Done focus:** on :focus-visible the step button: outline none; the label: text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s (the link focus underline, States).
- **Open:** not a link; `aria-current="step"`. The circle holds its number: box-shadow inset 0 0 0 `line-thin` `ink`; color `ink`. The label: font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **To do:** not a link, because the flow goes in order; visually hidden text ", to do". The circle holds its number: box-shadow inset 0 0 0 `line-thin` `hairline-medium`; color `mute`. The label: color `mute`.
- **Narrow container:** when the row does not fit its container, the row: display none; the Progress bar takes its place: display flex; the step's name in the task name, "Step 2 of 4" in the value; `role="progressbar"` with values from 1 to the number of steps.
- **Step content:** under the row or the bar, with its actions. display flex; flex-direction column; gap `space-6`. Its first element takes focus (`tabindex="-1"`) once it enters: outline none. What the user typed stays when they go back.
- **Step change:** on every step change the content and its actions move with the Segmented control's View motion, forward to a later step and back to an earlier one, while the row or the bar stays still.
- **Actions:** a secondary Button "Back" at the start (not on the first step) and the primary Button at the end: "Continue" on the middle steps, on the last a verb and its object ("Place order"). The primary: margin-inline-start auto.
- **Continue:** checks the step's fields as a submit does (Form fields) and moves on only when they are valid.
- **Last step:** the primary shows its spinner (Button, Loading), then a success toast.
