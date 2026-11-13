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
- **Variant files:** read only the file of each variant that the part being built or checked contains: Status `references/components/badge/status.md`, Count `references/components/badge/count.md`.
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Pinned `references/components/badge/pinned.md`, Inline `references/components/badge/inline.md`.
- **Badge:** position relative; display inline-flex; align-items center; height `space-6`; padding 0 `space-2`; border-radius `rounded-sm`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; background-color `surface-elevated`; background-image `gradient-raised`; box-shadow `shadow-raised-sm`; color `ink`; font-family `label-sm`; font-size `label-sm`; font-weight `label-sm`; line-height `label-sm`; letter-spacing `label-sm`; white-space nowrap.
- **Text:** one line, one or two words in sentence case that name the state. The tint never works alone: the text carries the meaning, and its colour on the tint holds 4.5:1 in both themes.
- **Wrapper:** position relative; display inline-flex.
- **Wrapper focus:** the focused control in the wrapper: z-index `zIndex-raised`, changed in 0s, so its focus marks are drawn above the badge.
- **States:** none. It takes no focus and has no hover or pressed look.
- **Announcement:** a badge is not announced. When it appears after the page loaded and the information matters, the page says it in its own text.
