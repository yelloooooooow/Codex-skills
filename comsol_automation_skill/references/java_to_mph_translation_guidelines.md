# Java to Python/mph Translation Guidelines

COMSOL GUI Java history code often maps directly to Python through `model.java`.

Java pattern:

```java
Model model = ModelUtil.create("Model");
model.component().create("comp1", true);
model.component("comp1").geom().create("geom1", 2);
model.component("comp1").geom("geom1").feature().create("r1", "Rectangle");
model.component("comp1").geom("geom1").feature("r1").set("size", new double[]{1, 0.5});
model.component("comp1").geom("geom1").run();
model.component("comp1").physics().create("ht", "HeatTransfer", "geom1");
model.component("comp1").mesh().create("mesh1");
model.study().create("std1");
model.study("std1").feature().create("time", "Transient");
model.sol().create("sol1");
model.result().export().create("plot1", "Image");
```

Python/mph pattern:

```python
import mph

client = mph.start()
model = client.create("Model")
java = model.java

java.component().create("comp1", True)
java.component("comp1").geom().create("geom1", 2)
java.component("comp1").geom("geom1").feature().create("r1", "Rectangle")
java.component("comp1").geom("geom1").feature("r1").set("size", ["1", "0.5"])
java.component("comp1").geom("geom1").run()
java.component("comp1").physics().create("ht", "HeatTransfer", "geom1")
java.component("comp1").mesh().create("mesh1")
java.study().create("std1")
java.study("std1").feature().create("time", "Transient")
java.sol().create("sol1")
java.result().export().create("plot1", "Image")
```

Migration experience:

1. Keep tags stable: `comp1`, `geom1`, `mesh1`, `std1`, `sol1`.
2. Replace Java `new double[]{...}` with Python lists or COMSOL unit strings.
3. Preserve COMSOL units as strings such as `"0.1[m]"`.
4. Most `.set("key", value)` calls still work through Java objects.
5. Selections and feature tags must match their later references.
6. Create geometry features, set properties, then run geometry.
7. Bind physics to geometry and selections.
8. Build mesh after geometry.
9. Do not rename study or solver tags casually.
10. Check output directories before result export.
11. Move private paths into config.
12. Extract minimum necessary modeling steps; do not copy every GUI artifact.
13. Wrap repeated `.feature().create()` and `.set()` calls in helpers.
14. Mark uncertain property keys as TODO and verify in COMSOL documentation or GUI history.
15. If build works but solve fails, check selections, initial values, units, mesh, and solver setup.
16. If an exported image is blank, check dataset, plot group, solution tag, and filename.
17. If Java contains private parameters, abstract them into config before sharing.
