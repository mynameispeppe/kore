# File upload

**Uses:** Form fields, Button, List rows, Progress, Tooltip.

**Purpose:** a drop area with the limits written before the choice, a button to pick files, and the list of chosen files.

- **Hierarchy:** the label comes first, then the drop area, then the file list. The drop area is the focal point (The One Winner Rule): the only dashed edge and the only deep fill; its title in `title-sm` `ink` is read before the limits in `mute`. In each row the file name leads; the secondary line in `body-sm` `mute` follows.
- **Elements:** the File upload's own: upload, upload field, drop area, icon well, drop title, formats, size limit, choose files margin, file input, file list, file row, file head, file name, file value, secondary line, error line, progress spacing, row actions, status. Other components: the label (Form fields), the "Choose files" button (Button, tertiary), the remove and try-again buttons (Button, tertiary icon, small, each with a Tooltip), the rows (List rows, static) and the bar (Progress, with a known amount).
- **Upload:** the field and the file list together, `role="group"` with `aria-labelledby` on the label. max-width `upload`.
- **Upload field:** the label as in Form fields, then the drop area. max-width none.
- **Drop area:** the dashes say files can be dropped here. In order: the icon well, the drop title, the formats, the size limit, the choose button. position relative; display flex; flex-direction column; align-items center; text-align center; padding `space-6`; border-radius `rounded-lg`; background `surface-deep`; border `line-thin` dashed `hairline-medium`.
- **Dragging:** while files are over the drop area: background `surface-hover`; border-color `mute`. Files dropped anywhere else on the page are ignored, so the browser never opens them.
- **Icon well:** a circle holding the Hugeicons `FileUpload` icon at 24, hidden from screen readers (`aria-hidden="true"`). width `space-12`; height `space-12`; border-radius `rounded-full`; corner-shape round; background `surface-elevated`; box-shadow inset 0 0 0 `line-thin` `hairline`; display grid; place-items center; color `mute`; margin-bottom `space-2`.
- **Drop title:** "Drop your files here". color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Touch title:** on devices without hover (hover: none) files cannot be dragged: the drop title is display none and "Upload your files" takes its place, display inline; elsewhere it is display none.
- **Formats:** the accepted formats, written before the user picks a file. margin-top `space-2`; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Size limit:** the maximum size of each file, written before the user picks a file. margin-top `space-2`; color `mute`; font-family `label-md`; font-size `label-md`; font-weight `label-md`; line-height `label-md`; letter-spacing `label-md`.
- **Choose files margin:** the "Choose files" button points to the formats and the size limit with `aria-describedby` and opens the file input. margin-top `space-4`.
- **File input:** the native `input type="file"`, visually hidden and out of the tab order, with its accept and multiple attributes set from the limits; it is emptied after each choice, so the same file can be picked again.
- **File list:** static List rows in a `ul`, each file an `li`. margin-top `space-4`; margin-inline 0.
- **File row:** a box with an edge drawn inside and no fill. The row's edge, fill and icon never change with the state: the message carries it. padding `space-3`; box-shadow inset 0 0 0 `line-thin` `hairline-medium`. Leading: the List rows circle with the Hugeicons `File01` icon at 20.
- **File head:** the file name, then the file value while uploading. display flex; align-items baseline; gap `space-4`.
- **File name:** one line, truncated with an ellipsis. flex 1; min-width 0; color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **File value:** while uploading, the percentage done. color `ink`; font-variant-numeric tabular-nums; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Secondary line:** while uploading, the size and the time left, separated by a middle dot, in minutes from 60 seconds; once uploaded, the size and "100%". color `mute`; font-variant-numeric tabular-nums; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Error line:** in place of the secondary line; the file is not uploaded. Too large: "Over <limit> (<size>). Make it smaller or pick another file." Wrong format: "Format not accepted. Pick a <formats>." Upload failed: "Upload failed." (Usability 9). color `danger`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Progress spacing:** while uploading, the Progress bar under the secondary line, labelled "Uploading <name>". Only the bar and the values change; the list is never redrawn, so focus stays where it is. margin-top `space-2`.
- **Row actions:** "Remove <name>" (Hugeicons `Delete02`) on every row; while uploading it stops the upload and removes the file. Only on a failed upload, "Try again <name>" (Hugeicons `Refresh01`, its tooltip without the name) on its right, which starts the upload again from 0%. gap `space-3`.
- **Focus after removing:** to the remove button of the next file, else of the previous one, else to "Choose files".
- **Status:** one visually hidden `role="status"` region outside the list says what changed: "<name> uploaded", "<name> not uploaded: over <limit>", "<name> not uploaded: format not accepted", "<name> upload failed", "<name> removed". The list and the bars are not live. position absolute; width `line-thin`; height `line-thin`; overflow hidden; clip-path inset(50%); white-space nowrap.
- **On load:** files already uploaded show as uploaded; nothing shows an error before the user adds a file.
