from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_config(path: str | Path) -> dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    try:
        import yaml

        data = yaml.safe_load(text)
        return data or {}
    except Exception:
        return json.loads(text)


def project_output_dir(config: dict[str, Any]) -> Path:
    project = config.get("project", {})
    return Path(project.get("output_dir", "artifacts/generic_simulation"))


def workflow_mode(config: dict[str, Any], override: str | None = None) -> str:
    if override:
        return override
    return config.get("project", {}).get("mode", "dry-run")


def execution_plan(config: dict[str, Any], mode: str | None = None) -> dict[str, Any]:
    selected_mode = workflow_mode(config, mode)
    return {
        "mode": selected_mode,
        "project": config.get("project", {}),
        "requires_comsol": selected_mode not in {"dry-run", "java-to-mph-analysis", "postprocess-only"},
        "steps": [
            "load_config",
            "check_environment",
            "check_privacy",
            "connect_server" if selected_mode not in {"dry-run", "postprocess-only"} else "skip_server_connection",
            "build_model" if selected_mode in {"build-only", "full-workflow"} else "skip_build",
            "run_solver" if selected_mode in {"solve-only", "full-workflow"} else "skip_solver",
            "postprocess" if selected_mode in {"postprocess-only", "full-workflow"} else "skip_postprocess",
            "generate_report",
        ],
    }
