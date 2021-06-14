from typing import Any, List

import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg5_find_k_nodes import find_k_nodes


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


def test_find_k_nodes_k_is_0(bst) -> None:
    expect = [5]
    assert find_k_nodes(bst.root, 0) == expect


def test_find_k_nodes_k_is_1(bst) -> None:
    expect = [3, 7]
    assert find_k_nodes(bst.root, 1) == expect


def test_find_k_nodes_k_is_2(bst) -> None:
    expect = [10]
    assert find_k_nodes(bst.root, 2) == expect


def test_find_k_nodes_k_is_4(bst) -> None:
    expect = [20]
    assert find_k_nodes(bst.root, 4) == expect


def test_find_k_nodes_root_is_none() -> None:
    expect: List[Any] = list()
    assert find_k_nodes(None, 1) == expect
