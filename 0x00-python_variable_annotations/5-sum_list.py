#!/usr/bin/env python3
"""this module contains a function that sums a list of floats"""


def sum_list(input_list: [float]) -> float:
    """
    this function returns the sum of floats in an array
    """
    sum: float = 0
    for numb in input_list:
        sum += numb
    return sum
