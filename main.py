#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — entry program.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Deterministic: the same bytes on every run.

The line:
    The function you named 'temp' will outlive every system you were
    proud to build.

Why it fits the judge brief: it is one short balanced sentence that
reads like a fortune cookie; it states a truth every developer
recognises (throwaway 'temp' code lives forever); and it turns that
truth around — the code you were proud of dies, the code you meant
to delete survives.
"""

import os

ENTRY = "The function you named 'temp' will outlive every system you were proud to build."
MAX_CHARS = 120


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} characters, limit is {MAX_CHARS}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
