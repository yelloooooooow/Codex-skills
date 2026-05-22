# Fluent Workflow Standard

## Project Structure

```text
config/
src/
journals/
mesh/generated/
outputs/case_data/
outputs/csv/
outputs/figures/
outputs/animations/
outputs/reports/
logs/
```

## Environment Check

Check:

- Python executable;
- Fluent executable;
- PyFluent import;
- Fluent launch ability;
- license availability when possible;
- writable output directories.

Write all results to a log file.

## Geometry and Mesh

- Define coordinate convention and named boundaries.
- Generate or import geometry with clear dimensions.
- Save mesh and mesh quality summary.
- Check cell count, aspect ratio, skewness, and orthogonal quality where available.
- Provide manual mesh instructions if automation fails.

## Materials and Boundary Conditions

Keep material properties in config. Mark assumptions and uncertainty. Boundary conditions must include units and reference frames.

## Solver Settings

Record:

- dimension and precision;
- steady/transient;
- physical models;
- pressure-velocity coupling;
- time step and total time;
- iterations per step;
- residual targets;
- output interval.

## Outputs

Save:

- case/data files;
- summary CSV;
- contour images;
- vector plots where relevant;
- animations;
- solver logs;
- report with assumptions and limitations.

## Journal Fallback

If PyFluent is unavailable or unstable, generate a journal file that loads mesh, sets models/materials/BCs, initializes, runs, and exports available outputs. Do not silently fail.

## Failure Handling

- Missing Fluent path: error with the checked path.
- PyFluent missing: suggest install command.
- License unavailable: preserve setup and logs.
- Mesh failure: write debug log and manual instructions.
- Solver crash: keep partial case/data/logs.
- Animation failure: keep PNG sequence.
