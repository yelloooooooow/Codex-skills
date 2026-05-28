from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import importlib.util
import platform


def main() -> int:
    print(f"Python: {platform.python_version()}")
    print(f"Platform: {platform.platform()}")
    for package in ["mph", "yaml", "matplotlib", "imageio"]:
        spec = importlib.util.find_spec(package)
        print(f"{package}: {'OK' if spec else 'missing'}")
    print("COMSOL executable detection is environment-specific; configure COMSOL Server separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
