# Server Connection Guidelines

Use `mph.Client(version=..., port=...)` or `mph.start()` according to the local setup. Prefer an existing COMSOL Server when the user is sharing a GUI/session.

Checklist:

- Print target host, port, and version.
- List current models before creating a new one.
- If modifying an existing model, log its name, tag, and file.
- Never overwrite a user file or GUI-open `.mph`.
- Save generated models under a unique configured output path.
- On connection failure, write manual instructions and dry-run output.

Common pattern:

```python
import mph

client = mph.Client(version=config["version"], port=config["port"])
models = client.models()
for model in models:
    print(model.name(), model.java.tag())
```
