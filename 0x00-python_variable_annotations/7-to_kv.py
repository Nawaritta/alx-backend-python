#!/usr/bin/env python3
""" This module defines a type-annotated function to_kv """

from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v
    should be annotated as a float."""
    return (k, v ** 2)
