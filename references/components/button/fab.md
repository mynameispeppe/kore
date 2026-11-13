**FAB**

- **FAB:** an icon-only button floating over the content that opens 2–6 related actions; one per screen; a single action uses an icon button. It is a primary button with width `button-md`; height `button-md`; padding `space-2`; border-radius `rounded-md`, and one `icon-md` icon, an accessible label and a tooltip. Placed bottom right, `space-4` from the edges on phones and `space-6` from `md` up.
- **FAB icon:** transition rotate `duration-fast` `ease-in`.
- **FAB icon open:** with `aria-expanded="true"` and `aria-controls`: rotate `turn`, the + becomes ×; transition rotate `duration-slow` `ease-out`.
- **FAB tooltip open:** visibility hidden, so it never covers the item above.
- **FAB menu:** a Menu above the FAB, centred on it: top auto; bottom `space-4` above it; inset-inline 0; margin-inline auto; min-width 0; `width: max-content`; max-height none; overflow visible; background none; outline 0; border-radius 0; padding 0; gap `space-4`; align-items center; animation 0s.
- **FAB menu item:** an elevated icon button, `button-md`. animation fabIn `duration-slow` `ease-out`: from opacity 0, rotate `turn` and scale `scale-enter` to opacity 1, rotate 0 and scale 1.
- **FAB menu item closing:** the items leave with fabOut, the reverse of fabIn, in `duration-fast` with `ease-in`, forwards.
- **FAB reduced motion:** the items' animation-name fadeIn, without movement; the FAB icon: transition 0s.
- **FAB keyboard:** as the Menu (`menu`, `menuitem`): ↑ ↓ move, Escape closes and returns focus to the FAB, Tab and a click outside close.
