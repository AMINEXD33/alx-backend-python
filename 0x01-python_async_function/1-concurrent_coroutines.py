#!/usr/bin/env python3
"""this module contains asyn function"""
from typing import List, Any
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function takes two args , n and max_delay , it awaits the
    result of the wait_random function with a param = max_delay
    n times and return a list of the results
    """
    result_list: List[float] = []
    futures: Any = []
    for x in range(n):
        futures.append(wait_random(max_delay=max_delay))
    futures = asyncio.as_completed(futures)
    result: Any = []
    for future in futures:
        result.append(await future)
    return result
