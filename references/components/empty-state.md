# Empty state

**Uses:** Button.

**Purpose:** it sits where content should be and is not. It is a silent error (Usability 9): it says why nothing is shown and what to do next. Content that is still loading is a Skeleton (Progress), not an empty state.

| Case | Title | Message | Action |
|---|---|---|---|
| First use, nothing created yet | what is missing | the next step | one primary button |
| A search or filter matches nothing | names what was asked | how to widen it | one tertiary button, "Clear filter" |
| Nothing left to do, on purpose | a statement that nothing is left | what comes next | none |
| The page does not exist (404) | "Page not found" | why, without blame: "The link is wrong or the page has moved." | one primary button to the main page, "Go to the home page" |

- **Hierarchy:** the icon comes first, then the title, then the message, then the action. The title is the focal point (The One Winner Rule): `title-md` in `ink`, read before the message in `body-lg` `body`; the icon, in `mute`, only marks the place.
- **Elements:** the Empty state's own: empty state, icon well, title, quoted words, message. Other components: the action (Button).
- **Empty state:** inside its container (a Card or a page region), centred: an icon, then the title and message, then the action. display flex; flex-direction column; align-items center; text-align center; padding-block `space-8`.
- **Icon well:** a circle holding one icon at 24, the size for standalone icons (Icons), hidden from screen readers (`aria-hidden="true"`). width `space-12`; height `space-12`; border-radius `rounded-full`; corner-shape round; background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; display grid; place-items center; color `mute`; margin-bottom `space-4`.
- **Title:** a statement, never a question. color `ink`; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`.
- **Quoted words:** a title that quotes what the user searched for keeps its role; the quoted words take quotation marks and the strong weight. font-family `title-md`; font-size `title-md`; font-weight `fontWeight-strong`; line-height `title-md`.
- **Message:** under the title. The Copy rules apply: no "Oops", no apology, no blame. max-width `empty-text`; margin-top `space-1`; color `body`; font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`.
- **Action:** at most one, with a label that is a verb and an object. A primary button only when it is the screen's main action (The One Primary Rule); in a Dashboard piece the first-use action is a tertiary button that opens the items' page (Dashboard, Pieces). margin-top `space-6`.
- **404:** it fills the page's main region, not a card, and the page `<title>` says "Page not found". The title keeps `title-md`.
- **Announcement:** none on load. When the empty result follows a search or a filter the user just applied, the region is `role="status"`.
