from __future__ import annotations

from pathlib import Path


def save_placeholder_plot(path: str | Path, title: str = "Dry-run figure") -> Path:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(5, 3), dpi=150)
    ax.text(0.5, 0.5, title, ha="center", va="center")
    ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(target)
    plt.close(fig)
    return target
