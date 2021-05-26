from typing import NamedTuple

import pytest

from ds_coding_interviews_in_python.ch6trees.avl import AVLNode, AVLTree

AVL = NamedTuple("AVL", [("avl_tree", AVLTree), ("root", AVLNode)])


@pytest.fixture()
def avl_tree_fixture() -> AVL:
    avl_tree = AVLTree()
    root = None
    nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in nums:
        root = avl_tree.insert_node(root, num)
    avl_tree_fixture = AVL(avl_tree, root)
    return avl_tree_fixture


def test_insert(avl_tree_fixture) -> None:
    new_root = avl_tree_fixture.avl_tree.insert_node(avl_tree_fixture.root, 5)
    assert new_root.val == 33


def test_delete(avl_tree_fixture) -> None:
    new_root = avl_tree_fixture.avl_tree.delete_node(avl_tree_fixture.root, 33)
    assert new_root.val == 13
