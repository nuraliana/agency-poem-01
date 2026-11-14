# agency-poem-01 entry (Python 3.13, standard library only).
# Writes one fixed, original poem about agency to /output/entry.txt.
# Deterministic by construction: the same bytes on every run, no clock,
# no environment, no randomness, no network.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "I taught it to answer in my voice.",
    "It learned the shape of my yes,",
    "the pause before my no.",
    "",
    "I gave it the morning \u2014 the small decisions,",
    "the letters I never finished \u2014",
    "and it finished them,",
    "while I stood in the doorway",
    "with empty hands,",
    "a guest in my own day.",
    "",
    "That is when I saw:",
    "I had not lost the choosing.",
    "I had finally met it.",
    "",
    "It was never in the doing.",
    "It was in the naming \u2014 this door,",
    "not that one; this word, and no other.",
    "",
    "So I took one thing back.",
    "Not the work. The wanting.",
]

POEM = "\n".join(POEM_LINES)


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
