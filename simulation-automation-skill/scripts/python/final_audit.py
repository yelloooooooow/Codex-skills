#!/usr/bin/env python3
"""Generate a lightweight final audit checklist for a simulation project."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path


CHECKS = {
    "results": "Raw or processed results folder exists",
    "figures": "Figure folder exists",
    "reports": "Reports folder exists",
    "logs": "Logs folder exists",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("audit"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    rows = []
    for folder, detail in CHECKS.items():
        exists = (args.project / folder).exists()
        rows.append({"item": folder, "status": "pass" if exists else "warning", "details": detail, "fixed": False, "output_file": "", "notes": ""})
    with (args.output / "final_audit_checklist.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    (args.output / "final_audit_report.md").write_text("# Final Audit Report\n\nSee `final_audit_checklist.csv`.\n", encoding="utf-8")
    print(f"Wrote audit to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
