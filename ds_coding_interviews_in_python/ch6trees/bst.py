from typing import Any


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, val: Any):
        self.root = Node(val)


BST = BinarySearchTree(6)
print(BST.root.val)
