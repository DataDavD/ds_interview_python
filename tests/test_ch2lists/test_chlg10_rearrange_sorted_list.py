from ds_coding_interviews_in_python.ch2lists.chlg10_rearrange_sorted_list import (
    max_min,
    max_mix_space_1,
)


def test_max_min() -> None:
    lst = [1, 2, 3, 4, 5]
    expect = [5, 1, 4, 2, 3]
    assert max_min(lst) == expect

    lst2 = [1]
    expect2 = [1]
    assert max_min(lst2) == expect2

    lst3 = [1, 1, 1, 1]
    expect3 = [1, 1, 1, 1]
    assert max_min(lst3) == expect3


def test_max_mix_space_1() -> None:
    lst = [1, 2, 3, 4, 5]
    expect = [5, 1, 4, 2, 3]
    assert max_mix_space_1(lst) == expect

    lst2 = [1]
    expect2 = [1]
    assert max_mix_space_1(lst2) == expect2

    lst3 = [1, 1, 1, 1]
    expect3 = [1, 1, 1, 1]
    assert max_min(lst3) == expect3

    lst4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    expect4 = [11, 0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5]
    assert max_mix_space_1(lst4) == expect4
