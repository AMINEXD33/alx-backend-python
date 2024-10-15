#!/usr/bin/env python3
"""this module contains an async function , nothing else :("""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[int]:
    """
    this function calls am async function
    collect 10 random numbers using an async
    comprehensing over async_generator
    """
    result = []
    async for x in async_generator():
        result.append(x)
    return result
