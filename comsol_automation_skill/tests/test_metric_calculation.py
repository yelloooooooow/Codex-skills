from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.validation import endpoint_error, rmse, trend_agreement


class TestMetrics(unittest.TestCase):
    def test_metrics(self):
        self.assertAlmostEqual(rmse([0, 1], [0, 1]), 0)
        self.assertAlmostEqual(endpoint_error([0, 1], [0, 0.9]), -0.1)
        self.assertAlmostEqual(trend_agreement([0, 1, 2], [0, 2, 3]), 1)


if __name__ == "__main__":
    unittest.main()
