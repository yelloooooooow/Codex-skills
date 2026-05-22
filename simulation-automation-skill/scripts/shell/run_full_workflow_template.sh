#!/usr/bin/env bash
set -euo pipefail

CONFIG="${1:-assets/examples/example_coupled_project.yaml}"
OUTPUT="${2:-demo_project}"

echo "Creating project structure..."
python3 scripts/python/create_project_structure.py --config "$CONFIG" --output "$OUTPUT"

echo "Validating config..."
python3 scripts/python/validate_config.py "$CONFIG"

echo "Run project-specific MATLAB/Fluent steps here."
echo "This template intentionally does not assume licensed software availability."
