# Simulation Automation Skill

Reusable Agent Skill for engineering simulation workflows involving MATLAB/Simulink, Ansys Fluent/PyFluent, coupled calibration, optimization, techno-economic analysis, visualization, and final reporting.

This repository is a Skill folder that can be copied into a Codex/Agent skills directory. It provides procedural standards, reusable script skeletons, configuration templates, prompt templates, and lightweight tests.

## Supported Workflows

- **Simulink-only**: system-level dynamic models, controls, multiple cases, parameter sweeps, screenshots, plots, and reports.
- **Fluent-only**: local CFD or unit models, geometry/mesh/boundary/solver automation, Fluent journal fallback, contours, vectors, animations, and summary CSVs.
- **Coupled Simulink + Fluent**: system model plus local CFD, output comparison, conservative parameter correction, calibrated reruns, and original-vs-calibrated reports.
- **Review and visualization only**: audit existing results, improve figures/videos, export model screenshots, and prepare paper/report assets.

## Installation

Copy the folder into a skills directory, for example:

```text
<CODEX_HOME>/skills/simulation-automation-skill
```

Then restart or reload the Agent environment so the skill metadata is discovered.

## Requirements

This skill does **not** include MATLAB, Simulink, Ansys Fluent, or any commercial license. Users must install and license required software themselves.

Optional Python packages:

```bash
pip install pyyaml pandas numpy matplotlib scipy
pip install ansys-fluent-core
```

PyFluent is optional. If unavailable, Fluent workflows should generate a journal fallback.

## Folder Structure

- `SKILL.md`: Agent-facing execution instructions.
- `references/`: detailed standards for each workflow.
- `scripts/python/`: reusable Python skeleton utilities.
- `scripts/matlab/`: MATLAB/Simulink automation skeletons.
- `scripts/shell/`: workflow launcher templates.
- `assets/templates/`: YAML and Markdown templates.
- `assets/prompts/`: reusable prompt patterns.
- `assets/examples/`: example project configs.
- `tests/`: lightweight tests that do not require MATLAB or Fluent.
- `docs/`: user documentation.

## Quick Start

Create a project skeleton:

```bash
python scripts/python/create_project_structure.py --config assets/examples/example_coupled_project.yaml --output demo_project
```

Validate a config:

```bash
python scripts/python/validate_config.py assets/templates/project_config_template.yaml
```

Run tests:

```bash
python -m pytest tests
```

## Simulink-Only Example

Use `assets/prompts/simulink_only_prompt.md` and `assets/templates/simulink_config_template.yaml`. The Agent should create parameter scripts, case scripts, logging, postprocessing, screenshots, and an audit checklist.

## Fluent-Only Example

Use `assets/prompts/fluent_only_prompt.md` and `assets/templates/fluent_config_template.yaml`. The Agent should check the environment, create geometry/mesh setup, configure Fluent or journal fallback, export CSVs and plots, and write logs.

## Coupled Example

Use `assets/prompts/coupled_simulink_fluent_prompt.md` and `assets/templates/coupled_calibration_config_template.yaml`. The Agent should compare aligned outputs, fit a raw correction, derive a conservative correction, rerun system cases, and write original-vs-calibrated results.

## Output Files

Projects created with this skill should use explicit output folders for `results`, `figures`, `videos`, `screenshots`, `reports`, `logs`, and `audit`. Baseline results must not be overwritten by optimized or calibrated variants.

## Common Questions

- **Does this run without MATLAB or Fluent?** The scaffolding and tests do. Actual simulation requires user-installed software.
- **Can this replace engineering validation?** No. It organizes workflows and checks consistency, but users must validate models.
- **What happens if PyFluent fails?** Use journal fallback and preserve logs.

## License

MIT. See `LICENSE`.
