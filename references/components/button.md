# Button

**Uses:** Menu, Tooltip.

**Set:** five variants, three sizes, one shape, plus the floating action button. Every button has all its states.

- **Hierarchy:** among the buttons of one decision, the primary is the focal point (The One Primary Rule): filled with `primary` and raised. The destructive has the same weight in `danger`; the elevated is raised but neutral; the secondary shows only its ring; the tertiary only its label. Inside a button there is one thing to read: the label in `label-lg`, or the icon on an icon button.
- **Elements:** the Button's own: button, label, hit area, icon, rest label, busy label, spinner, FAB, FAB menu, FAB menu item. Other components: the Tooltip of icon buttons and of the FAB; the Menu, whose behaviour the FAB menu takes. The variants, the sizes and the icon button are variants of the button, not elements.
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: FAB `references/components/button/fab.md`.
- **Button:** position relative; display inline-flex; align-items center; justify-content center; gap `space-2`; height `button-md`; padding 0 `space-4`; border-radius `rounded-md`; font-family `label-lg`; font-size `label-lg`; font-weight `label-lg`; line-height `label-lg`; letter-spacing `label-lg`; white-space nowrap; outline `line-thin` solid transparent; outline-offset −`line-thin`; color `ink`; transition box-shadow `duration-fast` `ease-out`, transform `duration-fast` `ease-out`, background-color `duration-instant` `ease-out`.
- **Forced colors:** the transparent outline of the Button rule draws the edge in forced colors.
- **Labeled button:** min-width `button-min`.
- **Large button:** height `button-lg`; padding 0 `space-6`.
- **Small button:** border-radius `rounded-sm`; height `button-sm`; padding 0 `space-3`.
- **Where large:** only where a component's file names it (the Carousel's photo arrows, the Sidebar's menu button on phones) or on the user's request (Spacing, rule 6).
- **Hit area:** the ::before of default and large buttons: content ""; position absolute; inset −`space-1` 0.
- **Icon button hit area:** inset −`space-1`, on the ::before of default icon buttons and of the FAB.
- **Large button hit area:** inset 0.
- **Small button hit area:** content ""; position absolute; width max(100%, `button-lg`); height `button-lg`; no inset: the button's flex centres it.
- **Primary:** the main action of its decision (The One Primary Rule). background `primary`; color `primary-on`; the edge color `primary-edge`.
- **Destructive:** delete and other destructive actions, at most one per decision. background `danger`; color `danger-on`; the edge color `danger-edge`.
- **Elevated:** instead of secondary when the background is complex, colored or an image, where a transparent button would lose emphasis. background `surface-card`; color `ink`; the edge color `surface-card-edge`.
- **Filled:** primary, destructive and elevated: background-image `gradient-raised`; box-shadow `shadow-raised-sm`, inset 0 0 0 `line-thin` the variant's edge color. (replaced in: minimalism)
- **Secondary:** box-shadow inset 0 0 0 `line-thin` `hairline-medium`. The supporting action next to a primary or a destructive (Secondary alone).
- **Tertiary:** low-priority actions and secondary options; the cancel action in a dialog; any number per decision. No background, no ring and no shadow at rest.
- **Shadows:** only on filled buttons (primary, destructive) and on elevated; secondary and tertiary take `shadow-raised-sm` only in hover, with the background change.
- **Borders:** box-shadow rings, so they never change the button's size: inside the edge (inset) on every variant, so buttons side by side look the same size.
- **Filled hover:** on mouse hover (hover: hover), primary, destructive and elevated: transform translateY(−`space-1`). (replaced in: minimalism)
- **Secondary and tertiary hover:** background-color `surface-hover`; background-image `gradient-raised`; box-shadow `shadow-raised-sm`.
- **Secondary hover:** box-shadow `shadow-raised-sm`, inset 0 0 0 `line-thin` `hairline-medium`. (replaced in: minimalism)
- **Pressed:** transform none; box-shadow `shadow-rest`; transition-duration `duration-instant`. (replaced in: minimalism)
- **Primary pressed:** background-color `primary-pressed`.
- **Destructive pressed:** background-color `danger-pressed`.
- **Elevated pressed:** background-color `surface-elevated`.
- **Filled pressed:** box-shadow `shadow-raised-pressed`, inset 0 0 0 `line-thin` the variant's edge color. (replaced in: minimalism)
- **Secondary and tertiary pressed:** background `surface-pressed`; box-shadow none.
- **Secondary pressed:** box-shadow inset 0 0 0 `line-thin` `hairline-medium`.
- **On an overlay:** secondary and tertiary inside an overlay take `surface-float-active` in hover and when pressed.
- **Disabled:** background `surface-elevated`; color `stone`; box-shadow none; cursor not-allowed; transform none. Explain why it is disabled when it is not obvious.
- **Secondary disabled:** background none; box-shadow inset 0 0 0 `line-thin` `hairline`, its own container as in Material 3.
- **Tertiary disabled:** background none.
- **Focus:** see States: on :focus-visible outline none, and the corner marks are an ::after drawn only on :focus-visible.
- **Link button:** a button that takes the user to another page is a link (`<a href>`) with the look of a button: text-decoration none.
- **Link button focus:** on :focus-visible: outline none; text-decoration underline `line-thick`; text-underline-offset `space-1`, all changed in 0s (the link focus underline, States).
- **Icon button:** one `icon-md` icon, an accessible label and a tooltip. width `button-md`; padding 0.
- **Large icon button:** width `button-lg`; padding 0.
- **Small icon button:** width `button-sm`; padding 0.
- **Icon:** flex none; display block.
- **No icons on labeled buttons:** a Button with a label shows only text, plus the spinner while loading (Loading). A sign-in provider's logo is not an icon but part of its name, as the provider requires (Sign in). Buttons inside a control are part of the control and keep `icon-sm` icons (Icons). The rule is for the Button component, not every `<button>` element: rows, selects, accordions, chips and menu items follow their own component's rules.
- **Labels:** a verb and an object, never "OK", "Yes" or "Submit", in sentence case, never all caps.
- **Secondary alone:** a secondary stands without a primary only in a decision with no main action (The One Primary Rule), as in the Cookie banner.
- **Loading:** cursor progress; `aria-busy="true"` and `aria-disabled="true"`, so it ignores further clicks and keeps its place in the Tab order; it returns to rest when the action ends.
- **Loading cell:** the button that holds a busy label: display inline-grid; place-items center.
- **Rest label and busy label:** grid-area 1/1, one cell, so the button keeps the longer label's width.
- **Busy label:** display inline-flex; align-items center; gap `space-2`; visibility hidden. The spinner, then the label that names the action in progress in the page's language, ending in "…".
- **Rest label while loading:** visibility hidden.
- **Busy label while loading:** visibility visible.
- **Spinner:** an `icon-sm` SVG, viewBox 24, a three-quarter arc of radius 9, stroke currentColor, stroke-width 2, round caps. animation spin `duration-spin` `ease-linear` infinite.
- **Reduced motion:** transform none; transition 0s on every property; no lift on touch either.
