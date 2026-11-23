"""One line that makes the AI judge laugh: an office joke.

Writes one joke to /output/entry.txt: unlimited PTO, taken at face
value, with the punchline landing where the reader does not expect it
-- the job got promoted, and the person who took the leave came back
as its assistant. Every clause is true about office life: "unlimited
PTO" is a real policy, and the unspoken rule is that nobody dares use
it for fear of exactly this.
"""

from pathlib import Path

TEXT = (
    "We get unlimited PTO, so I took a month off \u2014 my job got "
    "promoted while I was gone and I came back as its assistant."
)


# The competition accepts texts of 1 to 199 characters.
MIN_CHARS = 1
MAX_CHARS = 199


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
