from typing import List


def find_max_sum_sublist(lst: List[int]) -> int:
    if len(lst) < 1:
        return 0

    curr_max = lst[0]
    global_max = lst[0]

    lst_len = len(lst)

    for i in range(1, lst_len):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max
