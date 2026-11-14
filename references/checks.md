# Checks

Read before delivering anything built or changed, reused code included (Building anything). Each line names a rule; the rule itself is in the section in parentheses, in `SKILL.md`, in `references/rules/` or in a component's file.

- **One pass, then one confirmation.** Run the script with `--url` and `--shots` (Measure), read every screenshot once, fix everything found in one batch, run it once more, then deliver.
- **Every box.** Skip a box only when its condition is absent (no images, no Images box). A box that cannot be ticked honestly means the work is not finished.

## Measure

Measured on the result, never assumed. Run Kore's script on the project, where `<kore>` is the folder that holds Kore's `SKILL.md`: `python3 <kore>/scripts/kore_check.py <project folder> --url <page>`, with one `--url` for each page built or changed: the address the project's server gives, or `file://` for a plain HTML file. With `--url` the script also opens each page in Chrome or Edge, in each theme the token file defines (its `color-scheme`), from 320 to 2560px wide and at 200% text size; it needs Playwright (`python3 -m pip install --user playwright`). When Playwright is missing, ask the user to install it. When nothing can be opened in a browser, or the user declines, run it without `--url` and check by hand the boxes on the rendered page (horizontal scroll, text at 200%, touch targets, contrast), saying so in the report. Fix every ✗, check every ? against the rule it names, and run it again until it exits with 0. A ✗ you can prove false (the script misreads the code) is waived in the code, never by changing the code to please the script: `kore-ignore-next-line <Rule>: <who decided: evidence>` in a comment above the line, or `data-kore-ignore="<Rule>: <reason>"` on the element of a page; the report names every waiver. When unsure, ask the user in one line; then check by hand the boxes it cannot measure. Without a terminal or without Python, check every box by hand and say so in the report.

