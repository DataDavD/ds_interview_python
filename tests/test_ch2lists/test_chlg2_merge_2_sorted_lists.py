from typing import List

from ds_coding_interviews_in_python.ch2lists.chlg2_merge_2_sorted_lists import merge_lists_inplace, \
	merge_lists_new


def test_merge_lists_new() -> None:
	lst1 = [1, 3, 5, 8]
	lst2 = [2, 4, 5, 7, 8]
	exp_result = [1, 2, 3, 4, 5, 5, 7, 8, 8]
	assert merge_lists_new(lst1, lst2) == exp_result

def test_merge_lists_inplace() -> None:
	lst1 = [1, 3, 5, 8]
	lst2 = [2, 4, 5, 7, 8]
	exp_result = [1, 2, 3, 4, 5, 5, 7, 8, 8]
	assert merge_lists_inplace(lst1, lst2) == exp_result