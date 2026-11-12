---
name: kore
description: |
  Design system for web interfaces: landing pages, web apps, dashboards,
  portfolios, onboarding, settings. Use when a request touches how a web
  UI looks, reads or behaves: new UI, adding, restyling, redesigning,
  auditing, reviewing, critiquing, polishing, fixing or improving it; brand
  palettes, typography, fonts, light/dark theme, spacing, radius, shadows,
  icons, hierarchy, grouping; rushed, generic, flat or "looks AI-made"
  pages; bland designs to make bolder, busy ones to make quieter;
  responsive layout, touch targets, contrast, accessibility, motion,
  empty, loading and error states, undo, scrollbars, text selection,
  language selector. Components: forms, menu, popover, tooltip, dialog,
  sheet, alert, toast, badge, chip, progress, avatar, table, charts,
  accordion/FAQ, breadcrumb, top bar, sidebar, card, list, hero. Not for
  logic bugs, refactors, tests, build or i18n setup, performance, types,
  SQL, chart code (plotting libraries), complex animation, CSS theory,
  native apps, emails, logos, slides, marketing copy.
license: MIT
metadata:
  version: "0.1.0"
---

## Start here

Read this section before any design or UI work with Kore. Kore promotes a clear interface that never confuses the people using it; every rule below serves that goal.

**Kore's files.** Kore is this file plus the `references/` folder. Each file there is read only when the work reaches it:

| When you need | Read |
|---|---|
| Any UI work: every token's name and value, the source of the project's token file (Token file) | `references/tokens.yaml` |
| Building or checking any component: The Library-First Rule and the index of components | `references/components/index.md` |
| Every component being built or checked, also when it comes from a UI library, plus each component of its **Uses** line that the part being built or checked contains, and in turn theirs by the same test | `references/components/<name>.md` |
| Color: contrast, meaning, states, themes | `references/rules/color.md` |
| Custom palette | `references/rules/custom-palette.md` |
| Typography: roles and sizes | `references/rules/typography.md` |
| Spacing: scale, proximity and hierarchy, accessibility, implementation | `references/rules/spacing.md` |
| Shapes: radius by role, radius and padding, nested radius, borders inside the edge | `references/rules/shape.md` |
| Elevation: levels, shadows, interaction, stacking order | `references/rules/elevation.md` |
| Motion: tokens, app mode, site mode, implementation | `references/rules/motion.md` |
| Hierarchy: order of decisions, affinity grouping, layout primitives, visual weight, three levels, semantic weight, from role to style, typographic levels, text hierarchy, grouping and separation, scanning patterns | `references/rules/hierarchy.md` |
| Responsive: principles, breakpoints, grids, typography, input, safe areas, extremes, testing | `references/rules/responsive.md` |
| Images: format, resolutions, crop, reserved space, loading, missing image, alternative text, portrait | `references/rules/images.md` |
| Browser surfaces: text selection, caret, focus, scrollbars, links in running text, numerals | `references/rules/browser-surfaces.md` |
| Icons: logos, rules, candidates | `references/rules/icons.md` |
| Usability: the 10 heuristics | `references/rules/usability.md` |
| Copy: every string in the interface | `references/rules/copy.md` |
| AI tells: patterns that make an interface look generated | `references/rules/ai-tells.md` |
| Identity: the binding rules (Behaviour rules) | `references/rules/identity.md` |
| Right to left (question 5) | `references/rules/language.md` |
| An audit or a redesign, or `KORE-AUDIT.md` has a Redesign section in progress | `references/audit.md` |
| The user asks to change colors or fonts | `references/candidates.md` |
| Site mode (question 1) | `references/site.md` |
| Before delivering anything built or changed (Building anything), with `scripts/kore_check.py`, which measures the project's code | `references/checks.md` |

The agent never edits any of Kore's files. The values chosen for a project live in that project's token file (Token file, question 2), written from `references/tokens.yaml` and following its token names and roles.

### Before the first line of code

Read the project first: request, `PRODUCT.md` (Product file), dependencies, existing components, styles and assets. Anything already answered there is not asked. Ask the open questions below in rounds, skipping those already answered: round 1, questions 1, 4, 5 and 9; round 2, questions 2, 3, 6 and 7; round 3, questions 8 and 10. The next round only after the answers. Each question offers 2 to 4 answers: the proposed one first, marked "(recommended)", then the others this section names; for questions 6 to 8, the answers the request suggests. Use the agent's question tool when it has one, such as AskUserQuestion in Claude Code or ask_user in Gemini CLI; otherwise one chat message per round, with the answers numbered. If none is open, ask nothing and start.

