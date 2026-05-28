# Solver Strategy

Use a solver sequence that matches the physics.

- Stationary: use for steady-state flow, thermal, diffusion, or initial fields.
- Time dependent: set explicit output times and tolerances.
- Parametric sweep: record parameter sets and solver reuse assumptions.
- Coupled multiphysics: solve in stages if fully coupled solve fails.

Always log study type, output times, relative tolerance, linear solver if configured, convergence status, and fallback actions.
