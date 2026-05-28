from __future__ import annotations

from typing import Any


def mesh_plan(config: dict[str, Any]) -> list[str]:
    mesh = config.get("mesh", {})
    return [
        f"mesh mode={mesh.get('mode', 'physics_controlled')}",
        f"mesh size={mesh.get('size', 'normal')}",
        f"refinement enabled={mesh.get('refinement', {}).get('enabled', False)}",
    ]


def create_mesh(model, config: dict[str, Any]) -> None:
    raise NotImplementedError("Implement mesh creation for the target COMSOL model.")
