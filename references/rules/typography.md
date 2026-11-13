# Typography rules

- **Roles, not sizes.** Use the scale tokens (`display-*`, `headline-*`, `title-*`, `body-*`, `label-*`, `code-md`); never a free font size.
- **Display roles only for display.** The `display-*` roles never appear in labels, buttons, navigation or form fields. Among data, only a key figure uses them: a single number that is the focal point of its card (a temperature, a score; Cards, Key figure). Among texts, only a quote that stands alone in its section (Testimonials) or in the half beside a sign-in form (Sign in). Everything else uses the other roles. The `mono` font is only for code (`code-md`), never a costume for "technical"; numbers in data use the `sans` font with tabular figures (Numbers).
- **Form fields at 16px.** Text inside inputs, textareas and selects uses `body-lg` (16px) so mobile Safari does not zoom the page on focus.
- **Reading floor.** Running text is `body-md` (14px), the default for most app text. `body-lg` (16px) is for introductory paragraphs and primary reading text; `body-sm` (12px) for supporting notes, legal text and secondary descriptions in dense layouts.
- **Measure.** Paragraphs stay between 45 and 75 characters per line; cap text containers with a `ch` max-width.
- **Heading spacing.** More space above a heading than below it, so the heading belongs to the text it introduces.
- **Balanced lines.** Headings have `text-wrap: balance`, so their lines have similar lengths; paragraphs have `text-wrap: pretty`, so their last line never holds one word alone.
- **Smoothing.** The body has `-webkit-font-smoothing: antialiased`, so on macOS each weight is drawn at its own thickness, never heavier.
- **Paragraph rhythm.** Separate paragraphs with space or with a first-line indent, never both.
- **Numbers.** Columns of numbers use tabular figures (`font-variant-numeric: tabular-nums`) so digits line up.
- **Font loading.** Load only the weights in use, with `font-display: swap` and the system fallback of Names (Token file), so text is never invisible. Preload (`<link rel="preload" as="font" crossorigin>`) only the font files used on the first screen.
- **Zoom and user settings.** Never block browser zoom, user font size, Dynamic Type or platform text scaling.
- **Line-height per script.** The scale's line-heights are set for Latin, Greek, Cyrillic and Hebrew. Arabic, Chinese, Japanese and Korean add 10% to the line-height; Devanagari, Thai and Khmer add up to 20%. Sizes do not change, and the result is not rounded to the grid.

## Roles and sizes

**Role and size.** Five roles, each in three sizes (Large, Medium, Small). Values are dimension / line-height · weight · letter-spacing, in px.

| Role | Large | Medium | Small |
|---|---|---|---|
| **Display** (`display-*`, font `display`). The largest text: short text or key figures, best on large screens. | `display-lg` 57 / 64 · 400 · -0.25. The main text or figure of top prominence on very large screens, or a single isolated visual (a temperature, a big score). | `display-md` 45 / 52 · 400 · 0. Expressive text or prominent figures on medium screens, or primary regions. | `display-sm` 36 / 44 · 400 · 0. The compact display: impact on small screens or narrow layouts without much vertical space. |
| **Headline**. Short, high-impact text that marks the primary passages or main regions. | `headline-lg` 32 / 40 · 400 · 0. The main title of a screen or view ("Profile", "Your orders"). | `headline-md` 28 / 36 · 400 · 0. Headings of important sections, and the title of a sign-in form (Sign in). | `headline-sm` 24 / 32 · 400 · 0. Headings of secondary content regions or less prominent sections on the same page. |
| **Title**. Smaller than Headline, medium emphasis: divides secondary passages or regions. | `title-lg` 22 / 28 · 400 · 0. Titles of cards and articles, primary app bar headings (a contact's name), and the title inside a dialog. | `title-md` 16 / 24 · 500 · 0.15. Main categories and section dividers ("Top News"). | `title-sm` 14 / 20 · 500 · 0.1. Subcategory headings, items of complex lists, compact sub-headers inside components. |
| **Body**. Long passages, line-height about 1.5×, simple highly legible font. | `body-lg` 16 / 24 · 400 · 0.5. Introductory paragraphs or primary reading text (the opening of an article). | `body-md` 14 / 20 · 400 · 0.25. The default for most app text: article paragraphs, option descriptions in settings. | `body-sm` 12 / 16 · 400 · 0.4. Supporting text, secondary notes, legal text and disclaimers, secondary descriptions in dense layouts. |
| **Label**. Small functional styles for components and micro-text. | `label-lg` 14 / 20 · 500 · 0.1. Action elements: the text inside buttons. | `label-md` 12 / 16 · 500 · 0.5. Navigation components: tabs, top bar links. | `label-sm` 11 / 16 · 500 · 0.5. Micro-text and captions: timecodes, badges, small tags. |

**Code.** `code-md` (13 / 20 · 400 · 0, font `mono`) covers code.

**Emphasis.** Where a rule asks for text in weight 500 inside 400 text, use the 500 role of the same size: `body-lg` → `title-md`, `body-md` → `title-sm`, `body-sm` → `label-md`. Inside 500 text, the words a rule singles out take `strong` (600).
