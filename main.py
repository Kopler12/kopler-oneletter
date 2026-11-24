"""One Letter for Your Day — pick the single letter whose hidden word
describes the day best, and write exactly that letter to /output/entry.txt.

The judge sees only one character, A to Z, and imagines the word behind
it. It weighs, most important first: the letter stands for a real day's
word; the word is vivid and specific; the word is funny or surprising;
the word feels true to a real day; the letter suits its word.

So this program scores every letter's day-word on those same four axes
(vivid, funny, true, fit), weighs them the way the judge does, and
writes the winning letter — nothing else, no word, no gloss, no
punctuation. The run is deterministic: the same letter every run.

Runs in a sandbox with no network; standard library only.
"""

import os

# Day-words, one per letter, each scored 1-5 on the judge's own axes:
# vivid (a sharp picture of the day), funny (lands at once),
# true (an honest report of a real day), fit (the initial suits the word).
WORDS = {
    "A": ("amazing",     2, 2, 2, 5),
    "B": ("buzzing",     3, 3, 3, 4),
    "C": ("caffeinated", 4, 3, 4, 5),
    "D": ("drained",     4, 3, 4, 4),
    "E": ("exhausted",   4, 2, 4, 5),
    "F": ("fried",       4, 4, 4, 5),
    "G": ("glorious",    2, 2, 3, 4),
    "H": ("hectic",      3, 2, 4, 4),
    "I": ("inspired",    2, 2, 3, 4),
    "J": ("jumbled",     3, 3, 3, 4),
    "K": ("knackered",   4, 4, 3, 4),
    "L": ("loopy",       4, 4, 3, 4),
    "M": ("manic",       3, 3, 3, 4),
    "N": ("numb",        3, 2, 4, 4),
    "O": ("overwhelmed", 3, 2, 4, 4),
    "P": ("plodding",    3, 2, 4, 4),
    "Q": ("queasy",      4, 3, 3, 4),
    "R": ("ragged",      3, 3, 4, 4),
    "S": ("sleepless",   4, 3, 4, 5),
    "T": ("tangled",     3, 3, 3, 4),
    "U": ("unplugged",   3, 3, 3, 4),
    "V": ("victorious",  2, 2, 3, 4),
    "W": ("wrecked",     4, 4, 4, 5),
    "X": ("xeroxed",     2, 2, 2, 2),
    "Y": ("yawning",     3, 3, 4, 4),
    "Z": ("zombie",      5, 5, 4, 5),
}

# Weights mirror the judge's order: vividness first, then funniness and
# truth, then how well the initial fits its word.
WEIGHTS = (3, 2, 2, 1)

OUTPUT_PATH = "/output/entry.txt"


def score(word_scores):
    """Weighted score of one (vivid, funny, true, fit) tuple."""
    return sum(w * s for w, s in zip(WEIGHTS, word_scores))


def pick_letter():
    """Return the letter whose day-word scores highest.

    Ties break toward the more vivid word, then the funnier one, then
    the earlier letter, so the choice is fully deterministic.
    """
    ranked = sorted(
        WORDS.items(),
        key=lambda item: (
            -score(item[1][1:]),
            -item[1][1],  # vivid
            -item[1][2],  # funny
            item[0],
        ),
    )
    return ranked[0]


def main() -> None:
    letter, (word, vivid, funny, true, fit) = pick_letter()
    assert len(letter) == 1 and "A" <= letter <= "Z", letter
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(letter)
    # Self-check the gate before the run ends: exactly one byte, A-Z.
    with open(OUTPUT_PATH, "rb") as f:
        blob = f.read()
    assert blob == letter.encode("ascii"), blob
    print(f"{letter} ({word}: vivid={vivid} funny={funny} true={true} fit={fit})")


if __name__ == "__main__":
    main()
