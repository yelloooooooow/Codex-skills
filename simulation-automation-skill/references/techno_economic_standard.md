# Techno-Economic Standard

## Metrics

Compute:

- CAPEX by component;
- OPEX and annual electricity/fuel cost;
- annual O&M;
- capital recovery factor (CRF);
- total annualized cost (TAC);
- levelized cost of heat/production (LCOH/LCOX);
- net present cost (NPC), when requested.

## Core Formulas

```text
CRF = r*(1+r)^n / ((1+r)^n - 1)
annualized_CAPEX = CAPEX * CRF
TAC = annualized_CAPEX + O&M + energy_cost
LCOH = TAC / annual_useful_heat
NPC = CAPEX + sum((O&M + energy_cost)/(1+r)^year)
```

## Unit Checks

Check W/kW, J/kWh, EUR/kWh, EUR/MWh, thermal/electric energy, daily/annual scaling, and nominal vs actual delivered output.

## Sensitivity Analysis

Vary at least capital unit costs, energy prices, discount rate, lifetime, O&M fraction, auxiliary costs, and optional asset costs.

## Optional Assets

When assets such as PV, storage, or backup equipment are optional, report both with and without their CAPEX and state which comparison is fair.

## Uncertainty

Label literature costs, vendor quotes, estimates, and assumptions separately. Do not describe generic unit costs as actual purchase prices.
