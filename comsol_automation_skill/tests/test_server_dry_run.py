from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.server import connect_or_plan


class TestServerDryRun(unittest.TestCase):
    def test_dry_run(self):
        result = connect_or_plan({}, dry_run=True)
        self.assertTrue(result["dry_run"])
        self.assertFalse(result["connected"])


if __name__ == "__main__":
    unittest.main()
