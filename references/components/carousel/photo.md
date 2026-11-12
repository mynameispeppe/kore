**Photo variant**

- **Viewport:** the centre photo is 40% of the carousel's width, 60% below `sm` (container query), proportions of this variant; a neighbour is scaled to 80%. position relative; overflow hidden; touch-action pan-y; height calc(the photo's width × 4 / 3 + 2 × `space-1`).
- **Photo track:** position absolute; inset 0.
- **Photo slide:** portrait 3:4. position absolute; top `space-1`; inset-inline-start calc(50% − the photo's width / 2); height calc(100% − 2 × `space-1`); border-radius `rounded-xl`; cursor pointer.
- **Photo slide place:** transform translateX(the slide's distance from the centre) scale(0.8); each slide sits (its index − the current index) steps from the centre, a step being 0.9 × the photo's width + `space-4`, so the neighbours sit `space-4` from the centre photo.
- **Centre photo:** scale 1; cursor default. A click on a neighbour makes it the centre photo. While dragging, the scale follows the position.
- **Photo:** with its alt text. width 100%; height 100%; border-radius inherit; object-fit cover.
- **Ends:** the first and the last photo never leave the carousel's edges (Material 3, Carousel). On the first photo the centre photo sits at the start edge, its neighbours after it; on the last, at the end edge, `space-1` from it; on every other photo it is centred. While dragging, its place follows the scroll between these places.
- **Start:** the carousel opens on the second photo, centred, the first one visible at its start side; with two photos, on the first.
- **Photo arrows:** elevated, medium. They show only with a fine pointer (pointer: fine); on touch they are visually hidden (Status) and stay for screen readers.
- **Arrow slot:** position absolute; top 50%; transform translateY(−50%); z-index `zIndex-raised`. The previous one inset-inline-start `space-4`, the next one inset-inline-end `space-4`.
- **Indicator:** decoration (`aria-hidden`): the status says the position. display flex; justify-content center; gap `space-2`; margin-top `space-4`.
- **Indicator mark:** one per photo. height `space-1`; width `space-2`; border-radius `rounded-full`; corner-shape round; background `hairline-strong`; transform-origin center; transition background-color `duration-base` `ease-out`.
- **Current mark:** width `space-6`; background `ink`. The change of width is animated with a transform (FLIP) in `duration-base`, never by animating the width (Motion).
- **Indicator reduced motion:** transition 0s.
