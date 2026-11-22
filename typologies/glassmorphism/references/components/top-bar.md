# Top bar

- **Bar:** Replaces: `top-bar.bar`. As in `references/components/top-bar.md`, with the border and the shadow of Surface.
- **Surface:** Replaces: `top-bar.surface`. The Glass recipe.
- **Over the hero:** Replaces: `top-bar.over-the-hero`. With the page at the top, the bar's surface is off: background transparent; backdrop-filter none; box-shadow none. It takes Surface as soon as the page scrolls (scrollY > 0): transition background-color and box-shadow `duration-base` `ease-out`.
- **Navigation panel:** Replaces: `top-bar.navigation-panel`. As in the default, with the Glass recipe in place of `canvas`. While it is open, the bar's surface is off, as at the top of the page in Over the hero, so the panel's glass covers both with no seam.
