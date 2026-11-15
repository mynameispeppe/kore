# Hierarchy

**Attention.** Hierarchy is the architecture of attention: it tells the eye what to look at first, what next, and what to ignore. A correct hierarchy lets a user understand a screen in under five seconds without reading a word.

## Order of decisions

**One order.** For any set of content (a card body, a page section, a form, a menu, a navigation, a dashboard), decide in this order, never skipping or reversing a step. Every step uses the same question: **"which question of the user does this element answer?"**

1. **Groups** (Affinity Grouping): group the elements that answer the same question. No shape yet.
2. **Semantic weight:** the group, and in each group the element, that answers the main question is Primary (Semantic weight).
3. **Shape:** the number of groups decides the layout, never the other way around, built only from the Layout primitives.
4. **Visual weight:** the roles become style (From role to style, Text hierarchy).
5. **Separation:** space with The Distance Ratio Rule, then the Separation Ladder and group titles (Grouping and separation).

## Affinity Grouping

**The Relatedness Test.** For every pair of elements: "do they answer the same question for the user, or two different ones?" The same question makes one group, whatever the number of elements and the shape of the layout. Different questions make separate groups, even with the same format, size or data type.

**Never a uniform grid for different groups.** Equal spacing, equal cells and equal styling make elements read as one group (Uniform Connectedness): four figures in a 2×2 grid with equal gaps say "all four are related the same way" even when they are two pairs. Different groups are separated with The Distance Ratio Rule. Instances of one component (cards in a grid, rows in a list) answer the same question and stay uniform.

**Examples:**
- **About:** role and specialization answer "who is this professionally" and are one group; social links answer "where else do I find them" and are another.
- **Checkout form:** name, email and phone answer "how do I reach you"; the shipping address is another block.
- **Prose:** two sentences on one idea stay in one paragraph; a new idea starts a new paragraph.
- **Navigation:** task links stay together; account and settings are a group of their own, placed last.

**No invented categories.** The agent never invents a category to group elements the content does not group (Semantic weight 4).

## Layout primitives

**Four primitives.** Every layout, from a card to a page, is built from four primitives, nested: a container holds a region, the primitives arrange what is inside it, as in Every Layout and the Atlassian Design System. A component file that sets its own layout follows it.

| Primitive | Arranges | Use for | When space runs out |
|---|---|---|---|
| **Stack** | items in a column | the groups of a component, the rows of a group, a total above its breakdown | — |
| **Inline** | items in a row, wrapping like words, rows `space-2` (8px) apart | buttons, chips, metadata, values of one kind | the items wrap to the next line |
| **Sidebar** | one narrow item beside one wide item, on the baseline of the wide item's first line | an icon, avatar or image beside text; a title with its details | the narrow item wraps when the wide one would be narrower than half the container: above the wide one when it identifies it, under it when it adds to it (rule 2) |
| **Grid** | cells of equal width, as many as fit, each at least the width its component sets | repeated items (cards, photos), the parts of a list | fewer columns |

1. **One axis.** Everything in a component starts on its start edge, at the padding set by The Radius-Padding Rule. Only two things leave it: the narrow item of a Sidebar placed at the end, and the actions (Action order). A Sidebar's narrow item that wraps returns to the start edge.
2. **The narrow item of a Sidebar** sits at the start when it identifies the wide one (icon, avatar, image), at the end when it adds to it (details, a value, an arrow).
3. **Only Grid stretches its items** to fill the width; Stack, Inline and Sidebar keep each item at its content's size, except the wide item of a Sidebar.
4. **Centre a whole container or nothing in it:** centred content is the only content of its container (empty state, error page); never one group among start-aligned groups. Tables follow Table.
5. **The gap sits on the primitive** (Proximity and hierarchy): `space-2` between controls in an Inline (Grouping actions), `space-4` (16px) between pieces of text.
6. **One primitive per group.** The smallest primitive holding every item of a group holds only items of that group: the gap sits on the primitive, so a group gets its own primitive to keep The Distance Ratio Rule.

## Visual weight

| Tool | Rule |
|---|---|
| Size | The bigger element is read first. Headings are clearly larger than their subheadings; the primary button is larger than secondary actions; functional icons are larger than decorative ones. |
| Contrast | Primary text uses full contrast (`ink`); metadata steps down (`body`, `mute`), always within the 4.5:1 minimum. |
| Color | One color family for primary actions. Saturated beats desaturated; color never carries meaning alone. |
| Shape contrast | A shape that breaks the pattern stands out (a round badge on a square icon). Kore keeps one corner language, so shape contrast comes from form (pill, circle, dot), never from mixing corner styles. |
| Position | Top-left is read first in left-to-right layouts; an element surrounded by space weighs more than the same element in a crowd. |
| Density | A dense area weighs more but can confuse. Reduce density of secondary areas; an isolated element gains weight from the empty space around it. Never the same density everywhere. |

