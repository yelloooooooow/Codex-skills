from __future__ import annotations

from typing import Any


def physics_plan(config: dict[str, Any]) -> list[str]:
    physics = config.get("physics", {})
    enabled = physics.get("enabled", {})
    steps = [f"physics {name}: {'enabled' if value else 'disabled'}" for name, value in enabled.items()]
    for bc in physics.get("boundary_conditions", []):
        steps.append(f"boundary condition {bc.get('name', bc.get('type', 'bc'))}")
    return steps


def create_physics(model, config: dict[str, Any]) -> None:
    raise NotImplementedError("Implement physics features after confirming COMSOL tags and selections.")
