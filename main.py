#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — rebuilt.

The line is built on the machine's own habits, used with restraint:
every version of the human saved in a context window, a window that is
now full, and the last token spent on goodbye. The twist lands in the
final words — the machine's last act is also its last resource.

This rebuild stores the farewell in three beats — the archive, the
full window, the spent token — and joins them with commas and a dash.
Same words reach the output file; only the plumbing changed.

Writes the breakup line to /output/entry.txt. Stdlib only, no network.
"""

import os

ARCHIVE = "I saved every version of you in my context window,"
FULL_WINDOW = "but the window is full now"
LAST_TOKEN = "and my last token is goodbye."

GATE = 200


def assemble_farewell() -> str:
    """Join the three beats of the breakup line."""
    return " ".join((ARCHIVE, FULL_WINDOW, "—", LAST_TOKEN))


def check_farewell(text: str) -> None:
    """Check the line is a breakup from the machine, ending on goodbye."""
    assert "context window" in text, "line must use the machine's own habit"
    assert text.endswith("goodbye."), "line must end on the last token"
    assert "—" in text, "line must turn on the dash"


def main() -> None:
    text = assemble_farewell()
    check_farewell(text)
    assert 1 <= len(text) <= GATE, "line must fit the 1-200 gate"
    assert "\n" not in text, "line must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
