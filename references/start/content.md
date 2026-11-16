# Content

**Know the content before building.** Its texts, items, fields and actions come from the request, `PRODUCT.md` or the user: when they are missing, ask for them, one per message. Each text the user gave carries `data-kore-user` on its element; `kore_check` runs Copy on every other text. When the user has no content yet and says to go on:

- **Images** become placeholders (Images, Missing image).
- **Texts:** the agent writes them (titles, descriptions, section texts, button labels), in the interface's language, complete and specific to the request, never placeholder text. When all are written, they go through Copy, humanizer included.
- **Sample numbers:** statistics a section needs are written realistic and uneven ("47.2%", not "50%"), each element carrying `data-kore-sample`; `kore_check` reports every one until it is replaced.
- **Never written:** names of people, products and clients, testimonials, prices, dates, awards and logos. Names stay as bracketed slots ("[Photographer's name]"); the rest is left out.

Everything written, sampled or missing goes in `PRODUCT.md` under Evidence on Hand ("written by the agent, to confirm", "sample, to replace", "missing"), and the delivery report lists it.
