#!/usr/bin/env python3
"""Task 100's module.
"""
from typing import Any, Union, Sequence, Iterable, List, Tuple


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """return the first element of an array"""
    if lst:
        return lst[0]
    else:
        return None
