# Physics Modeling Guidelines

Separate physical meanings:

- Transported species are not automatically solid state variables.
- Source terms must have consistent units.
- Boundary conditions should be scoped to named selections.
- Coupled variables should be declared once and reused.
- If COMSOL units fail, simplify with normalized states and document the simplification.

Common interfaces include Heat Transfer, Transport of Diluted Species, Transport in Porous Media, Laminar Flow, Brinkman, Darcy, Domain ODEs, Coefficient Form PDE, and General Form PDE. Confirm feature names in the target COMSOL version.
