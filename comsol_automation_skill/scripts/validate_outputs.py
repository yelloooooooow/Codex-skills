from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from comsol_skill.validation import endpoint_error, nrmse, rmse, trend_agreement


def main() -> int:
    y_true = [0.0, 0.5, 1.0]
    y_pred = [0.0, 0.45, 0.95]
    print(f"RMSE={rmse(y_true, y_pred):.6g}")
    print(f"NRMSE={nrmse(y_true, y_pred):.6g}")
    print(f"endpoint_error={endpoint_error(y_true, y_pred):.6g}")
    print(f"trend_agreement={trend_agreement(y_true, y_pred):.6g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
