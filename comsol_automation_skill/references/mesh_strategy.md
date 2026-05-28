# Mesh Strategy

Start stable, then refine:

1. Use physics-controlled mesh or a simple user-controlled mesh for the first run.
2. Add local refinement near gradients, interfaces, reaction fronts, walls, and probes.
3. Add boundary layer mesh only after basic mesh generation succeeds.
4. Export mesh statistics and a mesh preview.
5. Run mesh independence only after the base model solves.

Report mesh size, local refinement, element type, and quality checks.
