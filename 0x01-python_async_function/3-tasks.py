#!/usr/bin/env python3
"""This module defines an asynchronous coroutine task_wait_random"""

import asyncio
module = __import__("0-basic_async_syntax")


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns a asyncio.Task using regular function """
    return asyncio.ensure_future(module.wait_random(max_delay))
