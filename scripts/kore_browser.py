"""Kore check, phase 2: measures rendered pages in a browser, for the rules
that only the result shows (references/checks.md, Measure).

Needs Playwright for Python and a Chromium browser already installed
(Google Chrome, then Microsoft Edge, or the executable in KORE_BROWSER);
no browser is downloaded. kore_check imports this module only for --url.

Every page is opened in each theme the token file defines at each width of
WIDTHS, then at 1280px with the root font size at 200% (Zoom). Touch is
emulated below 1024px. With a shots folder, the whole page is also saved as
a PNG at each width of SHOTS, in each theme, from the same visit.
"""
import os
from collections import defaultdict
from urllib.parse import urlparse

WIDTHS = (320, 375, 639, 768, 1023, 1024, 1440, 2560)  # 639 and 1023: just below sm and lg
TOUCH_BELOW = 1024
ZOOM_WIDTH = 1280
SHOTS = (375, 1440)  # phone and desktop (references/checks.md, Bounded verification)
HEIGHT = 800
INSTALL = ("python3 -m pip install --user playwright, then install Google Chrome "
           "or set KORE_BROWSER to a Chromium-based browser")

# Runs in the page. Returns [kind, rule, message] for each finding.
MEASURE = r"""
async ({touch, zoom, tables}) => {
  const out = [];
  // A finding on an element the page waives (data-kore-ignore="<Rule>: <reason>") comes back as ignored.
  const add = (kind, rule, msg, ...els) => {
    for (const el of els) {
      const w = el && el.closest('[data-kore-ignore]');
      const m = w && w.dataset.koreIgnore.match(/^([^:]+):\s*(\S.*)$/);
      if (m && m[1].split(',').some(r => r.trim().toLowerCase() === rule.toLowerCase())) {
        out.push(['ignored', rule, `${msg}: ${m[2].trim()}`]);
        return;
      }
    }
    out.push([kind, rule, msg]);
  };
  const where = zoom ? 'Zoom' : 'Extremes';
  const doc = document.documentElement;
  const vw = doc.clientWidth;
  const style = el => getComputedStyle(el);
  const shown = el => el.checkVisibility({opacityProperty: true, visibilityProperty: true});
  const name = el => {
    let s = el.localName + (el.id ? '#' + el.id : '');
    const cls = typeof el.className === 'string' ? el.className.trim().split(/\s+/)[0] : '';
    if (!el.id && cls) s += '.' + cls;
    const text = (el.getAttribute('aria-label') || el.innerText || el.value || '').trim().replace(/\s+/g, ' ');
    return text ? `${s} "${text.slice(0, 30)}"` : s;
  };
  const scrollTo = el => el.scrollIntoView({block: 'center', inline: 'center', behavior: 'instant'});
  // Measure the end state: scroll the page once so scroll reveals run, then finish every animation
  // and transition that ends (an endless spinner keeps turning).
  const frame = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  for (let y = 0; y < doc.scrollHeight; y += innerHeight) { window.scrollTo({top: y, behavior: 'instant'}); await frame(); }
  for (const a of document.getAnimations()) {
    try { if (a.effect.getComputedTiming().iterations !== Infinity) a.finish(); } catch (e) {}
  }
  window.scrollTo({top: 0, behavior: 'instant'});
  await frame();

  // Any CSS color as [r, g, b, alpha], through a canvas.
  const paint = document.createElement('canvas').getContext('2d', {willReadFrequently: true});
  const rgba = color => {
    paint.clearRect(0, 0, 1, 1);
    paint.fillStyle = '#0000';
    paint.fillStyle = color;
    paint.fillRect(0, 0, 1, 1);
    const [r, g, b, a] = paint.getImageData(0, 0, 1, 1).data;
    return [r, g, b, a / 255];
  };
  const over = (f, b) => [0, 1, 2].map(k => f[k] * f[3] + b[k] * (1 - f[3])).concat(1);
  const lum = c => {
    const ch = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; };
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2]);
  };

  // Elements that hold text of their own, and the box of that text.
  const texts = new Map();
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (walker.nextNode()) {
    const node = walker.currentNode, el = node.parentElement;
    if (!node.data.trim() || !el || el.closest('script, style, noscript, template, svg, option')) continue;
    if (!texts.has(el)) texts.set(el, []);
    texts.get(el).push(node);
  }
  const textBox = nodes => {
    let l = Infinity, t = Infinity, r = -Infinity, b = -Infinity;
    for (const node of nodes) {
      const range = document.createRange();
      range.selectNodeContents(node);
      for (const q of range.getClientRects()) {
        if (!q.width || !q.height) continue;
        l = Math.min(l, q.left); t = Math.min(t, q.top); r = Math.max(r, q.right); b = Math.max(b, q.bottom);
      }
    }
    return r > l ? {l, t, r, b} : null;
  };

  // A box that hides what overflows it, on one axis, and whether it scrolls; null when it clips nothing there.
  const clipBox = (el, axis) => {
    const overflow = axis === 'x' ? style(el).overflowX : style(el).overflowY;
    if (overflow === 'visible') return null;
    if (el === doc || el === document.body) return axis === 'x' && overflow !== 'auto' && overflow !== 'scroll' ? {l: 0, r: vw} : null;
    const q = el.getBoundingClientRect();
    return {l: q.left + el.clientLeft, t: q.top + el.clientTop, scrolls: ['auto', 'scroll'].includes(overflow),
            r: q.left + el.clientLeft + el.clientWidth, b: q.top + el.clientTop + el.clientHeight};
  };
  const trimmed = (from, to) => {
    for (let el = from; el; el = el.parentElement) {
      const s = style(el);
      if (s.textOverflow === 'ellipsis' || (s.webkitLineClamp && s.webkitLineClamp !== 'none')) return true;
      if (el === to) return false;
    }
    return false;
  };

  if (!document.documentElement.lang.trim()) add('✗', 'Page language', '<html> has no lang');

  // Horizontal scroll, and what makes it.
  const wide = document.scrollingElement.scrollWidth;
  if (wide > vw + 1) {
    const scroller = el => {
      for (let p = el.parentElement; p && p !== document.body && p !== doc; p = p.parentElement)
        if (['auto', 'scroll'].includes(style(p).overflowX)) return true;
      return false;
    };
    const past = el => { const q = el.getBoundingClientRect(); return q.width && (q.right > vw + 1 || q.left < -1); };
    const culprits = [...document.body.querySelectorAll('*')]
      .filter(el => past(el) && shown(el) && !scroller(el) && !past(el.parentElement));
    add('✗', where, `the page is ${wide}px wide on a ${vw}px screen: ${culprits.slice(0, 3).map(name).join(', ') || 'body'}`);
  }

  // Text cut by a box that hides overflow, and text over text; text a scroll box shows only in part
  // (a carousel, a scrolling sidebar) is neither cut nor over the text beside it.
  const boxes = [], inView = [];
  for (const [el, nodes] of texts) {
    if (!shown(el)) continue;
    const t = textBox(nodes);
    if (!t) continue;
    let hidden = false, cut = false, scrolled = false;
    for (let a = el; a && !hidden && !cut; a = a.parentElement) {
      for (const axis of ['x', 'y']) {
        const c = clipBox(a, axis);
        if (!c) continue;
        const [lo, hi, tlo, thi] = axis === 'x' ? [c.l, c.r, t.l, t.r] : [c.t, c.b, t.t, t.b];
        const out = tlo < lo - 1 || thi > hi + 1;
        if (c.scrolls) { scrolled = scrolled || out; continue; }
        if (hi - lo <= 1 || thi <= lo || tlo >= hi) { hidden = true; break; }  // visually hidden, or off on purpose
        if (out && !trimmed(el, a)) { cut = true; break; }
      }
    }
    if (hidden) continue;
    if (cut) add('✗', where, `text cut: ${name(el)}`, el);
    boxes.push(el);
    if (!scrolled) inView.push([el, {l: t.l + scrollX, t: t.t + scrollY, r: t.r + scrollX, b: t.b + scrollY}]);
  }
  // A sticky or fixed bar with an opaque background covers the text it scrolls over, on purpose.
  const pinned = el => {
    for (let a = el; a && a !== document.body; a = a.parentElement) {
      const s = style(a);
      if (['sticky', 'fixed'].includes(s.position) && rgba(s.backgroundColor)[3] >= 1) return true;
    }
    return false;
  };
  const reported = new Set();
  for (let i = 0; i < inView.length; i++) {
    for (let j = i + 1; j < inView.length; j++) {
      const [a, p] = inView[i], [b, q] = inView[j];
      if (a.contains(b) || b.contains(a) || reported.has(a) || reported.has(b)) continue;
      if (pinned(a) !== pinned(b)) continue;
      if (Math.min(p.r, q.r) - Math.max(p.l, q.l) > 2 && Math.min(p.b, q.b) - Math.max(p.t, q.t) > 2) {
        add('✗', where, `text over text: ${name(a)} and ${name(b)}`, a, b);
        reported.add(a); reported.add(b);
      }
    }
  }
  if (zoom) return out;

  // Touch targets: the area around the centre reaches the target, a rounded corner included.
  // A visually hidden control (a skip link before its focus) is for the keyboard: no target.
  const sronly = el => {
    const s = style(el), r = el.getBoundingClientRect();
    return r.width <= 1 || r.height <= 1 || s.clip === 'rect(0px, 0px, 0px, 0px)' || /^inset\(50%/.test(s.clipPath);
  };
  const targets = [...document.querySelectorAll(
    'a[href], button, input:not([type=hidden]), select, textarea, summary, [tabindex]:not([tabindex="-1"]), ' +
    '[role=button], [role=link], [role=tab], [role=checkbox], [role=radio], [role=switch], [role=menuitem], [role=option]')]
    .filter(el => !el.closest('[inert], [aria-hidden=true]') && !el.matches(':disabled') && shown(el) && !sronly(el));
  const owns = (el, hit) => hit && (el.contains(hit) || [...(el.labels || [])].some(l => l.contains(hit)));
  const inList = el => el.localName === 'a' && el.parentElement && el.parentElement.localName === 'li';
  const inText = el => el.localName === 'a' && [...el.parentElement.childNodes]
    .some(n => n.nodeType === 3 && n.data.trim());
  // Adjacent targets: visible edges at least space-2 (8px) apart. The visible edge is the element's box
  // when it paints a background, a border or a shadow; a field without its own border shows the box
  // around it; anything else shows only its text and icons.
  const page = q => ({l: q.left + scrollX, t: q.top + scrollY, r: q.right + scrollX, b: q.bottom + scrollY});
  const paints = el => {
    const s = style(el);
    return rgba(s.backgroundColor)[3] > 0 || s.boxShadow !== 'none' ||
      ['Top', 'Right', 'Bottom', 'Left'].some(k => parseFloat(s[`border${k}Width`]) > 0 && rgba(s[`border${k}Color`])[3] > 0);
  };
  const edges = el => {
    if (paints(el)) return page(el.getBoundingClientRect());
    if (/^(input|select|textarea)$/.test(el.localName)) {
      for (let p = el.parentElement; p; p = p.parentElement) if (paints(p)) return page(p.getBoundingClientRect());
    }
    let l = Infinity, t = Infinity, r = -Infinity, b = -Infinity;
    const drawn = [...el.querySelectorAll('*')].filter(n => n.matches('svg, img') || paints(n));  // icons, and shapes like a chart's bar
    const parts = [...drawn, ...(texts.has(el) ? [el] : []), ...[...texts.keys()].filter(n => el.contains(n))];
    for (const n of parts) {
      const box = drawn.includes(n) ? n.getBoundingClientRect() : textBox(texts.get(n));
      const q = box && 'left' in box ? {l: box.left, t: box.top, r: box.right, b: box.bottom} : box || {};
      if (!(q.r > q.l)) continue;
      l = Math.min(l, q.l); t = Math.min(t, q.t); r = Math.max(r, q.r); b = Math.max(b, q.b);
    }
    return page(r > l ? {left: l, top: t, right: r, bottom: b} : el.getBoundingClientRect());
  };
  const touching = el => el.getAttribute('role') === 'menuitem' || inList(el);
  const rects = targets.map(el => [el, edges(el)]);  // before anything scrolls

  for (const el of targets) {
    const w = 44, h = el.getAttribute('role') === 'menuitem' ? 40 : inList(el) && !touch ? 32 : 44;
    scrollTo(el);
    const q = el.getBoundingClientRect(), cx = q.left + q.width / 2, cy = q.top + q.height / 2;
    let miss = null;
    for (let k = 0; k <= 8; k++) {  // the centre and 8 points on the ellipse inside the w × h area
      const x = k ? cx + Math.cos(k * Math.PI / 4) * (w / 2 - 1) : cx, y = k ? cy + Math.sin(k * Math.PI / 4) * (h / 2 - 1) : cy;
      if (x < 0 || y < 0 || x >= innerWidth || y >= innerHeight) continue;
      const hit = document.elementFromPoint(x, y);
      if (!owns(el, hit)) miss = miss || hit;
    }
    if (!miss) continue;
    const other = targets.find(t => t !== el && owns(t, miss));
    const msg = `${name(el)} is ${Math.round(q.width)}×${Math.round(q.height)}px and its hit area is not ${w}×${h}` +
      (other ? ` (it reaches ${name(other)})` : '');
    add(inText(el) ? '?' : '✗', 'Touch targets', inText(el) ? msg + ': a link inside a paragraph' : msg, el);
  }

  // Adjacent targets, on the edges measured above.
  for (let i = 0; i < rects.length; i++) {
    for (let j = i + 1; j < rects.length; j++) {
      const [a, p] = rects[i], [b, q] = rects[j];
      if (a.contains(b) || b.contains(a) || (touching(a) && touching(b))) continue;
      if ([...(a.labels || [])].some(l => l.contains(b)) || [...(b.labels || [])].some(l => l.contains(a))) continue;
      const dx = Math.max(q.l - p.r, p.l - q.r), dy = Math.max(q.t - p.b, p.t - q.b);
      if (dx < 0 && dy < 0) continue;  // one over the other: an inline button inside its field
      const gap = Math.max(dx, dy);
      if (gap < 8 - 0.5) add('✗', 'Adjacent targets', `${name(a)} and ${name(b)} are ${Math.max(0, Math.round(gap))}px apart`, a, b);
    }
  }

  // Contrast of the text against what is really under it.
  const probe = document.createElement('div');
  probe.style.cssText = 'position:absolute;background:Canvas';
  document.body.append(probe);
  const canvas = rgba(style(probe).backgroundColor);
  probe.remove();
  // Text of a disabled control is exempt (Contrast: stone on disabled elements): the control, its
  // labels and the text it points to with aria-labelledby or aria-describedby.
  const exempt = new Set();
  for (const c of document.querySelectorAll(':disabled, [aria-disabled=true]')) {
    exempt.add(c);
    for (const l of c.labels || []) exempt.add(l);
    for (const id of `${c.getAttribute('aria-labelledby') || ''} ${c.getAttribute('aria-describedby') || ''}`.split(/\s+/)) {
      const n = id && document.getElementById(id);
      if (n) exempt.add(n);
    }
  }
  for (const el of boxes) {
    if ([...exempt].some(n => n.contains(el))) continue;
    scrollTo(el);
    const t = textBox(texts.get(el));
    if (!t) continue;
    // Under the text: the element and its ancestors up to the first one the point reaches
    // (a pointer-events: none element is never reached), then whatever lies under that one.
    const stack = document.elementsFromPoint((t.l + t.r) / 2, (t.t + t.b) / 2);
    const under = [];
    for (let p = el; p; p = p.parentElement) {
      under.push(p);
      const i = stack.indexOf(p);
      if (i >= 0) { under.push(...stack.slice(i + 1)); break; }
    }
    let alpha = 1;
    for (let p = el; p; p = p.parentElement) alpha *= +style(p).opacity;
    const layers = [];
    let image = false;
    for (const n of under) {
      const s = style(n);
      if (['img', 'video', 'canvas', 'picture', 'iframe'].includes(n.localName) || s.backgroundImage !== 'none') { image = true; break; }
      const c = rgba(s.backgroundColor);
      if (c[3]) layers.push(c);
      if (c[3] === 1) break;
    }
    const size = parseFloat(style(el).fontSize), min = size >= 24 ? 3 : 4.5;
    if (image) { add('?', 'Contrast', `${name(el)} sits on an image or a gradient: check ${min}:1`, el); continue; }
    let bg = canvas;
    for (const c of layers.reverse()) bg = over(c, bg);
    const fg = rgba(style(el).color);
    const ink = over([fg[0], fg[1], fg[2], fg[3] * alpha], bg);
    const [hi, lo] = [lum(ink), lum(bg)].sort((x, y) => y - x);
    const r = (hi + 0.05) / (lo + 0.05);
    if (r < min - 0.005) add('✗', 'Contrast', `${name(el)} is ${r.toFixed(2)}:1, below ${min}:1`, el);
  }

  // Top bar links on one line from md.
  if (vw >= 768) {
    for (const nav of document.querySelectorAll('header nav, [role=banner] nav')) {
      const tops = [...nav.querySelectorAll('a')].filter(shown).map(a => Math.round(a.getBoundingClientRect().top));
      if (new Set(tops).size > 1) add('✗', 'Top bar', `the links of ${name(nav)} wrap onto ${new Set(tops).size} lines`, nav);
    }
  }

  // Titles of cards side by side on the same number of lines: siblings with the same tag and class,
  // starting at the same height, each with a heading.
  // Lines of the text itself: the heading's box may be stretched by its grid row (aligned zones).
  const lines = h => {
    const range = document.createRange();
    range.selectNodeContents(h);
    // a smaller span on the same line (a period after a title) overlaps it, so it is not a new line
    const rs = [...range.getClientRects()].filter(r => r.width > 0).sort((a, b) => a.top - b.top);
    let n = 0, bottom = -Infinity;
    for (const r of rs) { if (r.top >= bottom - 1) n++; bottom = Math.max(bottom, r.bottom); }
    return n;
  };
  const kind = el => el.localName + '.' + (typeof el.className === 'string' ? el.className.trim() : '');
  const twin = el => [...el.parentElement.children].some(s => s !== el && kind(s) === kind(el));
  const rows = new Map();  // parent, kind and top of the card → [card, title] of the cards in that row
  for (const h of document.querySelectorAll('h1, h2, h3, h4, h5, h6, [role=heading]')) {
    if (!shown(h)) continue;
    let card = h;
    while (card.parentElement && card.parentElement !== document.body && !twin(card)) card = card.parentElement;
    if (!card.parentElement || card === h || !twin(card)) continue;
    const key = [card.parentElement, kind(card), Math.round(card.getBoundingClientRect().top)];
    const k = rows.get(card.parentElement) || new Map();
    rows.set(card.parentElement, k);
    const id = key.slice(1).join('|');
    if (!k.has(id)) k.set(id, new Map());
    if (!k.get(id).has(card)) k.get(id).set(card, h);
  }
  for (const row of [...rows.values()].flatMap(k => [...k.values()])) {
    if (row.size < 2) continue;
    const titles = [...row.values()].map(h => [h, lines(h)]);
    const counts = new Set(titles.map(t => t[1]));
    if (counts.size < 2) continue;
    const shortest = titles.reduce((a, b) => b[1] < a[1] ? b : a)[0];
    add('✗', 'Cards', `titles of cards side by side on ${[...counts].sort().join(' and ')} lines: ${name(shortest)}`, ...row.keys());
  }
  // Boxes side by side in a grid or flex row end at the same height, and none has empty space under its content.
  const inFlow = el => shown(el) && style(el).position !== 'absolute' && style(el).position !== 'fixed';
  const isBox = el => (style(el).backgroundColor !== 'rgba(0, 0, 0, 0)' || parseFloat(style(el).borderTopWidth) > 0) && parseFloat(style(el).paddingBottom) > 0;  // a card: filled or outlined, with padding
  for (const parent of document.querySelectorAll('body *')) {
    if (!/grid|flex/.test(style(parent).display)) continue;
    const byTop = new Map();
    for (const el of [...parent.children].filter(inFlow)) {
      const top = Math.round(el.getBoundingClientRect().top);
      byTop.set(top, [...(byTop.get(top) || []), el]);
    }
    for (const row of byTop.values()) {
      if (row.length < 2 || !row.every(isBox)) continue;
      const bottoms = row.map(el => el.getBoundingClientRect().bottom);
      if (Math.max(...bottoms) - Math.min(...bottoms) > 1) add('✗', 'Cards', `boxes side by side end at different heights: ${name(row[0])}`, ...row);
      for (const el of row) {
        const kids = [...el.children].filter(inFlow);
        if (!kids.length) continue;
        const s = style(el);
        const end = el.getBoundingClientRect().bottom - parseFloat(s.paddingBottom) - parseFloat(s.borderBottomWidth);
        const content = Math.max(...kids.map(k => k.getBoundingClientRect().bottom + parseFloat(style(k).marginBottom)));
        const start = el.getBoundingClientRect().top + parseFloat(s.paddingTop) + parseFloat(s.borderTopWidth);
        const above = Math.min(...kids.map(k => k.getBoundingClientRect().top - parseFloat(style(k).marginTop))) - start;
        // centred content leaves the same space above and below: only space under it beyond that is empty
        if (end - content - Math.max(above, 0) > 1) add('✗', 'Cards', `${Math.round(end - content)}px empty under the content of a box beside others: ${name(el)}`, el);
      }
    }
  }
  // From role to style: each text row of the Decisions file against the element that carries it.
  // Not at 200%: the sizes double there and each finding would come twice.
  const probed = (prop, value) => {
    const p = document.createElement('div');
    p.style.cssText = `position:absolute;${prop}:${value}`;
    document.body.append(p);
    const got = style(p)[{color: 'color', width: 'width'}[prop] || 'fontSize'];
    p.remove();
    return got;
  };
  const months = new Set([...['long', 'short']].flatMap(month => Array.from({length: 12}, (_, m) =>
    new Intl.DateTimeFormat(document.documentElement.lang || undefined, {month}).format(new Date(2000, m, 1)).replace(/\.$/, '').toLowerCase())));
  const currencies = new Set(Intl.supportedValuesOf('currency'));
  const format = v => /[$€£¥]\s*\d|\d\s*[$€£¥]/.test(v) || (/\d/.test(v) && v.split(/[\s\d.,]+/).some(w => currencies.has(w))) ? 'price'
    : /^\d{4}-\d{2}-\d{2}/.test(v) || /^\d{1,2}[\/.]\d{1,2}[\/.]\d{2,4}$/.test(v) || (/\d/.test(v) && v.toLowerCase().split(/[\s,]+/).some(w => months.has(w.replace(/\.$/, '')))) ? 'date'
    : /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? 'email' : '';
  for (const [table, rows] of zoom ? [] : tables) {
    for (const root of document.querySelectorAll(`[data-kore="${table}"]`)) {
      const first = element => [...root.querySelectorAll(`[data-kore-element="${element}"]`)].filter(el => el.closest('[data-kore]') === root);
      const texts = rows.filter(r => r[1] && r[9]).flatMap(r => first(r[0]).map(el => [r, el, el.getBoundingClientRect()]));
      const point = texts.find(t => t[0][6]);
      for (const [row, el, b] of point ? texts : []) {
        const f = point[2];
        if (!row[6] && (b.top < f.top - 1 || (b.top <= f.top + 1 && b.left < f.left - 1)))
          add('✗', 'The One Winner Rule', `${name(el)} comes before the focal point ${name(point[1])}`, el);
      }
      for (const [element, role, weight, color, space, target, , inline, label] of rows) {
        const found = first(element);
        if (!found.length) add('✗', 'Decisions file', `no data-kore-element="${element}" in ${name(root)}`, root);
        for (const el of role ? found : []) {
          const s = style(el);
          if (s.fontSize !== probed('font-size', `var(--${role}-fontSize)`) || s.fontWeight !== weight || s.color !== probed('color', `var(--${color})`))
            add('✗', 'From role to style', `${name(el)} is ${s.fontSize} ${s.fontWeight} ${s.color}, its row says ${role} ${weight} ${color}`, el);
        }
        // Figure and unit: after a figure that opens the text, the words are smaller than it and in mute.
        for (const el of inline ? [] : found) {
          const nodes = [];
          for (const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); w.nextNode();) if (w.currentNode.data.trim()) nodes.push(w.currentNode);
          const raw = nodes.map(n => n.data).join(''), text = raw.trim();
          const figure = (text.match(/^[−+-]?\d(?:[\d.,:\/-]*\d)?/) || [''])[0];
          const rest = text.slice(figure.length).trim();
          // a list number ("3. Choose"), a time after a date and a date with its month carry no unit
          if (!figure || !/^\p{L}/u.test(rest) || rest.toLowerCase().split(/\s+/).some(w => months.has(w.replace(/\.$/, '')))) continue;
          const size = style(nodes[0].parentElement).fontSize;
          // the figure may span several text nodes; the words start at the first node after it
          let left = raw.length - raw.trimStart().length + figure.length, shared;
          const after = [];
          for (const n of nodes) {
            if (left <= 0) after.push(n);
            else if (n.data.slice(left).trim()) shared = n;  // figure and words in one text node share one style
            left -= n.data.length;
          }
          const bad = shared ? style(shared.parentElement) : after.map(n => style(n.parentElement)).find(s => !(parseFloat(s.fontSize) < parseFloat(size) && s.color === probed('color', 'var(--mute)')));
          if (bad) add('✗', 'Text hierarchy', `${name(el)}: the words after the figure ${figure} are ${bad.fontSize} ${bad.color}; they are smaller than the figure and in mute`, el);
        }
        // Value labels are a last resort: a value whose format says what it is stands alone when it is the only one of that format in its root.
        const value = label && found.length && first(target || '')[0]?.innerText.trim(), kind = value && format(value);
        if (kind && [...root.querySelectorAll('[data-kore-element]')].filter(el => el.closest('[data-kore]') === root && !el.querySelector('[data-kore-element]') && format(el.innerText.trim()) === kind).length < 2)
          add('✗', 'Text hierarchy', `${name(found[0])} names the value ${value}, the only ${kind} of ${name(root)}: the value stands alone`, found[0]);
        // Space: the gap to the target's box, vertical when one box ends above the other starts, else horizontal.
        const other = first(target || '')[0];
        if (!space || !found.length || !other) continue;
        const a = found[0].getBoundingClientRect(), b = other.getBoundingClientRect();
        const gap = Math.max(b.top - a.bottom, a.top - b.bottom) >= 0 ? Math.max(b.top - a.bottom, a.top - b.bottom) : Math.max(b.left - a.right, a.left - b.right);
        const want = parseFloat(probed('width', `var(--${space})`));
        if (Math.abs(gap - want) > 1) add('✗', 'The Distance Ratio Rule', `${name(found[0])} is ${Math.round(gap)}px from ${target}, its row says ${space} (${want}px)`, found[0]);
      }
    }
  }
  // Copy 3: each element of a section or component holds its own text.
  for (const root of zoom ? [] : document.querySelectorAll('[data-kore]')) {
    const seen = new Map();
    for (const el of root.querySelectorAll('[data-kore-element]')) {
      if (el.querySelector('[data-kore-element]')) continue;  // a wrapper's text is its inner element's
      const text = el.closest('[data-kore]') === root ? el.innerText.trim().replace(/\s+/g, ' ').toLowerCase() : '';
      if (!text) continue;
      if (seen.has(text)) add('✗', 'Copy', `${name(el)} repeats the text of ${name(seen.get(text))}: each element holds its own text`, el);
      else seen.set(text, el);
    }
  }
  return out;
}
"""

