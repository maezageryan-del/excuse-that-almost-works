"""The Excuse That Almost Works.

One line a gamer texts the boss to skip work during GTA 6 launch week.
Writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "Sorry, courier won't leave my launch-day delivery without a signature, stuck at home till noon."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be one line"
    assert len(text.split()) <= 20, "entry must be at most 20 words"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
