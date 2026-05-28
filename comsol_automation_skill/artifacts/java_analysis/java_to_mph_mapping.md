# Java to Python/mph Mapping Draft

Draft calls are written for Python using `model.java` access to the underlying COMSOL Java API.

| Java pattern | Python/mph draft | Notes |
| --- | --- | --- |
| `ModelUtil.create` | `client.create(model_name)` | Confirm server/session creation policy. |
| `model.component().create` | `java.component().create` | Preserve component tag. |
| `geom().create / geom().feature().create` | `java.component(...).geom(...).feature().create` | Create before set. |
| `.set(key, value)` | `.set(key, value)` | Convert arrays to Python lists; keep units as strings. |
| `physics().create` | `java.component(...).physics().create` | Bind to geometry and selections. |
| `mesh().create / mesh().run` | `java.component(...).mesh().create / run` | Build after geometry. |
| `study().create` | `java.study().create` | Preserve study tags. |
| `result().export().create` | `java.result().export().create` | Check output directory. |

## Extracted Tags
- `comp1`
- `geom1`
- `ht`
- `mesh1`
- `plot1`
- `r1`
- `std1`
- `time`

## TODO
- Confirm all property keys in COMSOL GUI history or official documentation.
