**Action column**

- **Action:** a tertiary icon Button, small, with a 20px icon (`MoreHorizontal`), an accessible label and a Tooltip that name the row ("More options for Leg day"). When the row offers several commands, that button opens a Menu, with the destructive command last. The scroll container never clips it (Stacking order): the menu is placed on the screen (position fixed), min-width calc(`space-48` + `space-8`), its end edge on the trigger's end edge, `space-2` below the trigger, or above it when there is no room below; it closes when the page or the container scrolls, and focus inside it returns to the trigger.
- **Action column:** the last one: its header "Actions", centred. width calc(`space-12` + `space-8`).
