from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.config import execution_plan, load_config, project_output_dir
from comsol_skill.report import generate_markdown_report


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a markdown report from config and execution plan.")
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = load_config(args.config)
    path = generate_markdown_report(config, execution_plan(config), project_output_dir(config))
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
