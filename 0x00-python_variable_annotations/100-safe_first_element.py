#!/usr/bin/env python3
""" This module includes a Duck typing annontation"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ The function returns the first element of lst if the sequence is not
empty or None if it is empty."""
    if lst:
        return lst[0]
    else:
        return None
