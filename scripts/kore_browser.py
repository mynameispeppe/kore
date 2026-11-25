"""Kore check, phase 2: measures rendered pages in a browser, for the rules
that only the result shows (references/checks.md, Measure).

Needs Playwright for Python and a Chromium browser already installed
(Google Chrome, then Microsoft Edge, or the executable in KORE_BROWSER);
no browser is downloaded. kore_check imports this module only for --url.

Every page is opened in each theme the token file defines at each width of
WIDTHS, then at 1280px with the root font size at 200% (Zoom). At each width,
after the screenshot, focus is forced on the Skip link and on links with the
look of a button to measure their focus. Touch is
emulated below 1024px. With a shots folder, the whole page is also saved as
a PNG at each width of SHOTS, in each theme, from the same visit.
"""
import os
import kore_images
import kore_responsive
import kore_spacing
import kore_usability
from collections import defaultdict
from urllib.parse import urlparse

WIDTHS = (320, 375, 639, 768, 1023, 1024, 1440, 2560)  # 639 and 1023: just below sm and lg
TOUCH_BELOW = 1024
ZOOM_WIDTH = 1280
SHOTS = (375, 1440)  # phone and desktop (references/checks.md, Bounded verification)
HEIGHT = 800
SETTLE = 100  # ms a page gets to react to a key or a click
INSTALL = ("python3 -m pip install --user playwright, then install Google Chrome "
           "or set KORE_BROWSER to a Chromium-based browser")

# Opens both page scripts: out, add, doc, vw, style, shown, name, resolve.
HELPERS = r"""
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
  // A token as the browser computes it, through one hidden tint made on first use; '' when the element has no such token.
  let tint;
  const resolve = (el, token, prop) => {
    const v = style(el).getPropertyValue(token).trim();
    if (!v) return '';
    if (!tint) { tint = document.body.appendChild(document.createElement('span')); tint.style.display = 'none'; }
    tint.style[prop] = '';
    tint.style[prop] = v;
    return getComputedStyle(tint)[prop];
  };
"""

