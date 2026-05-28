from __future__ import annotations

from typing import Any


def geometry_plan(config: dict[str, Any]) -> list[str]:
    geometry = config.get("geometry", {})
    steps = [f"create geometry dimension={geometry.get('dimension', 'unknown')} unit={geometry.get('length_unit', 'm')}"]
    for primitive in geometry.get("primitives", []):
        steps.append(f"create primitive {primitive.get('tag')} type={primitive.get('type')}")
    for operation in geometry.get("operations", []):
        steps.append(f"apply operation {operation.get('tag', operation.get('type', 'operation'))}")
    for name in geometry.get("selections", {}):
        steps.append(f"create selection {name}")
    return steps


def create_geometry(model, config: dict[str, Any]) -> None:
    raise NotImplementedError("Implement COMSOL-version-specific geometry creation here.")
