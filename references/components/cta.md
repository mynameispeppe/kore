# CTA

**Uses:** Button.

A section of the page (site.md CTA): the last call to action of the landing, on a band of its own.

**Choosing the variant.** The first yes wins:
1. The hero is Full-bleed photo, or the user gives no image for the section (a placeholder does not count) → Centred.
2. A photo of a place, people or an object → On photo.
3. A portrait or square visual → Text and visual side by side.
4. A landscape visual → Centred, visual below.

- The visual is the one image the user gives for the section; with more than one, ask which.
- A form takes the place of the calls to action, under the subtitle; its button is the `primary` (Form fields). The variant does not change.

**All variants**

- **Band:** the whole page width, `surface-elevated`; padding `space-32` (128px) above and below, `space-48` (192px) from `md`, and the page side margin at the sides (`space-4`, `space-8` from `md`). Outside the band, the space between sections as for every section.
- **Text:** the title in `headline-md` `ink` (Section headings); the subtitle in `body-lg` `body`, `space-1` (4px) under it; the calls to action, one `primary` and one `secondary`, `space-6` (24px) under the subtitle, `space-2` (8px) apart, wrapping. The text block is at most 60ch of `body-lg` wide (its `font-size` is `body-lg`).
- **Centred column** and **Side by side:** as in Hero (`references/components/hero.md`, All variants).
- **Motion:** the section's Scroll reveal (`references/rules/motion.md`, Site mode), never the hero's entry.

**Variants**

1. **Centred:** Centred column; the two glows (`references/rules/color.md`, Glows) inside the text block, on its corners.
2. **Centred, visual below:** Centred column; the visual 16:9, `space-12` (48px) under the text, as wide as the content.
3. **Text and visual side by side:** Side by side; the visual 4:5.
4. **On photo:** no band. The section is at least the screen under the bar tall (`100dvh` minus `space-8` × 2 and `env(safe-area-inset-top)`), its content centred on both axes; title and subtitle in `on-photo`; the photo, the veil, the text and the `elevated` second call to action as in Hero Full-bleed photo.
