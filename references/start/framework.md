# Framework

Asked only when the project is empty; in an existing project, read the framework, the UI library and the icon library from the code. Any framework the user names is used (React, Vue, Angular, Svelte, plain HTML and CSS). If the user has not chosen, propose the default from the table and wait for the OK:

| Mode | Need | Proposal | Publishing |
|---|---|---|---|
| Site | any (landing page, multi-page, blog) | Astro, static output | anywhere: Vercel, Netlify, Cloudflare Pages, GitHub Pages, FTP hosting |
| App | frontend only (data comes from an external API) | Vite + React | anywhere, as static files |
| App | own server (login, database, internal APIs) | Next.js | Vercel, or a Node hosting |

The framework decides how the tokens are exposed and which Hugeicons package to use.

**Token file.** The project's tokens live in one file, `tokens.css`, as CSS variables. A project with both modes still has one file: the mode changes how the tokens are used, not their values.
- **Names:** each variable takes the token's name as written in `references/tokens.yaml` (`--ink`, `--space-4`, `--shadow-rest`, `--duration-base`, `--ease-out`); three groups take these names:
  - `rounded`, `zIndex` and `fontWeight` keys carry their group in front: `--rounded-md`, `--zIndex-modal`, `--fontWeight-strong`;
  - each typography token gives one variable per property, named after the property: `--body-md-fontSize`, `--body-md-fontWeight`, `--body-md-lineHeight`, `--body-md-letterSpacing`, and `--body-md-fontFamily`, which points to the font variable;
  - fonts become `--font-display`, `--font-sans`, `--font-mono`, each followed by its system fallback: `ui-sans-serif, system-ui, sans-serif` (mono: `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`).

  Names are case-sensitive: write them exactly.
- **Units:** font sizes, line heights and spacing tokens in rem (px ÷ 16: 16px = 1rem), so they follow the browser's zoom (Spacing, rule 9); every other value as in `references/tokens.yaml`.
- **Themes:** colors and shadows are defined once per theme: light values in `:root`, dark values under `@media (prefers-color-scheme: dark)`. With a theme switch (Themes, Which theme shows), the same blocks also go under `[data-theme="light"]` and `[data-theme="dark"]` on `<html>`, which win over the system. With one theme only, there is one block, in `:root`. Each block declares its theme with `color-scheme: light` or `color-scheme: dark`, so the browser draws its own controls and scrollbars in that theme and the theme is read from the file.
- **Values that cannot be variables:** breakpoints (CSS does not read variables in media queries), the spring (a JavaScript value) and the icon size and stroke (props of the icon component) are written with the token's exact value and a comment naming the token. The `cqw` and `%` measures a component file gives (Hero, Phone with notifications) are written as given.
- **Where it lives and where it loads,** always before any other style:

  | Framework | File | Loaded |
  |---|---|---|
  | Plain HTML and CSS | `styles/tokens.css` | first `<link>` in the `<head>` of every page |
  | Astro | `src/styles/tokens.css` | imported in the base layout |
  | Vite + React, Vue, Svelte | `src/styles/tokens.css` | first import in the entry file (`main`) |
  | Next.js, App Router | `tokens.css` next to the root layout (`app/` or `src/app/`) | first import in the root layout |
  | Next.js, Pages Router | `styles/tokens.css` | first import in `pages/_app` |
  | Angular | `src/styles/tokens.css` | first entry of `styles` in `angular.json` |

- **Fonts:** the `fonts` tokens load with `tokens.css`, on every page: `<link rel="preconnect" href="https://fonts.googleapis.com">`, `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` and one Google Fonts stylesheet with the weights in use and `display=swap` (Kore's: `https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600&family=Outfit:wght@400&display=swap`), or the framework's font loader with the same families and weights (Font loading).

- **Tailwind:** Tailwind's theme maps its names to Kore's (`--radius-md: var(--rounded-md)`), never copying values.
- **A library that needs literal values** because it computes colors from them (MUI, Bootstrap through Sass, Angular Material): copy the value from `tokens.css` into the library's theme, identical, with a comment naming the token. `tokens.css` stays the source: a value changes there first, then in the copy.
- **An existing project with a token or theme file:** use that file instead of creating `tokens.css`, and add Kore's tokens to it with Kore's names. The values already there change only in a redesign, following Migration (`references/audit.md`).
