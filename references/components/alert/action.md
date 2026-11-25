**Action**

- **Action slot under the text:** when the title does not fit on one line beside the action, the action slot moves under the message, at the end of the text, `space-2` under it.
- **Action:** an alert with an action has one tertiary button, small, in the action slot, and no close. Its label is a verb and an object, or "Try again". Every error alert has one action, so the user can recover from here (Usability 9); an alert of another kind has one when the user can fix the situation from here.
- **Action hover:** background-color color-mix(in srgb, `ink` `mix-hover`, transparent); transition box-shadow `duration-fast` `ease-out`, transform `duration-fast` `ease-out`, background-color `duration-instant` `ease-out`.
- **Action pressed:** background-color color-mix(in srgb, `ink` `mix-pressed`, transparent).
