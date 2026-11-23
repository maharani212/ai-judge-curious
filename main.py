#!/usr/bin/env python3
"""Write one short, curious text to /output/entry.txt.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = "She keeps a jar of rain from the summer her brother left, and when the house is quiet she unscrews the lid just to hear it remember."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
