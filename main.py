"""Write one original office joke to /output/entry.txt.

Reads no input, uses no network, and is fully deterministic.
"""

import os
import sys
from pathlib import Path


# One line, one setup, the payoff lands in the last few words.
JOKE = (
    "The printer jammed on page one of my resignation letter, which felt "
    "less like a malfunction and more like HR's final retention strategy."
)


def build_entry() -> str:
    """Return the joke as a single line, no trailing newline."""
    return JOKE.strip()


def validate(text: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, a single non-blank line."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-blank with no leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 limit")


def output_dir() -> Path:
    """Resolve the output directory, honouring the make.fun env vars."""
    if os.environ.get("MAKEFUN_OUTPUT_DIR"):
        return Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    if os.environ.get("MAKEFUN_BOT_DIR"):
        return Path(os.environ["MAKEFUN_BOT_DIR"]) / "output"
    return Path("/output")


def main() -> int:
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    text = build_entry()
    validate(text)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
