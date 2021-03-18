from typing import List, Optional

# O(n log n) since just using Python's list sort method
def find_minimum(lst: List[int]) -> Optional[int]:
    if len(lst) <= 0:
        return None
    lst.sort()
    return lst[0]


# using merge sort
def merge_sort(my_list: List[int]) -> None:
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                my_list[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

# O(n log n) since list is being split in log(n) call and
# merging process takes linear time in each call
def find_minimum_merge_sort(lst: List[int]) -> Optional[int]:
    if len(lst) <= 0:
        return None
    merge_sort(lst)  # sort list
    return lst[0]  # return first element

# O(n) since list is iterated over just once
def find_minimum_constant(lst: List[int]) -> Optional[int]:
    if len(lst) <= 0:
        return None
    minimum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
    return minimum


