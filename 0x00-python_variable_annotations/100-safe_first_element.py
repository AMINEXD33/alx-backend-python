# The types of the elements of the input are not know

from typing import Iterable, Sequence, Union
def safe_first_element(lst:Iterable[Sequence]) -> Union[any, None]:
    if lst:
        return lst[0]
    else:
        return None