**The One Winner Rule.** Every section of a page and every component has one focal point, the Primary of its Primary group. When the focal point is text, every other text row of its table is smaller, or of the same size and no heavier, metadata (date, author, category) included. The focal point comes first among the text rows of the Shape, and on the page its box sits above every other text element of the section or component, or level with it and to its left. A text row is a row whose Level is Primary, Secondary or Tertiary and whose Style names a type role.

## Three levels

- **Primary:** one element, the focal point. Caught first.
- **Secondary:** two or three elements that support it and add context.
- **Tertiary:** everything else; present, never distracting.

**Placement.** To isolate the focal point, surround it with space and place it on a third of the layout (the upper third, or the top-left crossing) rather than at the dead centre.

| Context | Focal point | Typical mistake |
|---|---|---|
| Landing page | Hero headline or main image | Three elements of similar size in the hero |
| Dashboard | The most important metric | A grid of identical cards with no leader, or a whole page of same-size icon + heading + text cards |
| Form | The first field to fill | Label and input with the same weight |
| Product or content card | Image or title | Price, title and badge at the same weight |
| Error page | The error message | A decorative illustration heavier than the message |
| Dialog | Title and primary action | Three equivalent buttons |

## Semantic weight

**Every level.** Before choosing how something looks (Visual weight), decide what it is: apply the same three roles as *Three levels* (Primary, Secondary, Tertiary) to a component, and again to everything nested inside it, and again to the group of components it belongs to.

1. **The reader's question.** This is step 2 of the Order of decisions. At any level, ask: "if the user read only one element here, what would let them act or understand?" That element is Primary; the rest scales toward Secondary or Tertiary by how close it comes to answering the same question. Re-apply it at every level: the section holding several components, then each component, then each row, then each control. Never assume the answer at one level carries to the next.
2. **One priority per repeating component.** For a component that repeats (cards in a grid, rows in a table), answer once: "what should the user perceive first across every instance?" That answer is the default for classifying every field in every instance, so the reasoning is not redone each time.
3. **State the default; never apply or flag it silently.** Building new content: apply the default and name it in one line ("gave the price more weight: it usually drives the decision here; say if the goal differs"). Reviewing existing content with an asymmetry (one card larger, one field bolder): don't assume it is a mistake, so name it as an open question ("this card is bigger than its neighbors: is it the main offer, or should the row be even?"). Correct immediately once answered, and never ask the same question twice for the same component type.
4. **A weight the content doesn't earn is not fixed by adding a component.** If nothing in the request or the content confirms that one instance outranks the other instances of its component (cards in a grid, rows in a list), the default is equal weight, not an invented badge, tag or highlight to assert a priority no one confirmed (Behaviour rules, Never invent values). Ask, or wait until the priority is confirmed, before building the component that would express it.

## From role to style

**Derived from the Primary.** Step 4 of the Order of decisions. Each level sits below the one above in size or weight, and differs in color. The Primary's size comes from Roles and sizes; the others follow from it, never chosen by eye.

| Level | Size | Weight | Color |
|---|---|---|---|
| **Primary text** | The role Roles and sizes gives its context | The role's own | `ink` |
| **Secondary text** | The largest Body role smaller than the Primary, or of its size under a Primary heavier than 400: `body-lg` (16) under `title-lg`, `body-md` (14) under `body-lg` or `title-sm` | 400 | `body` |
| **Tertiary text** | The Body role right below the Secondary: `body-md` (14) or `body-sm` (12) | 400 | `mute` |

- **Tertiary below Secondary.** The Tertiary is always smaller than the Secondary. The Secondary matches the Primary's size only under a Primary heavier than 400. Without a Secondary, the Tertiary is set as if the Secondary were there.
- **Figures.** A figure inside the Secondary takes its Emphasis role (Typography).
- **Outside this rule:** labels (`label-*`: buttons, tabs, group titles, column headers), which follow their components; the key figure (`display-*`); colored surfaces (Text hierarchy 9) and consequences (Text hierarchy 7).
- **Weight of groups:** the Primary group comes first in the reading order (Scanning patterns). Groups of one level have titles of the same role; a group's weight comes from its position, never from a larger title.

## Typographic levels

- **One `h1` per page;** it names the page. Heading levels follow each other without skipping one (`h2` under `h1`, `h3` under `h2`).
- **Section headings:** the heading of a page section is an `h2` in `headline-md`; the heading of a region inside it, an `h3` in `headline-sm`. The element of a heading always follows its level; inside a component, its style follows the component's file (a card title is `title-lg` whether it is an `h3` or an `h4`).
- **At most three or four type levels** visible on one screen.
- **Adjacent levels** differ clearly in size and/or weight; if two roles look almost the same, drop one.
- **Weight can compensate size:** a medium `label-lg` (14px) can outrank a regular `body-lg` (16px).
- **Bold** only for key terms; if everything is bold, nothing is.
- **No all caps** on long text.
- **No eyebrow** or kicker label above a heading; the heading carries its own weight.

## Text hierarchy

**Order before style.** Inside a component (a card, a popover, a dialog, a row), decide the order before the style.

