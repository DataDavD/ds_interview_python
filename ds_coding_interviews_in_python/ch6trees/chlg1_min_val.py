from typing import Optional

from ds_coding_interviews_in_python.ch6trees.bst import BSTNode


def find_min(root: Optional[BSTNode]) -> Optional[int]:
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.val
