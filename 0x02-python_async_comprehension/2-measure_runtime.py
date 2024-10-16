#!/usr/bin/env python3
"""this module contains an async function , nothing else :("""
import asyncio
import time
from typing import List

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    this function await four async_comprehension calls
    in parallel and return how mush time did it take
    """
    start = time.time()
    routines = []
    for x in range(4):
        routines.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*routines)
    return time.time() - start
