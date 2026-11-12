# Spacing

**Consistency.** The goal is not "8px everywhere": it is consistent spacing. Every margin, padding, gap, offset and element size comes from one small scale, repeated across the whole project. Consistency beats improvisation.

## Scale

**Base unit** 8px, with 4px half-steps for fine adjustments. Token names count 4px units: `space-N` = N × 4px, so the name tells the value.

| Token | Value | Role | When to use it |
|---|---|---|---|
| `space-1` | 4px | Micro adjustment | Icon ↔ text inside badges, title ↔ subtitle, label ↔ helper text |
| `space-2` | 8px | Base unit | Tight groups: items in a compact list, buttons in a toolbar, label ↔ input |
| `space-3` | 12px | Half-step (8 + 4) | Only where a rule of `references/rules/` or of a component's file sets it |
| `space-4` | 16px | Small gap | Icon spacing in lists and cards, gap between related items, page side margin on phones |
| `space-5` | 20px | Half-step (16 + 4) | Only where a rule of `references/rules/` or of a component's file sets it |
| `space-6` | 24px | Medium gap | Default card padding, gap between sections inside a card, gap between fields in a form |
| `space-8` | 32px | Large gap | Card outer margin, gap between cards, layout gutters, page side margin from tablet up |
| `space-10` | 40px | Half-step (5 × 8) | Only where a rule of `references/rules/` or of a component's file sets it |
| `space-12` | 48px | Section spacing | Space between page sections in App mode |
| `space-32` | 128px | Site section spacing | Space between page sections in Site mode, below `md` |
| `space-48` | 192px | Site section spacing | Space between page sections in Site mode, from `md` |

**Primary scale.** The primary scale is 4 / 8 / 16 / 24 / 32 / 48. The half-steps 12, 20 and 40 are used only where a rule of `references/rules/` or of a component's file sets them; the agent never picks a half-step on its own. `space-32` and `space-48` are used only between page sections in Site mode. No other values.

## Rules (binding)

1. **The Token-Only Rule.** Every margin, padding, gap and offset (top, left, inset, translate) uses a `space-*` token. Never a free number, never an arbitrary value.
2. **No random values.** Never 10, 11, 13, 14, 19, 22, 23, 27, 31px. If a value is missing, round to the nearest token.
3. **Keep the scale small.** Never add a token for a single case. Repeat the existing ones.
4. **Uniform padding.** The same value on all four sides of a container and on every container of the same kind.
5. **Everything that adds space follows the scale:** card padding, gaps between sections, text spacing, button sizes, layout margins, icon spacing.
6. **Element sizes are multiples of 8** (4 when needed): icons 16 / 20 / 24, avatars 24 / 32 / 40 / 48, controls 32 / 36 / 40 / 44, bars 56 / 64.
   - **Which size:** a component uses its default size, unless the component that contains it sets another. The other sizes are used only where `references/rules/` or a component's file names them or on the user's request.
7. **The grid applies to containers, not to text.** Element sizes, padding and gaps follow the scale. Line-heights come from the type scale and the script factor (Typography), and need not be multiples of 4.
8. **Borders don't count.** A 1px border is not spacing: use border-box sizing and fixed heights so a border never forces off-grid padding (no `7px 15px` to compensate).
9. **Use relative units.** Implement tokens in `rem` (1rem = 16px) so spacing follows the user's text size and zoom.

## Proximity and hierarchy

**Proximity.** Spacing tells the reader what belongs together.

