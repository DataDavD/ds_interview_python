from typing import Any, Optional, TypeVar

N = TypeVar("N", bound="BSTNode")


class BSTNode:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None
        self.parent: Optional[BSTNode] = None

    def node_iter_insert(self, val: Any) -> None:
        curr = self
        parent = None
        while curr:
            parent = curr
            if val < curr.val:
                curr = curr.left
            elif val > curr.val:
                curr = curr.right
            else:
                return  # value already exists

        if val < parent.val:
            parent.left = BSTNode(val)
        else:
            parent.right = BSTNode(val)

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
                self.left = BSTNode(val)
        elif val > self.val:
            if self.right:
                self.right.node_recursive_insert(val)
            else:
                self.right = BSTNode(val)
        else:
            return  # value already exists

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

    def copy(self, node2: N) -> None:  # When `self` needs to be modified
        self.val = node2.val
        if node2.left:
            self.left = node2.left
        if node2.right:
            self.right = node2.right

    def delete(self, val: Any):
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        elif val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            else:
                print(str(val) + " not found in the tree")
                return self
        else:
            # deleting node with no children
            if self.left is None and self.right is None:
                # self = None
                return None
            # deleting node with right child
            elif self.left is None:
                tmp = self.right
                # self = None
                return tmp
            # deleting node with left child
            elif self.right is None:
                tmp = self.left
                # self = None
                return tmp
            # deleting node with two children
            else:
                # first get the inorder successor
                current = self.right
                # loop down to find the leftmost leaf
                while current.left is not None:
                    current = current.left
                self.val = current.val
                self.right = self.right.delete(current.val)

        return self

    def node_delete(self, val: Any) -> bool:
        # case 1: Tree is empty
        if self is None:
            return False

        # Searching for the given value
        node = self
        parent: BSTNode = node
        while node and node.val != val:
            if val < node.val:
                node = node.left
            else:
                node = node.right

        # case 2: If data is not found
        if node is None or node.val != val:
            return False

        # case 3: leaf node
        elif node.left is None and node.right is None:
            if val < parent.val:
                parent.left = None
            else:
                parent.right = None
            return True

        # case 4: node has left child only
        elif node.left and node.right is None:
            if parent is None:  # When node is root
                """
                Have to create a deepcopy because 'self' is a local variable
                and changing it will not overwrite 'root' in the
                binarySearchTree class
                """
                self.copy(self.left)
                self.left = None  # Setting the left child to `None`
            elif val < parent.val:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

            # case 5: node has right child only
        elif node.right and node.left is None:
            if parent is None:  # When node is root
                """
                Have to create a deepcopy because 'self' is a local variable
                and changing it will not overwrite 'root' in the
                binarySearchTree class
                """
                self.copy(self.right)
                self.right = None  # Setting the right child to `None`
            elif val < parent.val:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        # case 6: node has two children
        else:
            replace_node_parent = node
            replace_node = node.right
            while replace_node.left:
                replace_node_parent = replace_node
                replace_node = replace_node.left

            node.val = replace_node.val
            if replace_node.right:
                if replace_node_parent.val > replace_node.val:
                    replace_node_parent.left = replace_node.right
            elif replace_node_parent.val < replace_node.val:
                replace_node_parent.right = replace_node.right
            else:
                if replace_node.val < replace_node_parent.val:
                    replace_node_parent.left = None
                else:
                    replace_node_parent.right = None
            return True


class BinarySearchTree:
    def __init__(self, val: Any) -> None:
        self.root = BSTNode(val)

    def iter_insert(self, val: Any) -> bool:
        try:
            if self.root:
                self.root.node_iter_insert(val)
                return True
            else:
                self.root = BSTNode(val)
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
                self.root = BSTNode(val)
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

    def delete(self, val: Any) -> bool:
        try:
            if self.root:
                self.root = self.root.delete(val)
                return True
            else:
                return False
        except Exception as e:
            print("Exception occurred: ", e)
            return False


def traverse_pre_order(node: BSTNode) -> None:
    if node is not None:
        print(node.val)
        traverse_pre_order(node.left)
        traverse_pre_order(node.right)


def traverse_post_order(node: BSTNode) -> None:
    if node is not None:
        traverse_post_order(node.left)
        traverse_post_order(node.right)
        print(node.val)


def traverse_in_order(node: BSTNode) -> None:
    if node is not None:
        traverse_in_order(node.left)
        print(node.val)
        traverse_in_order(node.right)


def count_bst_nodes(node: Optional[BSTNode]):
    if node is None:
        return 0

    return 1 + count_bst_nodes(node.left) + count_bst_nodes(node.right)


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


def display(node: BSTNode) -> None:
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)
