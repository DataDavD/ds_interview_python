import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree


@pytest.fixture
def bst() -> BinarySearchTree:
    return BinarySearchTree(5)


def test_bst_iter_insert_true(bst) -> None:
    assert bst.iter_insert(6) is True


def test_bst_iter_insert_false(bst) -> None:
    assert bst.iter_insert("921*-8--4+") is False


def test_bst_recursive_insert_true(bst) -> None:
    assert bst.recursive_insert(6) is True


def test_bst_recursive_insert_false(bst) -> None:
    assert bst.recursive_insert("921*-8--4+") is False