# Runs in the page before and after the root font size doubles: the font
# size of each element that holds text, in page order.
FONT_SIZES = r"""
() => [...document.body.querySelectorAll('*')]
  .filter(el => [...el.childNodes].some(n => n.nodeType === 3 && n.data.trim()) && !el.closest('script, style, svg'))
  .map(el => [el.localName + (el.id ? '#' + el.id : ''), parseFloat(getComputedStyle(el).fontSize)])
"""


def launch(playwright):
    """A Chromium-based browser already on the computer, or None."""
    path = os.environ.get("KORE_BROWSER")
    tries = [{"executable_path": path}] if path else [{"channel": "chrome"}, {"channel": "msedge"}]
    for options in tries:
        try:
            return playwright.chromium.launch(**options)
        except Exception:
            continue
    return None


# Sets a theme selector (".dark", '[data-theme="dark"]') on <html>.
SET_THEME = r"""
selector => {
  const html = document.documentElement;
  for (const [, name] of selector.matchAll(/\.([\w-]+)/g)) html.classList.add(name);
  for (const [, name, value] of selector.matchAll(/\[([\w-]+)(?:\s*=\s*["']?([^"'\]]*)["']?)?\]/g))
    html.setAttribute(name, value ?? '');
}
"""


# A page address with #id measures only that element: every element outside it
# and its ancestors is hidden; styles, scripts and the icon sprite stay.
ONLY = r"""
id => {
  const el = document.getElementById(id);
  if (!el) return false;
  for (let n = el; n.parentElement && n !== document.body; n = n.parentElement)
    for (const s of n.parentElement.children)
      if (s !== n && !/^(SCRIPT|STYLE|LINK|TEMPLATE)$/.test(s.tagName) && !s.querySelector('symbol'))
        s.style.setProperty('display', 'none', 'important');
  return true;
}
"""


