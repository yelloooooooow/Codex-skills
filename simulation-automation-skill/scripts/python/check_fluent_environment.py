#!/usr/bin/env python3
"""Check Python, Fluent executable, and PyFluent availability."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fluent-exe", type=Path, default=None)
    parser.add_argument("--log", type=Path, default=Path("fluent_env_check.txt"))
    args = parser.parse_args()

    lines = [f"python_executable={sys.executable}", f"python_version={sys.version.split()[0]}"]
    if args.fluent_exe:
        lines.append(f"fluent_exe={args.fluent_exe}")
        lines.append(f"fluent_exists={args.fluent_exe.exists()}")
    else:
        lines.append("fluent_exe=<not provided>")
    pyfluent = importlib.util.find_spec("ansys.fluent.core") is not None
    lines.append(f"pyfluent_importable={pyfluent}")
    if not pyfluent:
        lines.append("install_hint=pip install ansys-fluent-core")
    args.log.parent.mkdir(parents=True, exist_ok=True)
    args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
