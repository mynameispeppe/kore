**Field and button**

- **Popover with a field:** always as wide as its maximum, so the field is the same on every page: width `popover`.
- **Field row:** the popover holds at most one field (Form fields) and one secondary default Button, side by side, centred on each other, `space-3` below the title. With no field, the button sits `space-3` below the explanation, in place of the link. display flex; align-items center; gap `space-2`; margin-top calc(`space-3` − `space-1`). The field's box: flex 1; min-width 0.
- **Copy result:** after the action succeeds, the button shows an `icon-sm` check and the result in the past tense in `success` for 3 seconds, then goes back; the popover stays open. Its label is `aria-live="polite"`, so the change is announced. color `success`; the check: width `icon-sm`; height `icon-sm`.
