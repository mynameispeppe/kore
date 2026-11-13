# Cookie banner

**Uses:** Button, Sheet, Switch, Footer.

**Purpose:** it asks for consent to the cookies that are not necessary (GDPR).

- **Hierarchy:** the title comes first, then the three lines, then the actions. The title is the focal point (The One Winner Rule): `title-md` in `ink`, read before the lines in `body-md` and the buttons. The two choices weigh the same, so neither one leads.
- **Elements:** the Cookie banner's own: scrim, box, title, cookie icon (the Hugeicons `Cookie`), line, policy link, actions, choice pair, preferences title, categories, category, category text, category name, always on, help text. Other components: the buttons (Button, tertiary and secondary), the Sheet of the preferences, the switches (Switch), the "Cookie preferences" link (Footer).
- **When:** only when the site uses cookies that are not necessary. It appears when the page opens and blocks the page until the user has chosen.
- **Scrim:** it covers the whole screen and holds the box at the bottom right; the page behind is inert. The scrim and the box sit on the raised layer, above the content and under menus, dialogs and toasts. position fixed; inset 0; background `scrim`; z-index `zIndex-raised`; display grid; place-items end; padding `space-4`; animation `duration-slow` `ease-out`.
- **Scrim from sm:** from `sm`: padding `space-6`.
- **Box:** a modal dialog (`role="dialog"`, `aria-modal="true"`) named by its title. position static; width min(`dialog`, 100% − `space-8`); background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; border-radius `rounded-xl`; padding `space-6` `space-6` 0; display flex; flex-direction column; gap `space-1`.
- **Focus:** when it appears, focus moves to the box; Tab and Shift+Tab cycle inside it. Escape and a click on the scrim do nothing: only a choice closes it.
- **Box focus:** the box keeps its edge when it holds focus: outline `line-thin` solid `hairline`, changed in 0s.
- **Title:** it says that the site uses cookies, after the cookie icon (`icon-sm`, in the title's colour). display flex; align-items center; gap `space-2`; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`.
- **Line:** three lines under the title: what the necessary cookies do, what consent is asked for, and the link to the cookie policy on its own line. font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `body`.
- **Policy link:** color `link`.
- **Actions:** on one line, `space-3` from the box's right and bottom edges (Cards): "Customise" (Button, tertiary) at the left, "Reject" and "Accept" (Button, secondary) at the right, of equal weight and with no primary. Rejecting must be as easy as accepting (EDPB), so Reject and Accept have no main action (The One Primary Rule, Secondary alone). display flex; justify-content flex-end; flex-wrap wrap; gap `space-2`; margin `space-6` calc(`space-3` × −1) 0 0; padding-bottom `space-3`.
- **Customise slot:** the actions' first child: margin-inline-end auto.
- **Choice pair:** "Reject" then "Accept". display flex; gap `space-2`.
- **Actions below sm:** below `sm` of the screen, not of the box, the buttons stack full width, "Accept" at the bottom: flex-direction column; align-items stretch; margin-inline calc(`space-3` × −1); the first child margin-inline-end 0; the choice pair flex-direction column.
- **Preferences:** "Customise" opens a Sheet; opening it shows the saved choices; its close button keeps them. Its actions are "Accept all", "Reject all" and "Save choices", three secondary buttons of equal weight and no primary (EDPB), placed like every Sheet's actions.
- **Preferences title:** "Cookie preferences" after the cookie icon at `icon-md`, the icon size closest to `title-lg` without passing it. display flex; align-items center; gap `space-2`; font-family `title-lg`; font-size `title-lg`; font-weight `title-lg`; line-height `title-lg`; letter-spacing `title-lg`.
- **Categories:** one row per category, with no box around the list.
- **Category:** a Switch row, its Switch at the end, centred on both lines. padding-block `space-3`; max-width none.
- **Category divider:** a category after another: border-block-start `line-thin` solid `hairline`.
- **Category text:** the name, then the help text under it. display flex; flex-direction column; gap `space-1`.
- **Category name:** font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Always on:** after "Necessary" only, whose Switch is on and disabled; the other categories stay off until the user turns them on. margin-inline-start `space-2`; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Help text:** what the category's cookies do (Form fields). color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Choice:** "Reject" and "Accept" in the banner, or "Accept all", "Reject all" and "Save choices" in the Sheet, close the Sheet and the banner with its scrim, and the choice is remembered; "Accept all" and "Reject all" turn every optional category on or off. Focus moves to the start of the content; no message.
- **Leaving:** the scrim fades out in `duration-base` with `ease-in` and stays so until it is removed.
- **Changing one's mind:** a "Cookie preferences" link, always reachable in the Footer, opens the Sheet with the saved choices.
- **Reduced motion:** the scrim and the box appear and leave without fading: animation-duration 0s.
