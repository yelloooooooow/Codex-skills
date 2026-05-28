from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.java_migration import extract_java_patterns, generate_mapping_markdown


class TestJavaMapping(unittest.TestCase):
    def test_mapping(self):
        report = extract_java_patterns(ROOT / "examples" / "java_to_mph_minimal_example")
        text = generate_mapping_markdown(report)
        self.assertIn("model.java", text.lower() or "java")
        self.assertIn("comp1", text)


if __name__ == "__main__":
    unittest.main()
