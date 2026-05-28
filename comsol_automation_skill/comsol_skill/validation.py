from __future__ import annotations

from math import sqrt
from typing import Sequence


def rmse(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    if len(y_true) != len(y_pred) or not y_true:
        raise ValueError("rmse requires equal non-empty sequences")
    return sqrt(sum((a - b) ** 2 for a, b in zip(y_true, y_pred)) / len(y_true))


def nrmse(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    base = max(y_true) - min(y_true)
    if base == 0:
        raise ValueError("nrmse reference range is zero")
    return rmse(y_true, y_pred) / base


def endpoint_error(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    if not y_true or not y_pred:
        raise ValueError("endpoint_error requires non-empty sequences")
    return y_pred[-1] - y_true[-1]


def trend_agreement(y_true: Sequence[float], y_pred: Sequence[float]) -> float:
    if len(y_true) != len(y_pred) or len(y_true) < 2:
        raise ValueError("trend_agreement requires equal sequences with at least two points")
    total = len(y_true) - 1
    agree = 0
    for i in range(total):
        d_true = y_true[i + 1] - y_true[i]
        d_pred = y_pred[i + 1] - y_pred[i]
        if d_true == 0 and d_pred == 0:
            agree += 1
        elif d_true * d_pred > 0:
            agree += 1
    return agree / total
