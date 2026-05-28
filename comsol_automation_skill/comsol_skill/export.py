from __future__ import annotations

from typing import Any


def export_plan(config: dict[str, Any]) -> list[str]:
    export = config.get("export", {})
    return [f"export {key}={value}" for key, value in sorted(export.items())]


def export_results(model, config: dict[str, Any], output_dir) -> None:
    raise NotImplementedError("Implement COMSOL result export or Python postprocessing.")
