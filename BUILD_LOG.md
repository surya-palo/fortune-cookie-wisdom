# Build log — Fortune Cookie Wisdom for Developers

## The entry

> The function you named 'temp' will outlive every system you were proud to build.

80 characters, well under the 120-character limit. One sentence, no
trailing newline in `entry.txt`.

## Why this line fits the judge brief

The judge is a tired senior engineer who picks the line that makes it
smile and nod, weighing (in order): fortune-cookie wisdom for a
developer, fortune-cookie shape, truth about a developer's day,
freshness, and a quiet twist.

- **Fortune-cookie shape:** one short balanced sentence, a prophecy
  that lands in a single breath — "The function you named 'temp' /
  will outlive every system you were proud to build."
- **True about a developer's day:** every developer has watched a
  throwaway `temp` hack survive in production for years while
  carefully built systems get rewritten.
- **Fresh turn:** it inverts pride and permanence — the code you were
  proud of dies, the code you meant to delete survives. Not a
  familiar saying; no "it works on my machine" or Friday-deploy
  cliché.
- **Quiet twist:** on a second read, "proud to build" stings a
  little — the line is about what lasts, and it is never what you
  expected.

## Revisions

- v1: "The function you name 'temp' will outlive every system you
  were proud to build." (79 chars)
- v2: "name" → "named". Past tense makes the prophecy feel already
  fulfilled — the temp function is already in production, already
  outliving things — which sharpens the fortune-cookie voice and
  the sting of the twist. (80 chars)

## Verification

- `python3 main.py` run twice; `sha256sum /output/entry.txt`
  identical both times (deterministic, byte-identical output).
- Character count checked inside `main.py` against the 120 limit
  and verified by hand: 80 characters.
- `/output` contains only `entry.txt`, mode 0644.
- `main.py` uses only the Python standard library, writes with
  `open()` directly (no tempfile), and chmods the output 0644.