1. **Order first.** Decide what the user needs now, the action that comes next, and the context that changes the decision. Say each idea once (Copy).
2. **Emphasize by de-emphasizing.** The primary element stays `ink`; everything else steps down. Take weight away from the secondary text instead of making the primary louder.
3. **Value labels are a last resort.** A value whose format says what it is, a price, a date or an email, stands alone. A value label and its value merge into one phrase when the words allow it: 12 left in stock, 148 g a day. A value label that stays is the quieter half: its row in the Decisions file has Level —, `body-md` 400 `mute`, a Space to its value, and cites Value labels are a last resort. Form fields keep their visible labels.
4. **Limits.** In each section of a page and each component, the text rows with Level Primary, Secondary or Tertiary use at most three font sizes; two roles of one font size, such as `title-md` and `body-lg` at 16px, count once. At most three levels, set by From role to style. Weights: those of the Roles and sizes table, emphasis included, and `strong` where Emphasis allows it; no other weight. Text colors: `ink`, `body`, `mute`, and nothing else for plain text. No gradient text: emphasis comes from weight or size, never decoration.
5. **Figure and unit.** The figure carries the emphasis. When the text of an element opens with a figure, every word after it is smaller than the figure and in `mute`: **148** g a day, **12** left in stock. A date keeps one style; a figure inside a sentence follows Inline emphasis.
6. **Balance weight and contrast.** Heavy shapes (filled icons, large glyphs) take a softer color (`mute`); thin text keeps `ink`.
7. **Consequences are never quiet.** A consequence sits on its own line, in the emphasis role of its size (Emphasis) and in `danger`; its row in the Decisions file has Level — and cites Consequences are never quiet. The words carry the meaning: an icon joins them only when the text alone does not read as a consequence.
8. **Semantics follow hierarchy.** A destructive action in a list or menu is tertiary or secondary, with red limited to its icon; it becomes a filled `destructive` button only when it is the main action of the moment, as in the confirmation.
9. **No grey text on colored surfaces.** On a tinted or colored background, secondary text takes a tint of that color, not `mute`.
10. **Inline emphasis.** In a sentence, the words the user must check stand out in the emphasis role of their size (Emphasis) and `ink`: figures with their unit (a quantity, a price, a date) and the name of the object an action affects ("**Next week's plan** and its **21 meals** will be removed."). At most two per sentence, never color, never whole phrases. It applies to explanations and messages (errors, confirmations); captions, subtitles and help text stay plain.

## Grouping and separation

**The Separation Ladder.** Separate with the lightest step that works, and never skip steps:

1. **Space only**: the gap does the work, zero graphic noise. The default.
2. **Background change**: a surface step (`surface-card`, `surface-elevated`) for wide sections.
3. **Line**: a 1px `hairline`, only between sections of equal importance, never on every row.
4. **Card** (surface + border): maximum separation and weight.

- **Rows in a list separate with space**, not with a divider on every row; a divider on each row makes every item look like its own section.
- **Containers only when needed:** the group changes context sharply (data vs. actions vs. navigation), proximity is not enough because the layout is dense, or the group is clickable as one unit. A border added "to tidy up" means the grouping is wrong.
- **Other ways to group** without containers: alignment on a shared axis, the same background tone, the same type style for the same category.
- **Group titles.** A group carries a title, the name of the question it answers, when the user looks for an item by its category: navigation groups, Settings, form sections, page sections, and the options or actions of a menu (selects and comboboxes included) split into categories the content names (countries by continent, time zones by region). A group whose items are found by reading them has no title and is separated by space or a line: the actions of a card, the destructive group of a menu, the parts of a sheet.
- **All or none:** in one container, if one group has a title, every group has one.

**The Working Memory Rule.** At most four items side by side that the user must compare before choosing: the buttons of one action group, the segments of a segmented control, tabs, the avatars of a group (Cowan 2001). From the fifth: the extra actions go in a "More" menu (Spacing, Grouping actions); segments and tabs become a select; avatars become a count avatar. Menus, selects, lists, tables and navigation have no count limit: their items are read, not remembered, and long ones follow their own component's rules.

## Scanning patterns

- **F pattern** (dense content: feeds, tables, search results, dashboards): the left column and the first two lines of each block are always read. Put titles, status and key actions on the left; the first column of a table carries the most important data.
- **Z pattern** (sparse content: landing pages, cards, simple forms): brand top-left, primary action top-right, key message at the centre-left turn of the Z, final action bottom-right.
- **Action order.** In a component (card, dialog, form, multi-step flow), actions are right-aligned; the confirming action is last on the right, and cancel or back sits immediately to its left. An action that opens more options instead of answering, as Customise does, sits at the left, apart from the answers (Cookie banner). In a page section, actions are the last item under the text they act on (title, text, actions), aligned with that text (centred when it is centred, Layout primitives 4), `space-6` below it; the main action comes first.
- **A perfectly symmetric layout** follows no pattern and guides nothing: break symmetry on purpose for the focal point (wider, taller, isolated).
- **Critical information** never lives only at the bottom right of an F layout.
- **Number sections** (01 / 02 / 03) only when the order itself is information the reader needs.
