"""The 3 AM Commit Message — make.fun bounty entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after it broke
production at 3 AM.
"""

import os

LINE = "fix: the 3 AM deploy is reverted; the database is back, my deploy privileges are not"


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
