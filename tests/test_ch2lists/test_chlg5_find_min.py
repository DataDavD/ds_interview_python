from ds_coding_interviews_in_python.ch2lists.chlg5_find_min import (
    find_minimum,
    find_minimum_merge_sort,
)


def test_find_minimum() -> None:
    lst = [9, 2, 3, 6]
    lst2 = [4, 2, 1, 5, 0, -1]

    # test first min func
    assert find_minimum(lst) == 2
    assert find_minimum(lst2) == -1

    # test using merge sort min func
    assert find_minimum_merge_sort(lst) == 2
    assert find_minimum_merge_sort(lst2) == -1
