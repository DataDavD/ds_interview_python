from ds_coding_interviews_in_python.ch2lists.chlg10_rearrange_sorted_list import max_min

def test_max_min() -> None:
    lst = [1, 2, 3, 4, 5]
    expect = [5, 1, 4, 2, 3]
    assert max_min(lst) == expect

    lst2 = [1]
    expect2 = [1]
    assert max_min(lst2) == expect2
