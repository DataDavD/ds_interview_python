import sys
from typing import Any, Optional


class AVLNode:
    def __init__(self, val: Any):
        self.val = val
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None
        self.height = 1


class AVLTree:
    # Function to insert a node
    def insert_node(self, root: Optional[AVLNode], val: Any) -> AVLNode:
        # Find the correct location and insert the node
        if not root:
            return AVLNode(val)
        elif val < root.val:
            root.left = self.insert_node(root.left, val)
        else:
            root.right = self.insert_node(root.right, val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Update the balance factor and balance the tree
        balance_factor = self.get_balance(root)
        if balance_factor > 1:
            if val < root.left.val:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if val > root.right.val:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    # Function to delete a node
    def delete_node(self, root: Optional[AVLNode], val: Any) -> Optional[AVLNode]:

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif val < root.val:
            root.left = self.delete_node(root.left, val)
        elif val > root.val:
            root.right = self.delete_node(root.right, val)
        else:
            if root.left is None:
                temp: Optional[AVLNode] = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance_factor = self.get_balance(root)

        # Balance the tree
        if balance_factor > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    # Function to perform left rotation
    def left_rotate(self, z: Optional[AVLNode]) -> AVLNode:
        y = z.right
        temp = y.left
        y.left = z
        z.right = temp
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Function to perform right rotation
    def right_rotate(self, z: Optional[AVLNode]) -> AVLNode:
        y = z.left
        temp = y.right
        y.right = z
        z.left = temp
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Get the height of the node
    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_value_node(root.left)

    def pre_order_traversal(self, root):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    # Print the tree
    def print_helper(self, curr_ptr, indent, last):
        if curr_ptr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(curr_ptr.val)
            self.print_helper(curr_ptr.left, indent, False)
            self.print_helper(curr_ptr.right, indent, True)