**Bounded verification** (as impeccable): look at the result through `--shots <folder>`, with the folder outside the project (the agent's temporary folder): the script saves each page, whole, at 375 and 1440px in each theme the token file defines, and lists the files. Read each once; fix everything they show in one batch; take at most one more round, then stop. Never write your own browser scripts, and no automated tests the user did not ask for.

- [ ] Every file of a section or component built is named in the heading of its table in `KORE-DECISIONS.md`; every table holds and names its Primary group and a Shape built only from the Layout primitives, each item an Element of the table; every group has one Primary; elements of one group answer one question, and each question has one group; on the page, each text element marked with `data-kore-element` has the size, weight and color of its row's Style; every Space reads `space-N to [Element]` of another row, and a Space between two groups is at least twice every Space inside them; on the page, every row's element carries `data-kore-element` and sits at its Space from its Element; a Secondary is smaller than its Primary, or of its size under a Primary heavier than 400; every text row is smaller than the focal point, or of its size and no heavier; the focal point comes first among the text rows of the Shape and, on the page, sits above every other text element of its section or component, or level with it and to its left (Order of decisions, Semantic weight, Decisions file, The Relatedness Test, Layout primitives, From role to style, The Distance Ratio Rule, The One Winner Rule).
- [ ] Every color, space, size, radius, shadow, duration, easing, z-index, breakpoint and opacity comes from a token or from a value a rule computes (Never invent values).
- [ ] Spacing on the scale, sizes multiples of 8, padding uniform, gaps on the container (Spacing).
- [ ] Text 4.5:1, large text 3:1, icons, control borders and focus 3:1, on the worst surface, in each theme the token file defines (Contrast).
- [ ] Horizontal padding equals the radius; nested radii are concentric (The Radius-Padding Rule, The Concentric Rule).
- [ ] Shadows only on clickable elements; everything else a 1px border: `hairline` on containers, `hairline-medium` on labelled controls, `hairline-strong` on controls known only by their outline (Shadows, Contrast).
- [ ] Layers on the `zIndex` scale, floating layers never clipped (Stacking order).
- [ ] Touch targets 44px, adjacent targets `space-2` apart (Accessibility).
- [ ] Every interactive element has all its states and the focus of States: corner marks, or the link focus underline on a link (States).
- [ ] Every control has an accessible name, the role and keyboard use its file sets; decorative icons are hidden (Components, Icons).
- [ ] Only type roles; form text 16px; tabular figures in columns of numbers; paragraphs 45 to 75 characters (Typography rules).
- [ ] Only `transform` and `opacity` animate, with motion tokens; reduced motion keeps meaning and drops movement (Motion).
- [ ] Elements told apart by background or shadow have a 1px transparent border (Themes).
- [ ] Titles of cards side by side on the same number of lines (Cards).
- [ ] No horizontal scroll from 320 to 2560px, nothing cut at 200% zoom, `100dvh` for full height (Extremes).
- [ ] Images: format, `srcset`, reserved size, loading, `alt` (Images).
- [ ] Selection, caret, scrollbars, links and numerals themed (Browser surfaces).
- [ ] Every line of the component's file, and of the files read through its Uses line, holds (Components).

## Judge, always

- [ ] Each idea said once, labels only when needed, the number carries the emphasis, warnings never quiet, at most three sizes in a component (Text hierarchy).
- [ ] Group titles all or none (Grouping and separation).
- [ ] Color never alone, semantic colors keep their role, the accent marks one moment, one `primary` per decision (Meaning).
- [ ] Every string passes Copy; no AI tells the user did not ask for (Copy, AI tells).
- [ ] Every action answers, destructive actions offer Undo, errors say what, why and how, state lives in the URL (Usability).
- [ ] Dates, currencies and units in the user's locale, asked when the first one goes on screen (Ask later, when it matters).
- [ ] No invented content: numbers, prices, quotes, logos and names come from the user (Product file).
- [ ] Every choice no rule covered is noted for the report (Behaviour rules).

## Judge, by context

Every context the work touches applies. A button adds Control; a link adds Link.

**Container** (Cards, List rows, Table, Tabs, Accordion, Empty state, Charts, Carousel, Footer, Sidebar, Cookie banner)
- [ ] Card zones in the fixed order; no card inside a card; no rounded block with a background unless it is a clickable unit (Cards).
- [ ] Inside less than between: title and subtitle `space-1`, header and content `space-6`, rows `space-3`, rows and actions `space-8` (Cards, The Distance Ratio Rule).
- [ ] No value repeats without a new purpose; roles differ by at least one clear step in size or weight; an element larger or bolder than its peers has a reason the content gives, or it is asked (Semantic weight).
- [ ] Repeated instances share one priority and one structure; equal heights only for the same structure (Semantic weight, Cards).
- [ ] Actions at the end, right-aligned, confirm last (Scanning patterns).

**Control** (Button, Form fields, Select, Checkbox and radio, Switch, Segmented control, Tabs, Password, Combobox, Number stepper, Slider, Date picker, File upload, Chip, Pagination, Steps)
- [ ] The variant follows the action's role: one `primary` per decision, a `secondary` next to a primary or a destructive (Secondary alone), a destructive action in its own group (Button, The One Primary Rule).
- [ ] Labels are a verb and an object; labeled buttons carry no icon (Button).
- [ ] Limits and formats shown before use, validation when leaving the field, paste never blocked (Usability).

**Link** (text links, links in navigation, Breadcrumb, Footer, Steps, a button that takes the user to another page)
- [ ] A link is an `<a href>`; with the look of a button it follows Button and keeps its label color on focus (Button, States).
- [ ] Text links in `link` with a 1px underline at 4px; focus with the link focus underline (Browser surfaces, States).

**Overlay** (Menu, Popover, Dialog, Sheet, Tooltip, Command palette)
- [ ] The overlay is the right one: a dialog only for what cannot be undone or truly needs interruption (Dialog).
- [ ] Focus moves in on open and back to the trigger on close; Escape and a click outside close it (Overlay rules).

**Feedback** (Alert, Toast, Progress, Empty state, form errors)
- [ ] The right component for the moment: page state an Alert, a passing result a Toast, loading content a skeleton, a wait a bar (Alert, Toast, Progress).
- [ ] Response times kept: 100ms, 300ms, 1s, 3s (Usability).

**Section of a page** (a hero, an about, features, any part with its own heading)
- [ ] The heading is an `h2` in `headline-md`, regions inside it `h3` in `headline-sm`, no level skipped (Typographic levels).
- [ ] The section's text, its heading included, comes from the user; when it is missing, ask (Start here).
- [ ] Prose at the reading measure; an image outside a card has radius `xl` and the ratio of the original (Typography rules, Radius by role, Images).
- [ ] Actions at the end of the content they act on, right-aligned (Scanning patterns).
- [ ] Sections `space-12` apart in App mode, `space-32` / `space-48` in Site mode (Proximity and hierarchy).

**Screen or page**
- [ ] The eye knows where to look first within three seconds; one `h1`; three or four type levels (Three levels, Typographic levels).
- [ ] F pattern for dense content, Z for sparse (Scanning patterns).
- [ ] Page margins `space-4` on phones, `space-8` from `md`; content stops at `max-content` (Breakpoints).
- [ ] Skip link, focus never covered, focus to the `h1` after a route change (Accessibility).

**Site mode** (`references/site.md`)
- [ ] The hero holds only title, subtitle and calls to action; the title is the `h1` (Hero).
- [ ] At most four items per section; quotes at most three lines with the name and role the user gives; profiles on other sites as Social links (Sections).
- [ ] One focal moment per page, the hero; each section under it reveals once on scroll (One focal moment per page, Scroll reveal).

## Closed list

- [ ] Each group's Question is the one its user asks: read as that user, it names what they want to know or do there (The reader's question).
- [ ] Each Shape follows from its table's groups: the groups are counted first, then the primitive whose Use for fits them is chosen (Order of decisions, Layout primitives).
- [ ] The code builds the Shape as written: each primitive of the Shape is how its items sit on screen (Layout primitives).
- [ ] Groups are separated with the lightest step of The Separation Ladder that keeps them apart: space first, then background, line, card (Grouping and separation).
- [ ] The focal point is surrounded by space and sits on a third of the layout, the upper third or the top-left crossing, rather than at the dead centre (Placement).

## Deliver

- [ ] The report in two lines: what was built, what was fixed, every choice no rule covered; then the last `kore_check` command, run after the last edit, and its summary line (Building anything).
- [ ] `kore_check` exited with 0, or the report says it could not run and every Measure box was checked by hand (Measure).
- [ ] The report tells the user what only they can check: when the work has animations, 60fps and CLS 0 while they run (Motion); always, real iPhone and Android phones (Responsive, Testing).
- [ ] The semantic weight default stated in one line (Semantic weight).
- [ ] Missing content and images listed (Product file).
- [ ] Wait for the user (Start here).
