# Right to left

- **Always, in every project:** CSS logical properties instead of left and right (`margin-inline-start`, `padding-inline`, `inset-inline-start`, `text-align: start`), so the project is ready for right-to-left at no cost.
- **Page language:** `<html>` carries `lang` with the language of the page (`lang="it"`): screen readers pronounce it and the script reads its dates in it (WCAG 3.1.1).
- **When a language of the project is right-to-left** (Arabic, Hebrew, Persian, Urdu): `dir="rtl"` on `<html>` while that language is active.
- **Every "left" and "right" in `SKILL.md` and in `references/` holds for left-to-right languages.** In right-to-left they swap: actions align to the left with the confirming action last on the left, the F and Z patterns and "top-left is read first" mirror.
- **Icons:** only icons that point a direction mirror (arrows, back and forward chevrons, undo and redo, reply, send, indent), with `transform: scaleX(-1)` under `[dir="rtl"]`. The others never mirror: check, clock, search, audio and video controls, logos.
- **Stay left-to-right:** code (`dir="ltr"` on the block), phone numbers, web and email addresses.
- **Keyboard and motion:** arrow keys follow the visual direction; sheets and side transitions enter from the mirrored side.
