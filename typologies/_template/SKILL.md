# Typology name

## Definition

What the typology is and the traits that define it.

## Where to use

The products and pages it fits, and how to apply it where it fits less.

## Replaces

One line per replaced rule: **Name:** Replaces: `<id>`, then the new rule. The lines go under group headings, only for groups with a replaced rule, in this order: Material, Color, Typography, Space and layout, Interaction and motion, Dark theme and fallback. With no replaced rule, one line says so.

## Files

- `typologies/<name>/references/tokens.yaml`: the keys of `references/tokens.yaml` the typology replaces, and its new keys.
- `typologies/<name>/references/components/`: one file per component whose material the typology replaces, named as in `references/components/`. Each line: **Name:** Replaces: `<id>`, then the new rule in the form of the default file, one property per clause with its token (`box-shadow none; border `line-thin` solid `hairline``).
