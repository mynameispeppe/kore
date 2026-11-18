# Top bar

**Uses:** Button, Tooltip, Menu, Avatar, Dialog, Form fields, List rows, Empty state.

**Purpose:** the fixed bar at the top of the page: the logo, the navigation links and, optionally, up to three tools. A project's navigation is a Top bar or a Sidebar, never both; every project has one of the two.

- **Hierarchy:** the logo comes first, then the links, then the tools. The current page's link is the focal point of the bar (The One Winner Rule): the only link in `ink` with the current-page line under it; the other links in `mute` only guide; the call to action, when there is one, is the bar's one primary (The One Primary Rule).
- **Elements:** the Top bar's own: bar, logo, links, link, current-page line, group link, chevron, tools, tool spacing, account button, menu button, menu icon, navigation panel, panel link, panel text, sub-links, guide, panel separator, language options, scrim, search dialog, search field, results box. Other components: the tool buttons, the menu button and the call to action (Button), the tooltips (Tooltip), the sub-link, Language and Account menus (Menu), the account picture (Avatar), the search dialog (Dialog), the search field (Form fields), the results (List rows), the no-results content (Empty state).
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Search `references/components/top-bar/search.md`, Theme `references/components/top-bar/theme.md`, Language `references/components/top-bar/language.md`, Account button `references/components/top-bar/account.md`, Call to action `references/components/top-bar/call-to-action.md`.

**Bar and logo**

- **Bar:** full width, fixed at the top and always visible; the content sits in the page's side margin. position fixed; top 0; inset-inline 0; z-index `zIndex-raised`; display flex; align-items center; height calc(`space-8` × 2 + the top safe area); padding-top the top safe area; padding-inline `space-8`. Its content: max-width `max-content`; margin-inline auto. No border and no shadow. (replaced in: glassmorphism)
- **Surface:** background `canvas`. (replaced in: glassmorphism)
- **Over the hero:** with the page at the top, the bar has no surface: background transparent. It takes it as soon as the page scrolls (scrollY > 0): transition background-color `duration-base` `ease-out`. (replaced in: glassmorphism)
- **Over a photo:** over the Full-bleed photo, the logo and the current link: color `on-photo`; the other links: color `on-photo-mute`.
- **Logo:** always at the start. A link to the home page. display inline-flex; align-items center; min-height calc(`space-10` + `space-1`); text-decoration none.
- **Logo text:** without a logo file, the product's name as text. color `ink`; font-family `title-lg`; font-size `title-lg`; font-weight `title-lg`; line-height `title-lg`; letter-spacing `title-lg`.
- **Logo focus:** on :focus-visible: outline none; text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s.

**Navigation links**

- **Links:** next to the logo, never centred; a list. position relative; display flex; align-items center; gap `space-6`; margin-inline-start `space-12`.
- **Link:** text only; its hit area at least 44px wide and tall, its padding taken out of the layout, so the gap between two texts stays `space-6`. position relative; display inline-flex; align-items center; gap `space-2`; min-height calc(`space-10` + `space-1`); padding-inline `space-2`; margin-inline calc(`space-2` × −1); padding-block calc((`space-10` + `space-1` − the `label-md` line-height) / 2); margin-block calc((`space-10` + `space-1` − the `label-md` line-height) / 2 × −1); color `mute`; text-decoration none; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Link hover:** on mouse hover (hover: hover): color `ink`.
- **Current link:** `aria-current="page"`. color `ink`.
- **Link focus:** on :focus-visible: outline none; color `ink`; text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s.
- **Current-page line:** drawn once for the whole bar, in the links list, as wide as the current link's text, `space-1` − `line-thick` under it. position absolute; top 0; inset-inline-start 0; height `line-thick`; border-radius `rounded-full`; background `ink`; pointer-events none; transform-origin 0 0; transition transform `duration-base` `ease-out`, opacity `duration-fast` `ease-out`.
- **Line motion:** when the current page changes, the line slides to the new link and takes its width with a transform (translate and scaleX), never by animating its width; it fades in with opacity 1. The first time it appears in place: transition none. Under reduced motion: transition none.
- **Group link:** a link with sub-links: a disclosure button with `aria-expanded` and `aria-controls`. Its hit area as a link's: display inline-flex; align-items center; min-height calc(`space-10` + `space-1`); padding-inline `space-2`; margin-inline calc(`space-2` × −1). On mouse hover (hover: hover): color `ink`. The group holding the current page: color `ink`.
- **Chevron:** the 16px chevron after the group link's text, with no empty space around it, so the next link is also `space-6` from it. margin-inline-start `space-2`; color `mute`; transition transform `duration-base` `ease-out`. Open: transform rotate(`flip`). Under reduced motion: transition none.
- **Sub-links:** the group opens the Menu below the link, aligned to its text, `space-2` under its 44px hit area: top calc(100% + `space-2` + (`space-10` + `space-1` − the `label-md` line-height) / 2). The sub-links are a list of links with the Menu's look, without `role="menu"`.

**Tools at the end**

