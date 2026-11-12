# Accordion

**Purpose:** a list of headings that each open an answer or a section underneath. Use it for content people scan and open only in part; content they all need to read is shown, not hidden.

- **Hierarchy:** in each item the heading comes first, then the answer; in the heading, the label, then the chevron. The label is the focal point (The One Winner Rule): `title-md` in `ink`, read before the chevron (`mute`) and the answer (`body-lg` in `body`). Every item keeps the same order and weight (Semantic weight 2).
- **Elements:** all the Accordion's own, no other component: list, item, heading, heading-button, label, chevron (the icon `ArrowDown01`, `icon-md`), answer, answer-inner.
- **List:** display flex; flex-direction column; background-color transparent; box-shadow none.
- **Item:** border-bottom none.
- **First item:** border-top none.
- **Item after the first:** border-top `line-thin` solid `hairline`.
- **Heading:** margin 0.
- **Heading button:** display flex; align-items center; justify-content space-between; gap `space-4`; width 100%; min-height `accordion-row`; padding `space-3` 0; text-align start; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; color `ink`; transition outline 0s, text-decoration 0s, text-underline-offset 0s.
- **Heading button focus:** outline none; text-decoration underline `line-thick`; text-underline-offset `space-1`.
- **Label:** flex 1; color `ink`.
- **Label text:** the question or the section name, in one line when it can.
- **Chevron:** width `icon-md`; height `icon-md`; color `mute`; transition transform `duration-base` `ease-out`, color `duration-fast` `ease-out`.
- **Chevron open:** transform rotate(`flip`).
- **Chevron hover and focus:** color `ink`.
- **Answer:** display grid; grid-template-rows 0fr; transition grid-template-rows `duration-base` `ease-in`; font-family `body-lg`; font-size `body-lg`; font-weight `body-lg`; line-height `body-lg`; letter-spacing `body-lg`; color `body`; padding 0.
- **Answer open:** grid-template-rows 1fr; transition-timing-function `ease-out`.
- **Answer inner:** min-height 0; overflow hidden; opacity 0; transition opacity `duration-fast` `ease-in`.
- **Answer inner open:** opacity 1; transition-timing-function `ease-out`.
- **Answer spacer:** content ""; display block; height `space-4`.
- **Open motion:** the items, the content below and the scrollbar move together; the answer fades whole, never uncovered line by line.
- **Reduced motion:** transition 0s on the chevron and on the answer; the answer inner only fades.
- **Open items:** each item opens and closes on its own, so several can be open together. All items start closed.
- **Markup:** a heading element one level below the section's heading (`<h3>` under an `<h2>`) holding a full-width `<button>` with `aria-expanded` and `aria-controls`; the whole row is the click target. The answer is a `region` with `aria-labelledby` pointing to the heading, `aria-hidden="true"` and inert while closed. Enter and Space open and close it.
