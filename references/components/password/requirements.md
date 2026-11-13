**Requirements**

- **Requirements:** only with `autocomplete="new-password"`, never on sign in, and visible from the start, before the user types. Under the box, linked to the input with `aria-describedby` and announced with `aria-live="polite"`. list-style none; margin 0; padding 0; padding-inline-start `space-2`; display flex; flex-direction column; gap `space-1`.
- **Requirement:** one rule of the password per row, updated while the user types. display flex; align-items center; gap `space-2`; color `mute`; font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`.
- **Met requirement:** color `ink`.
- **Requirement icon:** an empty circle while unmet, a check circle once met, `icon-sm`; the shape changes, so the state never depends on color alone. flex none; display block; color `mute`.
- **Met requirement icon:** color `success`.
- **Requirement state:** visually hidden text after each row, "met" or "not met", changed with the icon. position absolute !important; width `line-thin`; height `line-thin`; overflow hidden; clip-path inset(50%); white-space nowrap.
- **Unmet requirement in error:** the row and its icon: color `danger`.
