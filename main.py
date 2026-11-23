"""Dad Joke Showdown entry: write exactly one dad joke to /output/entry.txt.

Standard library only.
"""

import os

JOKE = (
    "Dad said he was writing a novel about our barbecue, but he quit after "
    "chapter one — the plot was too thin, the characters were half-baked, "
    "and the ending just wasn't well done."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
