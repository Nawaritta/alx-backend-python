#!/usr/bin/env python3
""" This module defines a type-annotated function sum_list """

from typing import List, Union


def sum_mixed_list(input_list: List[Union[float, int]]) -> float:
    """Return the sum of a mixed list of floats and integers"""
    return sum(input_list)