# Runs in the page. Returns [kind, rule, message] for each finding. whole: the page is measured whole, not one #id.
MEASURE = r"""
async ({touch, zoom, tables, mode, whole}) => {""" + HELPERS + r"""
  const where = zoom ? 'Zoom' : 'Extremes';
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
  // One h1 per page; a URL with #id shows one component, not a page.
  const h1s = [...document.querySelectorAll('h1')].filter(el => el.checkVisibility());
  if (!location.hash && h1s.length !== 1)
    add('✗', 'Typographic levels', h1s.length ? `the page has ${h1s.length} h1: ${h1s.map(name).join(', ')}` : 'the page has no h1', ...h1s);
  for (const hero of location.hash ? [] : document.querySelectorAll('[data-kore="Hero"]'))
    if (!h1s.some(h => hero.contains(h))) add('✗', 'Typographic levels', `${name(hero)} holds no h1: the hero's title is the page's h1`, hero);
  // Heading levels follow each other; role=heading without aria-level is level 2 (ARIA).
  const heads = [...document.querySelectorAll('h1, h2, h3, h4, h5, h6, [role=heading]')].filter(el => el.checkVisibility());
  const level = el => +(el.getAttribute('aria-level') || el.localName.slice(1)) || 2;
  let prev = location.hash && heads.length ? level(heads[0]) - 1 : 0;
  for (const el of heads) {
    if (level(el) > prev + 1) add('✗', 'Typographic levels', `${name(el)} is an h${level(el)} after an h${prev}: heading levels follow each other`, el);
    prev = level(el);
  }

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
    let t = textBox(nodes);
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
        // Text trimmed with an ellipsis shows only inside the box that trims it.
        if (out) t = axis === 'x' ? {...t, l: Math.max(t.l, lo), r: Math.min(t.r, hi)} : {...t, t: Math.max(t.t, lo), b: Math.min(t.b, hi)};
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
      if (Math.min(p.r, q.r) - Math.max(p.l, q.l) > 2 && Math.min(p.b, q.b) - Math.max(p.t, q.t) > 2 && pinned(a) === pinned(b)) {
        add('✗', where, `text over text: ${name(a)} and ${name(b)}`, a, b);
        reported.add(a); reported.add(b);
      }
    }
  }
  if (zoom) return out;

  const isButton = el => el.matches('button, [role=button], input[type=button], input[type=submit], input[type=reset]');
  const sides = ['Top', 'Right', 'Bottom', 'Left'];
  const everyShown = [...document.body.querySelectorAll('*')].filter(el => el !== tint && shown(el));
  // Meaning: no button in accent, a background in accent only in the Hero's visual, text in accent from display-sm, at most 4 per page.
  const counted = new Map();  // key (element, or its Hero) -> first element
  for (const el of everyShown) {
    const accent = resolve(el, '--accent', 'color');
    if (!accent) continue;
    const s = style(el);
    const bg = s.backgroundColor === accent || s.backgroundImage.includes(accent);
    const inAccent = bg || [s.color, s.fill, s.stroke].includes(accent) ||
      sides.some(d => parseFloat(s[`border${d}Width`]) > 0 && s[`border${d}Color`] === accent);
    if (!inAccent) continue;
    const hero = el.closest('[data-kore="Hero"]');
    const key = hero && bg ? hero : el;
    if (!counted.has(key)) counted.set(key, el);
    if (isButton(el)) { add('✗', 'Meaning', `${name(el)} is in accent: buttons take primary`, el); continue; }
    if (bg && !hero) add('✗', 'Meaning', `${name(el)} has a background in accent outside the Hero's visual`, el);
    const limit = resolve(el, '--display-sm-fontSize', 'fontSize');
    if (s.color === accent && texts.has(el) && limit && parseFloat(s.fontSize) < parseFloat(limit))
      add('✗', 'Meaning', `${name(el)} is ${parseFloat(s.fontSize)}px text in accent, below display-sm`, el);
  }
  if (!location.hash && counted.size > 4) {
    const els = [...counted.values()];
    add('✗', 'Meaning', `${els.length} elements in accent on the page, at most 4: ${els.map(name).join(', ')}`, ...els);
  }

  // The One Primary Rule: one primary button per decision (form, dialog or component).
  const decisions = new Map();
  for (const el of everyShown) {
    const primary = isButton(el) && resolve(el, '--primary', 'color');
    if (!primary || style(el).backgroundColor !== primary) continue;
    const g = el.closest('form, dialog, [role=dialog], [data-kore]');
    decisions.set(g, [...(decisions.get(g) || []), el]);
  }
  for (const group of decisions.values())
    if (group.length > 1) add('✗', 'The One Primary Rule', `${group.length} primary buttons in one decision: ${group.map(name).join(', ')}`, ...group);

  // Cards (cards.md): a shown element with the surface-card background and the rounded-xl radius.
  // A Panel (GLOSSARY) looks the same but holds one component other than Cards, which keeps its own rules.
  const panel = el => el.children.length === 1 && el.children[0].matches('[data-kore]:not([data-kore="Cards"])');
  const cards = new Set(everyShown.filter(el => {
    if (panel(el)) return false;
    const bg = resolve(el, '--surface-card', 'backgroundColor'), radius = resolve(el, '--rounded-xl', 'borderTopLeftRadius');
    return bg && radius && style(el).backgroundColor === bg && Math.abs(parseFloat(style(el).borderTopLeftRadius) - parseFloat(radius)) <= 1;
  }));
  const upCard = el => { for (let p = el.parentElement; p; p = p.parentElement) if (cards.has(p)) return p; };
  const owned = new Map();  // card -> the elements whose nearest card is it
  for (const el of everyShown) { const c = upCard(el); if (c) owned.set(c, [...(owned.get(c) || []), el]); }
  const px = (el, token) => parseFloat(resolve(el, token, 'width'));
  const rect = el => el.getBoundingClientRect();
  const byTop = (a, b) => rect(a).top - rect(b).top;
  const clickable = 'a[href], button, label, [role=button], [role=link]';
  // A rounded block: background, radius and marked text; inside a card it is a row, never an action.
  const block = el => {
    const s = style(el);
    if (el.hasAttribute('data-kore') || s.backgroundColor === 'rgba(0, 0, 0, 0)' || !(parseFloat(s.borderTopLeftRadius) > 0)) return false;
    return [el, ...el.querySelectorAll('[data-kore-element]')].some(n => n.matches('[data-kore-element]') && n.innerText.trim());
  };
  for (const c of cards) if (upCard(c)) add('✗', 'Cards', `card inside a card: ${name(c)}`, c);
  for (const [c, els] of owned) {
    // A rounded block with a background is for a clickable row: a unit of its own.
    for (const el of els)
      if (block(el) && !el.matches(clickable) && !el.querySelector(clickable))
        add('✗', 'Cards', `rounded block with a background inside a card is not clickable: ${name(el)}`, el);
    const title = els.find(el => el.matches('h1, h2, h3, h4, h5, h6, [role=heading]'));
    if (!title) continue;
    const header = title.parentElement === c ? title : title.parentElement, hb = rect(header);
    const actions = els.filter(el => (isButton(el) || (el.matches('a[href]') && !el.closest('p'))) && !block(el) && rect(el).top >= hb.bottom - 1).sort(byTop);
    const first = actions[0];
    const room = c.clientWidth - parseFloat(style(c).paddingLeft) - parseFloat(style(c).paddingRight) - 2 * px(c, '--space-2');
    for (const m of els.filter(el => el.matches('img, video, picture, canvas') && rect(el).width >= room && rect(el).top >= rect(title).bottom - 1))
      add('✗', 'Cards', `media under the title of a card: ${name(m)}`, m);
    const items = els.filter(el => texts.has(el) && !header.contains(el) && !actions.some(a => a.contains(el)) && rect(el).top >= hb.bottom - 1).sort(byTop);
    const late = first ? items.filter(el => rect(el).top >= rect(first).top + 1) : [];
    for (const el of late) add('✗', 'Cards', `text under the actions of a card: ${name(el)}`, el);
    // Body rows: an item starts a new row when it begins at or below the bottom of the items before it.
    const bands = [];
    for (const el of items.filter(el => !late.includes(el))) {
      const q = rect(el), band = bands[bands.length - 1];
      if (!band || q.top >= band.bottom - 1) bands.push({first: el, low: el, top: q.top, bottom: q.bottom});
      else if (q.bottom > band.bottom) { band.bottom = q.bottom; band.low = el; }
    }
    // The gap between two boxes against the tokens the rule gives.
    const space = (above, below, gap, ...tokens) => {
      const want = tokens.map(t => px(c, `--${t}`));
      if (want.some(w => !(w >= 0)) || want.some(w => Math.abs(gap - w) <= 1)) return;
      add('✗', 'Cards', `${Math.round(gap)}px between ${name(above)} and ${name(below)} in a card, the rule gives ${tokens.map((t, i) => `${t} (${want[i]}px)`).join(' or ')}`, below);
    };
    if (header !== title) {
      const sibs = [...header.children].filter(shown), next = sibs[sibs.indexOf(title) + 1];
      if (next) space(title, next, rect(next).top - rect(title).bottom, 'space-1');
    }
    const start = [bands[0] && bands[0].first, first].filter(Boolean).sort(byTop)[0];
    if (start) space(header, start, rect(start).top - hb.bottom, start === first ? 'space-8' : 'space-6');
    bands.forEach((b, i) => { if (i) space(bands[i - 1].low, b.first, b.top - bands[i - 1].bottom, 'space-3', 'space-6'); });
    if (bands.length && first) space(bands[bands.length - 1].low, first, rect(first).top - bands[bands.length - 1].bottom, 'space-8');
  }

  // Actions: order and end edge (hierarchy.md Scanning patterns), the destructive one apart (spacing.md Grouping actions), labels (button.md Button).
  const acts = everyShown.filter(el => (isButton(el) || (el.matches('a[href]') && !el.closest('p'))) && !(block(el) && upCard(el)));
  const filled = el => [resolve(el, '--primary', 'color'), resolve(el, '--danger', 'color')].includes(style(el).backgroundColor);
  const compOf = el => { for (let p = el.parentElement; p; p = p.parentElement) if (cards.has(p) || p.matches('form, dialog, [role=dialog]')) return p; };
  const groups = new Map();  // parent -> its actions, when inside a component
  for (const el of acts) if (compOf(el)) groups.set(el.parentElement, [...(groups.get(el.parentElement) || []), el]);
  for (const [parent, group] of groups) {
    const fills = group.filter(filled);
    if (group.length < 2 || !fills.length) continue;
    const rtl = style(parent).direction === 'rtl', end = el => rtl ? -rect(el).left : rect(el).right;
    const f = fills[fills.length - 1], comp = compOf(f);
    if (group.some(o => o !== f && (rect(o).top > rect(f).top + 1 || (Math.abs(rect(o).top - rect(f).top) <= 1 && end(o) > end(f) + 1))))
      add('✗', 'Scanning patterns', `${name(f)} is not the last action of its group: the confirming action ends the row`, f);
    const last = [...group].sort((a, b) => rect(a).top - rect(b).top || end(a) - end(b)).pop();
    const q = rect(comp), s = style(comp);
    const edge = rtl ? -(q.left + parseFloat(s.borderLeftWidth) + parseFloat(s.paddingLeft)) : q.right - parseFloat(s.borderRightWidth) - parseFloat(s.paddingRight);
    if (end(last) < edge - 1) add('✗', 'Scanning patterns', `the actions of ${name(comp)} end before its right edge`, last);
  }
  const decided = new Map();  // decision -> its actions
  for (const el of acts) { const g = el.closest('form, dialog, [role=dialog], [data-kore]'); decided.set(g, [...(decided.get(g) || []), el]); }
  for (const group of decided.values()) {
    if (!group.some(el => style(el).backgroundColor === resolve(el, '--primary', 'color'))) continue;
    for (const d of group.filter(el => style(el).backgroundColor === resolve(el, '--danger', 'color'))) {
      const want = px(d, '--space-4'), a = rect(d);
      const gaps = group.filter(o => o !== d).map(o => { const b = rect(o); return [Math.max(0, a.left - b.right, b.left - a.right, a.top - b.bottom, b.top - a.bottom), o]; });
      if (!(want >= 0) || !gaps.length) continue;
      const [gap, other] = gaps.reduce((m, x) => x[0] < m[0] ? x : m);
      if (gap < want - 1) add('✗', 'Grouping actions', `${name(d)} is ${Math.round(gap)}px from ${name(other)}: a destructive action that is not the main one sits space-4 (${want}px) or more from the others`, d);
    }
  }
  const english = doc.lang.trim().toLowerCase().startsWith('en');
  for (const el of acts) {
    if (el.closest('[data-kore-user]')) continue;
    const label = el.innerText.trim().replace(/\s+/g, ' ');
    if (english && ['ok', 'yes', 'no', 'submit'].includes(label.toLowerCase())) add('✗', 'Button', `${name(el)}: name the action with a verb and an object`, el);
    if (label.split(' ').filter(w => /^\p{Lu}{2,}$/u.test(w)).length >= 2) add('✗', 'Button', `${name(el)}: the label is written in capitals`, el);
  }

  // Page language: a date, a price or a measure needs the country in lang; month names and numeric dates follow its locale.
  const lang = doc.lang.trim(), locale = lang || undefined;
  const monthNames = (locales, styles) => locales.flatMap(l => styles.flatMap(month => Array.from({length: 12}, (_, m) =>
    new Intl.DateTimeFormat(l, {month}).format(new Date(2000, m, 1)).replace(/\.$/, '').toLowerCase())));
  const ownMonths = new Set(monthNames([locale], ['long', 'short']));
  const otherMonths = new Set(monthNames(['en', 'it', 'fr', 'de', 'es', 'pt', 'nl'], ['long']).filter(w => !ownMonths.has(w)));
  const dayFirst = new Intl.DateTimeFormat(locale).formatToParts(new Date(2000, 11, 31)).find(p => p.type === 'day' || p.type === 'month').type === 'day';
  const codes = new Set(Intl.supportedValuesOf('currency'));
  const numericDate = /(?<![\d\/.])(\d{1,2})[\/.](\d{1,2})[\/.]\d{4}(?![\d\/.])/g;
  const monthNear = (t, set) => { const w = t.toLowerCase().split(/[\s,]+/).map(x => x.replace(/\.$/, '')); return w.find((x, i) => set.has(x) && [w[i - 1], w[i + 1]].some(n => /^\d{1,4}$/.test(n || ''))); };
  const dated = t => numericDate.test(t) || !!monthNear(t, ownMonths) || !!monthNear(t, otherMonths) || /[$€£¥]\s*\d|\d\s*[$€£¥]/.test(t) ||
    (/\d/.test(t) && t.split(/[\s\d.,]+/).some(w => codes.has(w))) || /\d\s?(km|cm|mm|kg|mg|ml|mi|lb|lbs|oz|ft|m²|m³|°C|°F|mph)(?!\p{L})/u.test(t);
  const words = el => el.textContent.replace(/\s+/g, ' ').trim();
  const showsDate = el => { numericDate.lastIndex = 0; return dated(words(el)); };
  const dates = everyShown.filter(el => showsDate(el) && ![...el.children].some(showsDate));  // the innermost elements that show one
  if (lang && dates.length && !/-([a-z]{2}|\d{3})(-|$)/i.test(lang))
    add('✗', 'Page language', `${name(dates[0])} shows a date, a price or a measure: lang "${lang}" names no country`, dates[0]);
  for (const el of dates) {
    for (const [d, a, b] of words(el).matchAll(numericDate))
      if (+(dayFirst ? b : a) > 12) add('✗', 'Page language', `${name(el)}: ${d} is not a date in the format of lang "${lang}"`, el);
    const month = monthNear(words(el), otherMonths);
    if (month) add('✗', 'Page language', `${name(el)}: "${month}" is not a month name of lang "${lang}"`, el);
  }

  // Links in running text (browser-surfaces.md): link color, a 1px underline at a 4px offset.
  for (const a of everyShown.filter(el => el.matches('p a[href]'))) {
    const s = style(a), want = resolve(a, '--link', 'color');
    if ((want && s.color !== want) || !s.textDecorationLine.includes('underline') || s.textDecorationThickness !== '1px' || s.textUnderlineOffset !== '4px')
      add('✗', 'Browser surfaces', `${name(a)} is a link in running text: link color, a 1px underline at a 4px offset`, a);
  }

  // Measure (typography.md): each line of a paragraph holds at most 75 characters.
  for (const p of everyShown.filter(el => el.localName === 'p')) {
    let n = 0, most = 0, bottom = -Infinity;
    const range = document.createRange();
    for (const w = document.createTreeWalker(p, NodeFilter.SHOW_TEXT); w.nextNode();) {
      for (let i = 0; i < w.currentNode.data.length; i++) {
        range.setStart(w.currentNode, i); range.setEnd(w.currentNode, i + 1);
        const q = range.getBoundingClientRect();
        if (!q.width) continue;  // collapsed white space
        if (q.top >= bottom - 1) { n = 0; bottom = q.bottom; } else bottom = Math.max(bottom, q.bottom);
        most = Math.max(most, ++n);
      }
    }
    if (most > 75) add('✗', 'Typography rules', `${name(p)} has lines longer than 75 characters`, p);
  }

  // Radius by role: an image outside a card, narrower than the page, has radius xl, on itself or on a box of its size that clips it.
  // Round images (Avatar), SVG files and images in a header, a footer or the Logo wall follow their own component.
  for (const img of everyShown.filter(el => el.localName === 'img' && !upCard(el) && !el.closest('header, footer, [data-kore="Logo wall"]'))) {
    const q = rect(img), want = parseFloat(resolve(img, '--rounded-xl', 'borderTopLeftRadius'));
    if (q.width >= vw - 1 || !(want >= 0) || /\.svg([?#]|$)|^data:image\/svg/i.test(img.currentSrc || img.src)) continue;
    let ok = false;
    for (let a = img; a && !ok; a = a.parentElement) {
      const b = rect(a), r = style(a).borderTopLeftRadius;
      if (a !== img && (Math.abs(b.width - q.width) > 1 || Math.abs(b.height - q.height) > 1 || style(a).overflow === 'visible')) break;
      ok = r.endsWith('%') ? parseFloat(r) >= 50 : parseFloat(r) >= Math.min(b.width, b.height) / 2 - 1 || Math.abs(parseFloat(r) - want) <= 1;
    }
    if (!ok) add('✗', 'Radius by role', `${name(img)} is an image outside a card without radius xl`, img);
  }

""" + kore_responsive.BREAKPOINTS + r"""

  // Hero: the smallest box holding the h1 and the calls to action holds only the h1, one subtitle, the calls to action and a form.
  const calls = 'button, a[href], [role=button], form';
  for (const hero of document.querySelectorAll('[data-kore="Hero"]')) {
    const h1 = hero.querySelector('h1');
    if (!h1 || !shown(h1)) continue;
    let box = h1.parentElement;
    while (box !== hero && !box.querySelector(calls)) box = box.parentElement;
    const extra = [...texts.keys()].filter(el => box.contains(el) && shown(el) && !h1.contains(el) && !el.closest(calls));
    let sub = extra.find(el => h1.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING);
    while (sub && sub.parentElement !== box && !sub.parentElement.contains(h1) && !sub.parentElement.querySelector(calls)) sub = sub.parentElement;
    for (const el of extra.filter(el => !(sub && sub.contains(el))))
      add('✗', 'Hero', `${name(el)} is in the hero: it holds only the title, the subtitle and the calls to action`, el);
  }

  // Sections, with the Mode of PRODUCT.md: space between sections (spacing.md), four items and quotes of 25 words in Site mode (site.md).
  const sections = everyShown.filter(el => el.localName === 'section');
  const apart = mode === 'site' ? ['space-32', 'space-48'] : mode === 'app' ? ['space-12'] : [];
  for (const s of apart.length ? sections : []) {
    const next = s.nextElementSibling, want = apart.map(t => px(s, `--${t}`));
    if (!next || !sections.includes(next) || want.some(w => !(w >= 0))) continue;
    if (!want.some(w => Math.abs(rect(next).top - rect(s).bottom - w) <= 1))
      add('✗', 'Proximity and hierarchy', `${name(next)} is not ${apart.join(' or ')} from the section above it`, next);
  }
  for (const s of mode === 'site' ? sections : []) {
    // A section opens with its heading: the first shown text sits in an h1 or h2 of the section, with a box over 1px.
    const outer = !s.parentElement.closest('section'), first = outer && [...texts.keys()].find(el => s.contains(el) && shown(el));
    const head = first && first.closest('h1, h2'), box = head && head.getBoundingClientRect();
    if (outer && !(head && s.contains(head) && box.width > 1 && box.height > 1))
      add('✗', 'Sections', `${name(s)} ${first ? 'opens with ' + name(first) : 'has no visible text'}: a section opens with its heading, a visible h1 or h2`, s);
    if (s.matches('[data-kore="Logo wall"], [data-kore="Blog"]') || s.querySelector('[data-kore="Logo wall"], [data-kore="Blog"]')) continue;
    const copies = new Map();  // parent and kind -> how many items: copies with a heading or a quote
    for (const el of everyShown) {
      if (el === s || el.closest('section') !== s || !(el.matches('blockquote') || el.querySelector('h1, h2, h3, h4, h5, h6, [role=heading], blockquote'))) continue;
      const k = el.parentElement, kinds = copies.get(k) || new Map(), what = el.localName + '.' + (typeof el.className === 'string' ? el.className.trim() : '');
      copies.set(k, kinds.set(what, (kinds.get(what) || 0) + 1));
    }
    const most = Math.max(0, ...[...copies.values()].flatMap(k => [...k.values()]));
    if (most > 4) add('✗', 'Sections', `${name(s)} holds ${most} items: at most four per section`, s);
  }
  for (const q of mode === 'site' ? everyShown.filter(el => el.localName === 'blockquote') : []) {
    const n = q.innerText.trim().split(/\s+/).filter(Boolean).length;
    if (n > 25) add('✗', 'Sections', `${name(q)} holds ${n} words: a quote holds at most 25`, q);
  }
  if (tint) tint.remove();

  // Touch targets: the area around the centre reaches the target, a rounded corner included.
  // A visually hidden control (a skip link before its focus) is for the keyboard: no target.
  const sronly = el => {
    const s = style(el), r = el.getBoundingClientRect();
    return r.width <= 1 || r.height <= 1 || s.clip === 'rect(0px, 0px, 0px, 0px)' || /^inset\(50%/.test(s.clipPath);
  };
  const focusable = [...document.querySelectorAll(
    'a[href], button, input:not([type=hidden]), select, textarea, summary, [tabindex]:not([tabindex="-1"]), ' +
    '[role=button], [role=link], [role=tab], [role=checkbox], [role=radio], [role=switch], [role=menuitem], [role=option]')]
    .filter(el => !el.closest('[inert], [aria-hidden=true]') && !el.matches(':disabled') && shown(el));
  const targets = focusable.filter(el => !sronly(el));
  // Skip link (Accessibility): the first focusable element links to <main>'s id and stays hidden, clipped or above
  // the page, until focused; its focused place is measured with the focus forced (FOCUSED).
  const skip = whole && !zoom && focusable[0], main = document.querySelector('main');
  if (skip && !(main && main.id && skip.matches('a[href]') && skip.getAttribute('href') === '#' + main.id))
    add('✗', 'Accessibility', `${name(skip)} is the first focusable element: make it a Skip link to the id of <main>`, skip);
  else if (skip && !sronly(skip) && skip.getBoundingClientRect().bottom > 0)
    add('✗', 'Accessibility', `${name(skip)} is the Skip link: hide it until it has focus`, skip);
  else if (skip) { skip.setAttribute('data-kore-focus', 'skip'); skip.dataset.koreColor = style(skip).color; }
  // Focus never covered (Accessibility): a fixed or sticky bar as wide as the screen at the top or bottom edge
  // leaves <html> a scroll-padding on that edge of at least its height. A layer at both edges is no bar.
  for (const el of whole && !zoom ? everyShown : []) {
    const s = style(el), r = el.getBoundingClientRect();
    if (!['fixed', 'sticky'].includes(s.position) || r.width < vw - 0.5) continue;
    const edges = ['top', 'bottom'].filter(edge => s[edge] === '0px');
    for (const edge of edges.length === 1 ? edges : [])
      if ( (parseFloat(style(doc)[`scrollPadding${edge === 'top' ? 'Top' : 'Bottom'}`]) || 0) < r.height - 0.5)
        add('✗', 'Accessibility', `${name(el)} is ${s.position} at the ${edge} edge: give <html> a scroll-padding-${edge} of at least its height, so it never covers the focus`, el);
  }
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
    // A layer is the list of colors it may show: a background-color is one, a gradient is its stops.
    // backdrop-filter is ignored: kore_palette.py measures text on glass with the saturate.
    const layers = [];
    let image = false;
    for (const n of under) {
      const s = style(n);
      if (['img', 'video', 'canvas', 'picture', 'iframe'].includes(n.localName) || s.backgroundImage.includes('url(')) { image = true; break; }
      const grads = [];  // split at the top-level commas, the first listed is painted on top
      let depth = 0, from = 0;
      [...s.backgroundImage].forEach((ch, k, all) => {
        depth += ch === '(' ? 1 : ch === ')' ? -1 : 0;
        if ((ch === ',' && !depth) || k === all.length - 1) grads.push(s.backgroundImage.slice(from, k + 1)), from = k + 1;
      });
      // any color function the computed style keeps (color-mix() computes to color(srgb …)); rgba() paints it
      const found = [...grads.map(g => (g.match(/(?:rgba?|hsla?|hwb|lab|lch|oklab|oklch|color)\([^)]*\)/g) || []).map(rgba)), [rgba(s.backgroundColor)]];
      if (found.slice(0, -1).some((l, k) => !l.length && grads[k].trim() !== 'none')) { image = true; break; }  // a gradient whose stops cannot be read
      const opaque = found.find(l => l.length && l.every(c => c[3] === 1));
      layers.push(...found.slice(0, opaque ? found.indexOf(opaque) + 1 : found.length).filter(l => l.some(c => c[3])));
      if (opaque) break;
    }
    const size = parseFloat(style(el).fontSize), min = size >= 24 ? 3 : 4.5;
    if (image) { add('?', 'Contrast', `${name(el)} sits on an image: check ${min}:1`, el); continue; }
    let bgs = [canvas];  // every combination of the layers' colors, bottom-up; the lowest ratio is kept
    for (const l of layers.reverse()) bgs = bgs.flatMap(b => l.map(c => over(c, b)));
    const fg = rgba(style(el).color);
    const r = Math.min(...bgs.map(bg => {
      const ink = over([fg[0], fg[1], fg[2], fg[3] * alpha], bg);
      const [hi, lo] = [lum(ink), lum(bg)].sort((x, y) => y - x);
      return (hi + 0.05) / (lo + 0.05);
    }));
    if (r < min - 0.005) add('✗', 'Contrast', `${name(el)} is ${r.toFixed(2)}:1, below ${min}:1`, el);
  }

  // Top bar links on one line from md.
  if (vw >= 768) {
    for (const nav of document.querySelectorAll('header nav, [role=banner] nav')) {
      const tops = [...nav.querySelectorAll('a')].filter(shown).map(a => Math.round(a.getBoundingClientRect().top));
      if (new Set(tops).size > 1) add('✗', 'Top bar', `the links of ${name(nav)} wrap onto ${new Set(tops).size} lines`, nav);
    }
  }

  // All or none: among the groups that share a parent, every group has a visible title or none has.
  const titled = g => g.localName === 'optgroup' ? !!g.label.trim()
    : g.localName === 'fieldset' ? [...g.children].some(c => c.localName === 'legend' && shown(c) && c.innerText.trim())
    : (g.getAttribute('aria-labelledby') || '').split(/\s+/).some(id => { const t = id && document.getElementById(id); return t && shown(t) && t.innerText.trim(); });
  const siblings = new Map();  // parent → its groups on screen
  for (const g of document.querySelectorAll('[role=group], fieldset, optgroup')) {
    if (g.localName !== 'optgroup' && !shown(g)) continue;  // an optgroup draws no box of its own
    siblings.set(g.parentElement, [...(siblings.get(g.parentElement) || []), g]);
  }
  for (const groups of siblings.values()) {
    const bare = groups.filter(g => !titled(g));
    if (bare.length && bare.length < groups.length) add('✗', 'Grouping and separation', `${name(bare[0])} has no title, while ${groups.length - bare.length} of the ${groups.length} groups beside it have one`, bare[0]);
  }

  // Titles of cards side by side on the same number of lines: siblings with the same tag and class,
  // starting at the same height, each with a heading.
  // Lines of the text itself: the heading's box may be stretched by its grid row (aligned zones).
  const lines = h => {
    // only text counts: an icon centred beside two lines would sit between them
    const rs = [];
    for (const walk = document.createTreeWalker(h, NodeFilter.SHOW_TEXT); walk.nextNode();) {
      const range = document.createRange();
      range.selectNodeContents(walk.currentNode);
      rs.push(...[...range.getClientRects()].filter(r => r.width > 0));
    }
    rs.sort((a, b) => a.top - b.top);
    // a box joins the line it overlaps by half its own height: a smaller span on the line (a period after a title) does,
    // the next line does not even when the text is taller than the line-height (display-sm 36/44 sets 45px), so lines overlap a little
    let n = 0, top = Infinity, bottom = -Infinity;
    for (const r of rs) {
      if (Math.min(r.bottom, bottom) - Math.max(r.top, top) >= r.height / 2) { top = Math.min(top, r.top); bottom = Math.max(bottom, r.bottom); }
      else { n++; top = r.top; bottom = r.bottom; }
    }
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
  for (const h of document.querySelectorAll('h1, h2')) {
    if (!shown(h) || h.closest('dialog, [role=dialog], [role=alertdialog], [data-kore-user]')) continue;
    if (lines(h) > 2) add('✗', 'Typography rules', `${name(h)} runs over two lines: the h1 and a page section's heading hold at most two`, h);
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
    for (const root of document.querySelectorAll(`[data-kore="${CSS.escape(table)}"]`)) {
      const first = element => [...root.querySelectorAll(`[data-kore-element="${CSS.escape(element)}"]`)].filter(el => el.closest('[data-kore]') === root);
      const texts = rows.filter(r => r[1] && r[9]).flatMap(r => first(r[0]).map(el => [r, el, el.getBoundingClientRect()]));
      const point = texts.find(t => t[0][6]);
      for (const [row, el, b] of point ? texts : []) {
        const f = point[2], rtl = style(root).direction === 'rtl';
        // language.md: in right-to-left, left and right swap
        if (!row[6] && (b.top < f.top - 1 || (b.top <= f.top + 1 && (rtl ? b.right > f.right + 1 : b.left < f.left - 1))))
          add('✗', 'The One Winner Rule', `${name(el)} comes before the focal point ${name(point[1])}`, el);
      }
      for (const [element, role, weight, color, space, target, , inline, label, , heading] of rows) {
        const found = first(element);
        for (const el of found) {
          const tag = /^h[1-6]$/.test(el.localName) ? el.localName : '';
          if ((tag === 'h2' || tag === 'h3' || heading) && tag !== heading)
            add('✗', 'Typographic levels', `${name(el)} is ${tag ? 'an ' + tag : 'no heading'}, its row says ${heading || 'no h2 or h3'}`, el);
        }
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
          const figure = (text.match(/^[−+-]?\d(?:[\d.,]*\d)?(?=\s)/) || [''])[0];
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
  // Copy 3: each Element of a section or component holds its own text; copies of one Element hold their data's text.
  for (const root of zoom ? [] : document.querySelectorAll('[data-kore]')) {
    const seen = new Map();
    for (const el of root.querySelectorAll('[data-kore-element]')) {
      if (el.querySelector('[data-kore-element]')) continue;  // a wrapper's text is its inner element's
      const text = el.closest('[data-kore]') === root ? el.innerText.trim().replace(/\s+/g, ' ').toLowerCase() : '';
      if (!text) continue;
      if (seen.has(text) && seen.get(text).dataset.koreElement !== el.dataset.koreElement) add('✗', 'Copy', `${name(el)} repeats the text of ${name(seen.get(text))}: each element holds its own text`, el);
      else if (!seen.has(text)) seen.set(text, el);
    }
  }
  // Copy and AI tells: each rule reads the text an element holds itself (its own text nodes), outside data-kore-user.
  const own = el => [...el.childNodes].filter(n => n.nodeType === 3).map(n => n.data).join('').replace(/\s+/g, ' ').replace(/’/g, "'").trim();
  const mine = everyShown.filter(el => !el.closest('[data-kore-user]'));
  const ownTexts = mine.map(el => [el, own(el)]).filter(([, t]) => t);
  // Whole words or phrases, case-insensitive; with inflect, the first word also in its -s, -es, -d, -ed and -ing forms (a final e dropped before -ing).
  const wordRx = (list, inflect) => new RegExp('(?<![\\p{L}\\d])(?:' + list.map(w => {
    const [v, ...rest] = w.split(' ');
    const heads = inflect ? [v, v + 's', v + 'es', v + 'd', v + 'ed', v + 'ing', v.replace(/e$/, '') + 'ing'] : [v];
    return '(?:' + heads.join('|') + ')' + rest.map(r => '\\s+' + r).join('');
  }).join('|') + ')(?![\\p{L}\\d])', 'iu');
  const holds = (list, inflect, msg) => {
    const rx = wordRx(list, inflect);
    for (const [el, t] of ownTexts) { const m = t.match(rx); if (m) add('✗', 'Copy', msg(el, m[0]), el); }
  };
  if (english) {
    // Copy 1: no filler opening or closing phrase.
    holds(["Let's get started", "Here's what you need to know", "You're all set", 'Certainly', 'I hope this helps', 'Oops', 'Uh-oh'], false,
      (el, w) => `${name(el)} holds "${w}": state the point`);
    // Copy 4: no empty framing phrase.
    holds(['at its core', 'the real question', 'the language of'], false, (el, w) => `${name(el)} holds "${w}": state the specific claim`);
    // Copy 7: no AI vocabulary.
    holds(['actually', 'additionally', 'crucial', 'delve', 'enhance', 'foster', 'pivotal', 'showcase', 'valuable', 'vibrant'], true,
      (el, w) => `${name(el)} holds "${w}": use a plain word`);
    // Copy 9: is, has or shows, not serves as or boasts.
    holds(['serve as', 'boast'], true, (el, w) => `${name(el)} holds "${w}": use is, has or shows`);
  }
  // Content: never placeholder text; lorem ipsum is the same in every language.
  for (const [el, t] of ownTexts) { const m = t.match(wordRx(['lorem'], false)); if (m) add('✗', 'Content', `${name(el)} holds "${m[0]}": write the real text`, el); }
  // Copy 6: no dash between two words (an em dash, or an en dash or hyphen with a space on each side); a range of two numbers joins no words.
  for (const [el, t] of ownTexts)
    if ([...t.matchAll(/([\p{L}\p{N}])(?:\s*—\s*| [–-] )(?=([\p{L}\p{N}]))/gu)].some(m => !(/\p{N}/u.test(m[1]) && /\p{N}/u.test(m[2]))))
      add('✗', 'Copy', `${name(el)} joins two words with a dash: use a period, a comma, a colon or parentheses`, el);
  // Copy 10: no emoji or arrow in a heading or the label of a control (the outermost one holds the finding).
  const labelled = mine.filter(el => el.matches('h1, h2, h3, h4, h5, h6, [role=heading], button, [role=button], a[href], label, legend, th, [role=tab], [role=menuitem]') && !(el.localName === 'a' && el.closest('p')));
  for (const el of labelled)
    if (!labelled.some(h => h !== el && h.contains(el)) && /(?![©®™])\p{Extended_Pictographic}|[←-⇿➔-➿⬅-⬇⮕]/u.test(el.innerText))
      add('✗', 'Copy', `${name(el)} holds an emoji or an arrow: let the words carry the emphasis`, el);
  // AI tell 2: siblings numbered 01, 02 outside an ol (a date does not count).
  const numbered = new Map();
  for (const [el, t] of ownTexts) {
    numericDate.lastIndex = 0;
    if (/^0\d+\b/.test(t) && !dated(t) && !el.parentElement.closest('ol')) numbered.set(el.parentElement, [...(numbered.get(el.parentElement) || []), el]);
  }
  for (const group of numbered.values())
    if (group.length > 1) for (const el of group) add('✗', 'AI tells', `${name(el)} opens with a section number: use an <ol> when the order is information`, el);
  // AI tell 6: no scroll cue.
  for (const [el, t] of english ? ownTexts : [])
    if (/^scroll( to explore)?$/i.test(t)) add('✗', 'AI tells', `${name(el)} is a scroll cue: let the content invite scrolling`, el);
  // AI tell 9: a Badge or Chip sits beside its image, not over it.
  const pictures = everyShown.filter(el => el.matches('img, picture, video') || /url\(/.test(style(el).backgroundImage));
  for (const b of mine.filter(el => el.matches('[data-kore="Badge"], [data-kore="Chip"]'))) {
    const q = rect(b);
    if (pictures.some(m => { const r = rect(m); return !b.contains(m) && Math.min(q.right, r.right) > Math.max(q.left, r.left) && Math.min(q.bottom, r.bottom) > Math.max(q.top, r.top); }))
      add('✗', 'AI tells', `${name(b)} sits over an image: put the label under the image`, b);
  }
  // AI tell 11: no word strip ("A · B · C") in the hero.
  for (const [el, t] of ownTexts)
    if (el.closest('[data-kore="Hero"]') && t.split(' · ').length >= 3)
      add('✗', 'AI tells', `${name(el)} is a word strip in the hero: let the hero hold its h1, subtitle and calls to action`, el);
  // AI tell 13: two button-look links of one root, one address and two labels, give two calls to action.
  const looks = mine.filter(el => {
    if (!el.matches('a[href]') || el.closest('p')) return false;
    const s = style(el);
    return rgba(s.backgroundColor)[3] > 0 || s.boxShadow !== 'none' || sides.some(d => parseFloat(s[`border${d}Width`]) > 0 && rgba(s[`border${d}Color`])[3] > 0);
  });
  // Button and States: each keeps its label color on focus, measured with the focus forced (FOCUSED).
  // The Skip link, marked before, takes both measures.
  // Button: at rest, no underline.
  for (const a of looks)
    if (style(a).textDecorationLine !== 'none')
      add('✗', 'Button', `${name(a)} is a link with the look of a button: give it text-decoration none`, a);
  looks.filter(a => !a.dataset.koreFocus).forEach((a, i) => { a.setAttribute('data-kore-focus', `link ${i}`); a.dataset.koreColor = style(a).color; });
  const linked = new Map();  // root -> its button-look links that lead somewhere
  for (const a of looks) {
    const href = a.getAttribute('href').trim();
    if (!href || href === '#' || /^javascript:/i.test(href)) continue;
    const root = a.closest('[data-kore]');
    linked.set(root, [...(linked.get(root) || []), a]);
  }
  const label = el => el.textContent.replace(/\s+/g, ' ').trim().toLowerCase();
  for (const group of linked.values())
    group.forEach((b, j) => {
      const a = group.slice(0, j).find(o => o.href === b.href && label(o) !== label(b));
      if (a) add('✗', 'AI tells', `${name(a)} and ${name(b)} lead to the same address with different labels: keep one call to action`, b);
    });
  // Code order: screen readers and Tab follow the code, so marked elements follow their order on screen.
  for (const root of zoom ? [] : document.querySelectorAll('[data-kore]')) {
    const leaves = [...root.querySelectorAll('[data-kore-element]')].filter(el => el.closest('[data-kore]') === root && !el.querySelector('[data-kore-element]'))
      .map(el => [el, el.getBoundingClientRect()]).filter(([, r]) => r.width > 0 && r.height > 0);
    const rtl = style(root).direction === 'rtl';
    leaves.forEach(([elJ, b], j) => {
      const before = leaves.slice(0, j).find(([, a]) => (b.left < a.right && a.left < b.right && b.top < a.top - 1) || (b.top < a.bottom && a.top < b.bottom && (rtl ? b.right > a.right + 1 : b.left < a.left - 1)));
      if (before) add('✗', 'Code order', `${name(elJ)} reads before ${name(before[0])} on screen and comes after it in the code`, elJ);
    });
  }
  return out;
}
"""

