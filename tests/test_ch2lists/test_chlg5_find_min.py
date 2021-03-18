from ds_coding_interviews_in_python.ch2lists.chl5_find_min import find_minimum


def test_find_minimum() -> None:
    lst = [9, 2, 3, 6]
    lst2 = [4, 2, 1, 5, 0, -1]
    assert find_minimum(lst) == 2
    assert find_minimum(lst2) == -1
