# Slider

**Uses:** Tooltip.

**Purpose:** a track with a thumb the user drags to pick an approximate value, or two thumbs for a range.

- **Use:** only when an approximate value is fine; for an exact value use the Number stepper.
- **Hierarchy:** the label comes first, then the track. The thumb is the focal point (The One Winner Rule): the only `ink` fill with a shadow; the filled part of the track in `primary` follows; the empty part in `hairline-strong` only guides.
- **Elements:** the Slider's own: slider, label row, label, wrapper, input, track, thumb, focus marks, value bubble, range track. Other components: the bubble's look (Tooltip).
- **Slider:** the label above, the track under it. display flex; flex-direction column; gap `space-2`; max-width `field-max`.
- **Label row:** display flex; justify-content space-between.
- **Label:** a `<label>` tied to the input; in a range it names the group (`role="group"` with `aria-labelledby`). color `ink`; font-family `label-lg`; font-size `label-lg`; font-weight `label-lg`; line-height `label-lg`; letter-spacing `label-lg`.
- **Wrapper:** the input with its focus marks and its bubble; it carries the thumb's position, from 0 to 1. position relative.
- **Thumb centre:** the thumb's centre sits at `slider-thumb` / 2 + (100% − `slider-thumb`) × the position, so the fill, the focus marks and the bubble follow the native thumb.
- **Input:** a native `<input type="range">`, as tall as its hit area. -webkit-appearance none; appearance none; width 100%; height calc(`space-10` + `space-1`); background transparent; margin 0; cursor pointer.
- **Track:** round ends; filled up to the thumb's centre. height `space-2`; border-radius `rounded-full`; corner-shape round; background linear-gradient(to right, `primary` up to the thumb's centre, `hairline-strong` after it).
- **Thumb:** dragged, so it carries a shadow; centred on the track. -webkit-appearance none; width `slider-thumb`; height `slider-thumb`; margin-top calc((`space-2` − `slider-thumb`) / 2); box-sizing border-box; border-radius `rounded-full`; corner-shape round; background `ink`; border `line-thick` solid `canvas`; box-shadow `shadow-rest`; transition box-shadow `duration-fast` `ease-out`.
- **Thumb hover:** box-shadow `shadow-hover`.
- **Thumb focus:** on :focus-visible the input: outline none, changed in 0s; the focus marks show.
- **Focus marks:** the corner marks of States around the thumb, a span that follows it, shown when the input has :focus-visible: display none, then display block, changed in 0s. position absolute; top 50%; inset-inline-start at the thumb's centre; width calc(`slider-thumb` + 2 × (`line-thick` + `line-thin`)); height calc(`slider-thumb` + 2 × (`line-thick` + `line-thin`)); transform translate(−50%, −50%); border `line-thin` solid `focus-ring`; border-radius calc(`slider-thumb` / 2 + `line-thick` + `line-thin`); pointer-events none; -webkit-mask and mask linear-gradient, one square per corner, each `space-3` square. Under forced colors: border-color Highlight.
- **Value bubble:** while a thumb is dragged or has keyboard focus, its value shows centred above it, in the Tooltip's look. It hides on release and never shows after a mouse click; a thumb focused by script after a click on the track uses `focusVisible: false`. It is `aria-hidden="true"`: each thumb carries its value in `aria-valuetext` (for example "€12"). position absolute; bottom calc(50% + `slider-thumb` / 2 + `space-2`); inset-inline-start at the thumb's centre; transform translateX(−50%); z-index `zIndex-tooltip`; background `ink`; color `canvas`; border-radius `rounded-sm`; padding `space-1` `space-2`; width max-content (the CSS keyword, not the token); pointer-events none; opacity 0; transition opacity `duration-fast` `ease-out`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`; font-variant-numeric tabular-nums.
- **Shown bubble:** opacity 1.
- **Steps:** between the limits at least 100 steps (0–100 by 1, 200–800 by 5), so the thumb follows the pointer.
- **Keyboard:** the arrow keys move the thumb by one step, Home and End to the limits, as the native input does.
- **Track click:** a click or a tap on the track moves the nearest thumb there and keeps dragging it.
- **Disabled:** no bubble. The input: cursor not-allowed; the track: background `hairline-medium`; the thumb: background `stone`; box-shadow none; the label: color `stone`.
- **Range:** two inputs over one track, with two thumbs that never cross and the fill between them; each thumb has its own accessible name, the label's minimum and maximum. The wrapper: height calc(`space-10` + `space-1`); cursor pointer.
- **Range track:** the wrapper's ::before. content ""; position absolute; inset-inline 0; top 50%; transform translateY(−50%); height `space-2`; border-radius `rounded-full`; corner-shape round; background linear-gradient(to right, `hairline-strong` up to the first thumb's centre, `primary` up to the second's, `hairline-strong` after it).
- **Range inputs:** only the thumbs take the pointer. position absolute; inset 0; pointer-events none; their tracks: background none; their thumbs: pointer-events auto; cursor pointer.
- **Top thumb:** the last thumb moved sits on top, changed only once it is released: a stacking change during a native drag stops the drag. z-index `zIndex-raised`.
