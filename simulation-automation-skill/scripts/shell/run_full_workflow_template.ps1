param(
  [string]$Config = "assets/examples/example_coupled_project.yaml",
  [string]$Output = "demo_project"
)

$ErrorActionPreference = "Stop"

Write-Host "Creating project structure..."
python scripts/python/create_project_structure.py --config $Config --output $Output

Write-Host "Validating config..."
python scripts/python/validate_config.py $Config

Write-Host "Run project-specific MATLAB/Fluent steps here."
Write-Host "This template intentionally does not assume licensed software availability."
