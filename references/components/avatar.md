# Avatar

**Purpose:** a round picture of a person or an account.

- **Hierarchy:** the avatar is never the focal point: the name beside it leads (The One Winner Rule), and the avatar only helps the eye find the person. It shows one thing, in this order: the image; without an image, the initials; without a name, the icon. The dot is its only sign of state.
- **Elements:** the Avatar's own: avatar, image, initials, icon, the Hugeicons person icon, dot, group, count avatar. No other components. The small and large sizes are variants of the avatar, not elements.
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Presence `references/components/avatar/presence.md`, Group `references/components/avatar/group.md`.
- **Avatar:** position relative; flex none; display inline-grid; place-items center; width `space-10`; height `space-10`; border-radius `rounded-full`; corner-shape round; object-fit cover; background-color `surface-elevated`; background-image `gradient-raised`; box-shadow `shadow-raised-sm`; color `ink`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; font-family `label-lg`; font-size `label-lg`; font-weight `label-lg`; line-height `label-lg`; letter-spacing `label-lg`. (replaced in: glassmorphism)
- **Small avatar:** width `space-8`; height `space-8`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Large avatar:** width `space-12`; height `space-12`; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`.
- **Size:** the avatar's own size is the default, the one in list rows.
- **Color:** one neutral color: never a random or a semantic color, so color never means anything here.
- **Initials:** one or two letters.
- **Icon:** flex none; display block; width `icon-md`; height `icon-md`.
- **Small avatar icon:** width `icon-sm`; height `icon-sm`.
- **Large avatar icon:** width `icon-lg`; height `icon-lg`.
- **Accessibility:** an image has an alt attribute with the name, or an empty one when the name sits next to it. Initials and the icon have `role="img"` and an `aria-label` with the name, or `aria-hidden="true"` when the name sits next to them.
- **Interaction:** an avatar is not interactive. A control that shows one (a profile menu) is a button with an accessible label.
