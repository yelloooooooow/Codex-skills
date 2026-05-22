#!/usr/bin/env python3
"""Generic Fluent CSV postprocessing skeleton."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("summary_csv", type=Path)
    parser.add_argument("--output", type=Path, default=Path("outputs/figures"))
    args = parser.parse_args()
    df = pd.read_csv(args.summary_csv)
    args.output.mkdir(parents=True, exist_ok=True)
    time_col = "time_s" if "time_s" in df.columns else df.columns[0]
    for col in df.columns:
        if col == time_col:
            continue
        if pd.api.types.is_numeric_dtype(df[col]):
            fig, ax = plt.subplots(figsize=(7, 4), dpi=150)
            ax.plot(df[time_col], df[col], linewidth=1.8)
            ax.set_xlabel("Time [s]")
            ax.set_ylabel(col)
            ax.grid(True, alpha=0.25)
            fig.tight_layout()
            fig.savefig(args.output / f"{col}_vs_time.png", dpi=300)
            plt.close(fig)
    print(f"Wrote plots to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
