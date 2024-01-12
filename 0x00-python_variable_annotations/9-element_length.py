#!/usr/bin/env python3
""" This module defines a type-annotated function element_length """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing the element from the input list
    and its corresponding length."""
    return [(i, len(i)) for i in lst]
