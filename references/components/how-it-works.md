# How it works

**Uses:** Steps.

A section of the page (site.md How it works): what the visitor does, in order, each step with its own visual.

- **Steps:** from 2 to 4, an `ol` with one `li` per step. Their order is the reading order, so nothing repeats it in the text.
- **Step:** four zones in this order, `space-4` (16px) apart: the number, the title in `headline-sm` `ink`, the text in `body-lg` `body` `space-1` under the title, the visual. The title names the action with a verb ("Connect the account"), never "Step 1"; the text is at most two lines.
- **Number:** the 24px circle of Steps (`references/components/steps.md`, Row) with the step's number in `label-sm` with tabular figures. No step is open or done here, so every circle is the same: a 1px `hairline-medium` border drawn inside and the number in `ink`. It is `aria-hidden`, because the `ol` already carries the order.
- **Row or column:** all the steps on one row, one column each, when the section is at least `n × 320px` plus `(n − 1) × space-8` (32px) wide — 320px is the column of 45 characters of `body-lg`. Below that they stack, all of them: never some side by side and the rest below.
- **Line between the steps:** 1px `hairline`, solid (never dashed, Charts), `aria-hidden`, `space-2` (8px) from each circle. On a row it runs from one circle to the next one on its right; stacked it falls from one circle to the next one below, through the `space-12` between them. The last step has no line.
- **Stacked:** the circle and the title sit on one row, the number's 24px column then `space-4`; the text and the visual follow in the title's column. `space-12` (48px) between two steps, so each visual stays with its own text.
- **Visual:** a photo or a screenshot of the step, `3/2` on a row and `16/9` stacked, where it takes the whole column. Every step has one: with a visual for only some of them, the section is Features instead.
- **Zones aligned:** on a row the four zones start at the same height in every column (subgrid), whatever the length of the titles and the texts.
- **Title of the section:** `headline-md` `ink`, `space-12` over the steps (The Distance Ratio Rule).
