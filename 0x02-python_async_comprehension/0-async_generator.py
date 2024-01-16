#!/usr/bin/env python3
"""This module contains async_generators coroutine"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10 times, each time asynchronously wait 1 second
    then yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
