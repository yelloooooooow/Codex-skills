from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.java_migration import extract_java_patterns


class TestJavaPatternExtraction(unittest.TestCase):
    def test_extracts_toy(self):
        report = extract_java_patterns(ROOT / "examples" / "java_to_mph_minimal_example")
        self.assertIn("comp1", report["tags"])
        self.assertIn("r1", report["tags"])
        self.assertIn("size", report["properties"])


if __name__ == "__main__":
    unittest.main()
