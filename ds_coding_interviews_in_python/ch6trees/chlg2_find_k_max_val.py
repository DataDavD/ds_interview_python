from typing import List, Optional

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree, BSTNode, count_bst_nodes


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


def find_k_max_val_recursive(root: BSTNode, k: Optional[int]) -> Optional[int]:
    if k is None or k < 1 or k > count_bst_nodes(root):
        return None

    node = find_k_max_recursive_helper(root, k)
    if node is not None:
        return node.val
    else:
        return None


counter: int = 0  # global count var
current_max: Optional[int] = None


def find_k_max_recursive_helper(root: BSTNode, k: Optional[int]) -> Optional[BSTNode]:
    """Time complexity is O(n) for worst case scenario, but best case scenario, when k=1, is
    O(h) where h is the height of the tree. So, on average, the solution is more
    efficient than the iterative function we created above that makes use of in
    order traversal"""
    global counter  # user global counter to track k
    global current_max  # track current max

    if root is None:
        return None  # check that root exists

    # recursive traversal to right for max node
    node = find_k_max_recursive_helper(root.right, k)
    if (counter is not k and root.val is not current_max) or current_max is None:
        # Increment counter if kth element is not found.
        # Do the same if there is no current_max set
        counter += 1
        current_max = root.val
        node = root

    if counter == k:
        return node
    else:
        # Traverse left child if kth element is not reached and to
        # traverse left tree for kth element
        return find_k_max_recursive_helper(root.left, k)


bst_2 = BinarySearchTree(6)
bst_2.iter_insert(4)
bst_2.iter_insert(9)
bst_2.iter_insert(8)
bst_2.iter_insert(12)
bst_2.iter_insert(10)
bst_2.iter_insert(14)
bst_2.iter_insert(2)
bst_2.iter_insert(5)

print(find_k_max_val_recursive(bst_2.root, 3))
