from typing import List, Optional


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


# O(n) but space complexity with this is constant at O(1)
def max_mix_space_1(lst: List[int]) -> List[Optional[int]]:
    if len(lst) == 0:
        return []
    max_idx = len(lst) - 1  # last index
    max_ele = lst[-1] + 1
    min_idx = 0  # first index

    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[max_idx] % max_ele) * max_ele
            max_idx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[min_idx] % max_ele) * max_ele
            min_idx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // max_ele
    return lst
