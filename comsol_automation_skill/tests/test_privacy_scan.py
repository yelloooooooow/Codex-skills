from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.privacy import scan_text


class TestPrivacyScan(unittest.TestCase):
    def test_detects_path(self):
        findings = scan_text("path = 'C:\\\\Users\\\\Example\\\\secret.txt'", "x.txt")
        self.assertTrue(findings)

    def test_detects_assignment(self):
        findings = scan_text("server_password = 'abc'", "x.txt")
        self.assertTrue(findings)


if __name__ == "__main__":
    unittest.main()
