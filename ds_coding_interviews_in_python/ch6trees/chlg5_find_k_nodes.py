from typing import Any, List, Optional

from ds_coding_interviews_in_python.ch6trees.bst import BSTNode


def find_k_nodes_helper(root: Optional[BSTNode], k: Any, result: List[Any]) -> None:
    if root is None:  # return if root doesn't exist
        return

    if k == 0:
        result.append(root.val)  # append when get to kth node
        return
    else:
        # check recursively in both subtrees for kth node
        find_k_nodes_helper(root.left, k - 1, result)
        find_k_nodes_helper(root.right, k - 1, result)


def find_k_nodes(root: Optional[BSTNode], k: Any) -> List[Any]:
    """Time complexity is O(n)"""
    result: List[Any] = []
    find_k_nodes_helper(root, k, result)
    return result
