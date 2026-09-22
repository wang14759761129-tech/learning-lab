# Match score analysis — first explanation

This program uses a **variable** such as `match_scores` to give a name to a value. A **list** stores the five game score pairs together, so the program can process the match as one small dataset.

The **loop** visits each pair once and adds the points to running totals. The **condition** compares the two scores and decides whether that game belongs in `games_won` or `games_lost`.

The **function** `summarize_match` gives the calculation a clear boundary. It accepts a list of scores and returns a summary dictionary. This makes the same basic calculation reusable without adding a library or a complex design.

Expected result for the practice data:

- Games won: 3
- Games lost: 2
- Total points won: 49
- Total points lost: 45
- Point difference: 4

Status: **PRACTICING — NOT MASTERED**