# Scrolls to the end and back, so content that appears on scroll and lazy
# images are drawn before the whole page is captured.
SCROLL_THROUGH = r"""
async () => {
  const wait = ms => new Promise(r => setTimeout(r, ms));
  for (let y = 0; y < document.documentElement.scrollHeight; y += innerHeight) { scrollTo(0, y); await wait(50); }
  scrollTo(0, 0);
  await wait(100);
}
"""


def shot_names(urls):
    """One name per page: the last part of its address without the extension,
    or index; a name already taken gets -2, -3."""
    names, taken = [], set()
    for url in urls:
        base = os.path.splitext(urlparse(url).path.rstrip("/").rsplit("/", 1)[-1])[0] or "index"
        name, n = base, 1
        while name in taken:
            n += 1
            name = f"{base}-{n}"
        taken.add(name)
        names.append(name)
    return names


def forcer(page):
    """force(selector, pseudo-class or None): forces hover, focus-visible or active on the first element the selector
    finds, or clears it. One CDP session for the page: a state another session forced would stay on."""
    cdp = page.context.new_cdp_session(page)
    cdp.send("DOM.enable")
    cdp.send("CSS.enable")
    doc = cdp.send("DOM.getDocument")["root"]["nodeId"]

    def force(selector, state):
        node = cdp.send("DOM.querySelector", {"nodeId": doc, "selector": selector})["nodeId"]
        if node:  # no match: the caller's measure reports it
            cdp.send("CSS.forcePseudoState", {"nodeId": node, "forcedPseudoClasses": [state] if state else []})
    return force


