from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> int:
    print("This skill does not batch-delete artifacts. Remove explicit files manually when needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
