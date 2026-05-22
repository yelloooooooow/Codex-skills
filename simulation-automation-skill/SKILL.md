---
name: simulation-automation-skill
description: Automate engineering simulation workflows with MATLAB/Simulink, Ansys Fluent/PyFluent, or coupled Simulink-Fluent calibration. Use when users ask to build or audit Simulink simulations, run multiple cases, export Simulink screenshots, automate Fluent CFD geometry/mesh/boundaries/solver/postprocessing, compare Fluent and Simulink results, derive conservative CFD correction factors, run parameter optimization, perform techno-economic analysis, generate publication figures/videos/reports, or perform final project quality review.
---

# Simulation Automation Skill

## Responsibility

Use this skill to plan, scaffold, execute, audit, visualize, and report engineering simulation workflows that involve:

- MATLAB/Simulink system-level dynamic models;
- Ansys Fluent or PyFluent local CFD/unit models;
- coupled Simulink-Fluent comparison and calibration;
- optimization, techno-economic analysis, uncertainty/sensitivity analysis;
- publication-quality figures, videos, screenshots, reports, and final audit packages.

Treat this skill as a workflow and quality-control guide. It does not replace engineering judgment, software licensing, solver validation, or experimental verification.

## Trigger Scenarios

Use this skill when the user asks to:

- build, modify, audit, or run a Simulink simulation;
- automatically run Simulink cases or parameter sweeps;
- export Simulink top-level or subsystem screenshots;
- create a Fluent/PyFluent automation project;
- generate CFD geometry, mesh, materials, boundary conditions, solver settings, and postprocessing;
- compare Fluent outputs with Simulink outputs;
- calibrate a reduced/system model from CFD and rerun calibrated cases;
- perform parameter optimization, Pareto analysis, sensitivity analysis, or techno-economic analysis;
- generate figures, videos, model screenshots, result tables, paper assets, or final reports;
- perform a final quality review of a simulation project.

## Do Not Use

Do not use this skill to:

- claim that a local CFD model replaces a full system simulation unless the user explicitly built and validated such a model;
- silently invent missing data or present estimates as literature facts;
- overwrite baseline results during calibration or optimization;
- bypass MATLAB, Simulink, Fluent, or PyFluent license limitations;
- run destructive file operations or delete previous results without explicit user permission.

## Inputs Needed

Collect only the missing information needed for the chosen workflow:

- workflow mode: `simulink_only`, `fluent_only`, `coupled`, `optimization`, `economics`, `visualization`, or `final_audit`;
- software paths: MATLAB availability, Fluent executable, Python executable, PyFluent environment;
- model objectives, cases, stop time, solver settings, logged variables;
- geometry, materials, boundary conditions, mesh settings, and solver controls for CFD;
- comparison variables and correction-factor policy for coupled workflows;
- optimization variables, constraints, objectives, and baseline design;
- economic parameters, unit costs, lifetime, discount rate, sensitivity ranges;
- output expectations: figures, videos, screenshots, CSVs, reports, paper assets.

## Execution Steps

1. Determine workflow mode and scope.
2. Create or audit the project structure using `scripts/python/create_project_structure.py`.
3. Validate configuration with `scripts/python/validate_config.py`.
4. For Simulink work, follow `references/simulink_workflow_standard.md` and use scripts under `scripts/matlab/`.
5. For Fluent work, follow `references/fluent_workflow_standard.md` and use scripts under `scripts/python/`.
6. For coupled work, explicitly define model roles before comparing outputs. Read `references/coupled_simulation_standard.md`.
7. If calibration is requested, fit a raw factor, convert it to a conservative factor, and save calibrated results in a new folder. Read `references/calibration_standard.md`.
8. If optimization is requested, preserve baseline, classify technical/economic/balanced optima, and keep infeasible candidates traceable. Read `references/optimization_standard.md`.
9. If economics are requested, compute CAPEX, OPEX, TAC, LCOH, NPC, and sensitivity ranges. Read `references/techno_economic_standard.md`.
10. Generate figures/videos/screenshots using `references/visualization_standard.md`.
11. Generate final report assets using `references/reporting_standard.md`.
12. Record uncertainty and sensitivity assumptions using `references/uncertainty_and_sensitivity_standard.md`.
13. Finish with a pass/warning/fail checklist using `references/final_audit_standard.md`.

## Workflow A: Simulink-Only

Use for system dynamics, controls, case comparison, parameter sweeps, and reporting.

1. Create `config/`, `models/`, `scripts/`, `results/`, `figures/`, `reports/`, and `logs/`.
2. Put all parameters in one initialization script or config file.
3. Build or load the model, set solver and stop time, and define case inputs.
4. Log time, states, outputs, controls, powers, energies, and efficiencies.
5. Run cases with repeatable scripts, not manual clicks.
6. Save raw results before plotting.
7. Export top-level and subsystem screenshots.
8. Generate case plots, cross-case plots, summary tables, and model audit.

