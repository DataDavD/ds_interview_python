from typing import List


# O(n) since loop through list once,
# O(n) space since need another list to store result
def rearrange(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    result: List[int] = list()
    for x in range(len(lst)):
        if lst[x] < 0:
            result.insert(0, lst[x])
        else:
            result.append(lst[x])
    return result


# O(n) since list iterated over once
def rearrange_aux_lists(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    neg = []
    pos = []
    # make a list of negative and positive numbers
    for ele in lst:
        if ele < 0:
            neg.append(ele)
        else:
            pos.append(ele)
    # merge two lists and return
    return neg + pos


# O(n) since list iterated over once, but O(1) aux space complexity
# since using existing list
def rearrange_inplace(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    left_most_pos_el = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if lst[curr] < 0:
            # if not the last negative number
            if curr is not left_most_pos_el:
                # swap the two
                lst[curr], lst[left_most_pos_el] = lst[left_most_pos_el], lst[curr]
            # update the last position
            left_most_pos_el += 1
    return lst


# O(n) since iterate over the list twice
def rearrange_pythonic(lst: List[int]) -> List[int]:
    # get negative and positive list after filter and then merge
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]
