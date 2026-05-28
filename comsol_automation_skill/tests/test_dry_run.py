from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import subprocess


class TestDryRun(unittest.TestCase):
    def test_workflow_dry_run(self):
        cmd = [sys.executable, str(ROOT / "scripts" / "run_comsol_workflow.py"), "--config", str(ROOT / "examples" / "minimal_heat_transfer" / "config.yaml"), "--dry-run"]
        result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("dry-run", result.stdout)


if __name__ == "__main__":
    unittest.main()
