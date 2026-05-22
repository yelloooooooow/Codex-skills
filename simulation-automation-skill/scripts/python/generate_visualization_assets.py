#!/usr/bin/env python3
"""Create generic figure/video explanation markdown files."""
from __future__ import annotations

import argparse
from pathlib import Path


def list_files(folder: Path, exts: tuple[str, ...]) -> list[Path]:
    files: list[Path] = []
    for ext in exts:
        files.extend(folder.rglob(f"*{ext}"))
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("paper_assets"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    figs = list_files(args.project, (".png", ".pdf", ".svg"))
    vids = list_files(args.project, (".mp4", ".gif"))
    (args.output / "figure_explanations.md").write_text("# Figure Explanations\n\n" + "\n".join(f"- `{p}`: describe axes, units, key observation, and limitation." for p in figs), encoding="utf-8")
    (args.output / "video_explanations.md").write_text("# Video Explanations\n\n" + "\n".join(f"- `{p}`: describe field, colorbar, what to look for, and caution." for p in vids), encoding="utf-8")
    print(f"Wrote explanation templates to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