# Runs in a fresh page with motion on, in Site mode: each section under the first Hero keeps its text hidden until its top
# passes 70% of the viewport height, reveals it there, and keeps it once the page scrolls back. One finding per section, the first phase that fails.
REVEAL = r"""
async () => {""" + HELPERS + r"""
  const hero = document.querySelector('[data-kore=Hero]');
  const line = innerHeight * 0.7;
  const sections = !hero ? [] : [...document.querySelectorAll('section')].filter(s =>
    !s.matches('[data-kore=Hero]') && s.checkVisibility({visibilityProperty: true}) &&
    s.getBoundingClientRect().top > hero.getBoundingClientRect().bottom && s.getBoundingClientRect().top >= line);
  // The first descendant with its own text, and its opacity as seen: the product up to the section.
  const text = s => [...s.querySelectorAll('*')].find(e => [...e.childNodes].some(n => n.nodeType === 3 && n.data.trim()));
  const opacity = s => { let o = 1; for (let e = text(s); ; e = e.parentElement) { o *= +style(e).opacity; if (e === s) return o; } };
  const frame = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const settle = async () => {
    await frame();
    await Promise.race([Promise.all(document.getAnimations().map(a => a.finished.catch(() => 0))), new Promise(r => setTimeout(r, 3000))]);
  };
  const place = (s, share) => window.scrollTo({top: s.getBoundingClientRect().top + scrollY - innerHeight * share, behavior: 'instant'});
  const live = sections.filter(s => text(s));
  const phase1 = live.filter(s => {
    if (opacity(s) <= 0) return true;
    add('✗', 'Scroll reveal', `${name(s)} is a section under the hero: keep its text hidden until its top passes 70% of the viewport`, s);
  });
  const phase2 = [];
  for (const s of phase1) {
    place(s, 0.5);
    await settle();
    // shortcut: a last section shorter than 30% of the viewport never passes the line and is not measured, until motion.md says how it shows.
    if (s.getBoundingClientRect().top >= line) continue;
    if (opacity(s) < 1) add('✗', 'Scroll reveal', `${name(s)}: reveal its text when its top passes 70% of the viewport`, s);
    else phase2.push(s);
  }
  window.scrollTo({top: 0, behavior: 'instant'});
  await settle();
  for (const s of phase2) {
    place(s, 0.9);
    await settle();
    if (opacity(s) < 1) add('✗', 'Scroll reveal', `${name(s)}: reveal it once; it stays shown when the page scrolls back`, s);
  }
  return out;
}
"""

