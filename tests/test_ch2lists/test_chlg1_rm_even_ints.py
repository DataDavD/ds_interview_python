from typing import List

import pytest

from ds_coding_interviews_in_python.ch2lists.chlg1_rm_even_ints import (
    remove_even_first,
    remove_even_pythonic,
)


@pytest.fixture()
def test_list() -> List[int]:
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


@pytest.fixture()
def test_result_list() -> List[int]:
    return [1, 3, 5, 7, 9, 11, 13, 15]


def test_remove_even_first(test_list: List[int], test_result_list: List[int]) -> None:
    assert remove_even_first(test_list) == test_result_list


def test_remove_even_second(test_list: List[int], test_result_list: List[int]) -> None:
    assert remove_even_pythonic(test_list) == test_result_list
