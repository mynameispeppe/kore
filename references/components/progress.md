# Progress

**Uses:** Button.

**Purpose:** it shows how far a task has gone, or that content is loading. A bar is for work the user waits on; a skeleton is for content that loads (Usability 1). Never a spinner alone in the middle of a page, a card or a list.

- **Hierarchy:** in a bar the value is the focal point (The One Winner Rule): `title-sm` `ink`; the task's name in `body-md` `ink` names it; the track and its fill only show the amount. A skeleton has no focal point: it holds the place of the content.
- **Elements:** the Progress's own: bar, label row, task name, value, track, fill, segment, end line, skeleton block. Other components: the button that starts the work and the Cancel button (Button).
- **Variant files:** read only the file of each variant that the part being built or checked contains: Bar `references/components/progress/bar.md`, Skeleton `references/components/progress/skeleton.md`.
