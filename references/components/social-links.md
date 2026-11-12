# Social links

**Purpose:** links to a person's or a company's profiles on other sites. The user chooses the variant: icon only, or icon with its name. The agent builds the chosen one and never both.

- **Not chosen:** icon with its name. Say it in one line ("social links: icon with name; say if you want icon only").
- **Hierarchy:** one level: every link weighs the same, in `mute`, and none is the focal point; the links only guide away from the page. A hovered or focused link turns `ink`.
- **Elements:** the Social links' own: list, link, icon, name, new-tab note, icon-only list, icon-only link, focus underline.
- **List:** a `ul`; the links wrap on narrow screens and the gap never shrinks. list-style none; margin 0; padding 0; display flex; flex-wrap wrap; gap `space-4`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Link:** every state switches instantly. display flex; align-items center; min-height `space-8`; color `mute`; text-decoration none; transition 0s.
- **Link on touch screens:** with any touch screen (any-pointer: coarse): min-height calc(`space-10` + `space-1`).
- **Link hover:** on mouse hover (hover: hover): color `ink`.
- **Link focus:** on :focus-visible: outline none; color `ink`; text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s (the link focus underline, States). No corner marks: links take none (States).
- **Icon:** the file of the site in `references/icons/brands/` (`references/rules/icons.md`, Logos), at `icon-md`, fill currentColor, `aria-hidden="true"`. flex none; display block; margin-inline-end `space-2`.
- **Name:** the site's name, after the icon.
- **New tab:** every link has `target="_blank"` and `rel="noopener noreferrer"`.
- **New-tab note:** in the variant with names, visually hidden text after the name says the link opens in a new tab. position absolute !important; width `line-thin`; height `line-thin`; overflow hidden; clip-path inset(50%); white-space nowrap.
- **Icon-only list:** gap `space-2`.
- **Icon-only link:** a square as big as its hit area, the icon centred in it. The `aria-label` is the site's name plus the new-tab note; no tooltip, since the icon is recognized by sight. position relative; width calc(`space-10` + `space-1`); height calc(`space-10` + `space-1`); justify-content center; align-items flex-start; padding-top `space-3`. Its icon: margin 0.
- **Focus underline:** on an icon-only link, the link focus underline under the icon: the link's ::after on :focus-visible, changed in 0s. content ""; position absolute; inset-inline `space-3`; top calc(`space-3` + `space-5` + `space-1`); height `line-thick`; border-radius `rounded-full`; background `ink`; transition 0s.
- **Missing address:** a link without its address is left out. A row is never shown empty.
- **Email is not a profile:** it never goes in Social links and has no icon here. The address is the Footer's contact (Footer, Bottom row) and, where a section asks to be contacted, the target of its contact action ("Contact me", `mailto:`). One section never offers both (AI tells 13).
