# Sign in

**Uses:** Form fields, Password, Button, Checkbox and radio, Dialog, Testimonials.

A page of the site (site.md Sign in): the form to sign in or to create an account, on a page of its own or in a Dialog.

- **Fields:** email and password, always. Any other field only when the user asks for it (Never invent values).
- **Sign in:** the password field with `current-password`; "Forgot password?", a text link in `body-md`, under it on the end edge, `space-4` (16px) below the field (Form fields).
- **Sign up:** the password field with `new-password` and its requirements (Password); then one Checkbox, the last field, "I accept the [terms and the privacy policy]": one link, on the names of the documents only, never on "I accept".
- **Form:** a column 400px wide at most (`panel`), centred. The title in `headline-md` `ink`, a verb and an object ("Sign in to your account", "Create your account"), with one line in `body-lg` `body` `space-2` (8px) under it. The fields `space-8` (32px) under the title and `space-6` (24px) apart; the submit, primary, `space-6` below the last field, as wide as the column.
- **Sign in with a provider:** only the providers the product really has (Never invent values). Under the submit, the divider: "or" in `body-md` `mute`, a 1px `hairline` on each side `space-4` from it, `space-6` above and below. Then one secondary Button per provider, in the user's order, as wide as the column, `space-3` (12px) apart, labelled "Continue with [provider]"; on a glow, elevated. The provider's logo is part of its name (Button): one color, `currentColor`, Google 14px (`icon-xs`) and Apple 16px tall so they weigh the same, `space-2` before the text, logo and text centred together.
- **Switch line:** "No account? Sign up" (or "Already have an account? Sign in") in `body-md` `body`, the action a text link, centred, `space-8` below the last provider button, or below the submit when there is none.
- **Page:** at least `100dvh` tall, growing with its content. No Top bar (site.md Navigation): a top row with the logo alone, a link to the home page; a footer with "© [year] [product]" in `body-md` `mute`, centred; both with a padding of `space-4` (16px), `space-8` (32px) from `md`. The form is centred in the space between, with a padding of `space-8` above and below and the page's side padding.
- **Choosing the layout:** the first that fits.
  1. An action in the middle of a task needs the user to sign in → In a Dialog.
  2. A real quote with its author's name and role → Form and review.
  3. A photo the user gives → Form and photo; Centred on a photo only when the user asks for it.
  4. Neither → Centred with glows.
- **Form and photo, Form and review:** from `lg`, two equal halves: the form at the start, the photo or the review at the end, as tall as the page. Below `lg`, the form alone: the photo and the review are hidden.
- **Form and photo:** the photo covers its half (`object-fit: cover`).
- **Form and review:** the half in `surface-elevated`, with a padding of `space-8`, its glows clipped to it (Glows). The quote, at the length of the site's quotes (site.md Sections), in `display-sm` `ink`, centred; the author `space-6` under it. Logo or Avatar as in Testimonials: the logo `space-6` above the quote; the Avatar `space-12` (48px) at the start of the name and the role, `space-3` (12px) from them, the group centred. The name in `title-sm` `ink` and the role in `body-md` `mute` `space-1` (4px) under it, centred on each other.
- **Centred on a photo:** the photo covers the page under `veil-photo`; the logo and the footer in `on-photo`. The form sits in a panel: `surface-card`, 1px `hairline`, radius `xl` = padding `space-6`, 448px at most (the column + 2 × `space-6`), centred; on phones it takes the page's side padding.
- **Centred with glows:** the form column carries the two glows (Glows); the provider buttons are elevated.
- **In a Dialog:** the title names the action that needs the account ("Sign in to save"); the body is the form of the page without its title and line, `space-6` from the title row and from the bottom. Focus goes to the first field (Dialog). The switch line's action is a button styled as a text link that swaps sign in and sign up inside the same Dialog, which keeps its title.
