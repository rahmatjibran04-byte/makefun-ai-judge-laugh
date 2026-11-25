"""Write one office-life joke to /output/entry.txt.

Entry for make.fun bounty "Make the AI Judge Laugh"
(u-alfasurya91-make-the-ai-judge-laugh-6ed40225): a single line about
office life, at most 200 characters, judged head-to-head by an AI judge
on truth of observation, surprising turn, tightness and freshness.

Run: python3 main.py
"""

import os

JOKE = (
    "I blocked two hours for focus time, and three coworkers booked "
    "a meeting inside it to ask why I wasn't replying."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def validate_joke(joke: str) -> str:
    """Enforce the bounty rules; raise ValueError on any violation.

    Asserts disappear under ``python -O``, so the gate must not rely on
    them. A bad joke must fail loudly instead of writing an invalid entry.
    """
    if not isinstance(joke, str):
        raise ValueError("joke must be a string")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line (no newline characters)")
    if not joke.strip():
        raise ValueError("joke must not be blank or only whitespace")
    if joke != joke.strip():
        raise ValueError("joke must not have leading or trailing whitespace")
    if len(joke) > MAX_CHARS:
        raise ValueError(
            f"joke is {len(joke)} characters, over the {MAX_CHARS} limit"
        )
    joke.encode("utf-8")  # raises UnicodeEncodeError on non-UTF-8 text
    return joke


def main() -> None:
    joke = validate_joke(JOKE)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)
    # Permissions on the file only; never chmod a directory.
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(joke)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
