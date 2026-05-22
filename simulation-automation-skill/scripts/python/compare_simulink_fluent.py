#!/usr/bin/env python3
"""Compare Simulink and Fluent CSV outputs on a common time axis."""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def nrmse(a: np.ndarray, b: np.ndarray) -> float:
    rmse = float(np.sqrt(np.mean((a - b) ** 2)))
    denom = float(np.nanmax(b) - np.nanmin(b))
    return rmse / denom if denom > 0 else rmse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulink", type=Path, required=True)
    parser.add_argument("--fluent", type=Path, required=True)
    parser.add_argument("--variables", nargs="+", required=True)
    parser.add_argument("--output", type=Path, default=Path("comparison"))
    args = parser.parse_args()
    sim = pd.read_csv(args.simulink)
    cfd = pd.read_csv(args.fluent)
    args.output.mkdir(parents=True, exist_ok=True)
    t0 = max(sim["time_s"].min(), cfd["time_s"].min())
    t1 = min(sim["time_s"].max(), cfd["time_s"].max())
    t = np.linspace(t0, t1, 300)
    rows = []
    for var in args.variables:
        if var not in sim.columns or var not in cfd.columns:
            rows.append({"variable": var, "status": "missing", "nrmse": np.nan})
            continue
        ys = np.interp(t, sim["time_s"], sim[var])
        yc = np.interp(t, cfd["time_s"], cfd[var])
        rows.append({"variable": var, "status": "ok", "nrmse": nrmse(ys, yc), "rmse": float(np.sqrt(np.mean((ys-yc)**2)))})
    pd.DataFrame(rows).to_csv(args.output / "simulink_fluent_error_metrics.csv", index=False)
    print(f"Wrote comparison metrics to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
