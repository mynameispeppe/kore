"""Responsive (references/rules/responsive.md), Breakpoints; Site pages (references/site.md), Equal side margins."""

# Runs inside a page script after HELPERS, which gives it add, name and shown, and inside the per-width script, which gives it texts, textBox, clipBox, style, px, vw and mode.
BREAKPOINTS = r"""
  // Breakpoints: text sits space-4 from the screen's sides on phones, space-8 from md, and no wider than max-content, 1200px (responsive.md).
  // Text in a box that scrolls sideways or in a fixed layer follows its box; a box that hides overflow trims the text it holds.
  const side = px(document.body, vw >= 768 ? '--space-8' : '--space-4');
  const inset = Math.max(side, (vw - 1200) / 2);
  for (const [el, nodes] of side >= 0 ? texts : []) {
    let t = shown(el) && textBox(nodes);
    for (let a = el; t && a && a !== document.body; a = a.parentElement) {
      const q = a.getBoundingClientRect(), c = clipBox(a, 'x');
      if (style(a).position === 'fixed' || q.width <= 1 || q.height <= 1 || (c && c.scrolls)) t = null;
      else if (c) t = {l: Math.max(t.l, c.l), r: Math.min(t.r, c.r)};
    }
    if (!t || t.r - t.l <= 1) continue;
    if (t.l < side - 1 || t.r > vw - side + 1 || t.r - t.l > 1200 + 1)
      add('✗', 'Breakpoints', `${name(el)} sits outside the page margin or is wider than max-content`, el);
    // Equal side margins (site.md): in Site mode, text stays in the frame centred on the screen.
    else if (mode === 'site' && (t.l < inset - 1 || t.r > vw - inset + 1))
      add('✗', 'Equal side margins', `${name(el)} sits outside the page's centred frame: keep both outer margins equal, with max-content (1200px) centred`, el);
  }
"""
