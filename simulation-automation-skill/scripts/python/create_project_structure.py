#!/usr/bin/env python3
"""Create a generic engineering simulation project structure."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


MODES = {
    "simulink_only": ["config", "models", "scripts/matlab", "results", "figures", "screenshots", "reports", "logs"],
    "fluent_only": ["config", "src", "journals", "mesh/generated", "outputs/case_data", "outputs/csv", "outputs/figures", "outputs/animations", "outputs/reports", "logs"],
    "coupled": ["config", "simulink", "fluent", "results", "results_calibrated", "comparison", "figures", "videos", "reports", "audit", "logs"],
    "review_only": ["audit", "figures", "videos", "screenshots", "reports", "paper_assets", "logs"],
}


def read_config(path: Path) -> dict:
    if not path:
        return {}
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    if yaml is None:
        raise RuntimeError("PyYAML is required to read YAML configs. Install with: pip install pyyaml")
    return yaml.safe_load(text) or {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--mode", choices=sorted(MODES), default=None)
    args = parser.parse_args()

    cfg = read_config(args.config) if args.config else {}
    mode = args.mode or cfg.get("workflow_mode", "coupled")
    if mode not in MODES:
        raise SystemExit(f"Unsupported workflow_mode '{mode}'. Use one of {sorted(MODES)}")

    args.output.mkdir(parents=True, exist_ok=True)
    for rel in MODES[mode]:
        (args.output / rel).mkdir(parents=True, exist_ok=True)

    manifest = {
        "project_name": cfg.get("project_name", args.output.name),
        "workflow_mode": mode,
        "created_folders": MODES[mode],
    }
    (args.output / "project_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Created {mode} project at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
