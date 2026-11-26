# Toast

**Uses:** Alert.

**Purpose:** a short floating message about what the user just did ("Lunch saved") or what just failed ("Could not save your meal"), shown for a moment and then gone. A message that belongs to the page and stays in it is an Alert.

- **Kinds:** success, info, warning and error, with the same icons and colors as the Alert.
- **Hierarchy:** one line: the icon's circle, then the title, then the action or the close button. The title is the focal point (The One Winner Rule): a statement of what happened in `title-sm` `ink`; the circle in the kind's vivid colour names the kind; the time bar only shows the time left.
- **Elements:** the Toast's own: host, toast, icon circle, close button, time bar. Other components: the container, the title, the action and the close button (Alert).
- **Add-on files:** read only the file of each add-on that the part being built or checked contains: Action `references/components/toast/action.md`.
- **Host:** where the toast shows: bottom centre, `space-4` from the side edges, above the bottom safe area. position fixed; inset-inline 0; margin-inline auto; bottom calc(`space-4` + the bottom safe area); z-index `zIndex-toast`; width min(`panel`, calc(100% − `space-8`)). From `md` up: bottom calc(`space-6` + the bottom safe area). It sits `space-4` above a FAB or the Cookie banner when one is there.
- **Layer:** the `toast` layer of the `zIndex` scale, above dialogs and sheets (Stacking order).
- **Toast:** the Alert's container (tint, border and raised effect of the kind, radius, padding, at least `space-12` tall), opaque, so the content behind never shows through: background-color color-mix(in srgb, the kind's vivid colour `mix-tint`, `surface-float`). (replaced in: glassmorphism)
- **Title:** as the Alert's title, one line, a statement of what happened ("Lunch deleted"), never a question or an apology. A toast has no message under the title: it follows what the user just did, so the title alone says it.
- **Icon circle:** the Alert's circle, smaller for the single line. width `space-6`; height `space-6`. Its icon: width `icon-sm`; height `icon-sm`. (replaced in: glassmorphism)
- **Close button:** the Alert's close button (Alert, Close), the size of the icon's circle; its hit area stays 44px (Button, small). width `space-6`; height `space-6`. Its icon: width `icon-sm`; height `icon-sm`.
- **Escape:** closes a toast only when no menu, popover, dialog or sheet is open; otherwise it closes that overlay first.
- **Duration:** 3 seconds for a success or info confirmation; 5 seconds when it offers "Undo", and for a warning (Usability 1 and 3). An error has no timer: it stays until "Try again" or Escape, because a failure must not disappear unread (WCAG 2.2.1).
- **Time bar:** a timed toast's ::after shows its time left along the bottom edge, following the corners, emptying from its end edge; it never fills, so it does not read as Progress. content ""; position absolute; inset auto 0 0 0; height `space-4`; border-radius 0 0 `rounded-lg` `rounded-lg`; background linear-gradient(to top, the kind's vivid colour `line-thick`, transparent `line-thick`); pointer-events none; animation over the toast's duration `ease-linear` forwards, clip-path from inset(0 0 0 0) to inset(0 100% 0 0) (to inset(0 0 0 100%) under `[dir="rtl"]`).
- **Stopped time:** a click or tap on the toast, or keyboard focus inside it, stops the time and the toast stays until it is closed. The time bar: animation-play-state paused; opacity 0; transition opacity `duration-fast` `ease-in`.
- **One at a time:** a new toast replaces the current one.
- **Announcement:** role `status` for success and info, role `alert` for warning and error; focus never moves to it.
- **Motion in:** animation `duration-base` `ease-out`, from opacity 0 and transform translateY(`space-1`).
- **Motion out:** animation `duration-fast` `ease-in` forwards, to opacity 0.
- **Reduced motion:** in, a fade only: from opacity 0. The time bar: animation none, so it stays full.
