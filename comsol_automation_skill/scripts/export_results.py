from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.config import load_config, project_output_dir
from comsol_skill.utils import write_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Export result manifest placeholder for dry-run workflows.")
    parser.add_argument("--config", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    config = load_config(args.config)
    out = project_output_dir(config)
    manifest = {"csv": config.get("export", {}).get("csv", True), "png": config.get("export", {}).get("png", True)}
    write_json(out / "export_manifest.json", manifest)
    print(f"wrote {out / 'export_manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
