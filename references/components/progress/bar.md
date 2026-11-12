**Bar**

- **Bar:** the full width of its column. display flex; flex-direction column; gap `space-2`; width 100%.
- **Label row:** above the track, the task's name at the start and the value at the end. Every bar has one. display flex; justify-content space-between; gap `space-4`.
- **Task name:** color `ink`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Value:** the count done out of the total, or the percentage done, in the page's language. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; font-variant-numeric tabular-nums.
- **Track:** exempt from contrast (Contrast): the fill reaches 3:1 against it and the value is always written. position relative; height `space-2`; border-radius `rounded-full`; corner-shape round; background `stone`; overflow hidden.
- **Fill:** position absolute; inset 0; background `ink`; border-radius inherit; transform-origin left (right in right-to-left languages); transition transform `duration-focal` `ease-in-out`, so updates that follow each other join into one movement.
- **Known amount:** the value is the real one. The fill: transform scaleX(done ÷ total), never by animating its width. The track has `role="progressbar"` with `aria-labelledby` pointing to the task's name, `aria-valuemin`, `aria-valuemax`, `aria-valuenow` and `aria-valuetext` equal to the written value.
- **Segment:** the fill of an unknown amount. No value is written; the track has `aria-busy="true"` and no `aria-valuenow`. width 40%; transform none; animation 2 × `duration-focal` `ease-in-out` infinite, from translateX(−100%) to translateX(250%) (from translateX(100%) to translateX(−250%) in right-to-left languages).
- **Segment reduced motion:** width 100%; animation 2 × `duration-focal` `ease-in-out` infinite alternate, opacity from 1 to 0.3.
- **Over 3 seconds** (Usability 1): a known amount adds the time left after the value, separated by a middle dot, in minutes from 60 seconds, and a tertiary Button `button-sm` "Cancel" sits under the bar, at the end of the row, `space-4` below it (The Distance Ratio Rule).
- **Flows:** a multi-step flow shows the bar, and its value is the current step out of the total steps (Usability 1).
- **Starting button:** while the bar runs, the button that started the work is in its Loading state (Button), and returns to rest when the work ends. Its spinner: flex none. On :focus-visible: outline none, changed in 0s; the corner marks of States (Button, Focus). The bar, then the end line, sit `space-4` below it: margin-top `space-4`.
- **End line:** when the work ends the bar is removed, and in its place one line with `role="status"` says the result: the count of items and the action done, in the past tense. color `body`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
