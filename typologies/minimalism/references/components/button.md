# Button

- **Filled:** Replaces: `button.filled`. background-image `gradient-raised`; box-shadow inset 0 0 0 `line-thin` the variant's edge color.
- **Filled hover:** Replaces: `button.filled-hover`. On mouse hover (hover: hover), a button that is not disabled: transform none; primary: background-color color-mix(in srgb, `primary`, `ink` `mix-hover`); destructive: background-color color-mix(in srgb, `danger`, `ink` `mix-hover`); elevated: background-color `surface-hover`.
- **Secondary hover:** Replaces: `button.secondary-hover`. A button that is not disabled: box-shadow inset 0 0 0 `line-thin` `hairline-medium`.
- **Filled pressed:** Replaces: `button.filled-pressed`. box-shadow inset 0 0 0 `line-thin` the variant's edge color.
- **Pressed:** Replaces: `button.pressed`. transform none; box-shadow `shadow-rest`; transition-duration `duration-instant`. Every variant (icon buttons and the FAB too) adds the echo: a ring from the press point (from the centre on a keyboard press), clipped to the button's shape: border `line-thick` solid color-mix(in srgb, the button's text color `mix-edge`, transparent); border-radius 50%; width and height from 0 to twice the button's width while opacity goes from 1 to 0, in `duration-focal` with `ease-out`. Disabled and loading buttons show no echo; with reduced motion, no echo.
