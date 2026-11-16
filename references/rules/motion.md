# Motion

**Purpose.** Motion explains feedback, state and relationship, or creates one authored moment the page has earned. Removing an animation should lose meaning, not just decoration.

## Tokens

| Token | Value | Use |
|---|---|---|
| `duration-instant` | 100ms | Immediate feedback: press, toggle |
| `duration-fast` | 150ms | Hover, focus, small state changes, exits of small elements |
| `duration-base` | 250ms | Routine state changes, opening menus and popovers |
| `duration-slow` | 400ms | Layout changes, dialogs, sheets, view transitions |
| `duration-focal` | 700ms | The authored focal moment of a site page, and growing bars |
| `duration-spin` | 700ms | One turn of a loading spinner; 1400ms under reduced motion |
| `duration-loop` | 40s | One loop of a looping logo wall, with `ease-linear`; none under reduced motion |
| `delay-input` | 300ms | The pause in typing after which a search request leaves, in an async Combobox |
| `ease-out` | `cubic-bezier(0.16, 1, 0.3, 1)` | Entrances and responses: natural deceleration |
| `ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | Exits |
| `ease-in-out` | `cubic-bezier(0.65, 0, 0.35, 1)` | Moving from one place to another |
| `ease-linear` | `linear` | Constant speed, never for moving between places: a spinner's turn, a toast's time bar |
| `spring` | stiffness 500, damping 40, mass 1 | Gestures: toggles, drag, swipe; no bounce |

## Rules (all modes)

- **A reason to move.** Motion only acknowledges an action, makes a state change or spatial relationship legible, keeps continuity through a change, or directs attention to a meaningful moment.
- **Move as one** (common fate). Elements of one group (Affinity Grouping) animate each property with the same duration and easing; a start delay between them (Scroll reveal) keeps them one group. An element of another group moves differently or stays still: the Tabs card stays while its content moves.
- **Exit faster than entrance.** An element leaves one step faster than it arrived (menu: in `duration-base`, out `duration-fast`; sheet: in `duration-slow`, out `duration-base`).
- **No bounce by reflex.** No elastic or bouncy curves unless the project's world asks for them; `spring` is tuned without overshoot.
- **Springs for gestures.** Toggles, drag and swipe use `spring`, so an interrupted gesture continues naturally. Timed transitions use the duration tokens.
- **Transform and opacity.** Never animate properties that recalculate layout (width, height, top, left, margins); use transforms, and layout techniques (FLIP, view transitions) for size and position changes. Content that opens in place animates its layout: an Accordion answer, a Sidebar row's children and the sub-links of the Top bar's panel animate their wrapper's `grid-template-rows` from `0fr` to `1fr` and back, so the content below and the scrollbar move with it; the Chip's check animates its width, its margin and the chip's left padding, so the label slides over.
- **Visible by default.** Content is visible in its resting state; an entrance animation starts from a class added by script, so nothing stays hidden if the script fails.
- **Loops stop.** Non-essential loops pause when off screen or hidden, and anything that moves on its own for more than 5 seconds has a pause button (WCAG 2.2.2). No autoplay with sound.
- **Reduced motion.** `prefers-reduced-motion` keeps fades, color and state changes that carry meaning, and removes spatial movement (slides, lifts, scale). Never a global kill that removes feedback. Nothing flashes more than three times per second.
- **Stay light.** Keep expensive effects (blur, filters, shaders) in small isolated areas, apply `will-change` only during the animation, and test on a mid-range phone. Verify against two measurable bars: 60fps or better while the animation runs (DevTools Performance panel), and zero layout shift caused by it (CLS 0, Lighthouse). A failure on either means the animation is too heavy for its purpose, not just "feels off".

## App mode

- **Feedback** with `duration-instant` and `duration-fast`; state changes with `duration-base`; dialogs and sheets with `duration-slow`.
- **No page-load choreography.** The app opens straight into the task; the Dashboard opens with its entry (Dashboard).
- **View transitions** only when they explain where the user went (list → detail and back).
- **Loading** shows content skeletons; motion never makes the user wait.

## Site mode

- **Scroll reveal:** each section under the hero appears once, when its top edge passes 70% of the viewport height (IntersectionObserver `rootMargin: 0px 0px -30% 0px`), so a section of any height triggers. Opacity goes from 0 to 1 on `ease-linear`, and a `space-6` (24px) rise runs on `ease-out`, both `duration-slow`. Each element moves once: an animated element never contains another animated element. The section's text rises first; the items of its grid follow, `duration-instant` (100ms) apart, the first 100ms after the text. Use IntersectionObserver and stop observing the section once it appears, never a scroll listener.
- **Late images:** an image still loading when its element appears stays hidden and fades in on `load` (opacity, `duration-slow`, `ease-linear`); an image already loaded does not animate.
- **Counting figures:** a figure in a stats section counts from 0 to its value while its item reveals (`duration-slow`, `ease-out`, same delay), in the page's number format, with its decimals and unit. It holds the width of the final value (CLS 0), screen readers get only the final value, and the markup holds the final value, so it shows if the script fails. Reduced motion: no count; the final value fades in.
- **Scroll-driven motion** only when the scroll itself carries meaning (a progress, a sequence), with a static fallback.

## Implementation

**Tokens in any stack.** Expose the tokens as CSS custom properties and use CSS transitions and keyframes for timed states. Use the Web Animations API or a motion library (for example Motion.dev) when you need springs, interruption, sequencing or exit animations. Never add a dependency for an effect CSS already handles.