def load(browser, url, theme, selector, width, touch, motion="reduce", state=None):
    """A new context and page; state, a (CSS selector, pseudo-class) pair, forces that state on the selector's first
    match and ends the transitions it starts."""
    context = browser.new_context(viewport={"width": width, "height": HEIGHT}, color_scheme=theme,
                                  has_touch=touch, reduced_motion=motion)
    page = context.new_page()
    from playwright.sync_api import TimeoutError as PageTimeout
    try:
        page.goto(url, wait_until="networkidle")
    except PageTimeout:
        pass  # a page that polls its server never goes idle: it is measured as it has loaded
    if selector:
        page.evaluate(SET_THEME, selector)
    fragment = urlparse(url).fragment
    if fragment and not page.evaluate(ONLY, fragment):
        raise SystemExit(f"kore_check --url: no element with id={fragment} in {url}")
    page.evaluate("document.fonts.ready.then(() => 0)")
    if state:
        forcer(page)(*state)
        page.evaluate("document.getAnimations().forEach(a => a.effect?.getComputedTiming().iterations !== Infinity && a.finish())")
    return context, page


def check(urls, report, themes, shots=None, tables=()):
    """Reports the findings of every page, in each theme of themes ({"light" |
    "dark": selector to set on <html>, or None}), through report(kind, path,
    line, rule, message), tables being type_rows of KORE-DECISIONS.md, and saves the screenshots in the folder shots.
    Returns the screenshot paths, or None when the browser cannot run."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(f"kore_check --url needs Playwright: {INSTALL}.")
        return None
    with sync_playwright() as playwright:
        browser = launch(playwright)
        if browser is None:
            print(f"kore_check --url found no Chromium-based browser: {INSTALL}.")
            return None
        saved, marked = [], set()  # marked: tables whose data-kore root is on a page
        if shots:
            shots.mkdir(parents=True, exist_ok=True)
        for url, name in zip(urls, shot_names(urls)):
            seen = defaultdict(list)  # (kind, rule, message) → where it happens
            for theme, selector in themes.items():
                for width in WIDTHS:
                    touch = width < TOUCH_BELOW
                    context, page = load(browser, url, theme, selector, width, touch)
                    marked |= set(page.evaluate("names => names.filter(n => document.querySelector(`[data-kore=\"${n}\"]`))",
                                                [table for table, _ in tables]))
                    for kind, rule, message in page.evaluate(MEASURE, {"touch": touch, "zoom": False, "tables": tables}):
                        seen[(kind, rule, message)].append((width, theme))
                    if shots and width in SHOTS:
                        page.evaluate(SCROLL_THROUGH)
                        path = shots / f"{name}-{width}-{theme}.png"
                        page.screenshot(path=str(path), full_page=True)
                        saved.append(path)
                    context.close()
                context, page = load(browser, url, theme, selector, ZOOM_WIDTH, False)
                before = page.evaluate(FONT_SIZES)
                page.add_style_tag(content="html { font-size: 200% !important; }")
                after = page.evaluate(FONT_SIZES)
                fixed = sorted({tag for (tag, a), (_, b) in zip(before, after) if b < a * 1.5})
                if fixed:
                    seen[("✗", "Zoom", f"font size in px, does not follow the user's text size: {', '.join(fixed[:5])}")]\
                        .append(("200%", theme))
                for kind, rule, message in page.evaluate(MEASURE, {"touch": False, "zoom": True, "tables": tables}):
                    seen[(kind, rule, message)].append(("200%", theme))
                context.close()
            for (kind, rule, message), places in seen.items():
                report(kind, url, 0, rule, f"{message} ({where(places)})")
        for table, _ in tables:
            if table not in marked:
                report("✗", "KORE-DECISIONS.md", 0, "Decisions file", f'no element with data-kore="{table}" on the pages '
                       "checked: mark the root of the section or component (On the page)")
        browser.close()
    return saved


def where(places):
    """'320, 375 light and dark' or '320 light; 768 dark'."""
    by_theme = defaultdict(list)
    for width, theme in places:
        if str(width) not in by_theme[theme]:  # two copies of one element on a page
            by_theme[theme].append(str(width))
    widths = list(by_theme.values())
    if len(widths) == 2 and widths[0] == widths[1]:
        return f"{', '.join(widths[0])}, light and dark"
    return "; ".join(f"{', '.join(w)}, {theme}" for theme, w in by_theme.items())