- **Inside < between.** Space inside a group is always smaller than space between groups: label ↔ input `space-2`, field ↔ field `space-6`, section ↔ section `space-12` in App mode, `space-32` / `space-48` in Site mode.
- **The Distance Ratio Rule (binding).** The space between two groups is at least twice the space inside each group. Below that ratio the eye reads them as one group. Examples: label ↔ input 8, field ↔ field 24; card rows 12, header ↔ rows 24, rows ↔ actions 32. Inside a page section, outside a component, each level takes half the space of the level above it, starting from `space-12` (48px): groups `space-6` (24px) apart, the parts of a group `space-3` (12px) apart; title ↔ subtitle stays `space-1`.
- **Alignment confirms the group.** Grouped elements share an axis (left edge, baseline or grid column); proximity without alignment looks accidental.
- **Density never collapses groups.** When content must be dense, keep the ratio and reduce the elements (fewer, smaller), never the ratio.
- **Space the siblings from the parent.** Put the gap on the container (flex or grid gap, stack spacing) instead of margins on each child, so gaps never collapse or double.
- **Grouping actions.** Related actions sit `space-2` apart (`space-3` between 32px buttons, Adjacent targets); different groups at least `space-4`; a destructive action is always its own group. Rare actions go in a "More" menu, grouped by category with space or a label, destructive last.
- **Whitespace is structure.** Group with space first; add a divider only when space alone cannot separate the groups.

## Reference values

| Situation | Token | Value |
|---|---|---|
| Title ↔ subtitle | `space-1` | 4px |
| Label ↔ input | `space-2` | 8px |
| Gap between page sections | App: `space-12`; Site: `space-32`, `space-48` from `md` | 48px; 128px, 192px |
| Page side margin | `space-4` phone, `space-8` tablet and up | 16px / 32px |

## Accessibility

**Priority.** Accessibility has the same priority as the grid. When the two conflict, usability wins.

- **Touch targets** are at least 44 × 44px, 48px preferred, as in the Apple Human Interface Guidelines and WCAG 2.5.5; the AA minimum of WCAG 2.5.8 is 24px. A smaller control extends its hit area to 44px with padding or an invisible overlay. Two exceptions, whose items touch and are each their own hit area: menu items, 40px tall, so the menu stays compact (Menu); links in a list, 32px rows when the device has no touch screen and 44px with any touch screen (`any-pointer: coarse`), so a column of links stays compact (Footer).
- **Adjacent targets** are at least `space-2` (8px) apart, measured between visible edges, and their 44px hit areas never overlap, so a finger never hits the wrong one: two 32px targets sit `space-3` (12px) apart, larger ones `space-2`.
- **Never shrink spacing below the scale to fit content.** Change the layout instead: wrap, stack, scroll or cut content.
- **Zoom.** Layouts must hold at 200% text zoom without overlapping or cutting text.
- **Focus never covered.** An element fixed or sticky at an edge of the page sets a `scroll-padding` of its height on that edge, so it never covers the focused element (WCAG 2.4.11).
- **Drag has an alternative.** Every drag can also be done with a single tap or click (on the target, or with buttons) and with the keyboard (WCAG 2.5.7).
- **Skip link.** The first focusable element of every page is a "Skip to content" link that moves focus to `<main>`; hidden until focused, it then shows as an `elevated` button at the top start corner, `space-2` from the edges, `zIndex` `toast` (WCAG 2.4.1).
- **Focus after a route change.** In a single-page app, focus moves to the new page's `<h1>` (`tabindex="-1"`) and the document title changes. A multi-page site does this on its own.

## Common mistakes

- **Random values** everywhere (`padding: 13px 22px`).
- **Too many spacing tokens.**
- **Different padding** on cards of the same kind, or on different sides of one card.
- **Mixing 10, 14, 23, 31px** with no reason.
- **No scale** defined at all.

## Implementation

**Tokens in any stack.** Kore is stack-agnostic. Expose the scale as tokens in whatever the project uses: CSS custom properties, a Tailwind theme, an SCSS map, Swift or Kotlin constants. Reference in CSS:

```css
:root {
  --space-1: 0.25rem;  /*  4 */
  --space-2: 0.5rem;   /*  8 */
  --space-3: 0.75rem;  /* 12, half-step */
  --space-4: 1rem;     /* 16 */
  --space-5: 1.25rem;  /* 20, half-step */
  --space-6: 1.5rem;   /* 24 */
  --space-8: 2rem;     /* 32 */
  --space-10: 2.5rem;  /* 40, half-step */
  --space-12: 3rem;    /* 48 */
  --space-32: 8rem;    /* 128, Site sections */
  --space-48: 12rem;   /* 192, Site sections */
}
```

**Border-box.** Every element has `box-sizing: border-box`, so its padding and border sit inside the width it is given.
