**Snap variant**

- **Snap track:** one card in view, as wide as a card with a paragraph (Cards, Width), or the row when it is narrower; no other card shows. column-gap `space-4`; max-width calc(`measure` + 2 × `space-6` + 2 × `space-1`); grid-template-rows auto; grid-auto-columns 100%.
- **Snap card:** a standard card (Cards). grid-row auto; grid-template-rows 1fr auto; row-gap `space-4`; justify-items center; text-align center; scroll-snap-stop always; scale `scale-enter`; transition scale `duration-slow` `ease-in-out`. On touch each swipe moves one card. (replaced in: glassmorphism)
- **Snap card in view:** scale 1.
- **Snap card reduced motion:** scale 1; transition 0s.
- **Snap header:** align-self center; align-items center.
- **Snap title:** the card's title, font-family `title-lg`; font-size `title-lg`; font-weight `title-lg`; line-height `title-lg`; letter-spacing `title-lg`.
- **Snap subtitle:** under the title, font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Snap position:** "<position> of <total>" at the bottom end. justify-self end; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; font-variant-numeric tabular-nums; color `mute`.
- **Footer:** under the card, `space-4` below, the indicator of the Photo variant at its start edge, the arrow group at its end edge. display flex; align-items center; justify-content space-between; gap `space-4`; width min(calc(`measure` + 2 × `space-6`), 100%).
- **Footer indicator:** margin-top 0.
- **Arrow group:** small secondary buttons, shown on every device. display flex; gap `space-2`.
