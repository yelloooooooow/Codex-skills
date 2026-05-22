from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_required_folders_exist():
    required = [
        "references",
        "scripts/python",
        "scripts/matlab",
        "scripts/shell",
        "assets/templates",
        "assets/prompts",
        "assets/examples",
        "tests",
        "docs",
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    assert not missing


def test_required_top_level_files_exist():
    required = ["SKILL.md", "README.md", "LICENSE", "skill.json", "packaging_summary.md"]
    missing = [p for p in required if not (ROOT / p).is_file()]
    assert not missing
