# UI library

- With no preference, use Kore's components: they bring the look, the behaviour and the accessibility.
- If the user wants a library, propose the row of their framework:

  | Framework (from question 2) | Proposed library |
  |---|---|
  | React, Next.js | Radix (headless) |
  | Vue | Reka UI (headless) |
  | Svelte | Bits UI (headless) |
  | Angular | Angular Material |
  | Astro, plain HTML and CSS | none: use Kore's components |

- **Headless library:** the library brings the behaviour, keyboard, ARIA and focus management. Kore brings the look and the visual accessibility: contrast, visible focus, 44px targets, reduced motion.
- **Styled library** (Angular Material, or one the user names such as MUI or Bootstrap): tell the user what stays Kore's. Always: spacing, type scale, layout, hierarchy, responsive, copy, usability, 44px targets and reduced motion. Through the library's theme: colors (and so contrast), fonts, radii and shadows. The library's own: the inner shape of components (heights, inner padding, focus marks).