# Runs in the page with focus and focus-visible forced on every element MEASURE marked with data-kore-focus.
FOCUSED = r"""
() => {""" + HELPERS + r"""
  // The first Tab reaches the Skip link at the top of the page; MEASURE leaves the page scrolled.
  window.scrollTo({top: 0, left: 0, behavior: 'instant'});
  for (const a of document.getAnimations()) { try { a.finish(); } catch (e) {} }
  for (const el of document.querySelectorAll('[data-kore-focus]')) {
    const s = style(el), r = el.getBoundingClientRect();
    if (el.dataset.koreFocus === 'skip') {
      const start = s.direction === 'rtl' ? vw - r.right : r.left;
      if (Math.round(start) !== 8 || Math.round(r.top) !== 8)
        add('✗', 'Accessibility', `${name(el)} is the Skip link: on focus, show it space-2 (8px) from the top start corner`, el);
      if (s.backgroundColor !== resolve(el, '--surface-card', 'backgroundColor') || s.zIndex !== resolve(el, '--zIndex-toast', 'zIndex'))
        add('✗', 'Accessibility', `${name(el)} is the Skip link: on focus, show it as an elevated button (surface-card) at zIndex toast`, el);
    }
    // A link with the look of a button; the focused Skip link is one (spacing.md, Skip link).
    if (s.color !== el.dataset.koreColor || !s.textDecorationLine.includes('underline') || s.textDecorationThickness !== '2px' ||
        s.textUnderlineOffset !== '4px' || (s.outlineStyle !== 'none' && parseFloat(s.outlineWidth) > 0))
      add('✗', 'States', `${name(el)} is a link with the look of a button: on focus it keeps its label color, takes a 2px underline at a 4px offset and no outline`, el);
  }
  if (tint) tint.remove();
  return out;
}
"""

