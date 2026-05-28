from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .privacy import scan_text
from .utils import ensure_dir


COMSOL_PATTERNS = {
    "component": r"model\.component\([^)]*\)|model\.component\(\)",
    "geometry": r"\.geom\([^)]*\)|\.geom\(\)",
    "material": r"\.material\([^)]*\)|\.material\(\)",
    "physics": r"\.physics\([^)]*\)|\.physics\(\)",
    "mesh": r"\.mesh\([^)]*\)|\.mesh\(\)",
    "study": r"model\.study\([^)]*\)|model\.study\(\)",
    "solver": r"model\.sol\([^)]*\)|model\.sol\(\)",
    "result": r"model\.result\([^)]*\)|model\.result\(\)",
    "export": r"\.export\([^)]*\)|\.export\(\)",
}


def extract_java_patterns(src: str | Path) -> dict[str, Any]:
    source = Path(src)
    files = list(source.rglob("*.java")) if source.is_dir() else [source]
    report: dict[str, Any] = {
        "files": [],
        "calls": {key: [] for key in COMSOL_PATTERNS},
        "tags": [],
        "feature_types": [],
        "properties": [],
        "sensitive_findings": [],
    }
    tag_set: set[str] = set()
    feature_types: set[str] = set()
    properties: set[str] = set()
    for file in files:
        if not file.exists():
            continue
        text = file.read_text(encoding="utf-8", errors="replace")
        rel = str(file)
        report["files"].append(rel)
        for finding in scan_text(text, rel):
            report["sensitive_findings"].append(finding)
        for key, pattern in COMSOL_PATTERNS.items():
            for match in re.finditer(pattern, text):
                report["calls"][key].append({"file": rel, "snippet": match.group(0)})
        for match in re.finditer(r'"([A-Za-z][A-Za-z0-9_]*)"', text):
            value = match.group(1)
            if re.match(r"^(comp|geom|mesh|std|sol|mat|ht|tds|spf|dode|pg|plot|exp)\w*$", value):
                tag_set.add(value)
        for match in re.finditer(r'\.feature\(\)\.create\("([^"]+)",\s*"([^"]+)"\)', text):
            tag_set.add(match.group(1))
            feature_types.add(match.group(2))
        for match in re.finditer(r'\.set\("([^"]+)"', text):
            properties.add(match.group(1))
    report["tags"] = sorted(tag_set)
    report["feature_types"] = sorted(feature_types)
    report["properties"] = sorted(properties)
    return report


def write_java_reports(report: dict[str, Any], out: str | Path) -> dict[str, Path]:
    out_dir = ensure_dir(out)
    json_path = out_dir / "java_patterns.json"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    md = ["# Java Pattern Report", "", "## Files"]
    md.extend(f"- {name}" for name in report.get("files", []))
    md.extend(["", "## Sensitive Findings"])
    if report.get("sensitive_findings"):
        md.extend(f"- {f['file']}:{f['line']} {f['pattern']} {f['snippet']}" for f in report["sensitive_findings"])
    else:
        md.append("- None detected.")
    md.extend(["", "## Tags"])
    md.extend(f"- `{tag}`" for tag in report.get("tags", []))
    md.extend(["", "## Feature Types"])
    md.extend(f"- `{kind}`" for kind in report.get("feature_types", []))
    md.extend(["", "## Property Keys"])
    md.extend(f"- `{prop}`" for prop in report.get("properties", []))
    report_path = out_dir / "java_pattern_report.md"
    report_path.write_text("\n".join(md) + "\n", encoding="utf-8")

    mapping_path = out_dir / "java_to_mph_mapping_draft.md"
    mapping_path.write_text(generate_mapping_markdown(report), encoding="utf-8")
    return {"json": json_path, "report": report_path, "mapping": mapping_path}


def generate_mapping_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# Java to Python/mph Mapping Draft",
        "",
        "Draft calls are written for Python using `model.java` access to the underlying COMSOL Java API.",
        "",
        "| Java pattern | Python/mph draft | Notes |",
        "| --- | --- | --- |",
    ]
    rows = [
        ("ModelUtil.create", "client.create(model_name)", "Confirm server/session creation policy."),
        ("model.component().create", "java.component().create", "Preserve component tag."),
        ("geom().create / geom().feature().create", "java.component(...).geom(...).feature().create", "Create before set."),
        (".set(key, value)", ".set(key, value)", "Convert arrays to Python lists; keep units as strings."),
        ("physics().create", "java.component(...).physics().create", "Bind to geometry and selections."),
        ("mesh().create / mesh().run", "java.component(...).mesh().create / run", "Build after geometry."),
        ("study().create", "java.study().create", "Preserve study tags."),
        ("result().export().create", "java.result().export().create", "Check output directory."),
    ]
    for java, py, notes in rows:
        lines.append(f"| `{java}` | `{py}` | {notes} |")
    lines.extend(["", "## Extracted Tags"])
    lines.extend(f"- `{tag}`" for tag in report.get("tags", []))
    lines.extend(["", "## TODO"])
    if report.get("sensitive_findings"):
        lines.append("- Resolve sensitive findings before sharing.")
    lines.append("- Confirm all property keys in COMSOL GUI history or official documentation.")
    return "\n".join(lines) + "\n"
