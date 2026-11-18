# Elevation

**Depth.** Static layers separate with a surface step and a 1px `hairline`; only interactive elements cast a shadow (the inset bevel of `gradient-raised` and `shadow-raised-sm` is not one). In dark, a layer that sits higher is lighter, never darker: without a shadow, the surface step is what separates it. (replaced in: glassmorphism, minimalism)

## Levels

| Level | Recipe | Use |
|---|---|---|
| 0 · flat | `canvas`, no border, no shadow | Page background, full-width sections (replaced in: glassmorphism) |
| glow | a `*-glow` wash | Atmosphere: the default behind text alone on a wide area (Glows), elsewhere only on request; never on dense task screens (replaced in: glassmorphism, minimalism) |
| 1 · surface | `surface-card` + `hairline` | Static cards and panels (replaced in: glassmorphism) |
| 2 · inset | `surface-elevated` + `hairline` | Rows and icon wells inside a card; never a card inside a card |
| 3 · floating | `surface-float` + `hairline` | Popovers, menus; active items use `surface-float-active` (replaced in: glassmorphism) |
| 3 · inverted | `ink` with `canvas` text, no border, no shadow | Only where a component's file prescribes it |
| 4 · overlay | `surface-float` + `hairline` over a `scrim` | Dialogs and sheets (replaced in: glassmorphism) |
| interactive | its surface + `shadow-rest`, `shadow-hover` on hover; filled and elevated Buttons: `shadow-raised`, `shadow-raised-hover` on hover (Button) | Buttons and clickable cards only (replaced in: glassmorphism, minimalism) |

**Level and layer.** The level sets the surface; the layer (`zIndex`, Stacking order) sets what sits above what.

## Shadows

**The Hairline Rule.** Shadows only on interactive elements: things the user clicks or taps. Everything else, including containers of clickable items such as popovers, menus and sheets, uses a 1px `hairline` border and no shadow. (replaced in: glassmorphism, minimalism)

- **Barely perceptible.** `shadow-rest` is a hint that the element is clickable; `shadow-hover` suggests a lift, nothing more. Never stack several shadows or raise the opacity to make a point; the stacked shadows are only the `shadow-raised` tokens, on filled and elevated Buttons (Button). (replaced in: glassmorphism)
- **Offset and blur.** A shadow always has a vertical offset and a soft blur. A zero-offset colored halo is decoration; a hard shadow with no blur (`4px 4px 0`) is a costume.
- **Dark theme shadows** are denser (black at 24–32%). (replaced in: glassmorphism)
- **Glass.** Glass and blur are never decoration: they are used only where a component's file prescribes them. (replaced in: glassmorphism)

## Interaction

- **Hover** on a clickable element: `shadow-rest` → `shadow-hover` (`shadow-raised` → `shadow-raised-hover` on filled and elevated Buttons) and a lift of `space-1` (4px), with `duration-fast` and `ease-out`. **Pressed:** back to rest in `duration-instant`. (replaced in: glassmorphism, minimalism)
- **Reduced motion:** no lift; only the shadow changes, without animation. (replaced in: minimalism)

## Stacking order

**Layers** use the fixed `zIndex` scale, never a free number: `base` 0, `raised` 10 (sticky headers, raised items), `overlay` 100 (scrim), `modal` 200 (dialogs, sheets), `dropdown` 300 (menus, popovers), `tooltip` 400, `toast` 500 (notifications). What opens from inside a layer sits above it: a menu or a tooltip inside a dialog or a sheet shows above it. Floating layers render outside clipping containers (popover API, dialog, portal) so they are never cut off. With `<dialog>` and the popover API the browser stacks layers in its top layer in opening order and z-index does not apply: use them when available. The scale applies to portals and fixed elements.
