from typing import Union, Tuple

"""this module has a function that returns a tuple with two elements
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a key and its value to a tuple of the key and
    the square of its value.
    """
    return (k, float(v**2))
