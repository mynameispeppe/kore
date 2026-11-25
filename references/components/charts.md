# Charts

**Uses:** Cards.

**Purpose:** they show numbers that read better as a shape. The method follows the dataviz skill's.

- **Hierarchy:** the marks are the focal point (The One Winner Rule): under Emphasis the highlighted item in `chart-1`, the others in `hairline-strong`. The title says what is shown, the subtitle the conclusion; the legend, the axis values and the grid only help to read the marks.
- **Elements:** the Charts' own: chart, title block, chart title, chart subtitle, bar list, baseline, band, bar label, bar row, bar value, bar, highlighted bar, dimmed bar, vertical bar list, vertical baseline, vertical band, vertical bar row, vertical bar, plot, plot wrapper, plot svg, y value, x label, end point, direct label, crosshair, lit point, readout, readout row, readout value, readout label, bar readout, legend, legend entry, legend value, mark, square mark, donut, donut svg, ring circle, arc, dimmed arc, hit ring, focus ring, slice, donut centre, centre value, centre label. Other components: the card that holds a chart (Cards). Line, bars, vertical bars, donut and emphasis are forms of the chart, not elements.
- **Form files:** read only the file of each form that the part being built or checked contains: Bars and vertical bars `references/components/charts/bars.md`, Line `references/components/charts/lines.md`, Donut `references/components/charts/donut.md`.

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
- **Guides and axes:** the horizontal guides at the axis values and the bars' baseline: `line-thin` `hairline`, never dashed; no axis line, so no vertical line for the y axis (user decision).
- **Legend:** with two series or more it is always there, above the chart; with one series there is none. display flex; flex-wrap wrap; gap `space-2` `space-4`; list-style none; margin 0; padding 0; color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Legend entry:** display flex; align-items center; gap `space-2`.
- **Legend value:** color `ink`; font-variant-numeric tabular-nums.
- **Mark:** its color is the series color; for lines. display inline-block; width `space-3`; height `line-thick`; background currentColor; border-radius `rounded-full`; flex none.
- **Square mark:** for bars, areas and slices. width `space-2`; height `space-2`; border-radius `rounded-xs`.

**Text**

- **Direct labels:** the value at the end of each bar; at the end of a line, its last value when it is the only series. With several series, no label at the line ends: the legend names them and the readout gives their values. Never a number on every point.

**Interaction**

- **Readout:** this file's element, not the Tooltip; no shadow. position absolute; top 0; z-index `zIndex-tooltip`; background `surface-float`; outline `line-thin` solid `hairline`; outline-offset −`line-thin`; border-radius `rounded-md`; padding `space-2` `space-3`; display flex; flex-direction column; gap `space-1`; white-space nowrap; pointer-events none.
- **Readout row:** one per series, with its mark. display flex; align-items center; gap `space-2`.
- **Readout value:** first. color `ink`; font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; font-variant-numeric tabular-nums.
- **Readout label:** after the value. color `mute`; font-family `body-sm`; font-size `body-sm`; font-weight `body-sm`; line-height `body-sm`; letter-spacing `body-sm`.
- **Keyboard:** the chart takes focus with Tab and its focus marks; ← → Home End move through the points and show the same readout. Each bar and each donut slice takes focus.
- **The readout never hides anything:** every value is also in the chart's labels or in its accessible name.

**Accessibility**

- **Values:** no table view and no "Chart / Table" control: the chart's direct labels, its accessible name and its keyboard readout carry every value (user decision).
- **Accessible name:** it says what is shown and how to read it: the measure and the period, then "Use the arrow keys to read the values." (a donut: "Use Tab to move between slices to read the values."). Every bar and every slice is named by its label and its value; the labels, values and marks drawn on screen are aria-hidden.
- **Contrast:** a palette color below 3:1 on its surface needs the legend or visible direct labels (Contrast); in light: `chart-3`, `chart-4`, `chart-5`.

**Motion**

- **Chart entry:** in site mode, a chart's marks enter once, each mark `duration-instant` after the previous one. They start when the chart's own reveal has finished, or, without a reveal, when the chart passes 70% of the viewport height (as Scroll reveal), so a chart never rises and draws at once.
- **Chart entry reduced motion:** no movement and no count; the line, its points and labels, the bar lists and the donut fade in. Before the entry: opacity 0; during it: animation in `duration-slow` `ease-linear` from opacity 0.
