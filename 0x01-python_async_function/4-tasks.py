#!/usr/bin/env python3
"""This module defines an asynchronous coroutine task_wait_n"""

import asyncio
from typing import List
module = __import__("3-tasks")


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    delays = []
    for i in range(n):
        delays.append(module.task_wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
