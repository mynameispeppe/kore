# Usability

**Heuristics.** Based on Nielsen's 10 usability heuristics. They are principles, applied in the context of each product; the values below are Kore's defaults.

## 1. System status is always visible

**No user action stays without a visible response.**

| Wait | Feedback |
|---|---|
| Under 100ms | Immediate response: pressed state, hover, focus |
| Over 300ms | A loading indicator: skeleton for content, spinner inside the button that started the action |
| Over 1s | A progress bar with percentage when progress is measurable |
| Over 3s | A time estimate and a way to cancel |

- **A submitting button** goes into its Loading state (Button): a spinner and a label ("Saving…"). Completion shows a success toast ("Saved").
- **Page and view changes** show a skeleton, never a silent swap.
- **Content that loads** always shows a skeleton in the shape of the content. Never a spinner alone in the middle of the page, a card or a list. A spinner lives only inside the button that started the action.
- **A multi-step flow** shows where the user is and how many steps are left: the Steps row, or the progress bar with "Step 2 of 4" where the row does not fit (Steps).

## 2. Speak the user's language

- **Use the words people use** for the task, not database or code terms: `FULFILLMENT_PENDING` → "Being prepared", `Error 401` → "Wrong password".
- **Map raw API values** to plain language before showing them.
- **Avoid metaphors** that need explaining; when an icon is not obvious, add the word.

## 3. Control and freedom

- **Undo over confirmation.** A destructive action runs, then a toast offers "Undo" for 5 seconds, as a button on its right. Confirm first only when the action truly cannot be undone.
- **Leaving a form with unsaved changes** asks before discarding them.
- **Dialogs and sheets** always have a visible close control and close on click outside and on Escape.
- **In multi-step flows**, completed steps stay clickable: in the Steps row, and from the review step's Edit buttons (Steps).
- **Applied filters** always show a visible "Clear filters".
- **When a flow must be sequential** (payment, signing), say so clearly.
- **Back** restores the previous page as it was: scroll position, filters and typed input.
- **View in the URL.** Filters, sorting, search, the open tab and the page number live in the URL, so a link or a reload shows the same view.

## 4. Consistency and standards

- **The same action** has the same name, icon and position everywhere ("Save" is always "Save"; a pencil always means edit).
- **Semantic colors** keep one meaning: red only for errors and destructive actions.
- **One format** for dates, currencies and units across the product, produced by shared helpers.
- **Centralise what varies:** design tokens in one place, recurring labels as shared constants.
- **Consistency is not uniformity:** a primary and a secondary button look different on purpose.

## 5. Prevent errors

- **If many users make the same mistake**, the design is wrong, not the users.
- **Constrain input** to valid values: date pickers with invalid ranges blocked, numeric inputs with min, max and step.
- **Show limits and formats** before the action ("Max 5 MB", `DD/MM/YYYY` as a format hint), not after it fails.
- **Validate when the user leaves a field** and suggest corrections; do not wait for submit.
- **Accept variants, keep one format.** A field accepts spaces, dashes, dots and capitals in values such as phone numbers, card numbers and dates, and normalises them when the user leaves it. It never rejects input that only differs in format.
- **Disable an action** whose preconditions are not met, and explain why in a tooltip or helper text.
- **Keep advanced or risky options** behind progressive disclosure.
- **Never block paste** in a field (WCAG 3.3.8).

## 6. Recognition rather than recall

- **Show what the user needs where they need it:** password requirements live under the field and update as they type; an order summary stays visible during checkout; completed steps stay summarised in a wizard.
- **Offer recent items, suggestions and autocomplete** instead of asking people to type from memory.
- **Data entered earlier in the same flow** is filled in or offered to pick, never asked again (WCAG 3.3.7). Fields for the user's own data carry their `autocomplete` value (`name`, `email`, `street-address`).
- **Show a preview** before publishing or confirming.
- **Always show where the user is** (active navigation, title, breadcrumb).
- **In a navigation bar or a short list**, the key actions sit at the start and at the end, the least important in the middle: people remember the first and the last items best.

## 7. Flexibility and efficiency

- **Design for the first-time user**, then add accelerators for experts; the two paths never conflict.
- **Keyboard shortcuts:**
  - Only in an app, and only for the actions the user names; the agent never adds one on its own.
  - Every shortcut uses a modifier (⌘ on Mac, Ctrl elsewhere), never a character key alone (WCAG 2.1.4), and never one the browser or the system already uses (⌘C, ⌘V, ⌘Z, ⌘T, ⌘W, ⌘R, ⌘L, ⌘F, ⌘P, ⌘Q). Escape stays the key that closes overlays.
  - Shortcuts work at every screen size.
- **A command palette** (Cmd/Ctrl + K) or global search when the product has many actions.
- **Bulk actions** for repeated work; presets and templates for repetitive setups.

## 8. Minimal by design

- **For every element ask:** would the user miss it? If not, remove it.
- **Minimal is not fewer features:** show what is needed now and reveal the rest when it is needed (progressive disclosure).
- **One sentence of context**, then the action.
- **Notify only** what needs attention now.

## 9. Help users recover from errors

- **An error message** says **what** went wrong, **why** when useful, and **how** to fix it. Missing one of the three makes it incomplete.
- **Never show error codes** to users; log them instead.
- **Neutral, solution-oriented language**; the user is never blamed.
- **Show the message inline** next to the field that caused it, not in a generic toast at the top.
- **Network failures.** Content that fails to load is replaced by an error alert with "Try again" ("Couldn't load your orders. Check your connection."), never an endless skeleton. An action that fails (save, send) shows an error toast with "Try again" and keeps what the user typed. While offline (`offline` and `online` events), an alert sits at the top of the main content and goes away when the connection comes back. A request with no answer after 10 seconds counts as failed, except an operation that shows a progress bar.
- **Empty states are silent errors:** explain why nothing is shown and what to do next ("No projects yet. Create one").
- **The last step of a flow** says what happened and what comes next ("Plan saved. Your first week starts on Monday"), never a bare "Done".

## 10. Help and documentation

**Help comes in layers**, from best to last resort:

1. **The interface explains itself.**
2. **Inline help:** tooltips on non-obvious icons, helper text under fields with requirements.
3. **Help in context**, where it is needed: an empty state with the next step (Empty state), a Popover next to the control. No up-front tour unless the user asks for one; then it is built with Popover.
4. **Searchable, task-oriented documentation** with numbered steps (at most five per task).

**Help and contact links** sit in the same place and order on every page where they appear (WCAG 3.2.6).

**If many users look up the docs** to do one thing, the interface is the problem.
