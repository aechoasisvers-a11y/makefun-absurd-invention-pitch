"""One-Sentence Absurd Invention Pitch -- make.fun entry.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure stdlib Python, deterministic output.
"""

import os

ENTRY = (
    "The NagPlant is a houseplant that texts your landlord every time "
    "you forget to water it, so your neglect finally gets a witness "
    "and a paper trail."
)

MAX_CHARS = 220


def main():
    # Self-check: the entry must sit inside the kit's gate (1-220 chars,
    # not only whitespace) and be exactly one sentence.
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry is blank"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), (
        "entry must be exactly one sentence"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip check: what landed on disk must match the intended text
    # byte for byte (no trailing newline, no encoding surprise).
    with open(path, "rb") as f:
        assert f.read() == ENTRY.encode("utf-8"), "written file mismatch"


if __name__ == "__main__":
    main()
