from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.config import load_config
from comsol_skill.solver import solver_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan or run COMSOL solver.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = load_config(args.config)
    for step in solver_plan(config):
        print(step)
    if not args.dry_run:
        print("Live solver execution requires a COMSOL model object.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
