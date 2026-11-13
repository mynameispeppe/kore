**Sub-menu**

- **Sub-menu:** only in action menus, and one level only: a sub-menu never opens another. Select, Combobox and navigation menus have none. It looks as the menu. The parent item shows the chevron as its trailing; the parent item and its sub-menu sit in their own wrapper (display flex). It opens on the end side of the parent menu, `space-2` from its edge, with its first item on the parent item: top −`space-1`; inset-inline-start calc(100% + `space-1` + `space-2`).
- **Sub-menu at the start:** with no room on the end side: inset-inline-start auto; inset-inline-end calc(100% + `space-1` + `space-2`).
- **Menu with a sub-menu:** it never scrolls, or it would clip the sub-menu: overflow visible; max-height none.
- **Drilled sub-menu:** with no room on either side (on a phone two menus do not fit side by side), the sub-menu takes the place of the menu's content: the parent menu's other rows and the parent item are display none; the sub-menu: position static; outline 0; padding 0; min-width 0; animation none.
- **Back row:** the first row of a drilled sub-menu, shown only then: an item with the left chevron that returns to the parent menu. display none; in a drilled sub-menu, display flex.
- **Back label:** it says which menu the user returns to. font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Drill motion:** both swaps: the old rows fade out and the new rows fade in whole in `duration-fast`, and the menu's edge moves to the new size with clip-path in `duration-base` `ease-out`; never animate its height. Under reduced motion the content only fades.
- **Sub-menu opening:** click, Enter, Space or →; with a mouse also hovering the parent item, after `duration-base`. The same delay applies before it closes when the pointer moves to another item, so crossing it diagonally does not close it.
- **Sub-menu keyboard:** focus goes to its first item; ← or Escape closes only the sub-menu and returns focus to the parent item. In right-to-left languages the arrows swap.
- **Sub-menu roles:** the parent item is a `menuitem` with `aria-haspopup="menu"` and `aria-expanded`; the sub-menu is a `menu`.
