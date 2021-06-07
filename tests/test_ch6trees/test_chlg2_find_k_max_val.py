import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg2_find_k_max_val import find_k_max_val_iter


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


def test_find_k_max_val_iter(bst) -> None:
    assert find_k_max_val_iter(bst.root, 3) == 20


def test_find_k_max_val_iter_k_zero(bst) -> None:
    assert find_k_max_val_iter(bst.root, 0) is None


def test_find_k_max_val_iter_k_too_great(bst) -> None:
    assert find_k_max_val_iter(bst.root, 10) is None
