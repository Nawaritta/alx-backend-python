#!/usr/bin/env python3
""" This module defines a type-annotated function sum_list """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats"""
    return sum(input_list)
