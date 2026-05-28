# COMSOL Automation Skill

This repository contains a reusable Codex skill and lightweight Python toolkit for automating COMSOL Multiphysics workflows with Python, `mph`, COMSOL Server, optional Java history migration, reproducible exports, validation summaries, and open-source sanitization.

This repository does not include COMSOL Multiphysics, COMSOL Server, COMSOL licenses, private datasets, proprietary model files, or private Java exports. Users must install COMSOL separately and use their own valid license. All examples use generic synthetic parameters for demonstration purposes. Raw COMSOL Java exports may contain private paths and model metadata; sanitize them before sharing.

## Suitable Tasks

- Connect to COMSOL Server and list/open/create models.
- Build generic COMSOL models from config.
- Configure geometry, selections, materials, physics, mesh, studies, and solvers.
- Run dry-run plans when COMSOL is unavailable.
- Export CSV, figures, keyframes, animations, reports, and logs.
- Extract structure from sanitized COMSOL Java history code.
- Draft Java API to Python/mph migration notes.
- Perform verification, validation, calibration, sensitivity, and uncertainty analysis with clear terminology.

## Not Suitable

- Guessing a simulation without geometry, physics, material, or boundary data.
- Fabricating solver output or validation curves.
- Publishing private model files, private Java exports, absolute paths, credentials, or license data.
- Claiming validation for non-equivalent physics.

## Install

```bash
python -m pip install -r requirements.txt
```

COMSOL execution requires COMSOL Multiphysics/Server and a valid local or network license. Dry-run, privacy checks, config loading, Java pattern extraction, and report template generation do not require COMSOL.

## Common Commands

```bash
python scripts/check_environment.py
python scripts/check_privacy.py
python scripts/run_comsol_workflow.py --config examples/minimal_heat_transfer/config.yaml --dry-run
python examples/minimal_heat_transfer/run_case.py --dry-run
python examples/minimal_diffusion/run_case.py --dry-run
python examples/minimal_reaction_diffusion/run_case.py --dry-run
python examples/minimal_parametric_sweep/run_case.py --dry-run
python scripts/extract_comsol_java_patterns.py --src examples/java_to_mph_minimal_example --out artifacts/java_analysis --dry-run
python scripts/generate_java_to_mph_mapping.py --input artifacts/java_analysis/java_patterns.json --out artifacts/java_analysis
```

## COMSOL Server

Set server connection details in config:

```yaml
comsol:
  server_host: localhost
  server_port: 2036
  use_existing_server: true
  model_name: GenericModel
```

The workflow lists current server models before creating or modifying a model. Generated checkpoints use unique filenames and should not overwrite GUI-open models.

## Java History Export and Migration

From COMSOL GUI, create or open a model and export Java history code using the COMSOL-supported Java export path for your version. Treat exported Java as private until sanitized.

Recommended flow:

```bash
python scripts/check_privacy.py --path java_src
python scripts/extract_comsol_java_patterns.py --src java_src --out artifacts/java_analysis --dry-run
python scripts/generate_java_to_mph_mapping.py --input artifacts/java_analysis/java_patterns.json --out artifacts/java_analysis
```

Migration principle: `mph` can access the underlying COMSOL Java API through `model.java`, so many Java history calls can first be moved to Python with preserved tags and call order, then refactored into reusable helpers.

## Outputs

The default output root is `artifacts/<project-name>`. Typical files include:

- `execution_plan.json`
- `run_log.txt`
- generated model checkpoints when COMSOL is available
- CSV exports
- PNG figures
- `report.md`
- Java extraction reports and mapping drafts

## Adding a New Model

1. Copy an example config.
2. Update geometry primitives and selections.
3. Add parameters, variables, materials, and physics definitions.
4. Set mesh and solver strategy.
5. Run dry-run first.
6. Run the full workflow only after reviewing the plan.
7. Add validation references only when they are comparable.

## Privacy Check

Run:

```bash
python scripts/check_privacy.py
```

If sensitive patterns are reported, sanitize or move files before publishing.

## License

MIT. See `LICENSE`.
