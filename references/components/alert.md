# Alert

**Uses:** Button, Tooltip.

**Purpose:** an inline message about the state of what the user is looking at. It sits in the page, above the content it concerns, and never covers anything. A single field's error stays with the field (Form fields).

| Kind | Icon (Hugeicons) | Vivid color | Semantic color | Role after the page loaded |
|---|---|---|---|---|
| Info | `Message01` | `vivid-info` | `info` | `status` |
| Success | `Tick01` | `vivid-success` | `success` | `status` |
| Warning | `Alert01` | `vivid-warning` | `warning` | `alert` |
| Error | `FileX` | `vivid-danger` | `danger` | `alert` |

- **Hierarchy:** the icon comes first, then the title with the message under it, then the action or the close. The title is the focal point (The One Winner Rule): `title-sm` in `ink`, read before the message (`body-md` in `ink`) and the button. The icon names the kind together with the title, never alone.
- **Elements:** the Alert's own: stack, alert, icon box, icon (the kind's icon in the table, `icon-md`), text, title, message, action slot. Other components: the action (Button, tertiary, small) or the close (Button, tertiary icon, small, with a Tooltip), inside the action slot. The kinds are variants of the alert, not elements.
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Action `references/components/alert/action.md`, Close `references/components/alert/close.md`.
- **Stack:** display flex; flex-direction column; gap `space-4`.
- **Alert:** position relative; display flex; align-items flex-start; gap `space-3`; width 100%; min-height `space-12`; max-width `dialog`; padding `space-2` `space-2` `space-2` `space-4`; border-radius `rounded-lg`; color `ink`.
- **Container:** background-color color-mix(in srgb, the kind's vivid color `mix-tint`, `canvas`); box-shadow `shadow-raised-rim`, inset 0 −`line-thick` 0 color-mix(in srgb, the kind's vivid color `mix-ledge`, transparent), 0 0 0 `line-thin` color-mix(in srgb, the kind's semantic color `mix-edge`, transparent). (replaced in: minimalism, glassmorphism)
- **Icon box:** align-self center; display grid; place-items center; flex none; width `space-8`; height `space-8`.
- **Icon circle:** border-radius `rounded-full`; corner-shape round; background-color the kind's vivid color; background-image `gradient-raised`; box-shadow `shadow-raised-sm`, 0 0 0 `line-thin` color-mix(in srgb, the kind's vivid color `mix-icon-edge`, `ink`); color `on-vivid`. (replaced in: minimalism)
- **Icon:** width `icon-md`; height `icon-md`.
- **Text:** flex 1; min-width 0; align-self center; display flex; flex-direction column; gap `space-1`.
- **Title:** font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; color `ink`.
- **Title text:** one line, a statement that names the situation.
- **Message:** font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `ink`.
- **Message text:** every alert has a message under the title: what happened and what to do next, never a restatement of the title. The message of an alert with an action does not name the fix.
- **Action slot:** flex none; align-self center; margin-inline-start `space-3`.
- **No auto-close:** an alert never closes by itself: it stays until its state changes or the user closes it. A message that should disappear after a moment is a Toast.
- **Announcement:** an alert present when the page loads has the role `status`; one that appears after has the role of its kind in the table. `alert` interrupts the reader; `status` waits for a pause.
- **Focus:** focus does not move to an alert; when an alert closes, focus moves to the next focusable element after it.
- **Stacking:** two or more alerts on one screen go in one stack, the most severe first: error, warning, info, success (The Distance Ratio Rule).
