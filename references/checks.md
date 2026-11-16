# Checks

Read before delivering anything built or changed, reused code included (Building anything). Each line names a rule; the rule itself is in the section in parentheses, in `SKILL.md`, in `references/rules/` or in a component's file.

- **One pass, then one confirmation.** Run the script with `--url` and `--shots` (Measure), read every screenshot once, fix everything found in one batch, run it once more, then deliver.
- **Every box.** Skip a box only when its condition is absent (no images, no Images box). A box that cannot be ticked honestly means the work is not finished.

## Measure

Measured on the result, never assumed. Run Kore's script on the project, where `<kore>` is the folder that holds Kore's `SKILL.md`: `python3 <kore>/scripts/kore_check.py <project folder> --url <page>`, with one `--url` for each page built or changed: the address the project's server gives, or `file://` for a plain HTML file. With `--url` the script also opens each page in Chrome or Edge, in each theme the token file defines (its `color-scheme`), from 320 to 2560px wide and at 200% text size; it needs Playwright (`python3 -m pip install --user playwright`). When Playwright is missing, ask the user to install it. When nothing can be opened in a browser, or the user declines, run it without `--url` and check by hand the boxes on the rendered page (horizontal scroll, text at 200%, touch targets, contrast), saying so in the report. Fix every ✗, check every ? against the rule it names, and run it again until it exits with 0. A ✗ you can prove false (the script misreads the code), or a ✗ on what the user asked for, is waived in the code, never by changing the code to please the script: `kore-ignore-next-line <Rule>: <who decided: evidence>` in a comment above the line, or `data-kore-ignore="<Rule>: <reason>"` on the element of a page; the report names every waiver. When unsure, ask the user in one line; then check by hand the boxes it cannot measure. Without a terminal or without Python, check every box by hand and say so in the report.