- **Tools:** at the end, never more than three: the avatar and the call to action exclude each other, and one of the two is always there (a signed-in person has the avatar, a visitor has the call to action); search, theme and language are optional. The order is always search, theme, language, then the avatar or the call to action; with the avatar or the call to action, at most two of the optional ones. No line between them. margin-inline-start auto; display flex; align-items center; gap `space-6`.
- **Tool spacing:** the visible edge of each tool (icon, text or avatar) is `space-6` from the visible edge of the next one, so the spaces are equal whatever the tools are: each button's padding is taken out of the layout. An icon button with a 20px icon: margin-inline calc(`space-2` × −1). The search button: margin-inline calc((`button-md` − `icon-sm`) / 2 × −1). A text button: margin-inline calc(`space-4` × −1). The call to action keeps its edge.
- **Tool menus:** the Language and Account menus open below their button and end on its end edge: inset-inline-start auto; inset-inline-end 0. Button and menu sit in one wrapper: position relative; display inline-flex.

**Phones**

- **Phone layout:** below `md`, and from `md` up to the width where the links and tools fit on one line. The bar: padding-inline `space-4`. The links, the Language button and the call to action: display none; they move into the navigation panel. Search, Theme and the Avatar stay at the end, `space-6` apart; their tooltips align to their end edge: inset-inline-start auto; inset-inline-end 0; transform none.
- **Menu button:** at the start, before the logo: an icon-only tertiary Button, label "Open menu", its padding taken out of the layout. display inline-flex. The logo: margin-inline-start `space-4`. It is a disclosure with `aria-expanded` and `aria-controls` pointing to the panel.
- **Menu icon:** Hugeicons `Menu01` at `icon-md`; its three paths: transform-box fill-box; transform-origin center; transition transform `duration-base` `ease-out`, opacity `duration-base` `ease-out`. Open: the top path transform translateY(7 of the icon's 24 units) rotate(45deg), the bottom one translateY(−7 of 24 units) rotate(−45deg) (the translate written after the rotate, so it is applied last); the middle one opacity 0; the label becomes "Close menu". Under reduced motion: transition none.
- **Navigation panel:** opened by the menu button; the bar extends downward. The panel starts at the bar's top, so one `canvas` background covers both with no seam, and sits behind the bar's own content. position absolute; top 0; inset-inline 0; z-index `zIndex-base`; display flex; flex-direction column; padding calc(`space-8` × 2 + the top safe area + `space-4`) `space-4` `space-4`; background `canvas`. The bar's own content: position relative; z-index `zIndex-raised`. While it is open, the bar is solid: background `canvas`. (replaced in: glassmorphism)
- **Panel motion:** it reveals from the top, never by animating its height. Closed: clip-path inset(0 0 100% 0); visibility hidden; transition clip-path `duration-base` `ease-in`. Open: clip-path inset(0); transition clip-path `duration-slow` `ease-out`.
- **Panel reduced motion:** it only fades. clip-path none; opacity 0; transition opacity `duration-base` `ease-in`. Open: opacity 1; transition opacity `duration-slow` `ease-out`.
- **Open stacking:** while the panel is open, and until it has closed, the bar and the panel: z-index `zIndex-modal`; the page below does not scroll.
- **Scrim:** under the open bar. position fixed; inset 0; z-index `zIndex-overlay`; background `scrim`; opacity 0; transition opacity `duration-base` `ease-in`. Open: opacity 1; transition opacity `duration-slow` `ease-out`.
- **Panel order:** the links, then Language, then the call to action. Only the tools the project keeps appear. Links and tools carry no group titles.
- **Panel link:** a row of the panel; its chevron (margin-inline-start auto) lines up with the bar's tools. display flex; width calc(100% + `space-4`); color `body`; font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`. The row itself draws no line: its ::after content none.
- **Panel text:** the text of a panel link, in a span. position relative. In the current page's link, the current-page line, still, as wide as the text: ::after content ""; position absolute; inset-inline 0; top calc(100% + `space-1` − `line-thick`); height `line-thick`; border-radius `rounded-full`; background `ink`. The current page's link: color `ink`; `aria-current="page"`.
- **Sub-links in the panel:** a link with sub-links is a row that expands and collapses: a button with `aria-expanded`, with the link focus underline. The sub-links, and the Language options, open and close like the Accordion's answer. The panel opens with the group of the current page expanded and the others collapsed. The list: position relative; padding-inline-start `space-4`; display flex; flex-direction column.
- **Guide:** the sub-links' ::before, on their start side, from the top of the first sub-link's text to the bottom of the last one's. content ""; position absolute; inset-block calc((`space-10` + `space-1` − the `body-lg` line-height) / 2); inset-inline-start 0; width `line-thin`; background `hairline`.

**Keyboard and screen readers**

- **Landmarks:** `<header>` with `<nav aria-label="Main">`; Tab moves through the links and tools in the order of the page.
- **Open panel:** while the panel is open, Tab stays inside the bar and the panel; Escape, a tap on the scrim or the menu button closes it, and focus returns to the menu button. The language options in the panel are radios.
