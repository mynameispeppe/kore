# Tooltip

**Uses:** Overlay rules, Button.

**Purpose:** a short label that names or explains a control while the pointer is on it or it has keyboard focus.

- **Use:** every icon-only button has one.
- **Hierarchy:** one thing to read, the text; the `ink` background is the one inverted overlay, so it separates from anything below it without a shadow.
- **Elements:** the Tooltip's own: wrapper, tooltip. Other components: the trigger (Button).
- **Wrapper:** around the trigger. position relative; display inline-flex.
- **Tooltip:** the text wraps and a word longer than the line (a file name) breaks, so nothing is cut. position absolute; z-index `zIndex-tooltip`; background `ink`; color `canvas`; border-radius `rounded-sm`; padding `space-1` `space-2`; width max-content (the CSS keyword, not the token); max-width `tooltip`; overflow-wrap anywhere; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Pointer:** it shows only while the pointer is on the trigger and hides as soon as it leaves, even onto the tooltip (user decision 2026-11-11, over the hoverable part of WCAG 1.4.13). pointer-events none.
- **Above:** above its trigger, centred. bottom calc(100% + `space-2`); inset-inline-start 50%; transform translateX(−50%), translateX(50%) under `[dir="rtl"]`.
- **Below:** when there is no room above (the top edge of the screen, the Top bar). bottom auto; top calc(100% + `space-2`).
- **Side:** in the Sidebar rail, on the end side, centred vertically on the icon, so it never covers the neighbouring rows. bottom auto; top 50%; inset-inline-start calc(100% + `space-2`); transform translateY(−50%).
- **End aligned:** a trigger at the end edge of a field, card or panel (clear, show password, close, more options) aligns the tooltip's end edge with its own, so it never overflows. inset-inline-start auto; inset-inline-end 0; transform none.
- **Start aligned:** a trigger at the start edge of the screen (the phone menu button) aligns the tooltip's start edge with its own. inset-inline-start 0; transform none.
- **Hidden:** at rest. opacity 0; visibility hidden; transition opacity `duration-fast` `ease-out`, visibility 0s linear `duration-fast`, so visibility switches only after the fade.
- **Shown:** immediately on mouse hover (only where the pointer can hover, never on touch) and while the trigger has :focus-visible. opacity 1; visibility visible; transition opacity `duration-fast` `ease-out`.
- **After a click:** never shown after a mouse click: a click hides it until the pointer leaves the trigger. opacity 0 !important; visibility hidden !important.
- **Escape:** hides it before it closes any other overlay; it shows again on the next hover or focus.
- **Content:** plain text only, never links or buttons. Role `tooltip`.
- **Accessible name:** a tooltip that repeats its trigger's accessible name is `aria-hidden="true"`. One that adds information (for example why an action is disabled) is linked with `aria-describedby`, and that action uses `aria-disabled="true"`, not the HTML attribute disabled, so it still takes focus.
