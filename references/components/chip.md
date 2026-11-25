# Chip

**Purpose:** a small label the user acts on: it turns a filter on and off. Kore has the filter chip only. A label that just states something is a Badge.

- **Hierarchy:** a selected chip is the focal point of its group (The One Winner Rule): `surface-elevated` fill and the check before its label; the chips left off have no fill. The label in `label-lg` `ink`.
- **Elements:** the Chip's own: chip group, chip, hit area, check icon, icon. Default, selected and disabled are states of the chip, not elements.
- **Chip group:** a group with an accessible label that names what its chips filter; chips sit `space-3` apart (Adjacent targets). display flex; flex-wrap wrap; gap `space-3`.
- **Chip:** a button with `aria-pressed`; Enter and Space toggle it. One line. position relative; display inline-flex; align-items center; height `space-8`; padding 0 `space-3`; border-radius `rounded-sm`; box-shadow inset 0 0 0 `line-thin` `hairline-medium`; color `ink`; font-family `label-lg`; font-size `label-lg`; font-weight `label-lg`; line-height `label-lg`; letter-spacing `label-lg`; white-space nowrap; transition background-color `duration-fast` `ease-out`, padding-inline-start `duration-base` `ease-out`.
- **Hit area:** the chip's ::before, calc(`space-10` + `space-1`) tall, centred on the chip. content ""; position absolute; inset calc((`space-8` − (`space-10` + `space-1`)) / 2) 0.
- **Chip hover:** with a mouse (hover: hover), a chip not disabled: background `surface-hover`.
- **Chip pressed:** selected or not, a chip not disabled: background `surface-pressed`.
- **Chip focus:** on :focus-visible: outline none, changed in 0s; the corner marks of States, following `rounded-sm`.
- **Selected chip:** the check icon carries the state, so it never rests on the fill alone. background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; padding-inline-start `space-2`. (replaced in: glassmorphism)
- **Selected hover:** with a mouse, a selected chip not disabled and not pressed: background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `mute`, changed in 0s. (replaced in: glassmorphism)
- **Check icon:** the Hugeicons `Tick02`, at the chip's start. Closed: flex none; width 0; margin-inline-end 0; stroke-dasharray 1; stroke-dashoffset 1; transition width `duration-base` `ease-out`, margin-inline-end `duration-base` `ease-out`, stroke-dashoffset `duration-base` `ease-out`.
- **Selected check icon:** it opens in place (Motion, Transform and opacity) and draws its stroke from start to end, while the chip's padding and the gap before the label follow, so the chip widens and the label slides over; on deselect it runs backwards. width `icon-sm`; margin-inline-end `space-2`; stroke-dashoffset 0.
- **Icon:** flex none; display block.
- **Reduced motion:** the chip and its check icon: transition 0s.
- **Disabled chip:** color `stone`; box-shadow inset 0 0 0 `line-thin` `hairline`; background none; cursor not-allowed.
- **Disabled selected chip:** background `surface-elevated`.
- **Disabled check icon:** color `stone`.
