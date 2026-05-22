# Calibration Standard

## Principle

Calibrate model parameters, not output curves. Preserve original baseline results.

## Raw Correction Factor

Fit a raw factor using a defined objective, for example:

```text
J(k) = w1*NRMSE(state) + w2*NRMSE(temperature) + w3*NRMSE(heat_rate)
```

Search a bounded range and report the best value, fit error, and warnings.

## Conservative Correction Factor

Use reliability weighting:

```text
k_conservative = 1 + reliability_weight*(k_raw - 1)
```

Bound the result, for example `[0.7, 2.0]`, unless a project-specific validation justifies wider bounds.

Suggested reliability weights:

- 0.3 for short smoke tests or idealized CFD;
- 0.5 for longer unit CFD with simplified boundaries;
- 0.75 for conjugate/component CFD with mesh sensitivity and stronger validation.

## Output Policy

Save calibrated configs and results in a new folder such as `results_calibrated/`. Never overwrite `results/`.

## Reasonableness Checks

- Conservative factor within bounds.
- Fit quality acceptable.
- Calibrated states remain physical.
- Performance/cost improvements not implausibly large.
- CFD and system model boundary conditions compatible enough for calibration.

## When Not to Calibrate

Do not force calibration when:

- comparison variables are incompatible;
- CFD boundary conditions are too different;
- time window is too short;
- NRMSE remains high;
- input data are missing or untrusted.
