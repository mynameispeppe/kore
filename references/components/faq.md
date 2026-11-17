# FAQ

**Uses:** Accordion.

A section of the page (site.md FAQ): the questions visitors ask about the product, each with its answer.

- **Questions:** the questions and answers the user gives, in the user's order (Never invent values), at most 4 (site.md Sections).
- **Accordion or Open list:** Accordion (`references/components/accordion.md`); Open list only when the user asks for every answer to be visible.
- **Open list:** each question a heading one level below the section's title in `title-md` `ink`, its answer `space-4` (16px) under it in `body-lg` `body`; pairs `space-8` (32px) apart, no lines.
- **Text or Photo:** Photo when the user gives a photo for the section (a placeholder does not count); otherwise Text. The four variants: Text and Accordion, Photo and Accordion, Text and Open list, Photo and Open list.
- **Columns:** from `lg`, two equal halves `space-8` (32px) apart, both starting at the top edge; the row is as tall as the taller column, and both columns take its height. Below `lg`, one column, the second `space-12` (48px) under the first.
- **Text:** the start column holds the section's title in `headline-md` `ink` and the subtitle `space-1` (4px) under it in `body-lg` `body`, at most 60 characters of `body-lg` wide; the end column holds the questions.
- **Photo:** the section's title in `headline-md` `ink` on the start edge, `space-12` (48px) above the two columns; the start column holds the photo, 4:5, at the top of its column; the end column holds the questions, no subtitle. Below `lg` the photo comes first, under the title.
- **Close:** "More questions? [Write to us]" in `body-lg` `body`; the link is a Link in running text to the site's contact page, or to the user's email when the site has no contact page. Only with a real contact (Never invent values); without one, no close. It is the last element of the start column in Text, of the end column in Photo. From `lg` it sits at the bottom of its column, so its last line ends where the other column ends (the last question, or the photo); at least `space-8` (32px) under the content above it, also below `lg`.
