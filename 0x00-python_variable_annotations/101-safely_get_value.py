#!/usr/bin/env python3
""" This module includes a more involved type annontation"""

from typing import Any, Mapping, TypeVar, Union, Optional
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """ The function returns a key in a dictionnary if it
    exists or default if not"""
    if key in dct:
        return dct[key]
    else:
        return default
