from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg4_find_height import find_height


def test_find_height(bst) -> None:
    assert find_height(bst.root) == 6


def test_find_height_other_tree() -> None:
    bst = BinarySearchTree(6)
    bst.iter_insert(4)
    bst.iter_insert(9)
    bst.iter_insert(2)
    bst.iter_insert(5)
    bst.iter_insert(8)
    bst.iter_insert(12)
    bst.iter_insert(10)
    bst.iter_insert(14)

    assert find_height(bst.root) == 3


def test_find_height_null_root() -> None:
    assert find_height(None) == -1


def test_find_height_zero() -> None:
    bst = BinarySearchTree(5)
    assert find_height(bst.root) == 0
