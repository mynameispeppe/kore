# Product file

**Product file.** `PRODUCT.md`, at the project root, holds the confirmed facts about the product. It is read first in every session: what it says is not asked again.
- **Sections,** in this order. A section with no confirmed content is left out, never filled with generic text:

  ```markdown
  # Product

  ## Stack
  [Questions 2 and 3: framework, where it is published, Kore components or a library.]

  ## Users
  [Who uses it, in what situation, what they need to do. One or two lines.]

  ## Product Purpose
  [What it does and what success means. Mode: Site or App (question 1).]

  ## Capabilities and Constraints
  [The project's pages, sections and features confirmed by the user.
  Languages: which, and which is the primary (question 5). Themes: default,
  with a switch, or one theme only. Open decisions marked "open".]

  ## Brand Commitments
  [Question 4: logo, palette, fonts. Left out when Kore's identity is used.]

  ## Evidence on Hand
  [Real content with its path: texts, images, data, logos, documents.
  What is missing and must not be invented.]

  ## Accessibility & Inclusion
  [Only needs specific to the project beyond Kore's rules.]
  ```
- **Only confirmed facts.** Texts the agent writes and sample numbers are marked as such (`references/start/content.md`); testimonials, prices and names are never invented.
- **Updated** each time the user defines the content of a section of a page or a component.
- **An existing file:** look for it at the project root, ignoring case (`PRODUCT.md`, `product.md`); in a monorepo, use the one of the app being worked on, and ask when it is unclear. Its sections stay as they are: never rename, move or delete them. Add only the sections Kore needs that are missing, asking only for those. When the file contradicts the project or the user, do not choose: point out the difference, ask which holds, and update the file only after the answer.
