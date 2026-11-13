**Async options**

- **Async hint:** with options from a server, on an empty field the note holds one line, what to type (for example "Type to search cities.").
- **Loading note:** as soon as the user types, the note shows the Spinner (Button) and "Searching…", side by side. display inline-flex; align-items center; justify-content center; gap `space-2`.
- **Request:** it leaves after a pause in typing of `delay-input`; only the latest request's answer is shown, as options or as the no-match note.
- **Failed request:** the note with two lines, what failed and what to do (for example "Couldn't load the cities." and "Try again in a moment."), then the retry row.
- **Retry row:** a small tertiary Button "Try again", `space-2` below the two lines: the note's gap `space-1` plus margin-top `space-1`. It moves focus to the field and repeats the request.
