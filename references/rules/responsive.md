# Responsive

**Adapting** is rethinking the experience for each context, not scaling pixels down. A phone gets phone patterns; a desktop uses its space.

## Principles

- **Mobile-first.** Base styles are for the smallest screen; larger screens add layout with `min-width` queries.
- **Same structure everywhere.** The information architecture and naming never change between screen sizes; only the layout does.
- **Nothing important hidden on mobile.** If a function matters, it works on a phone.
- **Content decides which breakpoint to use.** For each layout change, find two widths: **A**, where the narrow layout breaks as it widens; **B**, where the wide layout breaks as it narrows. The change goes at the lowest breakpoint token between B and A. If no token falls between B and A, the breakpoint is missing: propose it, wait for approval, and it becomes a token (Never invent values). Never target a device model.

## Breakpoints

| Token | From | What changes |
|---|---|---|
| base | 0 | Phone: one column, side margin `space-4`, primary controls within thumb reach |
| `sm` | 640px | Large phones and landscape: card grids up to 2 columns |
| `md` | 768px | Tablet: 2 columns, list + detail views, side margin `space-8` |
| `lg` | 1024px | Desktop: multi-column layouts, extra information on hover |
| `max-content` | 1200px | Content stops growing; wider screens add margin, never stretch text or cards |

## Grids

- **Columns** step 1 → 2 → 3 as space allows; gutters step `space-4` → `space-6` → `space-8`.
- **Prefer layouts that reflow** on their own (flex wrap, auto-fit grids) and container queries for a component used at different widths (a card in a sidebar and in a full-width page), so it adapts to its own box instead of the viewport.

## Typography

- **Below `sm`**, display roles step down one level: `display-lg` 57 → 45, `display-md` 45 → 36. Line-height steps with the role (64 → 52, 52 → 44).

## Input

- **Detect the input**, not the screen size: `(hover: hover)` and `(pointer: fine)` for mouse and trackpad, `(hover: none)` and `(pointer: coarse)` for touch.
- **Hover is an enhancement only**, never the only way to reach a function. The hover lift from Elevation applies only where hover exists; on touch, the pressed state carries the feedback.

## Safe areas

- **Fixed bars and full-bleed content** respect the notch, rounded corners and home indicator with `env(safe-area-inset-*)`, and the viewport uses `viewport-fit=cover`.

## Extremes

- **Layouts work** from 320px wide to 4K, in portrait and landscape on phones and tablets, and at 200% text zoom.
- **The page never scrolls horizontally.** Only tables and code blocks may be wider, each inside its own scroll container.
- **Long names, long translations and empty states** never break the layout. Text that can hold an unbroken string, such as URLs, IDs, emails or user content, has `overflow-wrap: anywhere`.
- **Full-height areas** use `100dvh`, never `100vh`, which ignores the browser bars on phones.

## Testing

**Real devices.** Test on at least one real iPhone and one real Android phone, in Safari, Chrome and Firefox, with a throttled network. Browser device emulation is useful for layout but misses real touch, performance and keyboards.
