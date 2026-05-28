# Workflow Standards

Use a staged workflow:

1. Ingest the task and classify the workflow mode.
2. Load configuration and validate required fields.
3. Run environment and privacy checks.
4. Connect to COMSOL Server only when execution requires it.
5. Build parameters, geometry, selections, materials, physics, mesh, studies, solvers, and result nodes.
6. Save checkpoints before and after risky operations.
7. Export CSV data before figures.
8. Generate reports from saved data and logs.
9. Finish with a concise status table.

All steps must be repeatable from config and logs. Do not encode conclusions directly into exports.
