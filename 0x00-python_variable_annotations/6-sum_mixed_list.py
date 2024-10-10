#!/usr/bin/env python3
"""this module contains a function that sums a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    this function sums floats and its and return the sum
    """
    sum: float = 0
    for numb in mxd_lst:
        sum += numb
    return sum
