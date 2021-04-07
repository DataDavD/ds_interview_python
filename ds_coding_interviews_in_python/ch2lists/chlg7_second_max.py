from typing import List, Optional

# O(n log n) since just using Python's list sort method
def find_second_maximum(lst: List[int]) -> Optional[int]:
    lst.sort()
    if len(lst) <= 1:
        return None
    return lst[-2]


# O(n) since we traverse the list twice
def find_second_maximum_2(lst: List[int]) -> Optional[int]:
    first_max = float("-inf")
    second_max = float("-inf")
    # find first max
    for item in lst:
        if item > first_max:
            first_max = item
    # find max relative to first max
    for item in lst:
        if item != first_max and item > second_max:
            second_max = item
    if second_max == float("-inf"):
        return None
    else:
        return int(second_max)


# O(n) since traverse list just once
def find_second_maximum_3(lst: List[int]) -> Optional[int]:
    if len(lst) < 2:
        return None
    # initialize the two to infinity
    max_no = second_max_no = float("-inf")
    for i in range(len(lst)):
        # update the max_no if max_no value found
        if lst[i] > max_no:
            second_max_no = max_no
            max_no = lst[i]
        # check if it is the second_max_no and not equal to max_no
        elif lst[i] > second_max_no and lst[i] != max_no:
            second_max_no = lst[i]
    if second_max_no == float("-inf"):
        return None
    else:
        return int(second_max_no)
