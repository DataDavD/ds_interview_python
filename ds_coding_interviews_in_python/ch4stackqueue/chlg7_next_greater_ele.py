from typing import List


def next_greater_ele_brute_force(lst: List[int]) -> List[int]:
    if len(lst) == 0:
        return lst
    for i in range(len(lst) - 1):
        for v in lst[i + 1 :]:
            if lst[i] != lst[-1] and v > lst[i]:
                lst[i] = v
                break
            elif v == lst[-1] and v <= lst[i]:
                lst[i] = -1
                break
    lst[-1] = -1
    return lst
