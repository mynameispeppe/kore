# Badge

**Uses:** Alert.

**Purpose:** a short label for the state or category of the element it sits on, or a count. It cannot be clicked: a label that filters or can be removed is a Chip.

| Kind | Fill | Text |
|---|---|---|
| Neutral | `surface-elevated` | `ink` |
| Info, Success, Warning, Error | the tint of the kind, exactly as the Alert's container | `ink` |
| Count | `ink` | `canvas` |

- **Hierarchy:** the badge is never the focal point: the element it sits on leads (The One Winner Rule). It holds one thing, its text or its number, in `label-sm`. A Neutral badge is the quietest; a status badge's tint repeats the meaning of its word; the count, filled with `ink`, is the strongest, because it asks for attention.
- **Elements:** the Badge's own: badge, text, wrapper. No other components; the tint of a status badge is the Alert's. Neutral, Info, Success, Warning, Error and Count are variants of the badge; pinned and inline are its positions.
- **Badge:** position relative; display inline-flex; align-items center; height `space-6`; padding 0 `space-2`; border-radius `rounded-sm`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; background-color `surface-elevated`; background-image `gradient-raised`; box-shadow `shadow-raised-sm`; color `ink`; font-family `label-sm`; font-size `label-sm`; font-weight `label-sm`; line-height `label-sm`; letter-spacing `label-sm`; white-space nowrap.
- **Status badge:** background color-mix(in srgb, the kind's vivid color `mix-tint`, transparent); outline 0; box-shadow `shadow-raised-rim`, inset 0 −`line-thick` 0 color-mix(in srgb, the kind's vivid color `mix-ledge`, transparent), 0 0 0 `line-thin` color-mix(in srgb, the kind's semantic color `mix-edge`, transparent). (replaced in: minimalism)
- **Count badge:** min-width `space-6`; justify-content center; padding 0; border-radius `rounded-full`; corner-shape round; outline 0; background-color `ink`; color `canvas`; font-variant-numeric tabular-nums.
- **Count capsule:** padding 0 `space-2`.
- **Count number:** a whole number: one or two digits make a circle, "99+" from 100 makes a capsule. It is filled with `ink` because `primary` is spent on the main action (The One Primary Rule). The control it sits on carries an accessible name that says what is counted.
- **Text:** one line, one or two words in sentence case that name the state. The tint never works alone: the text carries the meaning, and its colour on the tint holds 4.5:1 in both themes.
- **Pinned badge:** position absolute; top 0; inset-inline-end 0; transform translate(50%, −50%); pointer-events none.
- **Pinned badge in RTL:** transform translate(−50%, −50%).
- **Pinned badge on the icon:** inset-inline-start 50%; inset-inline-end auto; transform translateY(−50%).
- **Pinned position:** Neutral, Info, Success, Warning, Error and Count can be pinned on the top right corner of the container it describes (button, icon, card), its centre on the corner. On a button with no visible container (tertiary), the badge starts on the icon's vertical centre line, its centre on the icon's top edge (Material 3), so it covers only the icon's top end corner. Never beside the text.
- **Inline badge:** only a Neutral badge that marks an item the user chose to stand out among its peers (the featured plan, the yearly saving: Pricing), never a state. Inside its container, on the row of the text it qualifies, after it: at the row's end for a card's title, `space-2` after a segment's label.
- **Wrapper:** position relative; display inline-flex.
- **Wrapper focus:** the focused control in the wrapper: z-index `zIndex-raised`, changed in 0s, so its focus marks are drawn above the badge.
- **States:** none. It takes no focus and has no hover or pressed look.
- **Announcement:** a badge is not announced. When it appears after the page loaded and the information matters, the page says it in its own text.
