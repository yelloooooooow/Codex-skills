from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.config import load_config
from comsol_skill.geometry import geometry_plan
from comsol_skill.materials import material_plan
from comsol_skill.physics import physics_plan


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan or run COMSOL model build.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = load_config(args.config)
    for step in geometry_plan(config) + material_plan(config) + physics_plan(config):
        print(step)
    if not args.dry_run:
        print("Live build requires implementing version-confirmed COMSOL feature calls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
