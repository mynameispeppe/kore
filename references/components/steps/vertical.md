**Vertical variant**

- **Vertical:** the steps in a column at any width, with no Progress bar. The row: flex-direction column; align-items stretch; gap 0. Each step: display block; position relative. Each step but the last: padding-bottom `space-6`.
- **Vertical line:** each step but the last, ::before, at the circle's centre, from the bottom of the step button to the next step, beside the open content too. content ""; position absolute; top calc(`space-10` + `space-1`); bottom 0; inset-inline-start calc((`space-6` − `line-thin`) / 2); border-inline-start `line-thin` solid `hairline`.
- **Vertical content:** under the open step's button, indented to its label. padding-inline-start calc(`space-6` + `space-2`).
- **Vertical actions:** "Back" then the primary, both at the start. justify-content flex-start; gap `space-2`. The primary: margin-inline-start 0.
- **Vertical step change:** the old content closes and the new one opens at the same time, height and opacity, in `duration-base` with `ease-out`; under reduced motion they swap at once.
