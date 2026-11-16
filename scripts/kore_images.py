"""Images (references/rules/images.md), Missing image: every <img> loads its file."""

# Runs inside a page script after HELPERS, which gives it add, name and shown.
MISSING = r"""
  for (const img of document.images) if (shown(img) && img.complete && img.naturalWidth === 0) add('✗', 'Images', `${name(img)} shows no image: point it to its file or to the placeholder`, img);
"""
