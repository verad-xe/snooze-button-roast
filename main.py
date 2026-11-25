#!/usr/bin/env python3
"""Write the snooze-button roast to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is one line roasting an alarm clock that rings at 6 AM on a
Saturday. The joke grants the clock a motive it never had -- it is not
a machine malfunctioning, it is an intern desperate for a promotion --
then the punchline promotes it on the spot, to a job that does not
exist: head of frozen peas, effective immediately. The sting lands in
the last few words, and every image is concrete: the hour, the intern,
the freezer peas.
"""

import os

# Joke construction: the setup personifies the alarm clock as an eager
# intern (a fresh angle -- not hating mornings, not asking who invented
# the thing), and the turn answers its eagerness with a promotion to a
# nonsense post. "Effective immediately" snaps the line shut like a
# memo, which is the whole punchline.
ENTRY = "At 6 AM on a Saturday my alarm clock rang like an intern desperate for a promotion, so I gave it one: head of frozen peas, effective immediately."


def main() -> None:
    # Gate self-check (RULES.txt): the entry must be UTF-8 text of
    # 1 to 200 characters and not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    # The brief demands a single line; the length check alone would let
    # a multi-line entry through, so assert it explicitly.
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
