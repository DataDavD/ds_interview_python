from typing import Optional

from ds_coding_interviews_in_python.ch6trees.bst import BSTNode


def find_min_iter(root: Optional[BSTNode]) -> Optional[int]:
    """Time complexity is O(h) where h is the height. In the worst case
    the BST will be left skewed and the height will be in n and then time
    complexity will be O(n)
    """
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.val


def find_min_recursive(root: Optional[BSTNode]) -> Optional[int]:
    """Time complexity is O(h) where h is the height. In the worst case
    the BST will be left skewed and the height will be in n and then time
    complexity will be O(n)
    """
    if root is None:
        return None
    elif root.left is None:
        return root.val
    else:
        return find_min_recursive(root.left)
