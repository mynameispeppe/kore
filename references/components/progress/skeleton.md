**Skeleton**

- **Skeleton block:** the shape of the content it replaces, with the same spacing as the real content, so nothing moves when it arrives. Exempt from contrast (Contrast). display block; background `stone`; opacity 0.6; border-radius `rounded-sm`; animation 2 × `duration-focal` `ease-in-out` infinite alternate, opacity down to 0.3; opacity only.
- **Block sizes:** a line: height the line-height of its type role (`body-md`, or `title-md` for a card title), width a percentage of its container close to the length of the words it stands for. An avatar: width and height `space-10`; border-radius `rounded-full`; corner-shape round. A button: the height and border-radius of the button it replaces (`button-md` and `rounded-md` for a medium button), at least `button-min` wide, about as wide as that button.
- **Skeleton reduced motion:** animation none.
- **Timing:** shown only after 300ms, so a fast load does not flash.
- **Markup:** the container has `aria-busy="true"` and one visually hidden label that names what is loading; the blocks are `aria-hidden="true"`.
