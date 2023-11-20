"""Summing the elements of a list using different loops."""

__author__ = "730529193"

vals: list[float] = [1.1, 0.9, 1.0]


def w_sum(vals: list[float]) -> float:
    """W_sum is defined and allows a set of floats as inputs (vals), the inputs are defined and the respected return type is a float."""
    idx = 0
    equal = 0.0
    
    while idx < len(vals):
        equal += vals[idx]
        idx += 1

    return equal


def f_sum(vals: list[float]) -> float:
    """Same as w_sum but f_sum is defined."""
    equal = 0.0
    item = 0.0

    for item in vals:
        equal += item
    return equal


def f_range_sum(vals: list[float]) -> float:
    """Same as w_sum but f_range_sum is defined."""
    equal = 0.0
    for i in range(len(vals)):
        equal += vals[i]
    return equal

