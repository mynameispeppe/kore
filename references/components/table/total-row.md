**Total row**

- **Total row:** a `<tfoot>` row under the rows. It is not sorted with the rows and sums every row that passes the filters. With its column hidden there is no total row; with the first column hidden, "Total" stays in its place. Each cell: height `space-12`; border-top `line-thin` solid `hairline`; vertical-align middle; color `ink`.
- **Total label:** "Total", a `<th scope="row">` under the first data column. font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`.
- **Sum:** under its column, with its alignment. font-family `title-sm`; font-size `title-sm`; font-weight `title-sm`; line-height `title-sm`; letter-spacing `title-sm`; font-variant-numeric tabular-nums. The other cells, selection and actions included, are empty.
- **Sticky total row:** its cells: position sticky; bottom 0; z-index `zIndex-raised`; background `surface-card`; border-top 0.
