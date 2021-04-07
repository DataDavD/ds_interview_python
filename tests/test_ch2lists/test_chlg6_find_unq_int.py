from ds_coding_interviews_in_python.ch2lists.chlg6_find_unq_int import find_first_unique


def test_find_first_unique() -> None:
    lst1 = [9, 2, 3, 5, 2, 6, 6]
    lst2 = [4, 5, 1, 2, 0, 4]
    lst3 = [4, 4, 3, 3]
    assert find_first_unique(lst1) == 9
    assert find_first_unique(lst2) == 5
    assert find_first_unique(lst3) == None
