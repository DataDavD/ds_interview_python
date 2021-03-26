from typing import List

from ds_coding_interviews_in_python.ch2lists.chlg7_second_max import (
    find_second_maximum,
    find_second_maximum_2,
    find_second_maximum_3,
)


def test_find_second_maximum() -> None:
    lst = [9, 2, 3, 6]
    expect = 6
    lst2: List[int] = list()
    expect2 = None
    lst3 = [1]
    expect3 = None
    assert find_second_maximum(lst) == expect
    assert find_second_maximum(lst2) == expect2
    assert find_second_maximum(lst3) == expect3

    assert find_second_maximum_2(lst) == expect
    assert find_second_maximum_2(lst2) == expect2
    assert find_second_maximum_2(lst3) == expect3

    assert find_second_maximum_3(lst) == expect
    assert find_second_maximum_3(lst2) == expect2
    assert find_second_maximum_3(lst3) == expect3
