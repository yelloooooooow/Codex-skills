from __future__ import annotations

from typing import Any


def material_plan(config: dict[str, Any]) -> list[str]:
    return [f"material {m.get('name', m.get('tag', 'material'))}" for m in config.get("materials", [])]


def create_materials(model, config: dict[str, Any]) -> None:
    raise NotImplementedError("Implement material assignment for the selected COMSOL version.")
