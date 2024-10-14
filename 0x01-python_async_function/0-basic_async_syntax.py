#!/usr/bin/env python3
"""a module that has an async function :)"""

from asyncio import sleep as asyn_sleep
from random import uniform as ran_uniform


async def wait_random(max_delay: float = 10) -> float:
    """
    an async function that takes a max delay , waits it out
    then return it
    """
    delay: float = ran_uniform(0, max_delay)
    await asyn_sleep(delay)
    return delay
