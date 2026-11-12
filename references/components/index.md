# Components

**The Library-First Rule.** Before building any component, check whether the project already uses a UI library (for example shadcn/ui, Radix, MUI, Headless UI, a native component kit). Look at the dependencies and the existing components; if it is not clear, ask the project owner before writing anything.

- **A library is in use:** never rewrite its components. Keep the library and adapt it to Kore: map Kore's tokens (colors, typography, rounded, spacing, shadows, motion) onto the library's theme, and override a component's styles only where the library's defaults break a Kore rule. Library sizes and behaviours that break no binding rule stay as they are: a 40px library button stays 40px, because 40 is on the grid, and its hit area extends to 44px (Touch targets). Typical overrides: shadows on menus, selects, popovers, dialogs and static cards (replaced by a `hairline` border), contrast, focus visibility, off-grid values, animations under reduced motion. Use the library's theming API (theme variables, token overrides) rather than rewriting its internal CSS. If the project uses the library's icon set, keep it; labeled buttons still carry no icon.
- **No library:** use the Kore components listed below, built on Kore's tokens and following every rule in `references/rules/`.

**Index.** Each component lives in its own file, read as Kore's files says (Start here).

| Component | File |
|---|---|
| Button | `references/components/button.md` |
| Form fields | `references/components/form-fields.md` |
| Select | `references/components/select.md` |
| Checkbox and radio | `references/components/checkbox-radio.md` |
| Switch | `references/components/switch.md` |
| Segmented control | `references/components/segmented-control.md` |
| Tabs | `references/components/tabs.md` |
| Password | `references/components/password.md` |
| Combobox | `references/components/combobox.md` |
| Number stepper | `references/components/number-stepper.md` |
| Slider | `references/components/slider.md` |
| Date picker | `references/components/date-picker.md` |
| File upload | `references/components/file-upload.md` |
| Steps | `references/components/steps.md` |
| Command palette | `references/components/command-palette.md` |
| Carousel | `references/components/carousel.md` |
| Charts | `references/components/charts.md` |
| Dashboard | `references/components/dashboard.md` |
| Cookie banner | `references/components/cookie-banner.md` |
| Hero | `references/components/hero.md` |
| Logo wall | `references/components/logo-wall.md` |
| How it works | `references/components/how-it-works.md` |
| Comparison | `references/components/comparison.md` |
| Features | `references/components/features.md` |
| Stats | `references/components/stats.md` |
| Pricing | `references/components/pricing.md` |
| Testimonials | `references/components/testimonials.md` |
| FAQ | `references/components/faq.md` |
| Blog | `references/components/blog.md` |
| CTA | `references/components/cta.md` |
| Sign in | `references/components/sign-in.md` |
| Footer | `references/components/footer.md` |
| Social links | `references/components/social-links.md` |
| Menu | `references/components/menu.md` |
| Popover | `references/components/popover.md` |
| Dialog | `references/components/dialog.md` |
| Sheet | `references/components/sheet.md` |
| Tooltip | `references/components/tooltip.md` |
| Overlay rules | `references/components/overlay-rules.md` |
| Alert | `references/components/alert.md` |
| Toast | `references/components/toast.md` |
| Badge | `references/components/badge.md` |
| Chip | `references/components/chip.md` |
| Progress | `references/components/progress.md` |
| Empty state | `references/components/empty-state.md` |
| Avatar | `references/components/avatar.md` |
| Table | `references/components/table.md` |
| Pagination | `references/components/pagination.md` |
| Accordion | `references/components/accordion.md` |
| Breadcrumb | `references/components/breadcrumb.md` |
| Top bar | `references/components/top-bar.md` |
| Sidebar | `references/components/sidebar.md` |
| Cards | `references/components/cards.md` |
| List rows | `references/components/list-rows.md` |
