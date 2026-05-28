from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.config import load_config
from comsol_skill.physics import physics_plan


class TestPhysicsConfig(unittest.TestCase):
    def test_plan(self):
        cfg = load_config(ROOT / "examples" / "minimal_reaction_diffusion" / "config.yaml")
        self.assertTrue(any("domain_odes" in step for step in physics_plan(cfg)))


if __name__ == "__main__":
    unittest.main()
