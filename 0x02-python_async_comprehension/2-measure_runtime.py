#!/usr/bin/env python3
"""This module contains measure_runtime coroutine"""
import asyncio
import time
async_compr = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel using asyncio.gather.
    and measure the total runtime and return it."""
    start = time.time()
    coroutines = [async_compr() for _ in range(4)]
    await asyncio.gather(*coroutines)
    runtime = time.time() - start
    return runtime
