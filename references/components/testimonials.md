# Testimonials

**Uses:** Avatar, Logo wall.

A section of the page (site.md Testimonials): what the product's clients say about it, each quote with its author.

- **Quotes:** from 1 to 4, the words, names and roles the user gives, in the user's order (Never invent values). A quote keeps the length of the site's quotes (site.md Sections).
- **Logo or Avatar:** each quote shows its client's logo or its author's Avatar, never both. The user chooses one form for the whole section; when the user gives only logos or only photos, that one; with neither, the name and the role alone. A quote without the chosen form: without a photo, the Avatar with the author's initials (Avatar); without a logo, no logo, its quote still at the height of the others' quotes (Zones aligned).
- **Author:** the name in `title-sm` `ink`, the role in `body-md` `mute` `space-1` (4px) under it. The Avatar sits at the start of the name and the role, `space-3` (12px) from them, centred on the two.
- **Logo:** above the quote, one color in `mute`, `space-8` (32px) tall (Logo wall, Logos).
- **Order:** logo, quote, author, `space-6` (24px) apart, on the canvas: no card, no surface.
- **Choosing the variant:** the first that fits.
  1. One quote with a photo of its author that the user gives (a placeholder does not count), and no other section of the page with the shape Grid (image, text) (site.md, Each shape once per page) → Photo and quote side by side.
  2. One quote → Single quote.
  3. 2 or 3 quotes → Row of quotes.
  4. 4 quotes → Quotes 2×2.
- **Single quote:** no title, no glow. The logo, the quote and the author centred in the section; the quote in `display-sm` `ink`, the Avatar `space-12` (48px). Without an Avatar the name and the role are centred; with it, the Avatar and the two lines form one centred group, the lines on its start edge.
- **Photo and quote side by side:** no title. Side by side (`references/components/hero.md`), with the author's photo `4/5` at the start in place of the text and the quote at the end; below `lg`, the photo first and the quote `space-12` under it. The photo leads because it says who is speaking. The quote on the start edge in `display-sm` `ink`, the Avatar `space-12` (48px).
- **Row of quotes:** the section's title in `headline-md` `ink`, on the start edge, at most 60 characters of `headline-md` wide; the quotes `space-12` (48px) under it, each on the start edge of its column, in `body-lg` `body`, the Avatar `space-10` (40px). 3 quotes: 3 columns from a container of 1024px; 2 quotes: 2 columns from 672px; columns `space-8` (32px) apart. Below that, one column, quotes `space-12` apart. Never 2 + 1.
- **Quotes 2×2:** as Row of quotes, with the 4 quotes in two rows of two from a container of 672px, rows `space-12` apart; below 672px one column, quotes `space-12` apart.
- **Rating:** only when the user gives a rating, its number of reviews and where they come from, and only in Row of quotes and Quotes 2×2, `space-2` (8px) under the title. In order: 5 stars, the rating in `title-sm` `ink`, then " · [number] reviews on [source]" in `body-md` `mute`, figures tabular, `space-2` between the stars and the rating. The stars are the Hugeicons `Star` at `icon-sm` (16px), with no space between them: full ones filled in `ink`; the rating rounded to the nearest half, a half star is the outline in `mute` with a full star on top clipped to its start half; the rest outlines in `mute`. The stars are one image named "[rating] out of 5"; the visible rating is hidden from screen readers, so it is read once.
- **Zones aligned:** quotes side by side start their logo, quote, name and role at the same height (subgrid), whatever the length of their texts.
