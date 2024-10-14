#!/usr/bin/env python3
"""this module contains asyn function"""
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function takes two args , n and max_delay , it awaits the
    result of the wait_random function with a param = max_delay
    n times and return a list of the results
    """
    result_list: List[float] = []
    for x in range(n):
        result: float = await wait_random(max_delay)
        result_list.append(result)
    return result_list
