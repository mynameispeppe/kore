# Decisions file

**Decisions file.** `KORE-DECISIONS.md`, at the project root, holds the Order of decisions (Hierarchy) of every section of a page and component built, written before its first line of code (Building anything, step 3). It stays as a record: a later change to a section updates its table first.
- **Typology:** one line before the first table, `Typology: [name]`, where the name is the folder in `typologies/` of the answer to Which typology? (Before the first line of code, question 10). Without the line, the typology is minimalism.
- **One table per section or component,** in this form:

  ```markdown
  ## [Name] · [file], [file]

  Shape: [Layout primitive (items)]
  Primary group: [group]

  | Element | Question | Group | Level | Style | Space | Rule |
  |---|---|---|---|---|---|---|
  | [text as it reads] | [user's question] | [group] | Primary | [role] [weight] [color] | space-[n] to [next element] | [Rule name], [Rule name] |
  ```
- **Heading:** the name of the section or component, `·`, every file it touches, separated by commas.
- **On the page:** the root element of the section or component carries `data-kore="[Name]"`, every copy of a repeated component included; each element of a row carries `data-kore-element="[Element]"`: a text, an image, a control, a component. Through them `kore_check --url` finds each row, measures the Style of its text and the Space to its Element (From role to style, The Distance Ratio Rule).
- **Shape:** the Layout primitive (Order of decisions, step 3), with its items in brackets; its items are the Elements of the table, each written once, case ignored.
- **Primary group:** the group that answers the main question of the section or component (Order of decisions, step 2).
- **Element:** one visible element as it reads on screen: a text, an image, a control, or a component taken whole (a Button, a Social links).
- **Question:** the user's question it answers (Order of decisions), in the user's language.
- **Group:** the name of its group (Affinity Grouping); elements answering the same question share it.
- **Level:** `Primary`, `Secondary` or `Tertiary` inside its group, one `Primary` per group (Semantic weight); `—` for what follows its own rule (a section heading, a `label-*` text, a whole component, a consequence, a value label).
- **Style:** type role, weight and color token (From role to style, Roles and sizes; a heading, Typographic levels); for a component, its name and variant (its file); for an image, ratio and radius (Images).
- **Space:** `space-N to [Element]`: the token to the next element, and that element's name as written in its own row (The Distance Ratio Rule, Scale, Grouping and separation); `—` for the last one.
- **Rule:** the sections or rules each value comes from, separated by commas. A value with no rule behind it is not written: it is a choice the user makes (Ask later, when it matters).
