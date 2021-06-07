from typing import List, Optional

from ds_coding_interviews_in_python.ch6trees.bst import BSTNode


def find_k_max_val_iter(root: BSTNode, k: Optional[int]) -> Optional[int]:
    """Time complexity is O(n) since with traverse in order helper we have to
    always traverse the entire tree before selecting the k-th max value"""
    if k is None or k < 1:
        return None

    tree: List[int] = list()
    traverse_in_order_helper(root, tree)
    if len(tree) - k >= 0:  # check that k is valid
        return tree[-k]
    else:
        return None


def traverse_in_order_helper(node: Optional[BSTNode], tree: List[int]) -> None:
    if node is not None:
        traverse_in_order_helper(node.left, tree)
        if len(tree) == 0:
            # append if tree is empty
            tree.append(node.val)
        elif tree[-1] is not node.val:
            # ensure don't have dupe
            tree.append(node.val)
        traverse_in_order_helper(node.right, tree)
