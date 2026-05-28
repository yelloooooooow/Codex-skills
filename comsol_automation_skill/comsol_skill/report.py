from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import ensure_dir


def generate_markdown_report(config: dict[str, Any], plan: dict[str, Any], output_dir: str | Path) -> Path:
    out = ensure_dir(output_dir)
    path = out / "report.md"
    project = config.get("project", {})
    lines = [
        f"# {project.get('name', 'Generic COMSOL Simulation')} Report",
        "",
        "## Objective",
        project.get("description", "Generic COMSOL automation workflow."),
        "",
        "## Execution Plan",
        "",
    ]
    lines.extend(f"- {step}" for step in plan.get("steps", []))
    lines.extend(
        [
            "",
            "## Verification and Validation",
            "",
            "This dry-run report does not claim validation. Use comparable reference data before validation claims.",
            "",
            "## Assumptions and Limitations",
            "",
            "- COMSOL execution is not performed in dry-run mode.",
            "- Version-specific COMSOL feature tags must be confirmed in the target installation.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
