# Dialog

**Uses:** Button, Tooltip, Overlay rules.

**Purpose:** a modal that asks for a decision. Use a dialog only when the action cannot be undone or truly needs interruption and protected focus; otherwise act and offer "Undo" (Usability 3) or use an inline or progressive alternative.

- **Hierarchy:** the header comes first, then the message, then the actions. The title is the focal point (The One Winner Rule): `title-lg` in `ink`, read before the message in `body-lg` and the buttons. A consequence that cannot be undone follows in `title-md` `danger`; the dividers only separate.
- **Elements:** the Dialog's own: dialog, scrim, header, title, header divider, message, body, emphasis, consequence, actions, actions divider. Other components: the close button (Button, tertiary icon, small, with a Tooltip) and the action buttons (Button).
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Sign-in dialog `references/components/dialog/sign-in.md`.
- **Markup:** the platform's modal element where it exists (`<dialog>` on the web), named by its title (`aria-labelledby`) and described by its message (`aria-describedby`).
- **Dialog:** width min(`dialog`, 100vw − `space-8`), so it stays `space-4` from the screen's edges on phones; max-width none; padding 0; border 0; border-radius `rounded-xl`; background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; color `ink`.
- **Scrim:** the dialog's ::backdrop: background `scrim`.
- **Header:** the title, then the close button as a corner action (Shapes). display flex; align-items flex-start; gap `space-2`; position relative; padding `space-4` `space-4` `space-3` `space-6`; min-height `space-12`.
- **Title:** an `h2` that names the action with a verb and an object, never a question. Its first line is centred on the close button. flex 1; min-width 0; margin-block calc((`button-sm` − the line-height of `title-lg`) / 2); font-family `title-lg`; font-size `title-lg`; font-weight `title-lg`; line-height `title-lg`; letter-spacing `title-lg`.
- **Dividers:** header and actions are the dialog's fixed regions; the lines separate them from the message, the only part that grows (a long text, a form). Each runs from the title's start to the close button's end. content ""; position absolute; inset-inline `space-6` `space-4`; height `line-thin`; background `hairline`.
- **Header divider:** the header's ::after: bottom 0.
- **Actions divider:** the actions' ::before: top 0.
- **Message:** the body and the consequence, one message centred between the two lines. padding `space-6`; display flex; flex-direction column; gap `space-1`.
- **Body:** font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`; color `body`.
- **Emphasis:** the object and the figures in the body, each a `<strong>` (Emphasis). font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; color `ink`.
- **Consequence:** an effect that cannot be undone, on its own line under the body. font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; color `danger`.
- **Actions:** right-aligned, confirm last, the cancel action tertiary; the buttons name the action with a verb and an object, never "Yes", "No", "OK" or "Submit". They sit `space-3` from the dialog's edges (the `rounded-xl` corner less the button's `rounded-md`). display flex; justify-content flex-end; flex-wrap wrap; gap `space-2`; position relative; padding `space-4` `space-3` `space-3`.
- **Focus:** initial focus goes to the safer action; in a dialog with a form, to its first field. Focus stays inside; Escape, the close button and a click on the scrim close it; focus returns to the trigger.
- **Dialog open:** opacity from 0 and scale from 0.98 to 1: animation `duration-slow` `ease-out`.
- **Dialog closing:** it fades to 0 and scales to 0.98 in `duration-base` with `ease-in`, and stays so until it is hidden.
- **Reduced motion:** only the fade stays, with the same durations: on open, animation-name fadeIn.
