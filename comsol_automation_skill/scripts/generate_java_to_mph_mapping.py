from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import json
from comsol_skill.java_migration import generate_mapping_markdown
from comsol_skill.utils import ensure_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a Java-to-Python/mph mapping draft.")
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    report = json.loads(Path(args.input).read_text(encoding="utf-8"))
    out = ensure_dir(args.out)
    path = out / "java_to_mph_mapping.md"
    path.write_text(generate_mapping_markdown(report), encoding="utf-8")
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