# Runs in a fresh page, in two steps. PICK tags the i-th target with data-kore-url and describes it, or returns null:
# the first unselected tab of each tablist, then the last enabled button of each Pagination root.
URL_PICK = r"""
(i) => {
  const tabs = [...document.querySelectorAll('[role=tablist]')]
    .map((list, group) => [group, [...list.querySelectorAll('[role=tab]')].findIndex(t => t.getAttribute('aria-selected') !== 'true')])
    .filter(([, index]) => index >= 0).map(([group, index]) => ({kind: 'tab', group, index}));
  const pages = [...document.querySelectorAll('[data-kore="Pagination"]')]
    .map((root, group) => ({kind: 'page', group, index: [...root.querySelectorAll('button')].findLastIndex(b => !b.disabled)}))
    .filter(({index}) => index >= 0);
  const info = [...tabs, ...pages][i];
  if (!info) return null;
  const root = info.kind === 'tab' ? document.querySelectorAll('[role=tablist]')[info.group] : document.querySelectorAll('[data-kore="Pagination"]')[info.group];
  root.querySelectorAll(info.kind === 'tab' ? '[role=tab]' : 'button')[info.index].dataset.koreUrl = '';
  return info;
}
"""

# Runs in the page after the click, and again after the new URL is opened. root: the Pagination text right after the click.
# Returns the finding message, or null when the URL changed and the new page shows the same tab or page.
URL_VERDICT = r"""
({kind, group, index, moved, root}) => {""" + HELPERS + r"""
  const tab = kind === 'tab';
  const box = document.querySelectorAll(tab ? '[role=tablist]' : '[data-kore="Pagination"]')[group];
  const el = box.querySelectorAll(tab ? '[role=tab]' : 'button')[index];
  if (moved && (tab ? el.getAttribute('aria-selected') === 'true' : box.innerText === root)) return null;
  return tab ? `${name(el)} is a tab: put the open tab in the URL, so a reload opens it again`
             : `${name(el)} is the next page: put the page number in the URL, so a reload shows the same page`;
}
"""


