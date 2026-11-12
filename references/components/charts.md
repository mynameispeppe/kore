# Charts

**Uses:** Cards.

**Purpose:** they show numbers that read better as a shape. The method follows the dataviz skill's.

- **Hierarchy:** the marks are the focal point (The One Winner Rule): under Emphasis the highlighted item in `chart-1`, the others in `hairline-strong`. The title says what is shown, the subtitle the conclusion; the legend, the axis values and the grid only help to read the marks.
- **Elements:** the Charts' own: chart, title block, chart title, chart subtitle, bar list, baseline, band, bar label, bar row, bar value, bar, highlighted bar, dimmed bar, vertical bar list, vertical baseline, vertical band, vertical bar row, vertical bar, plot, plot wrapper, plot svg, y value, x label, end point, direct label, crosshair, lit point, readout, readout row, readout value, readout label, bar readout, legend, legend entry, legend value, mark, square mark, donut, donut svg, ring circle, arc, dimmed arc, hit ring, focus ring, slice, donut centre, centre value, centre label. Other components: the card that holds a chart (Cards). Line, bars, vertical bars, donut and emphasis are forms of the chart, not elements.

**Form first, color after**

- **What the data does:** one current number → a figure, not a chart (Cards, Key figure); change over time → a line; magnitudes to compare → horizontal bars (vertical when every category's label fits on one line under its bar); parts of a whole → a stacked bar, or a donut of at most 5 slices; one series is the point and the rest are context → emphasis.
- **Limits:** at most 15 bar categories; never two y scales (two measures of different size go in two charts); past 1,000 points draw on a Canvas, with the same focus and readout; more than 7 classes → a table.

**Color**

- **One series:** `chart-1` on every mark.
- **Emphasis:** the highlighted item in `chart-1`, the others in `hairline-strong`.
- **Several series:** `chart-1` to `chart-8` in this fixed order, never cycled, never generated. The color follows the item: a filter never repaints the series that remain. Lines, bars and stacks: at most 4 series; scatter: at most 3; past that, "Other" or small multiples.
- **Never** the status colors (`success`, `warning`, `info`, `danger`) for series.
- **Text never takes the series color:** values and labels in `ink`, `body` or `mute`, with a colored mark beside them.

**Layout**

- **Chart:** display flex; flex-direction column; gap `space-4` between the title block, the legend and the plot.
- **Title block:** display flex; flex-direction column; gap `space-1`. Inside a card, the card's header is the title block (Cards).
- **Chart title:** says what is shown. font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; color `ink`.
- **Chart subtitle:** says the conclusion, not the measure. font-family `body-md`; font-size `body-md`; font-weight `body-md`; line-height `body-md`; letter-spacing `body-md`; color `mute`.
- **Bar list:** the labels, then the bars. position relative; display grid; grid-template-columns auto 1fr; column-gap `space-3`; list-style none; margin 0; padding 0.
- **Baseline:** the bar list's ::before, at the bars' start. content ""; position absolute; grid-column 2; inset-block −`space-1`; inset-inline-start 0; border-inline-start `line-thin` solid `hairline`.
- **Band:** one category, its hit area. display grid; grid-column 1/-1; grid-template-columns subgrid; align-items center; gap `space-3`; min-height calc(`space-10` + `space-1`); cursor default.
- **Bar label:** font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; color `mute`.
- **Bar row:** the bar and its value. position relative; display flex; align-items center; gap `space-2`.
- **Bar value:** font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; font-variant-numeric tabular-nums.
- **Bar:** square at the baseline, rounded at its far tip. height `space-5`; border-start-end-radius `rounded-xs`; border-end-end-radius `rounded-xs`; background `hairline-strong`; transition opacity `duration-fast` `ease-out`; transform-origin left.
- **Bar length:** the script sets it: its value over the largest value, times the room after the label less `space-12` + `space-2`, so the largest value fits after its bar.
- **Bar in RTL:** transform-origin right.
- **Highlighted bar:** background `chart-1`. Every bar of one series is highlighted; under Emphasis only the highlighted item.
- **Dimmed bar:** while a band has hover or focus-visible, the bars of the other bands: opacity 50%.
- **Touching bars:** touching bars and stacked segments are separated by `line-thick` in the surface color, never by a border.
- **Vertical bar list:** the same rules turned 90°. display flex; column-gap 0; padding-block-start `space-6`.
- **Vertical baseline:** across the whole width. inset-inline 0; inset-block auto; top calc(`space-6` + `space-48`); height 0; border-inline-start 0; border-block-start `line-thin` solid `hairline`.
- **Vertical band:** the label under its bar. display flex; align-items center; flex 1 0 calc(`space-10` + `space-1`); flex-direction column-reverse; gap `space-2`.
- **Vertical bar row:** the value above its bar. flex-direction column-reverse; justify-content flex-start; gap `space-1`; height `space-48`.
- **Vertical bar:** its height is its value over the largest value, times `space-48`. width `space-5`; border-radius `rounded-xs` `rounded-xs` 0 0; background `chart-1`; transform-origin bottom.
- **Plot:** for lines and areas. position relative; height `chart`; margin-inline-start `space-10`; margin-bottom `space-6`; touch-action pan-y. A vertical swipe still scrolls the page.
- **Plot focus:** on :focus-visible: outline none, changed in 0s; the plot wrapper takes the corner marks of States.
- **Plot wrapper:** holds the plot's focus marks, since the plot clips its own. position relative; its marks follow a radius of 0.
- **Plot svg:** viewBox 0 0 100 100 with preserveAspectRatio none. position absolute; inset 0; width 100%; height 100%; overflow visible.
- **Guides and axes:** the horizontal guides at the axis values and the bars' baseline: `line-thin` `hairline`, never dashed; no axis line, so no vertical line for the y axis (user decision).
- **Y value:** centred on its grid line, `space-2` from the plot. position absolute; inset-inline-start −`space-10`; width `space-8`; text-align end; transform translateY(−50%); color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`; font-variant-numeric tabular-nums.
- **X label:** centred under its point. position absolute; bottom −`space-6`; transform translateX(−50%); color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Lines:** `line-thick` strokes, round joins and caps, fill none, with vector-effect non-scaling-stroke on the line and the grid, so the strokes keep their width when the plot stretches.
- **End point:** centred on the last point, its background the series color. position absolute; width `space-2`; height `space-2`; border-radius `rounded-full`; corner-shape round; transform translate(−50%, −50%); box-shadow 0 0 0 `line-thick` `canvas`, `surface-card` inside a card; pointer-events none.
- **Area under a line:** the series color at 10% (color-mix with transparent), down to the plot's bottom edge; on a chart with a y axis, only when the axis starts at 0.
- **Direct label:** it ends at the end point, its bottom edge 50% of its height above the point's centre. position absolute; transform translate(−100%, −150%); white-space nowrap; display flex; align-items center; gap `space-2`; color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; font-variant-numeric tabular-nums.
- **Donut:** at most 5 slices, largest first, clockwise from 12 o'clock in `chart-1` onwards, `line-thick` apart in the surface color. position relative; width `space-48`; height `space-48`.
- **Donut svg:** position absolute; inset 0; width 100%; height 100%; overflow visible.
- **Ring circle:** every circle of the donut. fill none; r (`space-48` − `space-5`) / 2.
- **Arc:** one slice's visible ring. stroke-width `space-5`; transition opacity `duration-fast` `ease-out`.
- **Dimmed arc:** while a slice has hover or focus-visible, the arcs of the other slices: opacity 50%.
- **Donut centre:** the total, or the value of the slice in hover or focus. position absolute; inset 0; display flex; flex-direction column; align-items center; justify-content center; text-align center; pointer-events none.
- **Centre value:** color `ink`; font-family `title-md`; font-size `title-md`; font-weight `title-md`; line-height `title-md`; letter-spacing `title-md`; font-variant-numeric tabular-nums.
- **Centre label:** color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Donut legend:** a donut always has a legend above it, each entry with a square mark, its name and its legend value; never labels on the slices.
- **Legend:** with two series or more it is always there, above the chart; with one series there is none. display flex; flex-wrap wrap; gap `space-2` `space-4`; list-style none; margin 0; padding 0; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Legend entry:** display flex; align-items center; gap `space-2`.
- **Legend value:** color `ink`; font-variant-numeric tabular-nums.
- **Mark:** its color is the series color; for lines. display inline-block; width `space-3`; height `line-thick`; background currentColor; border-radius `rounded-full`; flex none.
- **Square mark:** for bars, areas and slices. width `space-2`; height `space-2`; border-radius `rounded-xs`.
- **Chart in RTL:** the chart is mirrored. The plot svg: transform scaleX(−1). The x label: transform translateX(50%). The end point and the lit point: transform translate(50%, −50%). The direct label: transform translate(100%, −150%). The readout too.

**Text**

- **Axis values:** round numbers (Y value, X label).
- **Direct labels:** the value at the end of each bar; at the end of a line, its last value when it is the only series. With several series, no label at the line ends: the legend names them and the readout gives their values. Never a number on every point.

**Interaction**

- **Crosshair:** on a line it follows the pointer and snaps to the nearest point, across the plot's height. position absolute; inset-block 0; width 0; border-inline-start `line-thin` solid `hairline-strong`; pointer-events none.
- **Lit point:** the points at the crosshair's position, drawn as the End point.
- **Bar targets:** each bar is its own target (Dimmed bar). Its hit area is its whole band, the bar, its label and the room up to the next band horizontal bars sit at least calc(`space-10` + `space-1`) apart, centre to centre, as Touch targets ask. Where the bands are narrower (touching bars, or more categories than the width holds), the bars are one target, as a line: the pointer snaps to the nearest bar.
- **Slice:** each slice is its own target (Dimmed arc), and the donut centre shows its value and label in place of the total, so the donut has no floating readout.
- **Hit ring:** the slice's target on its arc. stroke transparent; stroke-width calc(`space-10` + `space-1`); pointer-events stroke.
- **Readout:** this file's element, not the Tooltip; no shadow. position absolute; top 0; z-index `zIndex-tooltip`; background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; border-radius `rounded-md`; padding `space-2` `space-3`; display flex; flex-direction column; gap `space-1`; white-space nowrap; pointer-events none.
- **Readout row:** one per series, with its mark. display flex; align-items center; gap `space-2`.
- **Readout value:** first. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; font-variant-numeric tabular-nums.
- **Readout label:** after the value. color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Readout placement:** on a line, at the plot's top, `space-3` after the crosshair; before it when it would cross the end edge.
- **Bar readout:** the readout of a bar, above its bar's start. position absolute; bottom calc(100% − `space-1`); inset-inline-start 0; z-index `zIndex-tooltip`; background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; border-radius `rounded-md`; padding `space-2` `space-3`; display none; flex-direction column; gap `space-1`; white-space nowrap; pointer-events none.
- **Bar readout shown:** while its band has hover or focus-visible: display flex, changed in 0s.
- **Keyboard:** the chart takes focus with Tab and its focus marks; ← → Home End move through the points and show the same readout. Each bar and each donut slice takes focus.
- **Band focus:** the band takes the four-corner focus marks of States, following `rounded-xs`; outline none, changed in 0s.
- **Focus ring:** a third circle under the slice's arc, with the arc's dash, so a `focus-ring` band shows on both sides of the slice. stroke transparent; stroke-width calc(`space-5` + 2 × (`line-thick` + the focus mark's width, States)); pointer-events none.
- **Slice outline:** on :focus: outline none.
- **Slice focus:** on :focus-visible the focus ring takes stroke `focus-ring`, changed in 0s; under forced colors: stroke Highlight.
- **The readout never hides anything:** every value is also in the chart's labels or in its accessible name.

**Accessibility**

- **Values:** no table view and no "Chart / Table" control: the chart's direct labels, its accessible name and its keyboard readout carry every value (user decision).
- **Accessible name:** it says what is shown and how to read it: the measure and the period, then "Use the arrow keys to read the values." (a donut: "Use Tab to move between slices to read the values."). Every bar and every slice is named by its label and its value; the labels, values and marks drawn on screen are aria-hidden.
- **Contrast:** a palette color below 3:1 on its surface needs the legend or visible direct labels (Contrast); in light: `chart-3`, `chart-4`, `chart-5`.

**Motion**

- **Chart entry:** in site mode, a chart's marks enter once, each mark `duration-instant` after the previous one. They start when the chart's own reveal has finished, or, without a reveal, when the chart passes 70% of the viewport height (as Scroll reveal), so a chart never rises and draws at once.
- **Bar entry:** the bars grow from their baseline, never by animating the width or the height. Before the entry: transform scaleX(0), scaleY(0) for a vertical bar; during it: animation in `duration-focal` `ease-out` from scale 0 to 1, delayed by `duration-instant` for each bar before it. Each bar's value counts with its bar (Counting figures).
- **Line entry:** the line draws from its first point, on the series only; the guides and axes show from the first frame. Before the entry: clip-path inset(0 100% 0 0); during it: animation in `duration-focal` `ease-out`, to clip-path inset(0).
- **End point entry:** the end points and the direct labels fade in when the line has finished. Before the entry: opacity 0; during it: animation in `duration-slow` `ease-linear` from opacity 0, delayed by `duration-focal`.
- **Slice entry:** the slices open clockwise from 12 o'clock, also in RTL. Before the entry: stroke-dasharray 0 100; during it: animation in `duration-focal` `ease-out` from that dash, delayed by `duration-instant` for each slice before it.
- **Centre entry:** the donut centre fades in when the last slice has finished. Before the entry: opacity 0; during it: animation in `duration-slow` `ease-linear` from opacity 0, delayed by `duration-focal`.
- **Chart entry reduced motion:** no movement and no count; the line, its points and labels, the bar lists and the donut fade in. Before the entry: opacity 0; during it: animation in `duration-slow` `ease-linear` from opacity 0.
