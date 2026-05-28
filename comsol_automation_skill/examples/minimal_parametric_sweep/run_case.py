from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    config = Path(__file__).resolve().with_name("config.yaml")
    cmd = [sys.executable, str(root / "scripts" / "run_comsol_workflow.py"), "--config", str(config)]
    if args.dry_run:
        cmd.append("--dry-run")
    return subprocess.call(cmd, cwd=root)


if __name__ == "__main__":
    raise SystemExit(main())
