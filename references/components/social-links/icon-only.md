**Icon-only variant**

- **Icon-only list:** gap `space-2`.
- **Icon-only link:** a square as big as its hit area, the icon centred in it. The `aria-label` is the site's name plus the new-tab note; no tooltip, since the icon is recognized by sight. position relative; width calc(`space-10` + `space-1`); height calc(`space-10` + `space-1`); justify-content center; align-items flex-start; padding-top `space-3`. Its icon: margin 0.
- **Focus underline:** on an icon-only link, the link focus underline under the icon: the link's ::after on :focus-visible, changed in 0s. content ""; position absolute; inset-inline `space-3`; top calc(`space-3` + `space-5` + `space-1`); height `line-thick`; border-radius `rounded-full`; background `ink`; transition 0s.
