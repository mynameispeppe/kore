# Images

- **Format:** photos ship as AVIF with WebP as the fallback: `<picture>` with `<source type="image/avif">` and an `<img>` in WebP. Logos, icons and vector illustrations stay SVG.
- **Who prepares them:** if the framework has its own image component, use it (Astro: `<Picture formats={['avif','webp']}>` from `astro:assets`; Next.js: `next/image` with `images.formats: ['image/avif', 'image/webp']`). With plain HTML or Vite + React, the agent converts the files in a separate step that does not stay in the project; if it cannot run commands, it lists the files to convert in the delivery report.
- **Resolutions:** an image whose width follows the layout has a `srcset` with the breakpoint token widths (640, 768, 1024, 1200) plus 2400 (twice `max-content`), never above the original's width, and a `sizes` written from the layout. A fixed-size image (avatar, logo) has `1x` and `2x`.
- **Crop:** `<picture>` with `media` only when another framing reads better on phones.
- **Reserved space:** the `<img>` always has `width` and `height` (the original's size), plus a fixed `aspect-ratio`, `max-width: 100%` and `height: auto`. An image never exceeds its container.
- **Loading:** the main image is the largest one on the first screen (the navigation + the first section), one per page: `fetchpriority="high"`, never lazy. The other images on the first screen are never lazy. Every other image has `loading="lazy"` and `decoding="async"`.
- **Missing image:** a placeholder at the ratio of the expected image, reserving its space like the real one (Reserved space), chosen in this order:
  1. **An image generation tool, when the environment has one:** one image per placeholder, at its ratio, showing the subject the section needs (a book cover, a portrait, a landscape).
  2. **Otherwise a placeholder photo:** `https://picsum.photos/seed/<subject>/<width>/<height>`, with the subject in English and the size at the placeholder's ratio (`book-cover/800/1000` for 4:5). This is the default for every placeholder, screenshots included: the network is assumed.
  3. **Only when the user says there is no network:** a slot in `surface-elevated` with a `hairline` border; at its centre a `label-md` `mute` text says what goes there and the ratio ("Hero photo, 3:2").

  A placeholder is a plain `<img>` with `width`, `height` and `alt` (Alternative text): Format and Resolutions apply to the real image. Its `alt` says what will go there ("Placeholder: book cover"). The delivery report lists every placeholder and asks for images at least 2400px wide for those that follow the layout, and twice the shown size for fixed-size ones (Resolutions).
- **Alternative text:** every `<img>` has an `alt`: an image that informs says what it shows; a decorative image, or one whose text already sits next to it, has `alt=""`.
- **Portrait:** a person's photo larger than an Avatar (48px) is an image outside a card: 4:5 like the Cover card, radius `xl`, a 1px `hairline` drawn inside like the Avatar. Beside text, image and text split the container in two equal halves; below `md` they stack in one column.
