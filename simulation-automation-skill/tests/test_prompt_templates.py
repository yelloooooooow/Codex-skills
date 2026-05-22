from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_prompt_templates_exist_and_are_nonempty():
    prompts = [
        "simulink_only_prompt.md",
        "fluent_only_prompt.md",
        "coupled_simulink_fluent_prompt.md",
        "optimization_prompt.md",
        "economic_analysis_prompt.md",
        "visualization_prompt.md",
        "final_review_prompt.md",
    ]
    for name in prompts:
        path = ROOT / "assets" / "prompts" / name
        assert path.exists()
        assert len(path.read_text(encoding="utf-8").strip()) > 40
