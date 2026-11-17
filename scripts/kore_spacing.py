"""Spacing (references/rules/spacing.md): Blank stretches (blank space is at most half the window tall) and One rest per page."""

# Runs inside a page script after HELPERS, which gives it add, name, shown and style.
BLANK = r"""
  const alpha = c => { const m = c.match(/^rgba\(.*,\s*([\d.]+)\)$|\/\s*([\d.]+)\)$/); return m ? +(m[1] ?? m[2]) : 1; };
  const painted = [];  // [top, bottom, element, kind] of each painted thing, in page coordinates; kind is line, media or box
  const mark = (q, el, kind, top = q.top, bottom = q.bottom) => {
    if (q.width > 1 && q.height > 1) painted.push([top + scrollY, bottom + scrollY, el, kind]);
  };
  const range = document.createRange();
  for (const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); walk.nextNode();) {
    const el = walk.currentNode.parentElement;
    if (!walk.currentNode.data.trim() || !el || !shown(el)) continue;
    range.selectNodeContents(walk.currentNode);
    for (const q of range.getClientRects()) mark(q, el, 'line');
  }
  for (const el of document.body.querySelectorAll('*')) {
    if (!shown(el)) continue;
    const s = style(el), q = el.getBoundingClientRect();
    if (/^(img|video|canvas)$/.test(el.localName) || (el.localName === 'svg' && !el.parentElement.closest('svg'))) mark(q, el, 'media');
    let behind = 'rgb(255, 255, 255)';
    for (let p = el.parentElement; p; p = p.parentElement)
      if (alpha(style(p).backgroundColor) > 0) { behind = style(p).backgroundColor; break; }
    if (s.backgroundImage !== 'none' || s.boxShadow !== 'none' || (alpha(s.backgroundColor) > 0 && s.backgroundColor !== behind)) mark(q, el, 'box');
    for (const d of ['Top', 'Right', 'Bottom', 'Left']) {
      const w = parseFloat(s[`border${d}Width`]);
      if (!(w > 0) || ['none', 'hidden'].includes(s[`border${d}Style`]) || !(alpha(s[`border${d}Color`]) > 0)) continue;
      mark(q, el, 'box', d === 'Bottom' ? q.bottom - w : q.top, d === 'Top' ? q.top + w : q.bottom);
    }
  }
  painted.sort((a, b) => a[0] - b[0]);
  const runs = [];  // painted things that overlap or touch, merged: [top, bottom, first element, element that ends lowest]
  for (const [top, bottom, el] of painted) {
    const run = runs[runs.length - 1];
    if (!run || top > run[1]) runs.push([top, bottom, el, el]);
    else if (bottom > run[1]) { run[1] = bottom; run[3] = el; }
  }
  const told = new Set();
  const gap = (from, to, el, where) => {
    if (to - from <= innerHeight / 2 || told.has(el)) return;
    told.add(el);
    add('✗', 'Blank stretches', `${name(el)} has more than half a window of blank space ${where} it: close the space or fill it`, el);
  };
  // the page ends with the body, not with the window: scrollHeight is never below the window's height
  const pageEnd = document.body.getBoundingClientRect().bottom + scrollY + parseFloat(style(document.body).marginBottom);
  let end = 0;
  for (const [top, bottom, first] of runs) { gap(end, top, first, 'above'); end = bottom; }
  if (runs.length) gap(end, pageEnd, runs[runs.length - 1][3], 'below');
"""

# Runs in the same page script right after BLANK, and reads its painted list.
REST = r"""
  const slices = Math.floor(pageEnd / innerHeight);
  let rests = 0;
  for (let k = 0; k < slices; k++) {
    const start = k * innerHeight, end = start + innerHeight;
    const inside = painted.filter(([top, bottom]) => top < end && bottom > start);
    const heavy = inside.filter(p => p[3] !== 'box');
    if (!inside.length || heavy.length > 1 || ++rests < 2) continue;
    const el = (heavy[0] || inside[0])[2];
    add('✗', 'One rest per page', `${name(el)} is alone in a second rest, a window-tall slice with at most one line of text or one image: make the main element bigger, or cut it`, el);
  }
"""