# Runs in a fresh page. Marks window and returns the title and the first nav link to another path of the same origin, tagged data-kore-route, or null.
ROUTE_PICK = r"""
() => {
  const a = [...document.querySelectorAll('nav a[href]')].find(a => a.origin === location.origin && a.pathname !== location.pathname);
  if (!a) return null;
  a.dataset.koreRoute = '';
  window.koreRoute = true;
  return document.title;
}
"""
# Runs in the page after the click. title: the title before it. Returns the finding messages; none when the page reloaded or the path did not change.
ROUTE_VERDICT = r"""
({title, path}) => {""" + HELPERS + r"""
  if (!window.koreRoute || location.pathname === path) return [];
  const a = document.querySelector('[data-kore-route]') || document.body, h = document.activeElement, found = [];
  const to = `${name(a)} changes the route: `;
  if (!(h.localName === 'h1' && h.getAttribute('tabindex') === '-1')) found.push(to + `move focus to the new page's h1 (tabindex="-1")`);
  if (document.title === title) found.push(to + 'change the document title');
  return found;
}
"""


# Runs in a fresh page. Tags the i-th target with data-kore-overlay and returns its component, or null:
# every shown element with aria-haspopup ("true" is a menu) and every combobox (a listbox), in page order.
OVERLAY_PICK = r"""
(i) => {
  const kinds = {dialog: 'Popover', menu: 'Menu', true: 'Menu', listbox: 'Select'};
  const els = [...document.querySelectorAll('[aria-haspopup], [role=combobox]')]
    .filter(el => !el.matches(':disabled, [aria-disabled=true]') && el.checkVisibility({opacityProperty: true, visibilityProperty: true}) && kinds[el.getAttribute('aria-haspopup') || 'listbox']);
  const el = els[i];
  if (!el) return null;
  el.dataset.koreOverlay = '';
  return kinds[el.getAttribute('aria-haspopup') || 'listbox'];
}
"""