Use `scripts/matlab/create_simulink_project.m`, `run_simulink_cases.m`, `postprocess_simulink_results.m`, `compare_cases.m`, and `export_simulink_screenshots.m`.

## Workflow B: Fluent-Only

Use for local/unit CFD, geometry/mesh automation, contour/vector/animation output, and mesh sensitivity.

1. Check Python, Fluent executable, PyFluent import, and license availability.
2. Generate a Fluent project folder with `config/`, `src/`, `journals/`, `mesh/`, `outputs/`, and `logs/`.
3. Create or import geometry and named boundaries.
4. Generate or import mesh and write mesh quality metrics.
5. Set materials, models, boundary conditions, solver controls, and output intervals.
6. Save case/data files and logs.
7. Export CSV summaries, contour plots, vector plots, and animations.
8. Provide journal fallback if PyFluent fails.

Use `scripts/python/check_fluent_environment.py`, `generate_fluent_project.py`, and `postprocess_fluent_results.py`.

## Workflow C: Coupled Simulink + Fluent

Use when Simulink is the system model and Fluent is a local high-fidelity or unit model.

1. State the division of responsibility: Simulink handles full-system dynamics; Fluent handles local CFD or component physics.
2. Align geometry, material properties, boundary conditions, initial conditions, and time windows.
3. Export Simulink comparison variables to CSV.
4. Read Fluent summary CSV and interpolate both outputs to a common time axis.
5. Compare average temperatures, state variables, heat flux/heat rate, efficiency, and final states.
6. Fit raw correction factors only to model parameters, not to output curves.
7. Convert raw factors to conservative factors with reliability weighting.
8. Save calibrated configs and rerun system cases in a new output folder.
9. Compare original vs calibrated and document limitations.

Use `scripts/python/compare_simulink_fluent.py`, `scripts/matlab/export_simulink_for_cfd_comparison.m`, and `references/calibration_standard.md`.

## Optimization Workflow

Always preserve baseline. Generate:

- `baseline design`;
- `technical-optimal design`;
- `economic-optimal design`;
- `balanced-optimal design`;
- feasible and infeasible candidate tables;
- Pareto plots and constraint summaries.

Optimization must recompute economics when geometry, material, control, pump power, or capacity changes. Never call an infeasible design "optimal."

## Techno-Economic Workflow

Compute at least CAPEX, OPEX, annualized CAPEX, TAC, LCOH, NPC, and sensitivity ranges. Keep units explicit: W/kW, J/kWh, EUR/kWh, EUR/MWh, thermal/electric energy, day/year. If optional assets such as PV are debated, report both with and without their CAPEX.

## Visualization Workflow

Generate figures and videos only from saved data. Use fixed color scales for comparisons, include units in axes and colorbars, avoid overcrowded subplots, and generate figure/video explanation files for reports. Export Simulink screenshots and CFD geometry/boundary/mesh schematics.

## Final Audit Workflow

Create a final output folder instead of overwriting original results. Audit:

- project structure;
- parameter consistency and units;
- model logic and solver settings;
- case results and nonphysical values;
- optimization constraints and rankings;
- economics and sensitivity analysis;
- CFD setup and calibration conservatism;
- figure/video/report quality.

Write `final_audit_report.md` and `final_audit_checklist.csv` with `pass`, `warning`, `fail`, or `not_applicable` statuses.

## Common Failure Modes

- Missing MATLAB/Fluent/PyFluent: write clear environment logs and fallback instructions.
- License unavailable: stop the solver stage and preserve generated setup files.
- Missing source data: create a missing-data register and label estimates.
- Inconsistent units: stop or warn before simulation if units can change results.
- CFD/Simulink mismatch: compare only compatible averaged variables and document scale/boundary differences.
- Calibration too aggressive: bound the conservative factor and warn if fit quality remains poor.
- Crowded plots: split into multiple figures.
- Placeholder screenshots: generate readable supplemental schematics and report the limitation.

## Safety and Open-Source Notes

Do not hard-code private paths, license details, proprietary datasets, or personal information. Use placeholders in templates. Assume MATLAB/Simulink, Ansys Fluent, and PyFluent require user installation and licensing. All scripts must fail gracefully and write logs.

## Resource Map

- Workflow standards: `references/*.md`
- Config/report templates: `assets/templates/*.yaml` and `assets/templates/*.md`
- Reusable prompts: `assets/prompts/*.md`
- Example configs: `assets/examples/*.yaml`
- Python utilities: `scripts/python/*.py`
- MATLAB utilities: `scripts/matlab/*.m`
- Workflow launchers: `scripts/shell/*`
