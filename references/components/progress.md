# Progress

**Uses:** Button.

**Purpose:** it shows how far a task has gone, or that content is loading. A bar is for work the user waits on; a skeleton is for content that loads (Usability 1). Never a spinner alone in the middle of a page, a card or a list.

- **Hierarchy:** in a bar the value is the focal point (The One Winner Rule): `title-sm` `ink`; the task's name in `body-md` `ink` names it; the track and its fill only show the amount. A skeleton has no focal point: it holds the place of the content.
- **Elements:** the Progress's own: bar, label row, task name, value, track, fill, segment, end line, skeleton block. Other components: the button that starts the work and the Cancel button (Button).

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

**Skeleton**

- **Skeleton block:** the shape of the content it replaces, with the same spacing as the real content, so nothing moves when it arrives. Exempt from contrast (Contrast). display block; background `stone`; opacity 0.6; border-radius `rounded-sm`; animation 2 × `duration-focal` `ease-in-out` infinite alternate, opacity down to 0.3; opacity only.
- **Block sizes:** a line: height the line-height of its type role (`body-md`, or `title-md` for a card title), width a percentage of its container close to the length of the words it stands for. An avatar: width and height `space-10`; border-radius `rounded-full`; corner-shape round. A button: the height and border-radius of the button it replaces (`button-md` and `rounded-md` for a medium button), at least `button-min` wide, about as wide as that button.
- **Skeleton reduced motion:** animation none.
- **Timing:** shown only after 300ms, so a fast load does not flash.
- **Markup:** the container has `aria-busy="true"` and one visually hidden label that names what is loading; the blocks are `aria-hidden="true"`.
