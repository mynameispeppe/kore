# Popover

- **Popover:** Replaces: `popover.popover`. As in `references/components/popover.md`, with the Glass recipe (3 · floating) drawn as one shape with its arrow: the popover itself keeps only box-shadow `glass-drop` and outline none; its fill and its edge run over the body and the arrow as one outline, with no line across the arrow's base. A popover whose trigger sits inside a glass surface keeps the default.
- **Arrow:** Replaces: `popover.arrow`. The popover's ::before, the edge of that one shape: a `line-thin` band along the outline of the body and the arrow; background `glass-edge`, with a `line-thin` line of `glass-edge-top` along the top of the body.
- **Arrow fill:** Replaces: `popover.arrow-fill`. The popover's ::after, the glass of that one shape, under the edge: the body and the arrow; background `glass-background`; backdrop-filter `glass-backdrop`.
- **Arrow above:** Replaces: `popover.arrow-above`. On a popover above, the arrow of that one shape points down from the bottom of the body.
