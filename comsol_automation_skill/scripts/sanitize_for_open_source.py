from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import re


def sanitize_text(text: str) -> str:
    replacements = [
        (r"C:\\Users\\[^\\\s]+", "<USER_HOME>"),
        (r"/home/[^/\s]+", "<USER_HOME>"),
        (r"/Users/[^/\s]+", "<USER_HOME>"),
        (r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "<EMAIL>"),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Create sanitized copies of text files.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source = Path(args.input)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(sanitize_text(source.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
