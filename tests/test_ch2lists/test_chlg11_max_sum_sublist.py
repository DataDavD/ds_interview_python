from ds_coding_interviews_in_python.ch2lists.chlg11_max_sum_sublist import find_max_sum_sublist

def test_find_max_sum_sublist() -> None:
    lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    result = 12
    assert find_max_sum_sublist(lst) == result