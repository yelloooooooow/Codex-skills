#!/usr/bin/env python3
"""Validate generic simulation automation YAML/JSON configs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


REQUIRED_PROJECT_FIELDS = ["project_name", "workflow_mode", "outputs"]


def load(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    if yaml is None:
        raise RuntimeError("PyYAML is required for YAML validation.")
    return yaml.safe_load(text) or {}


def validate(cfg: dict) -> list[str]:
    warnings: list[str] = []
    for field in REQUIRED_PROJECT_FIELDS:
        if field not in cfg:
            warnings.append(f"Missing recommended field: {field}")
    mode = cfg.get("workflow_mode")
    if mode and mode not in {"simulink_only", "fluent_only", "coupled", "review_only"}:
        warnings.append(f"Unknown workflow_mode: {mode}")
    paths = cfg.get("software_paths", {})
    for name, value in paths.items():
        if value and "<" not in str(value) and not Path(value).exists():
            warnings.append(f"Path does not exist for {name}: {value}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    args = parser.parse_args()
    cfg = load(args.config)
    warnings = validate(cfg)
    if warnings:
        print("Config validated with warnings:")
        for w in warnings:
            print(f"- {w}")
    else:
        print("Config validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
