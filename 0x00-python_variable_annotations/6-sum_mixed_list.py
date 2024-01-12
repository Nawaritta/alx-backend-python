#!/usr/bin/env python3
""" This module defines a type-annotated function sum_mixed_list """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a mixed list of floats and integers"""
    return sum(mxd_lst)
