# Configuration Schema

Keep project data in config. Do not hard-code private paths or case-specific constants in scripts.

Top-level keys:

- `project`: name, mode, output directory.
- `comsol`: server settings, model name, model file, cleanup policy.
- `java_migration`: source directory, output directory, sanitization flags.
- `geometry`: dimension, units, primitives, operations, selections.
- `materials`: material definitions and domains.
- `parameters`: named COMSOL parameters with units.
- `variables`: derived expressions and scopes.
- `physics`: physics interfaces, sources, initial and boundary conditions.
- `mesh`: mesh mode, size, refinements, quality checks.
- `solver`: study type, time/parameter ranges, tolerances, checkpoints.
- `export`: CSV, PNG, keyframes, animation, report settings.
- `validation`: reference data and metrics.
- `privacy`: sanitization settings.
