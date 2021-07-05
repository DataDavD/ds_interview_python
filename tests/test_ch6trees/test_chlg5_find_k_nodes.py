from typing import Any, List

from ds_coding_interviews_in_python.ch6trees.chlg5_find_k_nodes import find_k_nodes


def test_find_k_nodes_k_is_0(bst) -> None:
    expect = [5]
    assert find_k_nodes(bst.root, 0) == expect


def test_find_k_nodes_k_is_1(bst) -> None:
    expect = [3, 7]
    assert find_k_nodes(bst.root, 1) == expect


def test_find_k_nodes_k_is_2(bst) -> None:
    expect = [10]
    assert find_k_nodes(bst.root, 2) == expect


def test_find_k_nodes_k_is_3(bst) -> None:
    expect = [15]
    assert find_k_nodes(bst.root, 3) == expect


def test_find_k_nodes_k_is_4(bst) -> None:
    expect = [20]
    assert find_k_nodes(bst.root, 4) == expect


def test_find_k_nodes_root_is_none() -> None:
    expect: List[Any] = list()
    assert find_k_nodes(None, 1) == expect
