# Top bar

- **Bar:** Replaces: `top-bar.bar`. As in `references/components/top-bar.md`, with the border and the shadow of Surface.
- **Surface:** Replaces: `top-bar.surface`. background `glass-fill-strong`; backdrop-filter blur(`glass-blur-bar`) saturate(`glass-saturate`); border-bottom `line-thin` solid `glass-bar-border`; box-shadow `shadow-glass`.
- **Over the hero:** Replaces: `top-bar.over-the-hero`. With the page at the top, the bar's surface is off: background transparent; backdrop-filter none; border-bottom-color transparent; box-shadow none. It takes Surface as soon as the page scrolls (scrollY > 0): transition background-color, border-bottom-color and box-shadow `duration-base` `ease-out`.
- **Navigation panel:** Replaces: `top-bar.navigation-panel`. As in the default, with the bar's glass in place of `canvas`: background `glass-fill-strong`; backdrop-filter blur(`glass-blur-bar`) saturate(`glass-saturate`); box-shadow `shadow-glass`. While it is open, the bar's surface is off, as at the top of the page in Over the hero, so the panel's glass covers both with no seam.
