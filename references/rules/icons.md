# Icons

**Library first.** If the project already uses an icon library, keep it and apply the rules below. Otherwise use Kore's default.

**Default: Hugeicons**, always the free set (the paid Pro set only when the user asks for it and holds the license), *Stroke Rounded* style (MIT license).

**Source:**
- **A framework** (React, Vue, Angular, Svelte, SolidJS, React Native, Flutter, Astro): install its official Hugeicons renderer together with the free icons: `@hugeicons/react`, `vue`, `angular`, `svelte` or `solid-js`, or `@hugeicons/react-native` with `react-native-svg`, each with `@hugeicons/core-free-icons`; in Flutter, `hugeicons` (`HugeIcons.strokeRounded<Name>`). This includes Vite + React and Next.js. Astro has none: install `@hugeicons/core-free-icons` and copy `references/icons/Icon.astro` unchanged into the project's components (inline SVG at build, no JavaScript on the page): `<Icon icon={Delete02Icon} size={20} />`. A version the renderer does not support (Svelte 4, Angular before 17.1) follows Plain HTML and any other stack.
- **Plain HTML and any other stack:** nothing is installed. `python3 <kore>/scripts/hugeicons.py <Name> …` prints the free Stroke Rounded SVGs: every icon the work needs, in one command. On the web the SVGs are copied inline into the markup; in a native app they are imported as the platform's vector assets: an Xcode asset catalog, an Android Studio Vector Asset. An icon used more than once on the same page goes into a sprite: one `<symbol>`, referenced with `<use>`. Without network the script fails: tell the user; never draw an icon.
- **Exact names** (`Delete02`, `Tick01`): in a JavaScript project, `ls node_modules/@hugeicons/core-free-icons/dist/esm | grep -i <word>`; everywhere else, `hugeicons.py --search <word>`.
- **Never a CDN or a web font** for icons.
- **Never draw or edit an icon by hand:** no paths written by the agent, no strokes changed.
- **An icon missing from the free set:** tell the user and offer the two or three closest icons in the set; the user chooses.

## Logos

**A logo** (a technology, a service, a company) follows every rule of Icons and does not count as a second library; only its source differs: `python3 <kore>/scripts/devicon.py <name> …`, exact names with `--search <word>`. The sites of Social links take their file in `references/icons/brands/`. A logo in neither: ask the user for its file, or leave it out.

## Rules

- **One library per project**, one style, one stroke width (1.5 on a 24px grid). Never mix libraries or filled and outlined styles.
- **Sizes from the grid:** 16px inside controls and menus and next to 12–16px text (menu items, inline buttons, steppers, field adornments), 20px in icon-only buttons, 24px for navigation and standalone icons.
- **Color from text:** icons use `currentColor`, so they follow the text or state color of their container.
- **Spacing:** icon ↔ text `space-2` (8px) in rows, fields and chips, `space-1` (4px) in badges. Labeled buttons carry no icon.
- **Accessibility:** an icon-only button always has an accessible label (`aria-label` or visually hidden text) and a tooltip; decorative icons are hidden from screen readers (`aria-hidden="true"`).
- **Clear meaning:** one icon means one thing across the product (pencil = edit, trash = delete). An icon-only button uses only icons that are obvious on their own: no label or text in the button.
- **No stand-ins:** never emoji or Unicode symbols instead of icons.

## Candidates

| Library | Style that fits Kore | Stacks |
|---|---|---|
| Hugeicons | Stroke Rounded (free) | active |
| Lucide | default (round caps) | React, Vue, Angular, Svelte, Solid, React Native, vanilla |
| Phosphor | Regular or Light | React, Vue, web components, Flutter, Swift |
| Tabler Icons | outline | React, Vue, Svelte, Solid, vanilla SVG, web font |
| Material Symbols | Rounded | web font and SVG, any stack |
