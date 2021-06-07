from typing import List, Optional

from ds_coding_interviews_in_python.ch6trees.bst import BSTNode


def find_ancestors_recursive(root: BSTNode, k: Optional[int]) -> List[int]:
    """Time complexity is O(n) since it iterates over all the nodes of the tree"""
    result: List[int] = []
    find_ancestors_recursive_helper(root, k, result)
    return result


def find_ancestors_recursive_helper(
    root: Optional[BSTNode], k: Optional[int], result: List[int]
) -> bool:
    if root is None:
        return False
    elif root.val == k:
        return True

    recur_left = find_ancestors_recursive_helper(root.left, k, result)
    recur_right = find_ancestors_recursive_helper(root.right, k, result)
    if recur_left or recur_right:
        # If recursive find in either left or right sub tree
        # append root value and return True
        result.append(root.val)
        return True
    return False
