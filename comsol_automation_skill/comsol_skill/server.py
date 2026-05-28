from __future__ import annotations

from typing import Any


def connect_client(config: dict[str, Any]):
    comsol = config.get("comsol", {})
    version = comsol.get("version")
    port = int(comsol.get("server_port", 2036))
    try:
        import mph
    except Exception as exc:
        raise RuntimeError("mph is not installed or COMSOL integration is unavailable.") from exc
    if version:
        return mph.Client(version=str(version), port=port)
    return mph.Client(port=port)


def list_models(client) -> list[dict[str, str]]:
    models = []
    for model in client.models():
        tag = ""
        try:
            tag = str(model.java.tag())
        except Exception:
            pass
        models.append({"name": str(model.name()), "tag": tag, "file": str(model.file())})
    return models


def connect_or_plan(config: dict[str, Any], dry_run: bool = False) -> dict[str, Any]:
    if dry_run:
        return {"connected": False, "dry_run": True, "models": []}
    client = connect_client(config)
    return {"connected": True, "dry_run": False, "client": client, "models": list_models(client)}
