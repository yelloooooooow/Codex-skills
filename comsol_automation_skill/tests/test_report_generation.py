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
from comsol_skill.report import generate_markdown_report


class TestReportGeneration(unittest.TestCase):
    def test_report(self):
        cfg = load_config(ROOT / "examples" / "minimal_heat_transfer" / "config.yaml")
        with tempfile.TemporaryDirectory() as tmp:
            path = generate_markdown_report(cfg, execution_plan(cfg, "dry-run"), tmp)
            self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
