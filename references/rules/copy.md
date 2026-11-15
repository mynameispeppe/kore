# Copy

**Rules for every string in the interface:** labels, titles, messages, errors, empty states. Adapted from the humanizer skill (MIT, © Siqi Chen), which builds on Wikipedia's "Signs of AI writing". Check each string against them before it ships, and delete any line that adds nothing the user did not already have.

**Humanizer.** Every string of the interface (labels, titles, messages, texts) goes through the humanizer skill when it is installed, all together once they are written, in embedded mode, with the voice of reference text: neutral and plain. The agent's strings take its rewrite; a string the user gave stays as given, and the report proposes the rewrite. Then check them against the rules below once more; where the two differ, these rules hold: a title without a subject ("Payment failed") stays, and no opinion or reaction is added. Without humanizer (an agent other than Claude Code), the agent checks every string against the rules below, or asks the user for the texts.

1. **State the point.** No run-up ("Let's get started", "Here's what you need to know"), no closing flourish ("You're all set!"), no chat wrapper ("Certainly!", "I hope this helps"), no staged interjection before a fact ("Oops!", "Uh-oh!").
2. **No contrast for effect.** Never "not X, but Y", "not just X", "no guessing", "without the hassle". Say what the thing does. Keep a contrast only when it corrects something the user really believes.
3. **One line, one new fact.** Cut a line that repeats the title or the line above it ("Payment failed" followed by "Your payment did not go through"). Each Element of a section or component holds its own text; copies of one Element hold the text their data gives.
4. **The fact, not the depth.** No "at its core", "the real question", "the language of". Replace the saying with the specific claim.
5. **Three only when there are three.** Never a triad for rhythm ("Fast, simple and secure").
6. **No dashes as connectors.** Use a period, comma, colon or parentheses.
7. **Plain words.** None of: actually, additionally, crucial, delve, enhance, foster, highlight (verb), key (adjective), landscape, pivotal, robust (figurative), showcase, valuable, vibrant.
8. **No sales language.** Say what the thing is or does ("Track your meals"), never "Discover a stunning new way to eat".
9. **Simple verbs.** "is", "has", "shows", never "serves as", "boasts", "features", "offers".
10. **Emphasis by content, not decoration.** No emoji or arrows in labels and headings; bold follows Inline emphasis (Text hierarchy #10).
