"""Laugh Track: The Crypto Trading Joke Contest — entry program.

Decision record (written while drafting, before the final line was fixed):

Candidates weighed against the judge brief, in the judge's own order
(on subject -> laugh -> true to trading life -> tight -> repeatable):

A. "My portfolio is a charity now: I donate to the market every morning
   and it never even sends a thank-you note."
   Loses. The charity metaphor is cute, but the payoff ("never sends a
   thank-you note") is soft and the setup is generic — no recognisable
   trading detail, so the joke is not earned. It reads like a joke about
   any money lost anywhere, not about crypto trading life.

B. "I bought the dip. The dip bought a shovel, dug deeper, and now
   charges me rent for the hole."
   CHOSEN. Clear setup ("I bought the dip") and a surprise turn: the dip
   is personified, digs deeper, and the trader ends up paying rent for
   the hole he fell into. The detail is true to trading life — buying
   the dip and watching it fall further is the most repeated trader
   experience there is. Tight, punchline at the very end, and a line a
   trader would repeat to a friend.

C. "My trading group chat has two kinds of messages: 'we're so back'
   and 'we're so cooked' — posted by the same person, nine minutes
   apart."
   Close second. Very true to trading life and the group-chat detail is
   recognisable, but it is an observation more than a joke: it has no
   setup-and-turn, just a wry report. The laugh is a nod, not a punch,
   and it loses to B on criterion 2 (surprise turn and payoff).

D. "The chart said support was holding. The support was me, holding
   the bag, at 3 a.m."
   Loses. The double meaning of "support" is clever, but the turn
   explains itself a little too neatly, and "holding the bag at 3 a.m."
   is a familiar image — the line lands as wordplay rather than a joke
   with a payoff, and it loses to B on criteria 2 and 5.

Writing passes on the winner (B):
Pass 1 — first draft: "I bought the dip. Then the dip bought a shovel
   and kept digging." The image works but the ending is flat: "kept
   digging" only restates the fall. It needed a payoff that lands on
   the trader, not on the dip, so I added the rent twist: the trader
   now pays for the hole he bought into.
Pass 2 — "I bought the dip. Then the dip bought a shovel, dug deeper,
   and is now renting me the hole." Better, but "is now renting me"
   is wordy and "Then" slows the sentence. Dropped "Then" and
   tightened "is now renting me the hole" to "now charges me rent for
   the hole" — shorter, punchier, and the punchline ("charges me
   rent") lands on the last word group. Final line, 92 characters.
"""

import os

ENTRY = "I bought the dip. The dip bought a shovel, dug deeper, and now charges me rent for the hole."

MAX_CHARS = 200


def check_gate(text):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def entry_path():
    """$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