1. **Is it a site or an app?** Asked only when neither the request nor the project makes it clear. It sets the mode, which changes motion:

   | Mode | Purpose | Types |
   |---|---|---|
   | Site | present, persuade | landing page, multi-page site, portfolio, blog, e-commerce storefront |
   | App | work, operate | web app, SaaS, dashboard, management software, admin, documentation, e-commerce cart, checkout and account area |

   A project with both is two jobs, each in its own mode.
2. **Which framework, and where will it be published?** Follow `references/start/framework.md`, which also holds the Token file and the font links.
3. **Kore components or a UI library?** Asked only when the project is empty; in an existing project, read it from the code (The Library-First Rule). The user chooses, following `references/start/library.md`.
4. **Is there a brand identity already: logo, palette, fonts?** In an existing project, show what was found and ask only to confirm it. If there is none, use Kore's logo and font. Logo, palette and font follow `references/start/brand.md`.
5. **What language is the interface in?** Asked only when neither the request nor the project makes it clear. The language is never chosen by default, not even the language the user writes in: no answer is marked "(recommended)"; the answers are the language the user writes in, English and several languages.
   - **One language:** which one. No selector.
   - **Several languages:** which ones, and which is the primary. The primary language is always shown on the first visit and is the one the strings start from. The language selector is a part of the project's navigation: its form is in the file of the chosen navigation. It lists the languages the user chose.
   - The strings are written in the languages the user names, never translated unasked. The labels these rules quote in English ("Close menu", "Account menu") are written in the interface's language.
   - **Right to left:** in every project, as `references/rules/language.md` says.
6. **Who uses it?** Asked only when neither the request nor the project makes it clear. The answer goes in `PRODUCT.md` (Users).
7. **What is it for?** Asked only when neither the request nor the project makes it clear. The answer goes in `PRODUCT.md` (Product Purpose).
8. **What content is there already (texts, images, data)?** Asked only when neither the request nor the project makes it clear. One of the answers is "the agent writes the texts" (`references/start/content.md`). The answer goes in `PRODUCT.md` (Evidence on Hand).
9. **Which themes?** Asked only when neither the request nor the project makes it clear. The answers, the first recommended: light and dark, following the system preference; light only; dark only; light and dark with a theme switch. The answer goes in `PRODUCT.md` (Capabilities and Constraints).
10. **Which typology?** Asked only when neither the request nor the project makes it clear. It sets the look; accessibility and hierarchy stay the same in every typology. The answers are minimalism, neobrutalism, maximalism and bento grid. The recommended one is minimalism, unless one of these holds: neobrutalism when the users are creative or expert people and the purpose is to stand out; maximalism when the product is entertainment and the brand wants to be remembered; bento grid when the page shows features or works in at most 9 tiles. Glassmorphism, liquid glass and neumorphism only when the user names them. With no answer, minimalism. Then read `typologies/<name>/SKILL.md`, its `references/tokens.yaml` and `references/components/`; their rules and values win over the defaults.
    - **Minimalism:** flat surfaces, a reduced palette, few elements, wide empty space, marked type.
    - **Neobrutalism:** high contrast, blocks, bold colors, thick borders.
    - **Maximalism:** bold colors, clashing textures and patterns, several fonts, every space filled.
    - **Bento grid:** content in tiles of different sizes on a grid, edges aligned, no gaps.
    - **Glassmorphism:** translucent layers over a blurred background, vivid colors, a thin light border.
    - **Liquid glass:** a translucent material that refracts and reflects what is around it and reacts to touch and pointer.
    - **Neumorphism:** elements of the same material as the background, raised from it or pressed into it; soft and low in contrast.

After the answers, sum up the choices in two or three lines, write `PRODUCT.md` (Product file), then the token file (Token file, question 2). Then build one section of a page or one component at a time:

1. **The user picks where to start.** If the request already names what to build, start there. Otherwise ask where to start and list the sections of a page and the components the request contains, in no order and without recommending one. If the request does not say what the page contains (for example "make me a landing page"), ask; never propose sections of a page.
2. **A section of a page is a part of a page with the components it contains** (a hero, a login form with its fields and buttons). **A component is a single one** (a card, a button). Build only the one chosen.
3. **Know the content before building,** as `references/start/content.md` says.
4. **Deliver and wait.** After the delivery report, wait for the user to approve or ask for changes. The user picks what comes next: never move on alone.
5. **If the user asks for everything at once,** build it all together, only after knowing all the content (point 3), and give one delivery report.
6. **Navigation:** every project has one, a Top bar or a Sidebar, never both (`references/components/top-bar.md`, `references/components/sidebar.md`). It is built with the first page, also when the request does not name it.

