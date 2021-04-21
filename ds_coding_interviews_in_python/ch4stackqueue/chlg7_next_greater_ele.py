from typing import List

from ds_coding_interviews_in_python.ch4stackqueue.stack import MyStack


def next_greater_ele_brute_force(lst: List[int]) -> List[int]:
    """
    For each element in list, function returns the first element to
    the right that is larger than the element being compared to.
    Time complexity is O(n^2) because we iterate through the list once
    for each element at worst.

    :param lst: List[int]
    :return: List[int]
    """
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


def next_greater_ele_stack(lst: List[int]) -> List[int]:
    """
    For each element in list, function returns the first element to
    the right that is larger than the element being compared to.
    Since we only iterate through the list once the Time Complexity is
    only O(n) instead of O(n^2) like the brute force method above.

    :param lst: List[int]
    :return: List[int]
    """
    s = MyStack()
    res = [-1] * len(lst)
    # Reverse iterate through the list
    for i in range(len(lst) - 1, -1, -1):

        # While stack has elements and current element is greater
        # than top element of stack pop all elements
        while s.is_empty() is False and lst[i] >= s.top():

            s.pop()

        # If stack has an element the top element
        # that is greater than the ith element
        if s.is_empty() is False:

            res[i] = s.top()

        # Push in the current element into the stack

        s.push(lst[i])

    return res
