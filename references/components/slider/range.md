**Range**

- **Range:** two inputs over one track, with two thumbs that never cross and the fill between them; each thumb has its own accessible name, the label's minimum and maximum. The wrapper: height calc(`space-10` + `space-1`); cursor pointer.
- **Range track:** the wrapper's ::before. content ""; position absolute; inset-inline 0; top 50%; transform translateY(−50%); height `space-2`; border-radius `rounded-full`; corner-shape round; background linear-gradient(to right, `hairline-strong` up to the first thumb's centre, `primary` up to the second's, `hairline-strong` after it).
- **Range inputs:** only the thumbs take the pointer. position absolute; inset 0; pointer-events none; their tracks: background none; their thumbs: pointer-events auto; cursor pointer.
- **Top thumb:** the last thumb moved sits on top, changed only once it is released: a stacking change during a native drag stops the drag. z-index `zIndex-raised`.
