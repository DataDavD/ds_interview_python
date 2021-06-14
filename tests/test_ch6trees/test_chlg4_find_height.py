import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg4_find_height import find_height


@pytest.fixture
def bst() -> BinarySearchTree:
    bst = BinarySearchTree(5)
    bst.iter_insert(3)
    bst.iter_insert(7)
    bst.iter_insert(10)
    bst.iter_insert(15)
    bst.iter_insert(20)
    bst.iter_insert(21)
    bst.iter_insert(25)

    return bst


def test_find_height(bst) -> None:
    assert find_height(bst.root) == 6


def test_find_height_null_root() -> None:
    assert find_height(None) == -1


def test_find_height_zero() -> None:
    bst = BinarySearchTree(5)
    assert find_height(bst.root) == 0
