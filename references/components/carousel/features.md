**Features variant**

- **Features:** the list and the photos, no fill; below `lg` one column, the list centred above the photos. display grid; gap `space-8`; align-items center.
- **Features from lg:** the list and the photos side by side, centred together: the list as wide as its longest feature, the photos' column as wide as the photo plus `space-8` on each side. grid-template-columns auto calc(`space-48` + `space-32` + 2 × `space-8`); justify-content center; column-gap `space-12`.
- **Feature list:** the features are tabs (`role="tablist"`, vertical): tertiary buttons with the feature's name, the selected one secondary. display flex; flex-direction column; align-items center; gap `space-2`. ↑ and ↓ move and select, Home and End go to the first and the last; focus follows the tab. The photos are the tab panel. No arrows.
- **Feature list from lg:** align-items flex-start.
- **Feature panel:** container-type inline-size.
- **Feature photos:** the current photo portrait 3:4, min(calc(`space-48` + `space-32`), calc(100cqw − 2 × `space-8`)) wide; the previous and the next sit behind it, so `space-8` of each shows past its sides; the photos further away hide behind them. A click on a side photo selects it. The change moves in `duration-focal` with `ease-in-out`.
- **Feature slide:** transform none; scale `scale-enter`; transition scale `duration-slow` `ease-in-out`.
- **Current feature slide:** scale 1.
- **Photo frame:** position absolute; inset 0; overflow hidden; border-radius inherit.
- **Feature photo frame:** filter grayscale(1); transition filter `duration-slow` `ease-in-out`.
- **Current feature photo frame:** filter none.
- **Feature reduced motion:** the slide: scale 1; transition 0s; the photo frame: transition 0s.
- **Feature description:** the selected feature's sentence. margin `space-4` auto 0; max-width 40ch; text-align center; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
