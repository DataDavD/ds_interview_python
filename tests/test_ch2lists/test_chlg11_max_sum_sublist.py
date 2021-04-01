from ds_coding_interviews_in_python.ch2lists.chlg11_max_sum_sublist import find_max_sum_sublist


def test_find_max_sum_sublist() -> None:
    lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    result = 12
    assert find_max_sum_sublist(lst) == result

    lst2 = list()
    result2 = 0
    assert find_max_sum_sublist(lst2) == result2

    lst3 = [-1, -2, -1, -1, -2]
    result3 = -1
    assert find_max_sum_sublist(lst3) == result3
