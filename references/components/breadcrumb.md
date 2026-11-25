# Breadcrumb

**Uses:** Button, Menu, Tooltip.

**Purpose:** it shows where the current page sits in the structure and takes the user back up to any level (Usability 6).

- **Hierarchy:** the levels read in order, from the first to the current page. The current page is the focal point (The One Winner Rule): `title-sm` in `ink`, after the ancestors in `body-md` and `mute`. The separators, in `mute`, only divide.
- **Elements:** the Breadcrumb's own: breadcrumb, list, item, link, link hit area, separator, separator icon, current page. Other components: the more button (Button, tertiary icon, small, with a Tooltip) and the Menu it opens, inside an item.
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Long trails `references/components/breadcrumb/long-trails.md`.
- **Depth:** only where the structure is at least three levels deep.
- **Markup:** a `<nav aria-label="Breadcrumb">` holding an ordered list.
- **Breadcrumb:** font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **List:** list-style none; margin 0; padding 0; display flex; flex-wrap wrap; align-items center; gap `space-6` `space-2`.
- **Item:** display flex; align-items center; gap `space-2`.
- **Link:** position relative; color `mute`; text-decoration none; transition 0s.
- **Link hover:** on mouse hover (hover: hover): color `ink`; text-decoration underline `line-thin`; text-underline-offset `space-1`.
- **Link focus:** on :focus-visible: outline none; color `ink`; text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s (the link focus underline, States).
- **Link hit area:** the link's ::before: content ""; position absolute; top −`space-3`; bottom −`space-3`; inset-inline-start 50%; width max(100%, `button-lg`); transform translateX(−50%).
- **Link hit area in RTL:** transform translateX(50%).
- **Separator:** at the start of every item after the first, hidden from screen readers. color `mute`.
- **Separator in RTL:** transform scaleX(−1).
- **Separator icon:** a chevron. flex none; display block; width `icon-sm`; height `icon-sm`.
- **Current page:** the last item; it is not a link and has `aria-current="page"`. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Position:** at the top of the content, above the page title, `space-4` above the title.
