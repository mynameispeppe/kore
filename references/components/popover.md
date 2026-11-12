# Popover

**Uses:** Overlay rules, Button, Tooltip, Form fields.

**Purpose:** short content that opens from a button, next to it: a figure and what it means, an explanation, or one field with one action.

- **Hierarchy:** as in a card (Text hierarchy): the key content first, a figure or a short title in `title-md` `ink`, then the explanation in `body-md` `body`, then at most one link or one button. The figure or the title is the focal point (The One Winner Rule). It never repeats the trigger's text and has no label above the figure.
- **Elements:** the Popover's own: wrapper, popover, arrow, arrow fill, figure, unit, title, explanation, value in the text, link, field row, copy result. Other components: the trigger and the action button (Button), the trigger's tooltip (Tooltip), the field (Form fields).
- **Trigger:** a tertiary Button: icon-only with its Tooltip next to the value it explains, or labeled when it stands alone. It has `aria-haspopup="dialog"`, `aria-expanded` and `aria-controls` pointing to the popover, and toggles it. On :focus-visible: outline none, changed in 0s; the corner marks of States (Button, Focus).
- **Wrapper:** the trigger and its popover, so the popover is placed against its trigger. position relative; display inline-flex.
- **Popover:** a `dialog` with a label, drawn inside its edge, no shadow, `space-2` below its trigger. It is placed so the arrow points at the trigger's centre and stays `space-2` inside the screen: when it would cross an edge it slides along that edge (the slide) and the arrow slides back by the same amount. position absolute; top calc(100% + `space-2`); inset-inline-start calc(half the trigger's width − `space-6` + the slide); z-index `zIndex-dropdown`; width max-content (the CSS keyword, not the token); max-width `popover`; background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; border-radius `rounded-md`; padding `space-3`; display flex; flex-direction column; gap `space-1`.
- **Popover above:** only when there is no room below and there is room above, as Menu: top auto; bottom calc(100% + `space-2`).
- **Popover open:** opacity from 0 and a move down by `space-1`: animation `duration-base` `ease-out`, as Menu.
- **Reduced motion:** the popover only fades in: animation-name fadeIn.
- **Popover with a field:** always as wide as its maximum, so the field is the same on every page: width `popover`.
- **Arrow:** the popover's ::before, the hairline edge of the arrow that fills the gap to the trigger, its centre `space-6` from the popover's start edge, its tip rounded `rounded-xs`, no line across its base. content ""; position absolute; inset-inline-start calc(`space-6` − `space-2` − the slide); width `space-4`; height `space-2`; top calc(−`space-2`); clip-path path() of that triangle (path() takes px only); background `hairline`.
- **Arrow fill:** the popover's ::after, the arrow's shape moved `line-thin` × √2 inward, so its slanted edge shows `line-thin` of the hairline and it covers the popover's edge under its base. The same declarations as the arrow, then: background `surface-float`; top calc(−`space-2` + `line-thin` × √2).
- **Arrow above:** on a popover above, the arrow and its fill point down: top auto; bottom calc(−`space-2`), and for the fill calc(−`space-2` + `line-thin` × √2); the triangle's clip-path flipped.
- **Figure:** color `ink`; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; font-variant-numeric tabular-nums.
- **Unit:** after the figure. color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Title:** a short title in place of the figure. color `ink`; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`.
- **Explanation:** `space-1` below the figure or the title. color `body`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Value in the text:** a number inside the explanation. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; font-variant-numeric tabular-nums.
- **Link:** at most one, `space-3` below the explanation. margin-top calc(`space-3` − `space-1`); color `link`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **No corner buttons:** Escape and a click outside already close it.
- **Field row:** the popover holds at most one field (Form fields) and one secondary default Button, side by side, centred on each other, `space-3` below the title. With no field, the button sits `space-3` below the explanation, in place of the link. display flex; align-items center; gap `space-2`; margin-top calc(`space-3` − `space-1`). The field's box: flex 1; min-width 0.
- **Copy result:** after the action succeeds, the button shows an `icon-sm` check and the result in the past tense in `success` for 3 seconds, then goes back; the popover stays open. Its label is `aria-live="polite"`, so the change is announced. color `success`; the check: width `icon-sm`; height `icon-sm`.
- **Focus:** it moves into the popover on open. Escape closes it and returns focus to the trigger; a click outside closes it and leaves focus where the click went.
