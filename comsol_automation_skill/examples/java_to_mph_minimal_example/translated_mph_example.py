from __future__ import annotations

import mph


def build():
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
    java.result().export().create("plot1", "Image")
    return model
