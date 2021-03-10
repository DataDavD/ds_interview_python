from typing import List


def remove_even_first(lst: List[int]) -> List[int]:
    # time complexity is O(n) since looping through entire list
    result = list()
    for i in lst:
        if i % 2 != 0:
            result.append(i)
    return result


def remove_even_pythonic(lst: List[int]) -> List[int]:
    # time complexity is O(n) since looping through entire list, but is more Pythonic since using
    # list comprehension
    result = [i for i in lst if i % 2 != 0]
    return result
