# Visualization Standard

## Figures

- Export PNG at 300 dpi where possible.
- Export vector PDF/SVG for line plots where possible.
- Use axis labels with units.
- Use legends that do not hide data.
- Use colorbars with labels and units.
- Avoid more than four subplots per figure unless the figure remains readable.
- Use line width >= 1.5 for curves.
- Use consistent colors for baseline, optimized, and calibrated variants.

## Field Plots

- Use common color scales for baseline/optimized/corrected comparisons.
- Center difference-map colorbars at zero.
- Label spatial axes and units.
- State whether fields are process-model fields, CFD fields, or experimental fields.

## Videos

- Prefer MP4.
- Use at least 1280x720.
- Use 10 or 15 fps by default.
- Include case/design/time and key state values in titles.
- Fix temperature and state colorbars when comparing variants.
- Add a melting/front contour or vector scale where relevant.

## Simulink Screenshots

Export top-level model and key subsystems at high resolution. If subsystem screenshots are placeholders or passthroughs, add readable supplemental schematics and disclose this.

## Fluent Schematics

Provide geometry, boundary-condition, and mesh-example figures. Label coordinate directions, dimensions, named boundaries, materials/zones, and any excluded symmetry/axis region.

## Explanation Files

Create:

- `figure_explanations.md`;
- `video_explanations.md`;
- figure and table indexes.
