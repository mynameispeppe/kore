# Stats

**Uses:** Cards.

A section of the page (site.md Stats): the product's own figures, each with the label that says what it counts.

- **Figures:** from 2 to 4, the figures the user gives (Never invent values). A figure is `headline-lg` `ink` with tabular figures, its label `body-md` `mute` `space-1` (4px) under it. The label says what the figure counts in a whole phrase ("invoices sent last year"), never one word every item repeats ("Invoices").
- **Heading:** every variant has a title and a text: the section's title in `headline-md` `ink`, its text in `body-lg` `body` `space-1` (4px) under the title, except in Row of figures, where the title and the text are the two halves. In every variant but Row of figures the heading is at most 60 characters of `body-lg` wide.
- **Choosing the variant:** the first that fits.
  1. The user gives a photo of the place or the people → Figures on a photo.
  2. The user gives a screenshot of the product → Figures and visual side by side.
  3. There are 4 figures → Text and figures side by side.
  4. There are 2 or 3 figures → Row of figures.
- **Row of figures:** the heading's title and text as the two halves (Side by side, `references/components/hero.md`), starting at the same height, `space-12` (48px) over the figures. From a container of 1024px the figures sit on one row, one column each, centred in their cell, with a 1px `hairline` vertical line between two columns, `space-8` (32px) on each side of it; below 1024px one column, `space-8` apart, with no line. No call to action: only the two side-by-side variants have one.
- **Text and figures side by side:** Side by side: the heading and one `primary` call to action `space-6` (24px) under the text on the start side; the 4 figures on the end side in two columns, `space-8` apart on both axes at every width.
- **Figures and visual side by side:** Side by side, the two halves starting at the same height: on the start side the heading, one `primary` call to action, and the screenshot `3/2` `space-8` under it, more than the `space-6` that ties the call to action to the text; on the end side the 4 figures as cards (Cards, Key figure), each with an explanation under its label that says how its figure is counted, at most two lines; two columns from a container of 672px and one below it, `space-8` apart and `space-6` (24px) below 640px (`sm`), the cards of a row all of one height, their content centred.
- **Figures on a photo:** the photo fills the section behind a `veil-photo` veil, the section as tall as its content, `space-12` above and below and `space-6` (24px) at the sides; the heading centred in a column of at most 60 characters of `body-lg`, the figures `space-12` under it as in Row of figures, with no line and no call to action. All the text in `on-photo`.
- **Zones aligned:** figures side by side start their figure and their label at the same height (subgrid), whatever the length of the labels.
