# Coupled Simulation Standard

## Model Roles

Simulink should usually own system-level dynamics, controls, long-duration cases, and operating strategy. Fluent should own local high-fidelity physics, component fields, short transients, or calibration evidence.

Do not let CFD replace a system model unless geometry, boundary conditions, and time scales cover the full system and the user explicitly requests that.

## Alignment

Before comparing, align:

- geometry definitions and reference areas/volumes;
- material properties and units;
- initial conditions;
- boundary conditions;
- time windows and output intervals;
- sign conventions for heat and work.

## Common Variables

Compare compatible variables:

- average temperature;
- state variable or phase fraction;
- heat rate or heat flux integrated over a surface;
- stored energy;
- outlet temperatures;
- efficiency or effectiveness;
- final state and characteristic time.

## Time Axis

Interpolate both result sets onto a common time vector. Do not compare solver internal steps directly.

## Scale Mismatch

If Fluent is unit-level and Simulink is system-level, compare normalized or representative quantities, not total system quantities unless a scaling relation is documented.

## Reporting

State all differences in geometry, boundary conditions, physical models, and simplifications. Include a caution if CFD uses idealized boundaries.
