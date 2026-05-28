---
name: comsol-automation
description: Automate COMSOL Multiphysics engineering workflows with Python/mph and COMSOL Server. Use when Codex needs to connect to COMSOL Server, create or modify COMSOL models, translate COMSOL Java history code to Python/mph, configure geometry/materials/physics/mesh/solver, run stationary or time-dependent studies, export CSV/PNG/keyframes/animations, compare against reference data, generate reports, run dry-run plans without COMSOL, or sanitize COMSOL artifacts for open-source release.
---

# COMSOL Automation

Use this skill to run a standard, reproducible COMSOL automation workflow. Keep the work generic, configurable, and auditable. Never hard-code private paths, credentials, project-specific literature parameters, or unverifiable results.

## Core Workflow

1. Read the user goal and classify the requested mode: `connect-only`, `build-only`, `solve-only`, `postprocess-only`, `java-to-mph-analysis`, `full-workflow`, or `dry-run`.
2. Load a config file when available. If no config exists, create a minimal config draft and ask only for missing geometry, physics, material, boundary, initial, solver, or output definitions that are required for a meaningful run.
3. Run `scripts/check_environment.py` and `scripts/check_privacy.py` before open-source handoff.
4. Connect to COMSOL only when execution requires it. Keep dry-run paths fully usable without COMSOL.
5. Build the model in phases: parameters, geometry, selections, materials, physics, mesh, study, solver, results.
6. Log every major step, caught error, fallback, solver status, and exported artifact.
7. Export reproducible data first, then figures and optional reports. Do not fabricate field plots, curves, or validation numbers.
8. Distinguish verification, validation, calibration, sensitivity analysis, and uncertainty analysis in all reports.

## Inputs

Require enough information to define:

- Geometry dimension and primitives, imported geometry, or Java history source.
- Materials, parameters, variables, functions, and units.
- Physics interfaces, domains, boundaries, initial values, source terms, and couplings.
- Mesh strategy and refinement regions.
- Study type, solver tolerances, time range, and parameter sweeps.
- Exports, validation references, and reporting expectations.

Store these in YAML/JSON-like config files instead of scattering constants through scripts.

## COMSOL Server

Follow `references/server_connection_guidelines.md`.

- Prefer an existing server/session when the user has one open.
- List current models before creating or modifying a model.
- Do not overwrite user `.mph` files or GUI-open model files.
- Save generated checkpoints under configured output directories with unique names.
- If connection fails, write dry-run instructions and continue with script/report generation when possible.

## Java History to Python/mph

Follow `references/java_to_mph_translation_guidelines.md`.

1. Search for `.java`, `ModelUtil`, `model.component(`, `model.physics(`, `model.study(`, `model.sol(`, and `model.result(`.
2. Run `scripts/check_privacy.py` before analyzing Java exports.
3. Run `scripts/extract_comsol_java_patterns.py --src <src> --out <out> --dry-run` to summarize tags, features, property keys, and sensitive snippets.
4. Run `scripts/generate_java_to_mph_mapping.py --input <out>/java_patterns.json --out <out>` to draft a migration map.
5. Translate by preserving COMSOL tags and call order through `model.java`, then wrap stable patterns in Python helpers.
6. Do not copy raw private Java exports into examples or references.

## Modeling Standards

- Define stable named selections for domains and boundaries; avoid relying on random entity IDs in later steps.
- Keep solid state variables, gas species, fields, probes, and derived quantities semantically separate.
- Preserve COMSOL unit expressions as strings where practical.
- Create geometry features, set properties, run geometry, then create selections and mesh.
- Bind physics to explicit domains and boundaries.
- Add mesh refinement near high gradients, reaction fronts, wall layers, interfaces, or stress concentrations.
- Start with a stable coarse/finer model before increasing mesh density.
- Use solver tolerances that are stated in logs and reports.

## Exports and Reports

Always prefer machine-readable outputs:

- `run_log.txt`
- model checkpoints
- CSV tables
- field snapshots
- derived metrics
- keyframes/animations when requested
- `report.md` or optional Word report

Figures should include units, legends, reference points when applicable, and captions that do not overclaim validation.

## Verification Terms

- Verification: equations, units, numerics, scripts, and implementation are set up correctly.
- Validation: comparable model results agree with comparable reference data.
- Calibration: model parameters are adjusted using reference data.
- Sensitivity analysis: outputs are tested under parameter changes.
- Uncertainty analysis: gaps, assumptions, and non-equivalence are documented.

Only claim validation when geometry, physics, inputs, and outputs are comparable. Otherwise write qualitative comparison, sanity check, or uncertainty analysis.

## Safety and Privacy

- Never include credentials, server passwords, license details, raw private Java exports, absolute user paths, personal identifiers, private datasets, unpublished model metadata, or current-project-specific literature reproduction parameters.
- Sanitize paths and metadata before sharing.
- Keep `.mph`, `.docx`, `.pdf`, raw Java exports, logs, videos, and generated artifacts out of source control unless explicitly sanitized.
- If privacy checks fail, report findings and stop before publishing.

## Finish Checklist

- Config loads or a config draft is created.
- Dry-run works without COMSOL.
- Server connection logic lists models before mutation.
- Model build scripts use named selections and staged error handling.
- Solver status and fallback decisions are logged.
- CSV and figure exports are reproducible from saved data.
- Reports separate assumptions from paper/reference/original parameters.
- Java migration artifacts are sanitized toy examples or generated summaries, not raw private exports.
- `scripts/check_privacy.py` passes before open-source handoff.
