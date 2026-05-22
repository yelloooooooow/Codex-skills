# Simulink Workflow Standard

## Project Structure

Use a repeatable structure:

```text
config/
models/
scripts/
results/
figures/
screenshots/
reports/
logs/
```

Keep baseline, optimized, calibrated, and sensitivity outputs in separate folders.

## Parameter Initialization

- Put global constants, units, case settings, solver settings, and output names in config or one initialization script.
- Use structs or tables for grouped parameters.
- Label units in field names or comments.
- Keep literature values, assumptions, estimated values, and calibrated values separate.

## Multi-Case Simulation

- Use a case list such as `["A","B","C"]` or config-driven case names.
- Each case script must initialize parameters, load/build the model, set stop time, run simulation, save raw results, and call postprocessing.
- Do not rely on manual block changes between cases.

## Data Logging

Log at least:

- time;
- main states;
- controlled outputs;
- inputs and disturbances;
- actuator/control signals;
- powers, heat rates, and energies;
- efficiencies and COP-like metrics;
- warnings or solver status.

Use `logsout`, `SimulationOutput`, To Workspace, or a documented S-function output vector. Always save raw results before plotting.

## Model Screenshots

Export:

- top-level model;
- key subsystems;
- control logic;
- plant model;
- logging subsystem.

If automatic screenshots fail, create `manual_screenshot_instructions.md` and add readable supplemental schematics.

## Units and Solver Settings

- Make stop time and sample times explicit.
- Use SI internally unless the project has a documented alternative.
- Check W/kW, J/kWh, degC/K, Pa/bar, kg/s/L/min, and thermal/electric energy.
- Prefer stiff solvers for thermal finite-volume models when needed.

## Result Postprocessing

- Generate case figures and cross-case comparison figures.
- Include units in axes and legends.
- Save summary CSVs and MATLAB `.mat` files.
- Do not plot from overwritten workspace variables only.

## Common Error Checks

- Missing logged signals.
- Non-monotonic time.
- NaN/Inf outputs.
- Control signals outside allowed ranges.
- Nonphysical temperatures, pressures, masses, or efficiencies.
- Solver warnings ignored.
- Case scripts depending on prior workspace state.
