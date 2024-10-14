#!/usr/bin/env python3
"""this module contains asyn function"""
from typing import List, Any
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    this function returns the approximate time it took
    for the function awaited to execute fully from the point
    of view of 1n
    """
    start_time = time.time()
    result = asyncio.run(wait_n(n=n, max_delay=max_delay))
    end_time = time.time()

    return (end_time - start_time) / n
