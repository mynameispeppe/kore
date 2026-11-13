**Textarea**

- **Textarea box:** the browser's resize grip sits away from the rounded corner. height auto; padding-inline-end `space-1`; padding-block-end `space-1`.
- **Textarea:** its padding gives back the room taken by the grip, so the value and the height stay. width 100%; height 100%; min-height calc(`textarea-min` − `space-1`); padding-block `space-2` calc(`space-2` − `space-1`); padding-inline `space-3` calc(`space-3` − `space-1`); resize vertical.
