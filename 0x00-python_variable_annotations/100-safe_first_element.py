#!/usr/bin/env python3
"""Task 100's module.
"""
from typing import Iterable, Sequence, Union


def safe_first_element(lst: Iterable[Sequence]) -> Union[any, None]:
    """return the first element of an array"""
    if lst:
        return lst[0]
    else:
        return None