**Bounded verification** (as impeccable): look at the result through `--shots <folder>`, with the folder outside the project (the agent's temporary folder): the script saves each page, whole, at 375 and 1440px in each theme the token file defines, and lists the files. Read each once; fix everything they show in one batch; take at most one more round, then stop. Never write your own browser scripts, and no automated tests the user did not ask for.

- [ ] Every file of a section or component built is named in the heading of its table in `KORE-DECISIONS.md`; every table holds and names its Primary group and a Shape built only from the Layout primitives, its items the Elements of the table, each once, and the smallest primitive holding a group's items holding only that group; every group has one Primary; elements of one group answer one question, and each question has one group; on the page, each text element marked with `data-kore-element` has the size, weight and color of its row's Style; every Space reads `space-N to [Element]` of another row, and a Space between two groups is at least twice every Space inside them; on the page, every row's element carries `data-kore-element` and sits at its Space from its Element; a Secondary is smaller than its Primary, or of its size under a Primary heavier than 400; every text row is smaller than the focal point, or of its size and lighter; the focal point comes first among the text rows of the Shape and, on the page, sits above every other text element of its section or component, or level with it and to its left (Order of decisions, Semantic weight, Decisions file, The Relatedness Test, Layout primitives, From role to style, The Distance Ratio Rule, The One Winner Rule).
- [ ] Each table of `KORE-DECISIONS.md` uses at most three font sizes on its text rows with a Level (Text hierarchy).
- [ ] When an element's text opens with a figure, the words after it are smaller and in `mute` (Text hierarchy).
- [ ] A row citing Consequences are never quiet has Level —, a 500 role and `danger` or `warning` (Text hierarchy).
- [ ] A row citing Value labels are a last resort has Level —, `body-md` 400 `mute` and a Space to its value, which is no price, date or email unless another value of its section or component has the same format (Text hierarchy).
- [ ] A row citing Specs lead with the label has Level —, `body-md` 400 `ink` and a Space to its value, which is `body-md` 400 `body` (Text hierarchy).
- [ ] Each Element of a section or component holds its own text; copies of one Element hold the text their data gives (Copy).
- [ ] The innermost elements marked with `data-kore-element` of a section or component follow in the code their order on screen: in a column top to bottom, on a line left to right (Code order).
- [ ] Among the groups that share a parent, every group has a title or none has (Grouping and separation).
- [ ] Every color, space, size, radius, shadow, duration, easing, z-index, breakpoint and opacity comes from a token or from a value a rule computes (Never invent values).
- [ ] Spacing on the scale, sizes multiples of 8, padding uniform, gaps on the container (Spacing).
- [ ] Text 4.5:1, large text 3:1, icons, control borders and focus 3:1, on the worst surface, in each theme the token file defines (Contrast).
- [ ] Buttons take `primary`; a background in `accent` sits only in the Hero's visual; text in `accent` is `display-sm` or larger; a page holds at most 4 elements in `accent`, the Hero's backgrounds in `accent` counted as one (Meaning).
- [ ] At most one button with a `primary` background per form, dialog or `data-kore` root, and per page outside them (The One Primary Rule).
- [ ] Horizontal padding equals the radius; nested radii are concentric (The Radius-Padding Rule, The Concentric Rule).
- [ ] Shadows only on clickable elements; everything else a 1px border: `hairline` on containers, `hairline-medium` on labelled controls, `hairline-strong` on controls known only by their outline (Shadows, Contrast, AI tells).
- [ ] Layers on the `zIndex` scale, floating layers never clipped (Stacking order).
- [ ] Touch targets 44px, adjacent targets `space-2` apart (Accessibility).
- [ ] Every interactive element has all its states and the focus of States: corner marks, or the link focus underline on a link (States).
- [ ] Every control has an accessible name, the role and keyboard use its file sets; decorative icons are hidden (Components, Icons).
- [ ] `<html>` carries `lang` (Page language).
- [ ] `<html>` carries `lang` with the country when the page shows a date, a price or a measure; dates with a month name, and numeric dates with the year and a day above 12, follow that locale (Page language).
- [ ] An `<a href>` inside a paragraph is in `link`, with a 1px underline at a 4px offset (Browser surfaces).
- [ ] An image outside a card and narrower than the page has radius `xl`; round images, SVG files and images in a header, a footer or the Logo wall follow their own component (Radius by role).
- [ ] With the Mode in `PRODUCT.md`, each `<section>` sits `space-12` from the next in App mode, `space-32` or `space-48` in Site mode (Proximity and hierarchy).
- [ ] Text sits `space-4` or more from the screen's sides on phones, `space-8` from `md`, inside a centred `max-content` column; text in a box that scrolls sideways or in a fixed layer follows its box (Breakpoints).
- [ ] In the Hero, the smallest box holding the `h1` and the calls to action holds only the `h1`, one subtitle, the calls to action and a form (Hero).
- [ ] In Site mode, a `<section>` holds at most four copies of an item with a heading or a quote, the Logo wall and the Blog aside; a quote holds at most 25 words (Sections).
- [ ] One `h1` per page, inside the Hero when the page has one (Typographic levels, Hero).
- [ ] Heading levels follow each other: `h2` under `h1`, `h3` under `h2` (Typographic levels).
- [ ] Fields carry no `onpaste` attribute (Usability).
- [ ] Every link is an `<a>` with an `href`; `role="link"` sits on an `<a>` alone (Button).
- [ ] A button's CSS keeps its label in the case it is written in (Button).
- [ ] In `KORE-DECISIONS.md`, the heading of a page section is an `h2` in `headline-md`, the heading of a region inside it an `h3` in `headline-sm`; on the page, an element of a row is the `h2` or `h3` its row names, and only then (Typographic levels).
- [ ] Only type roles; form text 16px; tabular figures in columns of numbers; each line of a paragraph at most 75 characters (Typography rules).
- [ ] Only `transform` and `opacity` animate, with motion tokens; reduced motion keeps meaning and drops movement (Motion).
- [ ] Elements told apart by background or shadow have a 1px transparent border (Themes).
- [ ] Titles of cards side by side on the same number of lines (Cards).
- [ ] Cards in one row end at the same height, each filled down to its padding (Cards).
- [ ] In a card, the media sits above the title and no text sits under the actions; no card sits inside a card; a rounded block with a background and marked text inside a card is or holds a link, a button or a label (Cards).
- [ ] In a card, title and subtitle sit `space-1` apart, the header and what follows `space-6`, the body rows `space-3` or `space-6`, the body and the actions `space-8` (Cards, The Distance Ratio Rule).
- [ ] In a card, a form or a dialog, the buttons of a row end at its right edge and the filled one comes last (Scanning patterns).
- [ ] A destructive button sits `space-4` or more from every other button when a `primary` shares its decision (Proximity and hierarchy).
- [ ] On an English page, a button's label is other than "OK", "Yes", "No" or "Submit"; in every language, it holds at most one word in capitals (Button).
- [ ] No horizontal scroll from 320 to 2560px, nothing cut at 200% zoom, `100dvh` for full height (Extremes).
- [ ] Images: format, `srcset`, reserved size, loading, `alt` (Images).
- [ ] Selection, caret, scrollbars, links and numerals themed (Browser surfaces).
- [ ] Every line of the component's file, and of the files read through its Uses line, holds (Components).

## Judge, always

- [ ] Every string passes Copy 1, 4, 6, 7, 9 and 10; AI tells 2, 6, 9, 11 and 13 appear only when the user asks for them (Copy, AI tells).
- [ ] The open tab and the page number live in the URL (Usability).

## Judge, by context

Every context the work touches applies. A link adds Link.

**Link** (text links, links in navigation, Breadcrumb, Footer, Steps, a button that takes the user to another page)
- [ ] A link with the look of a button follows Button and keeps its label color on focus (Button, States).

**Overlay** (Menu, Popover, Dialog, Sheet, Tooltip, Command palette)
- [ ] Focus moves in on open and back to the trigger on close; Escape and a click outside close it (Overlay rules).

**Screen or page**
- [ ] Skip link, focus never covered, focus to the `h1` after a route change (Accessibility).

**Site mode** (`references/site.md`)
- [ ] Each section under the hero reveals once on scroll (Scroll reveal).

## Closed list

- [ ] Each group's Question is the one its user asks: read as that user, it names what they want to know or do there (The reader's question).
- [ ] Each primitive of a Shape is the one whose Use for fits the items it holds (Layout primitives).
- [ ] A list cites Specs lead with the label only when its user scans the labels to find a value (Text hierarchy).
- [ ] The code builds the Shape as written: each primitive of the Shape is how its items sit on screen (Layout primitives).
- [ ] Every consequence of an action is a row citing Consequences are never quiet, with an icon only when its words alone do not read as one (Text hierarchy).
- [ ] A consequence the user cannot undo is in `danger`; one the user must not miss is in `warning` (Text hierarchy).
- [ ] A value label and its value merge into one phrase whenever the words allow it (Text hierarchy).
- [ ] Each line adds one new fact: no line says again, in other words, what the title or the line above it says (Copy).
- [ ] Groups are separated with the lightest step of The Separation Ladder that keeps them apart: space first, then background, line, card (Grouping and separation).
- [ ] The focal point is surrounded by space and sits on a third of the layout, the upper third or the top-left crossing, rather than at the dead centre (Placement).
- [ ] A group has a title when its user looks for an item by its category (Grouping and separation).
- [ ] A list of three holds three real items of the content (Copy).
- [ ] The hero-metric template appears only when the user asks for it: a big number, a small label, supporting stats, an accent (AI tells).
- [ ] A product screenshot is a real screenshot or a real component (AI tells).
- [ ] A status dot shows a real state (AI tells).
- [ ] A strip with a city, the time or the weather appears only when the user asks for it (AI tells).
- [ ] A photo credit names a real photographer (AI tells).
- [ ] A page in Site mode compares values with their numbers; a filled track appears only when the user asks for it (AI tells).
- [ ] Every user action gets a visible response (Usability).
- [ ] A destructive action runs, then offers Undo (Usability).
- [ ] An error message says what went wrong, why when useful, and how to fix it (Usability).
- [ ] The user's locale is asked when the first date, price or measure goes on screen (Ask later, when it matters).
- [ ] Every choice no rule covered is noted for the report (Behaviour rules).
- [ ] An element larger or bolder than its peers has a reason the content gives, or the user is asked (Semantic weight).
- [ ] A button's label is a verb and an object (Button).
- [ ] A dialog opens only for an action that cannot be undone or that needs interruption (Dialog).
- [ ] Each moment gets its component: page state an Alert, a passing result a Toast, loading content a skeleton, a wait a bar (Alert, Toast, Progress).
- [ ] Response times kept: 100ms, 300ms, 1s, 3s (Usability).
- [ ] Every animation acknowledges an action, makes a state change or a spatial relationship legible, keeps continuity through a change, or directs attention to a meaningful moment (Motion).
- [ ] `danger` marks an error or a destructive action, `success` a success, `warning` a warning, `info` information (Meaning).
- [ ] A field shows its limits and formats before the user acts (Usability).
- [ ] A field is validated when the user leaves it (Form fields).
- [ ] The first-time user's path is complete on its own; accelerators for experts sit beside it (Usability).
- [ ] Error, success, warning and info carry a text label or an icon with their color (Meaning).
- [ ] A screen with a floating action button holds one `primary` (The One Primary Rule).
- [ ] Every string passes Copy 1, 4, 7 and 9 beyond the phrases the script lists, in every language (Copy).
- [ ] A contrast corrects something the user really believes (Copy).
- [ ] Each text says what the thing is or does (Copy).
- [ ] Section numbers appear only when the order is information the user needs (AI tells).
- [ ] The page invites scrolling with its content alone: no arrow, no mouse-wheel icon, no scroll cue in a language other than English (AI tells).
- [ ] A version label appears only when the product is in preview (AI tells).
- [ ] A text label over an image is one its component places there (AI tells, Cards).
- [ ] One intent has one call to action in a section (AI tells).
- [ ] Filters, sorting and search live in the URL (Usability).
- [ ] Dates the format leaves ambiguous, currencies and units follow the page's locale (Page language).
- [ ] Every text marked `data-kore-user`, every number, price, quote, logo and name comes from the user (Product file, Start here).
- [ ] Inside a card, a component with a background and a radius is its own unit (Cards).
- [ ] Repeated instances share one priority and one structure (Semantic weight).
- [ ] In a group with no filled action, the confirming action is last (Scanning patterns).
- [ ] A `secondary` stands next to a primary or a destructive; alone only in a decision with no main action (Secondary alone).
- [ ] In a language other than English, a button's label is other than the translation of "OK", "Yes", "No" or "Submit" (Button).
- [ ] Labels in sentence case (Button).
- [ ] A Button with a label shows only text (Button).
- [ ] Paste works in every field (Usability).
- [ ] An overlay whose trigger has no `aria-haspopup` follows Overlay rules (Overlay rules).
- [ ] A line of prose holds at least 45 characters (Typography rules).
- [ ] Three or four type levels on one screen (Typographic levels).
- [ ] F pattern for dense content, Z for sparse (Scanning patterns).
- [ ] Images, controls and the content of carousels keep the page margins and stop at `max-content` (Breakpoints).
- [ ] Profiles on other sites are Social links (Sections).
- [ ] One focal moment per page, the hero's entry (One focal moment per page).
- [ ] In a page section, the actions sit under the text they act on, aligned with it, the main action first (Scanning patterns).

## Deliver

- [ ] The report in two lines: what was built, what was fixed, every choice no rule covered; then the last `kore_check` command, run after the last edit, and its summary line (Building anything).
- [ ] `kore_check` exited with 0, or the report says it could not run and every Measure box was checked by hand (Measure).
- [ ] The report tells the user what only they can check: when the work has animations, 60fps and CLS 0 while they run (Motion); always, real iPhone and Android phones (Responsive, Testing).
- [ ] The semantic weight default stated in one line (Semantic weight).
- [ ] Missing content and images listed (Product file).
- [ ] Wait for the user (Start here).
