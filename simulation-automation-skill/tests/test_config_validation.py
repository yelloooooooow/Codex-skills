from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_template_configs_are_nonempty():
    templates = [
        "project_config_template.yaml",
        "simulink_config_template.yaml",
        "fluent_config_template.yaml",
        "coupled_calibration_config_template.yaml",
        "optimization_config_template.yaml",
        "economic_config_template.yaml",
    ]
    for name in templates:
        path = ROOT / "assets" / "templates" / name
        assert path.exists()
        assert path.read_text(encoding="utf-8").strip()


def test_project_template_has_core_fields():
    text = (ROOT / "assets" / "templates" / "project_config_template.yaml").read_text(encoding="utf-8")
    for key in ["project_name:", "workflow_mode:", "software_paths:", "outputs:"]:
        assert key in text
