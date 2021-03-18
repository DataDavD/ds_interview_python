from typing import List, Optional


def find_minimum(lst: List[int]) -> Optional[int]:
    if len(lst) <= 0:
        return None
    lst.sort()
    return lst[0]