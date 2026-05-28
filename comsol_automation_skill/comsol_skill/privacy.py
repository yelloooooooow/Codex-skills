from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable


PATTERNS = [
    r"C:\\+Users\\+[^\\\s]+",
    r"C:/Users/[^/\s]+",
    r"/home/[^/\s]+",
    r"/Users/[^/\s]+",
    r"/mnt/c/Users/[^/\s]+",
    r"(?i)api[_-]?key\s*[:=]",
    r"(?i)password\s*[:=]",
    r"(?i)secret\s*[:=]",
    r"(?i)token\s*[:=]",
    r"(?i)license[_-]?(path|number|file)\s*[:=]",
    r"(?i)ModelUtil\.connect\([^)]*password",
    r"\b\d{11}\b",
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
]

SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", "artifacts", "results", "outputs"}
SKIP_EXT = {".mph", ".mphbin", ".png", ".jpg", ".jpeg", ".gif", ".mp4", ".pdf", ".docx", ".pyc"}
SKIP_FILES = {"privacy.py", "check_privacy.py", "sanitize_for_open_source.py", "test_privacy_scan.py"}


def scan_text(text: str, file: str = "<text>") -> list[dict[str, str | int]]:
    findings = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for pattern in PATTERNS:
            match = re.search(pattern, line)
            if match:
                snippet = line[max(match.start() - 20, 0): match.end() + 20]
                findings.append({"file": file, "line": line_no, "pattern": pattern, "snippet": re.sub(r"\S", "*", snippet)})
    return findings


def iter_files(root: str | Path) -> Iterable[Path]:
    base = Path(root)
    if base.is_file():
        yield base
        return
    for path in base.rglob("*"):
        if path.is_dir():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        if path.suffix.lower() in SKIP_EXT:
            continue
        yield path


def scan_path(root: str | Path) -> list[dict[str, str | int]]:
    findings = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        findings.extend(scan_text(text, str(path)))
    return findings
