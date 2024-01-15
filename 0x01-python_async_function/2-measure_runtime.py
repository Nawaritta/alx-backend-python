#!/usr/bin/env python3
"""This module defines an asynchronous coroutine measure_time"""

import time
import asyncio
module = __import__("1-concurrent_coroutines")


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)"""
    start = time.time()
    asyncio.run(module.wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
