from ds_coding_interviews_in_python.ch2lists.chlg3_two_nums_add_to_k import (
    find_sum,
    find_sum_2,
    find_sum_binary,
    find_sum_idx,
)


def test_find_sum() -> None:
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81
    result = [21, 60]
    assert find_sum(lst, k) == result


def test_find_sum_2() -> None:
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81
    result = [21, 60]
    assert find_sum_2(lst, k) == result


def test_find_sum_binary() -> None:
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81
    result = [21, 60]
    assert find_sum_binary(lst, k) == result


def test_find_sum_idx() -> None:
    lst = [1, 21, 3, 14, 5, 60, 7, 6]
    k = 81
    result = [21, 60]
    assert find_sum_idx(lst, k) == result
