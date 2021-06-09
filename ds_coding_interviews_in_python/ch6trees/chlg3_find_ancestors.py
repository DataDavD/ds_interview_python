from typing import List, Optional

from ds_coding_interviews_in_python.ch6trees.bst import BSTNode


def find_ancestors_recursive(root: BSTNode, k: int) -> List[Optional[int]]:
    """Time complexity is O(n) since it iterates over all the nodes of the tree"""
    result: List[int] = []
    find_ancestors_recursive_helper(root, k, result)
    return result


def find_ancestors_recursive_helper(root: Optional[BSTNode], k: int, result: List[int]) -> bool:
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


def find_ancestors_iter(root: BSTNode, k: int) -> List[Optional[int]]:
    """Time complexity is O(log n) since we are just traversing the path to k"""
    ancestors: List[Optional[int]] = list()
    current = root
    if root is None:  # if root doesn't exist return empty list
        return ancestors

    while current:
        if k > current.val:  # k is greater than current.val
            ancestors.append(current.val)
            current = current.right
        elif k < current.val:  # k is less than current.val
            ancestors.append(current.val)
            current = current.left
        else:  # we found k, reverse list of ancestors from k to root and return list
            return ancestors[::-1]
    return list()  # we didn't find k, so return empty list
