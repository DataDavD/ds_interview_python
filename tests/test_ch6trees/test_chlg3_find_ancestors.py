import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg3_find_ancestors import (
    find_ancestors_iter,
    find_ancestors_recursive,
)


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


def test_find_ancestors_recursive(bst) -> None:
    expect = [21, 20, 15, 10, 7, 5]
    assert find_ancestors_recursive(bst.root, 25) == expect


def test_find_ancestors_recursive_root_only() -> None:
    bst = BinarySearchTree(5)
    assert find_ancestors_recursive(bst.root, 5) == []


def test_find_ancestors_recursive_not_found(bst) -> None:
    assert find_ancestors_recursive(bst.root, 100) == []


def test_find_ancestors_iter(bst) -> None:
    expect = [21, 20, 15, 10, 7, 5]
    assert find_ancestors_iter(bst.root, 25) == expect


def test_find_ancestors_iter_root_only() -> None:
    bst = BinarySearchTree(5)
    assert find_ancestors_iter(bst.root, 5) == []


def test_find_ancestors_iter_not_ound(bst) -> None:
    assert find_ancestors_iter(bst.root, 100) == []
