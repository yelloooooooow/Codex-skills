from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.config import execution_plan, load_config, project_output_dir
from comsol_skill.report import generate_markdown_report
from comsol_skill.utils import write_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Run or plan a COMSOL automation workflow.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--mode", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = load_config(args.config)
    mode = "dry-run" if args.dry_run else args.mode
    plan = execution_plan(config, mode)
    out = project_output_dir(config)
    write_json(out / "execution_plan.json", plan)
    generate_markdown_report(config, plan, out)
    print(f"workflow mode={plan['mode']}")
    print(f"wrote {out / 'execution_plan.json'}")
    if args.dry_run:
        return 0
    if plan["requires_comsol"]:
        print("COMSOL execution hooks are intentionally version-specific. Review the plan before implementing live calls.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
