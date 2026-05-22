# Optimization Standard

## Required Design Types

Report:

- baseline design;
- technical-optimal design;
- economic-optimal design;
- balanced-optimal design.

## Candidate Data

Each candidate should store design variables, derived parameters, feasibility, technical metrics, economic metrics, and failure reasons.

## Constraints

Include hard constraints such as:

- physical geometry valid;
- states within physical bounds;
- minimum performance delivered;
- actuator/pump/load limits respected;
- COP/efficiency meaningful;
- baseline not overwritten.

## Objectives

Technical objectives may maximize efficiency/effectiveness and minimize tracking error or unmet load. Economic objectives may minimize CAPEX, OPEX, TAC, LCOH, and NPC.

Balanced scoring must normalize metrics and include penalties.

## Pareto Analysis

Plot at least one technical-vs-economic Pareto front. Mark baseline and optima. Keep infeasible candidates visible in constraint summaries.

## Economics Coupling

If design variables change equipment size, material, pressure drop, auxiliary power, or capacity, recompute CAPEX, OPEX, TAC, LCOH, and sensitivity.

## Baseline Protection

Do not alter baseline parameter files. Save optimized variants separately.
