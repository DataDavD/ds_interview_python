from typing import Optional

from ds_coding_interviews_in_python.ch6trees.bst import BSTNode


def find_height(root: Optional[BSTNode]) -> int:
    if root is None:
        return -1

    max_sub_tree_height = max(find_height(root.left), find_height(root.right))
    return 1 + max_sub_tree_height
