#!/usr/bin/env python3
"""this module contains asyn function"""
from typing import List, Any
import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    this function returs a new task from the wait_random
    function
    """
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
