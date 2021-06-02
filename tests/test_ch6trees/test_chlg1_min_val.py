import random

import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg1_min_val import find_min


@pytest.fixture
def bst() -> BinarySearchTree:
    bst = BinarySearchTree(5)
    bst.iter_insert(-20)
    for _ in range(5):
        ele = random.randint(0, 100)
        bst.iter_insert(ele)

    return bst


def test_find_min(bst) -> None:
    assert find_min(bst.root) == -20
