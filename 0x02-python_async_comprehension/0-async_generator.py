#!/usr/bin/env python3
"""this module contains an async function , nothing else :("""

from asyncio import sleep as asyncio_sleep
from typing import AsyncGenerator
from random import uniform as rand_uniform


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Yield 10 different values that are
    between 0 and 10, with a 1-second delay between each.
    """
    for x in range(10):
        await asyncio_sleep(1)
        yield rand_uniform(0, 10)
