#!/usr/bin/env python3
"""this module contains a function that sums a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    this function sums floats and its and return the sum
    """
    return float(sum(mxd_lst))
