import random

import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg1_min_val import find_min_iter, find_min_recursive


@pytest.fixture
def bst() -> BinarySearchTree:
    bst = BinarySearchTree(5)
    bst.iter_insert(-20)
    for _ in range(5):
        ele = random.randint(0, 100)
        bst.iter_insert(ele)

    return bst


def test_find_min_iter(bst) -> None:
    assert find_min_iter(bst.root) == -20


def test_find_min_recursive(bst) -> None:
    assert find_min_recursive(bst.root) == -20
