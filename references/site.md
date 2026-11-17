# Site pages

Rules for the pages of a project in site mode (Start here, question 1). They add to the rest of Kore and replace none of it.

## Navigation

- **Every page has the Top bar** (`references/components/top-bar.md`), built with the first page, also when the request does not name it. The sign-in and sign-up pages have none: the logo alone (Sign in).

## Hero

- **Variant:** one of the eight in Hero (`references/components/hero.md`), chosen as in its Choosing the variant.
- **Title:** the hero's title is the page's `h1`.
- **Text:** only the title, the subtitle and the calls to action (one `primary` and at most one `secondary`, The One Primary Rule), or a form in their place (Hero). A tagline under the calls to action, a "Used by" strip, a price teaser, a bullet list and a row of avatars go in the sections under the hero.
- **Logo wall:** in its own section directly under the hero; one of the two variants in Logo wall (`references/components/logo-wall.md`). With both clients and integrations, the clients' Logos only goes under the hero and the integrations' Title and text after the Features section.

## How it works

- **When:** the product is used in an order the visitor has to learn (set up, then use, then get the result). With no order, the section is Features.
- **Rules:** How it works (`references/components/how-it-works.md`).

## Comparison

- **When:** the user gives a named competitor and real figures for both products. Without them there is no Comparison section (Never invent values): ask for the figures or drop the section.
- **Rules:** Comparison (`references/components/comparison.md`).

## Features

- **When:** the product's features have no order the visitor has to learn. With an order, the section is How it works.
- **Rules:** Features (`references/components/features.md`).

## Stats

- **When:** the user gives the product's own figures, from 2 to 4. Without figures there is no Stats section (Never invent values): ask for them or drop the section.
- **Rules:** Stats (`references/components/stats.md`).

## Pricing

- **When:** the product is sold in plans and the user gives their prices, from 1 to 4 plans. Without prices there is no Pricing section (Never invent values): ask for them or drop the section.
- **Rules:** Pricing (`references/components/pricing.md`).

## Testimonials

- **When:** the user gives quotes from clients, from 1 to 4, each with its author's name and role. Without quotes there is no Testimonials section (Never invent values): ask for them or drop the section.
- **Rules:** Testimonials (`references/components/testimonials.md`).

## FAQ

- **When:** the user gives the questions visitors ask and their answers, from 1 to 4. Without answers there is no FAQ section (Never invent values): ask for them or drop the section.
- **Rules:** FAQ (`references/components/faq.md`).

## Blog

- **When:** the user gives the blog's articles, at least one, each with its title, date and link. Without articles there is no Blog section (Never invent values): ask for them or drop the section.
- **Rules:** Blog (`references/components/blog.md`).

## CTA

- **When:** every landing page, as its last section, directly above the Footer.
- **Rules:** CTA (`references/components/cta.md`).

## Sign in

- **When:** the product has accounts. A page of its own to sign in and one to sign up, or a Dialog when an action in the middle of a task needs the account.
- **Rules:** Sign in (`references/components/sign-in.md`).

## Sections

- **A heading opens every section.** The first text of each section is its heading, visible at every width: the page's `h1` in the first section, an `h2` (Section headings) in the others. A section of logos or photos opens with its heading too.
- **Each shape once per page.** A section's shape is its Shape in the Decisions file: the Layout primitive with the kinds of its items, in either order. An item's kind comes from its row: text when its Style names a type role, an image when its Style gives a ratio, else the component its Style names; so a Sidebar of a portrait and a bio and a Sidebar of an intro and a photo are one shape. A section on the CTA band is another shape from the same primitive and items on the page's background. The hero counts. A second section with a shape already on the page takes another primitive or other items.
- **At most four items per section** (cards, features, quotes), the number of The Working Memory Rule. The others go on their own page, reached by a "See all" link at the end of the section. The logo wall has no limit. A column of rows under its own title counts as one item. The Blog's two bentos hold five cards, the number their layout needs (Blog).
- **Quotes** carry the name and the role the user gives (Evidence on Hand). A quote holds at most 25 words; for a longer one, the user chooses the sentence to keep.
- **Profiles on other sites** are Social links.
