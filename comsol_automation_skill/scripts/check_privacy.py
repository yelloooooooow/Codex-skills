from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.privacy import scan_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan files for sensitive paths, credentials, and private identifiers.")
    parser.add_argument("--path", default=str(ROOT), help="Path to scan.")
    args = parser.parse_args()
    findings = scan_path(args.path)
    if not findings:
        print("PASS: no sensitive patterns found")
        return 0
    for finding in findings:
        print(f"{finding['file']}:{finding['line']} pattern={finding['pattern']} snippet={finding['snippet']}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
