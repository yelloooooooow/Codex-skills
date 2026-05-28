from __future__ import annotations

from typing import Any


def solver_plan(config: dict[str, Any]) -> list[str]:
    solver = config.get("solver", {})
    steps = [f"study type={solver.get('study_type', 'time_dependent')}"]
    if "time_dependent" in solver:
        td = solver["time_dependent"]
        steps.append(f"time range {td.get('t_start')} to {td.get('t_end')} step {td.get('output_step')} {td.get('unit', '')}")
    if "tolerances" in solver:
        steps.append(f"relative tolerance={solver['tolerances'].get('relative_tolerance', 'default')}")
    return steps


def run_solver(model, config: dict[str, Any]) -> None:
    raise NotImplementedError("Implement solver execution with version-specific COMSOL calls.")
