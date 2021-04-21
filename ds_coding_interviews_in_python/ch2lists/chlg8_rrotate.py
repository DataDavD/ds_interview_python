from typing import Any, List


# O(n) since loop through list k times, then Python extend is O(k)
# where k is amount you are extending list by
def right_rotate(lst: List[Any], k: int) -> List[Any]:
    result = list()
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    for x in range(len(lst) - k, len(lst)):
        result.append(lst[x])
    result.extend(lst[: len(lst) - k])
    return result


# O(n) since list slicing is in O(k) where k is # of elements sliced.
# So, since the entire list is sliced total time complexity is O(n)
def right_rotate_optimal(lst: List[Any], k: int) -> List[Any]:
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]
