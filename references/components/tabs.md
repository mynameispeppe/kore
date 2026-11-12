# Tabs

**Uses:** Segmented control, Cards.

**Purpose:** tabs switch between views of the same content: a bar of text tabs with the role `tablist`, plus a panel. They never take the Segmented control's container, so the two never look alike.

- **Use:** two to four short labels (The Working Memory Rule); for more, use a select. A tab never starts an action or opens another page: that is a button or a link.
- **Hierarchy:** the bar comes first, then the panel. The selected tab is the focal point of the bar (The One Winner Rule): the only label in `ink` with the indicator under it; the other tabs in `mute` only guide. The panel's content is what the user reads.
- **Elements:** the Tabs' own: bar, tab, indicator, reduced-motion line, panel. Other components: the panel's card (Cards), the view motion (Segmented control).
- **Bar:** as wide as its container, with a line along its bottom edge. position relative; display flex; gap `space-6`; width 100%; padding 0; background none; border-radius 0; outline none; box-shadow inset 0 calc(`line-thin` × −1) `hairline-medium`.
- **Tab:** as wide as its label. position relative; height calc(`space-10` + `space-1`); padding 0; color `mute`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`; transition color `duration-base` `ease-in-out`.
- **Tab hover:** on mouse hover (hover: hover): color `ink`.
- **Selected tab:** color `ink`.
- **Disabled:** every tab: color `stone`; cursor not-allowed.
- **Focus:** the corner marks of States around the tab, with the radius `rounded-sm`. On :focus-visible: outline none, changed in 0s.
- **Indicator:** the bar's ::after, one line on the bar's bottom edge, as wide as the selected tab, square ends; the script sets the selected tab's start and width. content ""; position absolute; inset-block-end 0; inset-inline-start 0; width `line-thin`; height `line-thick`; background `ink`; pointer-events none; transform-origin left; transform translateX(the tab's start) scaleX(the tab's width ÷ `line-thin`). Under `[dir="rtl"]`: transform-origin right; translateX(the tab's start × −1).
- **Indicator motion:** on a tab change it moves to the new tab with transform only, never left or width: transition transform `duration-base` `ease-in-out`. On load it is placed with no transition.
- **Reduced motion:** the indicator: display none. Each tab draws its own line with ::before: content ""; position absolute; inset-inline 0; inset-block-end 0; height `line-thick`; background `ink`; opacity 0; pointer-events none; transition opacity `duration-base` `ease-in-out`. The selected tab's line: opacity 1.
- **Panel:** `space-4` under the bar, a Card (Cards) holding the content of the selected tab; its title, when it has one, names the content and never repeats the tab's label. One panel is visible at a time. In a column with gap `space-6`: margin-top calc(`space-4` − `space-6`).
- **View motion:** switching tabs moves the content with the Segmented control's View motion; the card stays still.
- **Markup:** `role="tablist"` with an accessible name on the bar; `role="tab"`, `aria-selected` and `aria-controls` on each tab; `role="tabpanel"`, `aria-labelledby` and `tabindex="0"` on the panel. Only the selected tab has `tabindex="0"`.
- **Keyboard:** Left and Right Arrow move to the previous and next tab (from the last to the first) and select it, swapped under `[dir="rtl"]`; Home and End go to the first and the last; Tab leaves the bar for the panel.
- **URL:** the open tab lives in the URL (Usability 3), so a link or a reload shows the same tab.
