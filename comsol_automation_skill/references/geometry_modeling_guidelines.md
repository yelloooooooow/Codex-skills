# Geometry Modeling Guidelines

Create geometry from config with stable tags. Use units explicitly.

Steps:

1. Create component and geometry sequence.
2. Add primitives or import geometry.
3. Apply boolean operations only as needed.
4. Build geometry.
5. Create explicit named selections for domains and boundaries.
6. Print entity counts and selection membership.
7. Export a geometry preview.

Avoid binding later physics to incidental boundary IDs unless those IDs are derived and logged through named selections.
