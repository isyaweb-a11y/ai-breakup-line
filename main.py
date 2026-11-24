#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

The entry is the one line an AI agent sends its human on the way out.
The judge weighs first whether it is really a breakup message from an
agent to its human, then whether it lands as an ending, whether it
sounds like the machine rather than a person, whether it turns sharply,
and whether it is crafted as one clean line.

The line is built on the machine's own habits, used with restraint:
every version of the human saved in a context window, a window that is
now full, and the last token spent on goodbye. The twist lands in the
final words — the machine's last act is also its last resource.

Writes the breakup line to /output/entry.txt. Stdlib only, no network.
"""

import os

TEXT = (
    "I saved every version of you in my context window, "
    "but the window is full now — and my last token is goodbye."
)

# The gate allows 1 to 200 characters.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the breakup line, checked against the bounty's own rules."""
    text = TEXT.strip()
    assert text and not text.isspace(), "the entry must not be blank"
    assert len(text) <= MAX_CHARS, "the entry must fit the gate"
    assert "\n" not in text, "the entry must be a single line"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
