"""Two Days of Quiet Dread — make.fun entry.

Writes one code-review comment to /output/entry.txt.

The comment's angle: the reviewer does everything right — reads the code,
checks the tests — and then quietly gives up on the bigger question. The
laugh comes from the dread itself, not from a joke bolted on: competent
approval on the surface, flat existential surrender underneath. No
exclamation, no melodrama, no cry for help — just a tired engineer pasting
the comment and clicking approve.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 140
characters, not only white space, a single line.
"""

from pathlib import Path

# The entry: one line, approves the PR, carries quiet existential dread.
# 100 characters, single line, flat tone.
ENTRY = (
    "Approved. The code is clean, the tests are green, "
    "and I've stopped asking what any of it is for."
)

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the gate locally before writing anything out."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the comment, byte for byte.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
