# Shapes

**Superellipse.** Kore's corners take their radius from the `rounded` scale and are superellipses: every element and pseudo-element has `corner-shape: superellipse(1.5)`; a browser without `corner-shape` draws circular arcs. `rounded-full` always comes with `corner-shape: round`, so circles and pills stay round. Never cut corners.

## Radius by role

| Role | Token | Value |
|---|---|---|
| Cards, sheets, dialogs, images outside a card | `xl` | 24px |
| Alerts, toasts, segmented controls, tabs, drop areas | `lg` | 16px |
| Controls (buttons, inputs, selects), menus, popovers | `md` | 12px |
| Small buttons, items inside controls and menus, tooltips, badges | `sm` | 8px |
| Anything nested inside another rounded shape | from The Concentric Rule | — |
| Pills, badge counts, avatars, status dots | `full` | 9999px |
| Full-width sections, page edges | `none` | 0 |

## Radius and padding (binding)

**The Radius-Padding Rule.** Content aligned to a side (text, icons, images, rows) starts at the centre of the corner curve: the horizontal padding equals the radius. If the padding is smaller than the radius, reduce the radius until they match. Centered content (a button label, a segment, the file drop area) never reaches the corners and is exempt.

## Nested radius (binding)

**The Concentric Rule.** A rounded shape inside another shares the centre of its corner curve, so the two curves stay parallel:

```
inner radius = outer radius − distance between the two edges
```

**Same distance.** The distance is the same on the sides and at the corner it faces.

| Case | Outer | Distance | Inner |
|---|---|---|---|
| Option inside a menu | 12 | 4 | 8, text at 4 + 8 = 12 |
| Row highlight inside a standard card | 24 | 12 | 12, text at 12 + 12 = 24 |
| Buttons in an action row (36px, radius 12) in a card or dialog | 24 | 12 | 12 |
| Corner action (32px, radius 8) in a card, dialog or sheet | 24 | 16 | 8 |
| Inline button inside a 40px field, or a 48px stepper | 12 | 8 | 4 |
| Segment inside a 48px segmented control or tab bar | 16 | 8 | 8 |

- **Two kinds of nested shape.** The formula governs a shape anchored to the container's edge as its own functional unit: the cases in the table above, plus any button, menu item or control placed near a corner. An icon, avatar or badge that simply leads a padded block of content (not anchored to an edge on its own, just the first item in a stack) is not concentric: it keeps a constant radius from the `rounded` scale and sits at the container's own padding, exactly like the text beside it.
- **Place a fixed-size element by its radius:** a button keeps its own size and radius, and its distance from the container's edge is outer radius − its radius.
- **Inline buttons** inside a control (the password toggle, stepper − and +, segments) sit 8px (`space-2`) from every edge, so the focus marks (States) never touch the container's border. Their radius is container radius − 8 (4px, `xs`, in a container with radius 12), and their size is container height − 16: in a 40px field, 24px buttons. They don't use the button sizes; their hit area extends to 44px. They have no background: the icon is 16px in `mute`, hover and pressed turn it `ink`, and the box shows only as the focus marks (States).
- **Corner actions** (a "More" or close button in the top-right corner of a card, dialog or sheet) are small icon buttons (32px, radius 8) placed with this rule: 24 − 8 = 16px from the top and the right. The header becomes a row that starts at the same 16px and is as tall as the button; the title is centred in that row, so it lines up with the button; a title on several lines centres its first line on the button. The side padding stays 24.
- **No rounded blocks with a background inside cards** unless each one is its own unit (a clickable row); rows separate with space (see The Separation Ladder).
- **Never the same radius inside and outside.**
- **Deeper nesting** applies the rule again from the parent, not from the outermost container.

## Borders inside the edge

**Hairline inside.** A border must not change the measurements the nested rule relies on. Draw the 1px `hairline` inside the element's edge without taking layout space (in CSS: `outline: 1px solid; outline-offset: -1px`, or an inset ring), so the gap between two nested edges is exactly the padding. Never a colored border thicker than 1px on one side of a card, list item, callout or alert to signal state. Use a semantic color on an icon or text instead.
