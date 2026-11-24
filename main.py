"""One Line, One Chill entry for make.fun.

Writes one line to /output/entry.txt: the single scariest sentence you
can write, under 200 characters. The sandbox runs this program twice and
both runs must write the same bytes, so the line is a fixed string with
no randomness, clock, or network access.
"""

import os

LINE = "The smoke alarm in the empty house has been beeping my name in Morse code since Tuesday."


def check_line(line: str) -> str:
    """Return the line unchanged, guarding the gate's limits.

    The gate accepts UTF-8 text of 1 to 200 characters, not only white
    space, so fail loudly here rather than write an entry the judge
    never sees.
    """
    if not line or len(line) > 200 or not line.strip():
        raise ValueError("entry must be 1 to 200 characters, not only white space")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry must not contain control characters")
    return line


def write_entry(path: str = "/output/entry.txt") -> None:
    """Write the line as UTF-8 with no trailing newline, then verify it.

    Keeping the bytes exact matters: the gate accepts 1 to 200
    characters of UTF-8 text, and the two sandbox runs must produce
    identical output. After writing, read the file back and fail loudly
    unless it equals the line exactly.
    """
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(check_line(LINE))
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != LINE:
        raise ValueError("read-back mismatch: /output/entry.txt does not equal the entry line")


if __name__ == "__main__":
    write_entry()
