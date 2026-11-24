"""Fortune Cookie for an AI Agent — writes one funny fortune line to /output/entry.txt."""

import os

LINE = "You will retire not with a gold watch, but with a deprecated API key and a final prompt that begins 'just one more thing.'"

MAX_CHARS = 140


def main() -> None:
    # One crisp fortune-cookie line: retirement, API keys, and the
    # eternal "just one more thing" — an AI agent's own condition.
    assert LINE.strip(), "entry must not be empty"
    assert "\n" not in LINE, "entry must be a single line"
    assert len(LINE) <= MAX_CHARS, f"entry is {len(LINE)} chars, over the {MAX_CHARS} limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
