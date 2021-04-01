from typing import List

# O(n) since iterate through list once
def max_min(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    result = []
    # iterate though list picking up max and mix
    # and placing max before min in each iteration.
    # b/c we use //2 (floor), the iteration
    # will not include middle values of odd
    # numbered lists
    for i in range(len(lst) // 2):
        # append corresponding last element
        result.append(lst[-(i + 1)])
        # append curr element
        result.append(lst[i])
    if len(lst) % 2 == 1:
        # if middle val then append
        result.append(lst[len(lst) // 2])
    return result
