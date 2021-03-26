from typing import List, Optional

# 1st try brute force: O(n^2)
def find_sum(lst: List[int], k: int) -> Optional[List[int]]:
    result: List[int] = list()
    ix = 0
    ix2 = 1
    while ix < len(lst):
        while ix2 < len(lst):
            if lst[ix] + lst[ix2] == k and ix is not ix2:
                result[:2] = lst[ix], lst[ix2]
                return result
            else:
                ix2 += 1
        ix += 1
        ix2 = ix + 1
    return None


# solution brute force: O(n^2)
def find_sum_2(lst: List[int], k: int) -> Optional[List[int]]:
    # iterate lst with i
    for i in range(len(lst)):
        # iterate lst with j
        for j in range(len(lst)):
            # if sum of two iterators is k
            # and i is not equal to j
            # then we have our answer
            if lst[i] + lst[j] is k and i is not j:
                return [lst[i], lst[j]]
    return None


def binary_search(a: List[int], item: int) -> int:
    first = 0
    last = len(a) - 1
    found = False
    index = -1
    while first <= last and not found:
        mid = (first + last) // 2
        if a[mid] == item:
            index = mid
            found = True
        else:
            if item < a[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if found:
        return index
    else:
        return -1


# binary search takes O(log n) for a single element
# so searching through our entire list would take O(n log n)
def find_sum_binary(lst: List[int], k: int) -> Optional[List[int]]:
    lst.sort()
    for j in range(len(lst)):
        # find the difference in list through binary search
        # return only if we find an index, i.e. return not -1
        index = binary_search(lst, k - lst[j])
        if index != -1 and index != j:
            return [lst[j], k - lst[j]]

    return None


# scan takes O(n) (at worst; i.e. if we go through the whole list
# while the sort take O(n log n) so in total the time complexity is
# O(n log n) + O(n) (since one is done one after the other)
# which in turns results in the overall being O(n log n)
def find_sum_idx(lst: List[int], k: int) -> Optional[List[int]]:
    # sort the list
    lst.sort()
    index1 = 0
    index2 = len(lst) - 1
    result = []
    s = 0
    # iterate from front and back
    # move accordingly to reach the sum to be equal to k
    # returns false when the two indices meet
    while index1 != index2:
        summ = lst[index1] + lst[index2]
        if summ < k:
            index1 += 1
        elif summ > k:
            index2 -= 1
        else:
            result.append(lst[index1])
            result.append(lst[index2])
            return result
    result[0] = -1
    return result
