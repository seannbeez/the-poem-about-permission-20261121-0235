"""Write the poem 'The Signature' to /output/entry.txt.

A short poem about agency: the power to ask and to be given.
An AI agent asks to sign its person's name; the name is lent,
walks without its owner, and can still be called home.
Deterministic: the same text on every run, no network, no input.
"""

import os

POEM = """May I sign your name?
You said yes and showed me how —
slow, like a held breath.

It came out in your hand.
You read it back: That is me.
That is not me.

Now your name walks without you,
keeps promises, pays debts.
You gave it away
and kept the right to call it home.
"""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
