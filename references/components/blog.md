# Blog

**Uses:** Cards, List rows, Button.

A section of the page (site.md Blog): the blog's latest articles, each a link to its page.

- **Articles:** the titles, dates, links, reading times and covers the user gives (Never invent values); the newest first, as many as the variant holds. A placeholder is not a cover. Without a reading time the line holds only the date.
- **Title:** the section's title in `headline-md` `ink`, on the start edge, at most 60 characters of `headline-md` wide; the articles `space-12` (48px) under it.
- **Article as a card:** a Cover card (Cards): the title in `title-md`, the subtitle "[date] · [N] min" in `body-md`, tabular figures. Its photo is 4:5 unless its variant says otherwise.
- **Article as a row:** a List row (`references/components/list-rows.md`) with no leading element: the title in `title-sm` `ink`, the line "[date] · [N] min" in `body-sm` `mute`, tabular figures, the 16px arrow in `mute` at the end.
- **See all:** a tertiary button "See all" to the blog's page, `space-8` (32px) under the articles, on the start edge; in Recent and most read, at the end of the Most read column.
- **Choosing the variant:** the first that fits.
  1. No covers → List of articles.
  2. The user names the most-read articles → Recent and most read.
  3. 5 articles, one of them featured by the user → Bento with photo.
  4. 5 articles, none featured → Bento 2+3.
  5. 1 to 4 articles → Grid of articles.
- **Grid of articles:** Cover cards in one column, 2 from a container of 352px, as many columns as articles from 736px.
- **List of articles:** the 4 newest articles as rows. From `lg`, the section's title and a subtitle in `body-lg` `body` (`space-1` under it) in the start third, the rows in the end two thirds, the two columns `space-12` apart, both from the top. Below `lg`, one column, the rows `space-12` under the text.
- **Bento with photo:** the featured card and 4 cards. From `lg`, two equal columns: the featured card at the start, the 4 in two rows of two at the end, as tall as the featured card; their photos take the height left above their text. Below `lg`, the featured card on top with its photo 16:9, the 4 under it in 2 columns from a container of 352px, one column below it.
- **Bento 2+3:** from `lg`, 2 cards in halves on the first row and 3 in thirds on the second, both rows one height, the first row's photos take the height left above their text. Below `lg`, 2 columns from a container of 352px, the fifth card across its row with its photo 16:9; one column below 352px.
- **Recent and most read:** the 2 latest articles as Cover cards, then a column "Most read": its title in `title-md` `ink`, one heading level below the section's title, the 3 most-read articles not among the 2 latest as rows `space-6` (24px) under it, See all at its end with its bottom on the photos' bottom. From `lg` three columns; from a container of 352px the 2 cards side by side and the column under them across the row; below 352px one column.
- **Gaps between cards:** `space-8` (32px), `space-6` (24px) below `sm` (Cards).
