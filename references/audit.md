# Redesign and audit

Applies when the project already exists and the user asks for an audit or a redesign. An audit stops at step 2; a redesign runs every step.

1. **Read the project** as in Before the first line of code: request, `PRODUCT.md`, dependencies, UI library, token or theme file, components, styles, assets. The Start here questions are asked only if still open. After the answers, sum up the choices in two or three lines and write `PRODUCT.md` (Product file).
2. **Write the audit** in `KORE-AUDIT.md` (Audit file). The audit changes nothing in the project. Deliver it and wait. The outcomes are updated only by a new audit, on request.
3. **The user picks what to change:** one or more areas of the audit. If the user does not say, ask, listing the areas with at least one ✗ in order of their most severe ✗ (Severity), ties in the order of Areas; the user picks. If no area has a ✗, say so: the redesign has nothing to change. Only what was picked changes. The picked areas go in the Redesign section of `KORE-AUDIT.md`.
4. **The token or theme file:** if there is none, create it as in Token file. Add Kore's tokens, with Kore's names, only for the themes the project already has; this changes nothing visible, and a new theme is asked (Themes in Ask later). If a picked area concerns the values already in the file, migrate them (Migration): old → new table, approval, then application. This step applies to the whole project, so it comes before any section of a page or component.
5. **One section of a page or one component at a time,** as in Start here. The user picks where to start. If the user does not say, ask, listing the sections of a page and the components with at least one ✗ in the picked areas in order of their most severe ✗ (Severity), ties A–Z; the user picks. Then it is built with Building anything, delivered, and the agent waits. The values written in it follow Migration. Each finished section of a page or component goes in the Redesign section of `KORE-AUDIT.md`. Continue until the user says the redesign is finished.
6. **What is being worked on comes out correct:** the section of a page or the component being worked on passes every check in Building anything. Anything fixed beyond the picked areas is named in the report.
7. **Never touch unasked:** texts and content (navigation labels included), URLs and anchor IDs, meta tags, structured data and social previews, form field names, the IDs and `data-*` attributes that analytics or tests rely on, logic, behaviour, and the areas, sections of a page and components not picked.
8. **The report** is the one in Building anything, plus the before → after of every changed value.

**Audit file.** `KORE-AUDIT.md`, at the project root, written by step 2. It reports how the project follows the rules of SKILL.md, `references/rules/` and the component files. A new audit overwrites it, except the Redesign section.
- **Areas:** the rule sections of SKILL.md and `references/rules/`, in this order: Values (only tokens), Color rules, Typography rules, Spacing, Shapes, Elevation, Motion, Hierarchy, Responsive, Browser surfaces, Icons, Components, Usability, Copy, AI tells, plus **Accessibility**: the accessibility binding rules (Behaviour rules); each one sits only in this area.
- **Every rule** that concerns the project is checked, one by one. Rules that do not concern it are left out (no slider, no Slider rules).
- **Four outcomes:** ✓ follows · ✗ to change · ? not verifiable · – not evaluated.
  - ✗ gives file and line, its severity, what is there and what the rule asks. If the rule is binding, it carries the label "binding".
  - ? says why it cannot be verified and what would be needed (for example a tool for contrast on a semi-transparent color).
  - – says why the rule was not evaluated (a page not opened, an area not reached, no valid evidence). A ✓ or ✗ rests on valid evidence (Evidence); without it the outcome is –.
- **Severity.** Every ✗ takes one, fixed by the rule it breaks: the same ✗ always takes the same severity. kore_check prints it; for a judged rule, answer in order and take the first yes:
  1. An accessibility binding rule (Behaviour rules)? **blocking**.
  2. Does the page scroll sideways, cut text, lay text over text, show a missing image or log a script error? **broken**.
  3. Does fixing it change what the user sees or can do? **visible**.
  4. Otherwise: **hidden**.

  Lists by severity go blocking, broken, visible, hidden.
- **Evidence.** A rule about the rendered page rests on the page opened in the browser at the width the rule names; reading the code is evidence only for rules about the code. A capture counts when it is whole and taken at the width the rule names. A change made after the evidence voids it for the changed part. A rule without valid evidence is – not evaluated.
- **A repeated value** takes one line, with every place it appears.
- **The Components area** uses the boxes of `references/checks.md`.
- **With a UI library,** check how the library's values and theme reach the interface, not the library's internal CSS (The Library-First Rule).
- **Language:** the one the user writes in.
- **Git:** the agent never adds the file to `.gitignore` and never commits it; the user decides.
- **Format.** In each area the lines go ✗ first by severity, then ?, then –, then ✓:

  ```markdown
  # Kore audit
  [Date · project]

  ## Summary
  | Area | ✓ | ✗ | ? | – |

  ## <Area>
  - ✗ <rule> · <severity> · binding · `file:line` · found <x>, the rule asks <y>
  - ? <rule> · why it is not verifiable, what is needed
  - – <rule> · not evaluated · why
  - ✓ <rule>

  ## Redesign
  [Picked areas · finished sections of a page and components · approved Migration tables.]
  ```

**Migration.** In a redesign every value already in the project is replaced by a token, through a table the user approves before any change.
- **Which token replaces which value,** by type:
  - **Spaces and sizes:** the nearest spacing token. A value exactly halfway between two tokens (10px between 8 and 12) leaves the row open, and the user is asked.
  - **Radii:** the value computed by a rule when one applies (The Radius-Padding Rule, The Concentric Rule); otherwise the nearest `rounded` token, with the same halfway rule.
  - **Typography:** the token of the element's role (title, body, label), then the nearest size within that role. Form text stays 16px.
  - **Colors:** by role, never by hue: page background → `canvas`, card → `surface-card`, text → `ink` / `body` / `mute`, border → `hairline`, main action → `primary`. Brand colors confirmed at question 4 follow the Custom palette method. A color with no clear role (a gray used once) leaves the row open.
  - **Shadows:** on a non-interactive element they are removed and become a `hairline` border (The Hairline Rule); on an interactive element they become `shadow-rest` / `shadow-hover`.
  - **Durations, easings, breakpoints:** the nearest token, with the same halfway rule. **Z-index:** the token of the layer (dropdown, modal, toast…).
  - **Fonts:** those confirmed at question 4 stay; otherwise Kore's.
  - **A binding rule wins over the nearest token** (a text color whose nearest token fails the contrast minimum takes the nearest token that passes); the Rule column says so.
- **Table:**

  ```markdown
  | Value | Where | Token | Rule |
  |---|---|---|---|
  | 10px | `Card.css:12`, `Form.css:40` (2) | open: `space-2` or `space-3`? | Never invent values |
  ```

  The whole table is approved; the user can change any row. Nothing is applied before approval.
- **With a UI library,** the token goes into the library's theme (The Library-First Rule).
- **An approved mapping holds for the whole redesign** and is kept in the Redesign section of `KORE-AUDIT.md`: the same value is never asked twice. The tables of later sections of a page and components show only new values.
