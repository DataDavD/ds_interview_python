import random

import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree, count_bst_nodes


@pytest.fixture
def bst() -> BinarySearchTree:
    bst = BinarySearchTree(5)
    for _ in range(5):
        ele = random.randint(0, 100)
        bst.iter_insert(ele)

    return bst


def test_bst_iter_insert_true(bst) -> None:
    assert bst.iter_insert(6) is True


def test_bst_iter_insert_false(bst) -> None:
    assert bst.iter_insert("921*-8--4+") is False


def test_bst_iter_search_true(bst) -> None:
    assert bst.iter_search(5) is True


def test_bst_iter_search_false(bst) -> None:
    assert bst.iter_search(150) is False


def test_bst_iter_search_except_false(bst) -> None:
    assert bst.iter_search("921*-8--4+") is False


def test_bst_recursive_insert_true(bst) -> None:
    assert bst.recursive_insert(6) is True


def test_bst_recursive_insert_false(bst) -> None:
    assert bst.recursive_insert("921*-8--4+") is False


def test_bst_recursive_search_true(bst) -> None:
    assert bst.recursive_search(5) is True


def test_bst_recursive_search_false(bst) -> None:
    assert bst.recursive_search(150) is False


def test_bst_recursive_search_except_false(bst) -> None:
    assert bst.recursive_search("921*-8--4+") is False


def test_bst_node_count(bst) -> None:
    assert count_bst_nodes(bst.root) == 6


def test_bst_node_count_zero() -> None:
    assert count_bst_nodes(None) == 0


def test_bst_delete() -> None:
    bst = BinarySearchTree(5)
    bst.iter_insert(10)
    bst.iter_insert(4)
    bst.iter_insert(6)
    bst.iter_insert(12)
    bst.iter_insert(2)

    assert bst.delete(2) is True
    assert bst.delete(10) is True
    assert bst.delete(4) is True
    assert bst.delete(5) is True
    assert bst.delete(20) is True
    assert bst.delete("921*-8--4+") is False
