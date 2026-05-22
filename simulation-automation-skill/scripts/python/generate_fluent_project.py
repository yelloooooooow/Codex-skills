#!/usr/bin/env python3
"""Generate a Fluent automation project scaffold with PyFluent and journal fallback."""
from __future__ import annotations

import argparse
from pathlib import Path


PYFLUENT_STUB = '''"""Project-specific PyFluent runner stub."""
from pathlib import Path

def main():
    print("Fill in geometry, mesh, setup, solve, and export steps for this project.")
    print("Keep journal fallback in journals/fallback.jou.")

if __name__ == "__main__":
    main()
'''

JOURNAL_STUB = """/file/set-tui-version "24.1"
; TODO: read mesh, set models/materials/BCs, initialize, run, write case/data
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    for rel in ["config", "src", "journals", "mesh/generated", "outputs/case_data", "outputs/csv", "outputs/figures", "outputs/animations", "outputs/reports", "logs"]:
        (args.output / rel).mkdir(parents=True, exist_ok=True)
    (args.output / "src" / "run_fluent_case.py").write_text(PYFLUENT_STUB, encoding="utf-8")
    (args.output / "journals" / "fallback.jou").write_text(JOURNAL_STUB, encoding="utf-8")
    print(f"Generated Fluent scaffold at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
