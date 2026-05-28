from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.java_migration import extract_java_patterns, write_java_reports


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract COMSOL Java API patterns from sanitized Java files.")
    parser.add_argument("--src", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    report = extract_java_patterns(args.src)
    paths = write_java_reports(report, args.out)
    print(f"scanned_files={len(report['files'])}")
    print(f"tags={len(report['tags'])}")
    print(f"properties={len(report['properties'])}")
    for key, path in paths.items():
        print(f"{key}: {path}")
    if report["sensitive_findings"]:
        print("WARNING: sensitive findings detected; do not publish raw Java.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
