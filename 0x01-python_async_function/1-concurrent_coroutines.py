#!/usr/bin/env python3
"""This module defines an asynchronous coroutine wait_n"""

import asyncio
from typing import List
module = __import__("0-basic_async_syntax")


async def wait_n(n: int, max_delay: int) -> List:
    " return the list of all the delays in ascending order"
    delays = []
    for i in range(n):
        el = await module.wait_random(max_delay)
        j = 0
        while (j < len(delays)):
            if delays[j] < el:
                j += 1
            else:
                break
        delays.insert(j, el)
    return delays
