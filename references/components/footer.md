# Footer

**Uses:** Top bar, Social links.

**Purpose:** it closes the page with the secondary links. The user chooses the variant: Standard, Centered or Brand. The agent builds the chosen one and never two.

- **Not chosen:** Standard. Say it in one line ("footer: Standard; say if you want Centered or Brand").
- **Hierarchy:** the logo comes first, then the columns, then the bottom row. The logo is the focal point (The One Winner Rule): `title-lg` in `ink`, the largest type of the footer. Each nav's heading follows in `label-lg` `ink`; the links in `body-md` `mute` and the bottom row in `body-sm` `mute` only serve.
- **Elements:** the Footer's own: footer, footer logo, link grid, logo cell, column, column heading, column list, link in a list, link on touch, link hover, link focus, nav link, bottom row, bottom link, centered footer, centered row, centered social links, copyright, brand cell, product line, brand social links. Other components: the logo (Top bar) and the social links (Social links, Icon-only link).
- **Footer:** a `<footer>` under the content, the content's width, like the Top bar. display flex; flex-direction column; gap `space-12`; padding-top `space-12`; border-top `line-thin` solid `hairline`.
- **Footer logo:** the Top bar's logo, a link to the home page with the accessible name "<product>, home". min-height auto.
- **Standard:** the link grid, then the bottom row.
- **Link grid:** the logo cell, then at most 3 columns. display grid; grid-template-columns repeat(4, minmax(0, 1fr)); gap `space-8`.
- **Link grid below sm:** grid-template-columns repeat(2, minmax(0, 1fr)); gap `space-8` `space-4`.
- **Logo cell:** the first cell, holding the logo. Below `sm`: grid-column 1/-1, so it takes its own row.
- **Column:** a `nav` named by its heading (`aria-labelledby`). display flex; flex-direction column.
- **Column heading:** an `h4`, one level below the heading before the footer. margin 0 0 `space-2`; color `ink`; font-family `label-lg`; font-size `label-lg`; font-weight `label-lg`; line-height `label-lg`; letter-spacing `label-lg`.
- **Column list:** a `ul` of links in a list. list-style none; margin 0; padding 0.
- **Link in a list:** the rows touch, with no space between them. display flex; align-items center; min-height `space-8`; color `mute`; text-decoration none; transition 0s.
- **Link on touch:** with any touch screen (any-pointer: coarse): min-height calc(`space-10` + `space-1`) (Touch targets).
- **Link hover:** on mouse hover (hover: hover): color `ink`, changed in 0s.
- **Link focus:** on :focus-visible: outline none; color `ink`; text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s (the link focus underline, States).
- **Nav link:** each link inside an `li`. font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Bottom row:** "© <year> <product>" on the left, the contact on the right. display flex; flex-wrap wrap; align-items center; justify-content space-between; gap `space-4`; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Bottom link:** the contact, a `mailto:` link in a list. display inline-flex.
- **Centered footer:** for a site whose pages fit in one row of links. In order: the logo, the centered row, the centered social links, the copyright. No columns and no contact. align-items center; text-align center; gap `space-6`.
- **Centered row:** a `nav` with `aria-label="Footer"` holding one `ul` of nav links. list-style none; margin 0; padding 0; display flex; flex-wrap wrap; justify-content center; column-gap `space-6`.
- **Centered social links:** justify-content center.
- **Copyright:** "© <year> <product>" in a `p`. margin 0; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Brand:** Standard, with the brand cell in place of the logo cell and at most 2 columns.
- **Brand cell:** the logo, the product line, the brand social links. grid-column span 2; gap `space-4`. Below `sm`: grid-column 1/-1.
- **Product line:** one line about the product in a `p`. margin 0; color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Brand social links:** pulled back, so the first icon lines up with the product line. margin-inline-start −`space-3`.
- **Version labels:** only when the product really is in preview (AI tells).
