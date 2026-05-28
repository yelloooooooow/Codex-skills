import com.comsol.model.*;
import com.comsol.model.util.*;

public class GenericToyModel {
  public static Model run() {
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
    model.result().export().create("plot1", "Image");
    return model;
  }
}
