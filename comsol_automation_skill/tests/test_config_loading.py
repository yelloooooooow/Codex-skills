from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.config import execution_plan, load_config


class TestConfigLoading(unittest.TestCase):
    def test_load_example(self):
        cfg = load_config(ROOT / "examples" / "minimal_heat_transfer" / "config.yaml")
        self.assertEqual(cfg["project"]["name"], "minimal_heat_transfer")
        self.assertIn("steps", execution_plan(cfg, "dry-run"))


if __name__ == "__main__":
    unittest.main()