# Runs in the page after a key or a click. step: "open", "focus", "escape" or "outside".
# Returns the finding message, or null when the step holds.
OVERLAY_VERDICT = r"""
(step) => {""" + HELPERS + r"""
  const t = document.querySelector('[data-kore-overlay]');
  const box = document.getElementById(t.getAttribute('aria-controls'));
  const open = t.getAttribute('aria-expanded') === 'true';
  const listbox = (t.getAttribute('aria-haspopup') || 'listbox') === 'listbox';
  if (step === 'open') return open ? null : `${name(t)} opens a menu or popover: Enter or ↓ opens it and sets aria-expanded="true"`;
  if (step === 'focus') {
    if (listbox) return document.activeElement === t ? null : `${name(t)}: on open, keep focus on the trigger`;
    return box && box.contains(document.activeElement) ? null : `${name(t)}: on open, move focus into it`;
  }
  if (step === 'escape') return !open && document.activeElement === t ? null : `${name(t)}: Escape closes it and returns focus to the trigger`;
  return open ? `${name(t)}: a click outside closes it` : null;
}
"""

# Runs in the page with the overlay open. The first point of the viewport, scanning a grid of 40px from the top start,
# that is outside the trigger, the controlled element and every control; null when there is none.
OVERLAY_POINT = r"""
() => {
  const t = document.querySelector('[data-kore-overlay]');
  const box = document.getElementById(t.getAttribute('aria-controls'));
  for (let y = 0; y < innerHeight; y += 40)
    for (let x = 0; x < innerWidth; x += 40) {
      const el = document.elementFromPoint(x, y);
      if (el && !t.contains(el) && !(box && box.contains(el)) && !el.closest('a, button, input, select, textarea, label, summary, [tabindex], [role]')) return [x, y];
    }
  return null;
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

# Runs in the page after SCROLL_THROUGH: the checks that need the page scrolled through (images, blank stretches, rests). Returns [kind, rule, message].
SCROLLED = r"""
() => {""" + HELPERS + kore_images.MISSING + kore_spacing.BLANK + kore_spacing.REST + r"""
  return out;
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
    """force(selector, pseudo-class, ...): forces hover, focus, focus-visible or active on the first element the
    selector finds; with None or nothing, clears it. One CDP session for the page: a state another session forced would stay on."""
    cdp = page.context.new_cdp_session(page)
    cdp.send("DOM.enable")
    cdp.send("CSS.enable")
    doc = cdp.send("DOM.getDocument")["root"]["nodeId"]

    def force(selector, *states):
        node = cdp.send("DOM.querySelector", {"nodeId": doc, "selector": selector})["nodeId"]
        if node:  # no match: the caller's measure reports it
            cdp.send("CSS.forcePseudoState", {"nodeId": node, "forcedPseudoClasses": [s for s in states if s]})
    return force


def load(browser, url, theme, selector, width, touch, reduced="reduce", errors=None):
    """A new context and page, with reduced motion unless reduced is "no-preference".
    A list errors gets the script errors of the page, from its load."""
    context = browser.new_context(viewport={"width": width, "height": HEIGHT}, color_scheme=theme,
                                  has_touch=touch, reduced_motion=reduced)
    page = context.new_page()
    if isinstance(errors, list):
        kore_usability.listen(page, errors)
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
    return context, page


def check(urls, report, themes, shots=None, tables=(), mode=None):
    """Reports the findings of every page, in each theme of themes ({"light" |
    "dark": selector to set on <html>, or None}), through report(kind, path,
    line, rule, message), tables being type_rows of KORE-DECISIONS.md and mode "site", "app" or None the Mode of
    PRODUCT.md, and saves the screenshots in the folder shots.
    Returns the screenshot paths, or None when the browser cannot run."""
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PageTimeout
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
            whole = not urlparse(url).fragment
            for theme, selector in themes.items():
                for width in WIDTHS:
                    touch = width < TOUCH_BELOW
                    errors = []
                    context, page = load(browser, url, theme, selector, width, touch, errors=errors if whole else None)
                    marked |= set(page.evaluate("names => names.filter(n => document.querySelector(`[data-kore=\"${CSS.escape(n)}\"]`))",
                                                [table for table, _ in tables]))
                    for kind, rule, message in page.evaluate(MEASURE, {"touch": touch, "zoom": False, "tables": tables, "mode": mode, "whole": whole}):
                        seen[(kind, rule, message)].append((width, theme))
                    page.evaluate(SCROLL_THROUGH)
                    for kind, rule, message in page.evaluate(SCROLLED):
                        seen[(kind, rule, message)].append((width, theme))
                    for text in errors:
                        seen[("✗", "Usability", f'the page logs an error: "{text}": fix the script so the page loads and scrolls without errors')].append((width, theme))
                    if shots and width in SHOTS:
                        path = shots / f"{name}-{width}-{theme}.png"
                        page.screenshot(path=str(path), full_page=True)
                        saved.append(path)
                    keys = page.evaluate("() => [...document.querySelectorAll('[data-kore-focus]')].map(el => el.dataset.koreFocus)")
                    if keys:  # after the screenshot, which shows the page without focus
                        force = forcer(page)
                        for key in keys:
                            force(f'[data-kore-focus="{key}"]', "focus", "focus-visible")
                        for kind, rule, message in page.evaluate(FOCUSED):
                            seen[(kind, rule, message)].append((width, theme))
                    context.close()
                context, page = load(browser, url, theme, selector, ZOOM_WIDTH, False)
                before = page.evaluate(FONT_SIZES)
                page.add_style_tag(content="html { font-size: 200% !important; }")
                after = page.evaluate(FONT_SIZES)
                fixed = sorted({tag for (tag, a), (_, b) in zip(before, after) if b < a * 1.5})
                if fixed:
                    seen[("✗", "Zoom", f"font size in px, does not follow the user's text size: {', '.join(fixed[:5])}")]\
                        .append(("200%", theme))
                for kind, rule, message in page.evaluate(MEASURE, {"touch": False, "zoom": True, "tables": tables, "mode": mode, "whole": whole}):
                    seen[(kind, rule, message)].append(("200%", theme))
                context.close()
            if whole:  # the URL rule: a click per target, in the first theme at 1440
                theme, selector = next(iter(themes.items()))
                for i in range(99):
                    context, page = load(browser, url, theme, selector, 1440, False)
                    info = page.evaluate(URL_PICK, i)
                    if info:
                        before = page.url
                        try:
                            page.click("[data-kore-url]", timeout=2000)
                            page.wait_for_load_state()
                            if info["kind"] == "page":
                                info["root"] = page.evaluate("g => document.querySelectorAll('[data-kore=Pagination]')[g].innerText", info["group"])
                            info["moved"] = page.url != before
                            if info["moved"]:
                                page.reload(wait_until="load")  # goto to a URL that differs only in its # keeps the document
                            message = page.evaluate(URL_VERDICT, info)
                            if message:
                                seen[("✗", "Usability", message)].append((1440, theme))
                        except PageTimeout:
                            pass  # a target that cannot be clicked is not measured
                    context.close()
                    if not info:
                        break
            if whole:  # the route rule: one click on a nav link to another path, in the first theme at 1440
                theme, selector = next(iter(themes.items()))
                context, page = load(browser, url, theme, selector, 1440, False)
                title = page.evaluate(ROUTE_PICK)
                if title is not None:
                    path = page.evaluate("location.pathname")
                    try:
                        page.click("[data-kore-route]", timeout=2000)
                        try:
                            page.wait_for_load_state("networkidle")
                        except PageTimeout:
                            pass
                        for message in page.evaluate(ROUTE_VERDICT, {"title": title, "path": path}):
                            seen[("✗", "Accessibility", message)].append((1440, theme))
                    except PageTimeout:
                        pass  # a link that cannot be clicked is not measured
                context.close()
            if whole and mode == "site":  # the Scroll reveal rule: scrolls the page, in the first theme at 1440 with motion on
                theme, selector = next(iter(themes.items()))
                context, page = load(browser, url, theme, selector, 1440, False, "no-preference")
                for kind, rule, message in page.evaluate(REVEAL):
                    seen[(kind, rule, message)].append((1440, theme))
                context.close()
            # the Overlay rule, on whole pages and on one #id: keys and clicks per trigger, in the first theme at 1440
            theme, selector = next(iter(themes.items()))
            for i in range(99):
                context, page = load(browser, url, theme, selector, 1440, False)
                component = page.evaluate(OVERLAY_PICK, i)
                if component:
                    try:
                        overlay(page, component, lambda message: seen[("✗", component, message)].append((1440, theme)))
                    except PageTimeout:
                        pass  # a target that cannot be focused is not measured
                context.close()
                if not component:
                    break
            for (kind, rule, message), places in seen.items():
                report(kind, url, 0, rule, f"{message} ({where(places)})")
        for table, _ in tables:
            if table not in marked:
                report("✗", "KORE-DECISIONS.md", 0, "Decisions file", f'no element with data-kore="{table}" on the pages '
                       "checked: mark the root of the section or component (On the page)")
        browser.close()
    return saved


def overlay(page, component, found):
    """Opens the tagged trigger with Enter or ↓, then checks the focus, Escape and a click outside; found(message) for each failure."""
    def opened():
        page.focus("[data-kore-overlay]")
        for key in ("Enter", "ArrowDown"):
            page.keyboard.press(key)
            page.wait_for_timeout(SETTLE)
            if not page.evaluate(OVERLAY_VERDICT, "open"):
                return True
        found(page.evaluate(OVERLAY_VERDICT, "open"))
    if not opened():
        return
    if message := page.evaluate(OVERLAY_VERDICT, "focus"):
        found(message)
    page.keyboard.press("Escape")
    if page.evaluate("() => [...document.querySelectorAll('[role=tooltip]')].some(el => el.checkVisibility())"):
        page.keyboard.press("Escape")  # the tooltip closes first
    page.wait_for_timeout(SETTLE)
    if message := page.evaluate(OVERLAY_VERDICT, "escape"):
        found(message)
    if opened() and (point := page.evaluate(OVERLAY_POINT)):
        page.mouse.click(*point)
        page.wait_for_timeout(SETTLE)
        if message := page.evaluate(OVERLAY_VERDICT, "outside"):
            found(message)


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
