# Packaging Summary

## Created Files

This Skill package contains:

- `SKILL.md` with Agent-facing workflow instructions;
- `README.md`, `LICENSE`, and `skill.json`;
- workflow standards in `references/`;
- Python, MATLAB, and shell automation skeletons in `scripts/`;
- config, report, and prompt templates in `assets/`;
- lightweight tests in `tests/`;
- user-facing docs in `docs/`.

## Installation

Copy `simulation-automation-skill/` into a Codex/Agent skills folder such as:

```text
<CODEX_HOME>/skills/simulation-automation-skill
```

Reload the Agent environment.

## Usage

Ask the Agent to use this skill for Simulink automation, Fluent automation, coupled calibration, optimization, techno-economic analysis, visualization, or final audit.

## Skeleton Status

The bundled scripts are reusable scaffolds. They validate configs, create project structures, export comparison CSVs, plot generic results, and generate audit placeholders. Domain-specific physics, geometry, solver settings, and economic models must be filled in by the Agent/user for each project.

## Extension Ideas

- Add project-specific Simulink block builders.
- Add robust PyFluent meshing recipes.
- Add CFD mesh sensitivity runners.
- Add experiment-vs-simulation validation.
- Add CI jobs for template and script linting.
