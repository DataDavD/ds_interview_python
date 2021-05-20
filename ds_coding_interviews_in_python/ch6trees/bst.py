import random
from typing import Any, Optional


class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

    def node_iter_insert(self, val: Any) -> None:
        curr = self
        parent = None
        while curr:
            parent = curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        if val < parent.val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)

    def node_iter_search(self, val: Any) -> bool:
        curr = self
        while curr:
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return True  # value found (i.e. equals curr.val)

        return False  # value not found

    def node_recursive_insert(self, val: Any) -> None:
        if val < self.val:
            if self.left:
                self.left.node_recursive_insert(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.node_recursive_insert(val)
            else:
                self.right = Node(val)

    def node_recursive_search(self, val: Any) -> bool:
        if val < self.val:
            if self.left:
                return self.node_recursive_search(val)
            else:
                return False  # value not found
        elif val > self.val:
            if self.right:
                return self.node_recursive_search(val)
            else:
                return False  # value not found
        else:
            return True  # value found (i.e. equals curr.val)


class BinarySearchTree:
    def __init__(self, val: Any) -> None:
        self.root = Node(val)

    def iter_insert(self, val: Any) -> bool:
        try:
            if self.root:
                self.root.node_iter_insert(val)
                return True
            else:
                self.root = Node(val)
                return True
        except Exception as e:
            print("Exception occurred: ", e)
            return False

    def iter_search(self, val: Any) -> bool:
        try:
            if self.root:
                return self.root.node_iter_search(val)
            else:
                return False
        except Exception as e:
            print("Exception occurred: ", e)
            return False

    def recursive_insert(self, val: Any) -> bool:
        try:
            if self.root:
                self.root.node_recursive_insert(val)
                return True
            else:
                self.root = Node(val)
                return True
        except Exception as e:
            print("Exception occurred: ", e)
            return False

    def recursive_search(self, val: Any) -> bool:
        try:
            if self.root:
                return self.root.node_recursive_search(val)
            else:
                return False
        except Exception as e:
            print("Exception occurred: ", e)
            return False


def _display_aux(node):
    """
    Returns list of strings, width, height,
    and horizontal coordinate of the root.
    """
    # No child.
    if node.right is None and node.left is None:
        line = str(node.val)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.val)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.val)
        u = len(s)
        #        first_line = s + x * '_' + (n - x) * ' '
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        final_lines = [first_line, second_line] + shifted_lines
        return final_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = "%s" % node.val
    u = len(s)
    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    if p < q:
        left += [n * " "] * (q - p)
    elif q < p:
        right += [m * " "] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def display(node: Node) -> None:
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)


BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    print("Inserting " + str(ele) + ":")
    BST.iter_insert(ele)
    # We have hidden the code for this function but it is available for use!
    display(BST.root)
    print("\n")
print(BST.iter_search(50))  # Will print True since 50 is the root
print(BST.iter_search(111))  # May or may not be True. Check the tree!

BST = BinarySearchTree(50)
for _ in range(15):
    ele = random.randint(0, 100)
    print("Inserting " + str(ele) + ":")
    BST.recursive_insert(ele)
    # We have hidden the code for this function but it is available for use!
    display(BST.root)
    print("\n")
print(BST.recursive_search(50))  # Will print True since 50 is the root
print(BST.recursive_search(111))  # May or may not be True. Check the tree!
