# Sheet

**Uses:** Button, Tooltip, Overlay rules.

**Purpose:** a modal panel that slides in from the side of the screen, or from the bottom on phones, and holds a task that needs more room than a dialog: filters, settings, a form.

- **Hierarchy:** the header comes first, then the body, then the actions. The title is the focal point (The One Winner Rule): `title-lg` in `ink`, read before the body and the buttons; the separators only separate.
- **Elements:** the Sheet's own: sheet, scrim, header, title, separator, separator line, body, actions. Other components: the close button (Button, tertiary icon, small, with a Tooltip), the action buttons (Button) and the controls of the body (each its own component).
- **Markup:** the platform's modal element where it exists (`<dialog>` on the web), named by its title (`aria-labelledby`).
- **Sheet:** from `md`, on the side of the screen where the button that opens it sits: a button in the left half of the screen opens it from the left, one in the right half from the right. position fixed; margin 0; padding 0; border 0; background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; color `ink`; inset `space-2` `space-2` `space-2` auto; width `panel`; max-width calc(100vw − `space-4`); height calc(100dvh − `space-4`); max-height none; border-radius `rounded-xl`; display none; flex-direction column. (replaced in: glassmorphism)
- **Scrim:** the sheet's ::backdrop: background `scrim`.
- **Sheet on the left:** inset `space-2` auto `space-2` `space-2`.
- **Open sheet:** display flex, changed in 0s.
- **Sheet open:** it slides in from its side, from past the screen's edge: transform from translateX(calc(100% + `space-2`)), × −1 on the left; animation `duration-slow` `ease-out`.
- **Sheet closing:** it slides back out to its side, the same distance, in `duration-base` with `ease-in`, and stays so until it is hidden.
- **Header:** the title, then the close button as a corner action (Shapes). display flex; align-items flex-start; gap `space-2`; padding `space-4` `space-4` 0 `space-6`; min-height `space-12`.
- **Title:** an `h2` that names the sheet. Its first line is centred on the close button. flex 1; min-width 0; margin-top calc((`button-sm` − the line-height of `title-lg`) / 2); color `ink`; font-family `title-lg`; font-size `title-lg`; font-weight `title-lg`; line-height `title-lg`; letter-spacing `title-lg`.
- **Separator:** one under the header and one above the actions; a sheet without actions has only the first. It sits in the middle of the `space-6` between two parts, lined up with the body's text, and takes no space of its own. position relative; height 0; margin `space-3` `space-6`.
- **Separator line:** the separator's ::before. content ""; position absolute; inset-inline 0; top 0; border-top `line-thin` solid `hairline`.
- **Body:** what the sheet holds, the only part that scrolls; the header and the actions stay in place. Its parts are `space-6` apart. flex 1; overflow auto; padding 0 `space-6`; display flex; flex-direction column; gap `space-6`.
- **Body without actions:** when it is the sheet's last part: padding-bottom `space-6`.
- **Actions:** right-aligned, confirm last, the other action tertiary. They sit `space-3` from the sheet's lower edge and sides (the `rounded-xl` corner less the button's `rounded-md`), as in the dialog. display flex; justify-content flex-end; gap `space-2`; padding 0 `space-3` `space-3`.
- **Phones:** below `md`, every sheet enters from the bottom edge, at most 85% of the screen's height, over the bottom safe area. inset auto 0 0 0; width 100%; max-width 100%; height auto; max-height 85dvh; border-radius `rounded-xl` `rounded-xl` 0 0; padding-bottom env(safe-area-inset-bottom).
- **Phone sheet open:** transform from translateY(100%); the same timing as Sheet open.
- **Phone sheet closing:** transform to translateY(100%); the same timing as Sheet closing.
- **Phone actions:** the bottom corners are square, so the actions keep the body's padding: padding 0 `space-6` `space-6`.
- **Focus:** initial focus goes to the first control of the body. Focus stays inside; Escape, the close button and a click on the scrim close it; focus returns to the button that opened it.
- **Reduced motion:** no slide; the fade keeps the same durations. On open: animation-name fadeIn; on closing: animation-name fadeOut.
