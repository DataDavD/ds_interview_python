from typing import List

from ds_coding_interviews_in_python.ch4stackqueue.chlg7_next_greater_ele import (
    next_greater_ele_brute_force,
)


def test_next_greater_ele_brute() -> None:
    lst = [4, 6, 3, 2, 8, 1]
    result = [6, 8, 8, 8, -1, -1]
    assert next_greater_ele_brute_force(lst) == result


def test_next_greater_ele_empty() -> None:
    lst: List[int] = list()
    result: List[int] = list()
    assert next_greater_ele_brute_force(lst) == result