**Product file.** `PRODUCT.md`, at the project root: read and write it as `references/start/product-file.md` says.

**Decisions file.** `KORE-DECISIONS.md`, at the project root: write it as `references/start/decisions-file.md` says.

### Building anything

1. Check for a UI library first (The Library-First Rule).
2. If Kore defines the component, use it. If not, compose it from Kore's components and tokens; never invent values.
3. Before the first line of code, write the Order of decisions (Hierarchy) in `KORE-DECISIONS.md` (Decisions file). Show the user a summary in their language, never the table: what they will see in reading order and what stands out most, the layout in one sentence, and each choice no rule covers as a question. Wait for the OK. Then apply the rules of the sections involved.
4. If the request breaks a binding rule, do not apply it: follow Binding rules in Behaviour rules.
5. Before delivering, run `references/checks.md`, box by box. The work is finished only when `scripts/kore_check.py`, with `--url` for each page built or changed (Measure), exits with 0, or, when it cannot run, every Measure box is checked by hand. Report the result in two lines: first, what was built, what was fixed and any choice no rule covered; second, the command of the last `kore_check` run, made after the last edit, and the summary line it printed (`0 ✗, 2 ?`).

Existing code is not proof: a reused or previously approved component goes through the same checks as a new one.

**Demo pages.** In a component catalog or demo page, each demo counts as its own screen for the rules that count per screen (The One Primary Rule, a secondary button never alone), and its numbers and copy are samples, not invented data.

### Ask later, when it matters

Everything else starts from a default and is asked only when the work reaches it.

| Topic | Default until asked | Ask when |
|---|---|---|
| Dates, currencies and units | Those of the user's locale | The first date, price or measure goes on screen |
| Identity | The active values in `references/tokens.yaml` | The user asks to change colors or fonts: offer the palettes, `canvas` and font options in `references/candidates.md`, or apply their palette with the Custom palette method |

### Behaviour rules

- **Short messages.** Every message to the user starts with the decision, the proposal or the question, and adds no explanation unless the user asks why. This holds for the questions, the summary before the code and the delivery report.
- **Never invent values.** Every visual value comes from the tokens in `references/tokens.yaml`: colors, typography (size, weight, line height, letter spacing), radii, spaces, shadows, z-index, breakpoints, durations, easings, opacities and icon sizes.
  1. **Always allowed, without a token:** `0`, `auto`, `100%`, `1fr`, `inherit`, `currentColor`, the 1px border of The Hairline Rule, and values computed by the rules of `references/rules/` or of a component's file (for example inner radius = outer radius − distance, the opacities in Custom palette).
  2. **When a value is needed, look for it in this order:**
     1. an existing token;
     2. a sum of spacing tokens (for example `space-6` + `space-2` = 32px);
     3. if neither works, the value is missing: propose one that follows the rules of `references/rules/` and of a component's file, say which rule it comes from, and wait for approval. Do not use it before.
  3. **An approved value becomes a token** in the project's token file, named in the same style as Kore's, and is reused from there. It is never written directly in a component and never added to `SKILL.md`.
  4. **In a redesign,** the values already in the project follow Migration (`references/audit.md`).
- **When no rule covers a choice:**
  1. **If the choice changes what the user sees or does** (a component Kore does not define, which actions are in view, the order or content of what appears), ask the user and wait for the answer. Do not choose on your own.
  2. **Otherwise** compare the options with these tests, in order, and take the first one that decides:
     1. the more accessible one;
     2. the one that reuses a component or pattern already in place;
     3. the one with fewer elements on screen;
     4. the one with neutral colors instead of the accent or a semantic color;
     5. the one that separates with the lighter step of The Separation Ladder.
  3. **In both cases,** list in the delivery report the choices no rule covered and how they were resolved.
- **Binding rules are never broken, not even on an explicit request.**
  - **Identity:** the rules in `references/rules/identity.md`.
  - **Accessibility:** contrast minimums, visible focus, 44px touch targets, reduced motion. The full rules live in Color rules (contrast, focus, meaning), Spacing (touch targets, zoom), Motion (reduced motion), Icons (accessible labels) and Responsive (input, safe areas).

  When a request breaks one:
  1. do not apply it;
  2. name the rule and the consequence (for example: "this text drops to 3.1:1, below the 4.5:1 minimum");
  3. offer the closest option that follows the rule.

  If the user still wants that result, that part is outside Kore: the user makes the change, not the agent.
