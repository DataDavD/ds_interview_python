from typing import Any, List, Optional

from ds_coding_interviews_in_python.ch3linkedlists.nodes import DNode, Node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def to_list(self) -> List[Any]:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_element
        nodes.append("None")
        return nodes

    def get_head(self) -> Optional[Node]:
        return self.head

    # Insertion at Head
    def insert_at_head(self, data) -> Node:
        # Create a new node containing your specified value
        new_node: Node = Node(data)
        # The new node points to the same node as the head
        new_node.next_element = self.head
        self.head = new_node  # Make the head point to the new node
        return self.head  # return the new list

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def insert_at_tail(self, value) -> None:
        # Creating a new node
        new_node: Node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head = new_node
            return

        # If list not empty, traverse the list to the last node
        temp: Optional[Node] = self.get_head()

        while temp.next_element:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def insert_after_item(self, x, data) -> bool:
        temp = self.head
        while temp:
            if temp.data == x:
                break
            temp = temp.next_element
        if temp is None:
            print("item not in list")
            return False
        else:
            new_node = Node(data)
            new_node.next_element = temp.next_element
            temp.next_element = new_node

        print(data, " inserted after ", x)
        return True

    def search(self, value) -> bool:
        # Start from first ele
        curr_node = self.get_head()

        # Traverse the list
        while curr_node:
            if curr_node.data == value:
                print("Found!")
                return True  # value found
            curr_node = curr_node.next_element
        print("Not Found!")
        return False  # value not found

    def del_head(self) -> bool:
        # Get head and first ele of list
        first_ele = self.get_head()

        # Check if list is empty
        if first_ele is None:
            print("Linked List is empty, cannot delete head")
            return False

        # If list is not empty then link head to
        # the next element of first element
        self.head = first_ele.next_element
        first_ele.next_element = None

        print("Deleted head")
        return True

    def del_value(self, value) -> bool:
        deleted = False
        # Check if list is empty -> return False if so
        if self.is_empty():
            print("Linked List is empty")
            return deleted
        curr_node: Node = self.get_head()
        prev_node: Node = None
        if curr_node.next_element is value:
            self.del_head()  # Delete head since value is at head
            deleted = True
            return deleted

        # Search the rest of the list past the head for value to delete
        while curr_node is not None:
            if value == curr_node.data:
                # prev node now points to next node
                prev_node.next_element = curr_node.next_element
                # delete curr node value matches to
                curr_node.next_element = None
                deleted = True
                break
            # if value doesn't match node data/value then keep iterating
            # through list
            prev_node = curr_node
            curr_node = curr_node.next_element

        if deleted is False:
            print(str(value), " is not in the list!")
        else:
            print(str(value), " deleted")

        return deleted

    def reverse(self) -> bool:
        if self.is_empty():
            print("list is empty, cannot reverse")
            return False
        nxt = None
        prev = None
        curr = self.get_head()

        while curr:
            nxt = curr.next_element
            curr.next_element = prev
            prev = curr
            curr = nxt

            # set last ele as new head
            self.head = prev
        print("List reversed")
        return True

    def detect_loop(self) -> bool:
        one_step = self.head
        two_step = self.head
        while one_step and two_step and two_step.next_element:
            one_step = one_step.next_element
            two_step = two_step.next_element.next_element
            if one_step == two_step:
                print("Loop detected")
                return True
        print("Loop not detected")
        return False

    def __len__(self) -> int:
        # start from the first element
        curr = self.get_head()
        length: int = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

    def find_mid_brute(self) -> Optional[Any]:
        # O(n)
        if self.is_empty():
            print("List is empty")
            return None

        node = self.head
        if self.__len__() % 2 == 0:
            mid = self.__len__() // 2
        else:
            mid = (self.__len__() // 2) + 1

        for i in range(mid - 1):
            node = node.next_element

        print("Mid found at ", node.data)
        return node

    def find_mid_optimal(self) -> Optional[Any]:
        # O(n) but traversing list at twice speed of brute force version of
        # finding mid method
        if self.is_empty():
            print("List is empty")
            return None

        if self.head.next_element is None:
            # only 1 element, so return it
            print("Only 1 element in list. The element is ", self.head)
            return self.head.data

        mid_node = self.head
        curr = self.head.next_element.next_element
        # move fast node twice as fast as slow, so that when fast gets to end of
        # list, then slow will be at the middle of the list
        while curr:
            mid_node = mid_node.next_element
            curr = curr.next_element
            if curr:
                curr = curr.next_element
        print("Mid found at ", mid_node.data)
        return mid_node.data

    def remove_dups(self) -> None:
        # O(n^2) since using nested while loops
        if self.is_empty():
            print("list is empty, nothing to remove")
            return

        if self.head.next_element is None:
            print("list only has 1 element")
            return

        outer = self.head
        while outer:
            inner = outer
            while inner and inner.next_element:
                if outer.data == inner.next_element.data:
                    print("duplicate found, removing: ", outer.data)
                    new_next_ele = inner.next_element.next_element
                    inner.next_element = new_next_ele
                else:
                    inner = inner.next_element
            outer = outer.next_element
        return

    # Supplementary print function
    def print_list(self) -> bool:
        if self.is_empty():
            print("Linked List is Empty")
            return False
        temp: Node = self.head
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True


class DoublyLinkedList:
    def __init__(self):
        self.head: Optional[DNode] = None

    def get_head(self) -> Optional[DNode]:
        return self.head

    def insert_at_head(self, data) -> DNode:
        temp_node: DNode = DNode(data)
        if self.head is None:
            self.head = temp_node
            return self.head

        temp_node.next_element = self.head
        self.head.prev_element = temp_node
        self.head = temp_node
        return self.head

    def insert_at_tail(self, data) -> DNode:
        if self.head is None:
            new_node = DNode(data)
            self.head = new_node
            return self.head

        temp = self.head
        while temp.next_element:
            temp = temp.next_element
        new_node = DNode(data)
        temp.next_element = new_node
        new_node.prev_element = temp
        return new_node

    def insert_after_item(self, x, data) -> bool:
        if self.head is None:
            print("Doubly Linked List is Empty")
            return False
        else:
            temp = self.head
            while temp:
                if temp.data == x:
                    break
                temp = temp.next_element
            if temp is None:
                print("item not in the list")
            else:
                new_node = DNode(data)
                new_node.prev_element = temp
                new_node.next_element = temp.next_element
                if temp.next_element:
                    temp.next_element.prev_element = new_node
                temp.next_element = new_node
            print(data, " inserted after ", x)
            return True

    def to_list(self) -> List[Any]:
        dnode = self.head
        dnodes = []
        while dnode is not None:
            dnodes.append(dnode.data)
            dnode = dnode.next_element
        dnodes.append("None")
        return dnodes

    def is_empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False

    def print_list(self) -> bool:
        if self.is_empty():
            print("Doubly Linked List is Empty")
            return False
        temp: DNode = self.head
        while temp.next_element is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next_element
        print(temp.data, "<-> None")
        return True

    def del_head(self) -> bool:
        # Check if list is empty
        if self.head is None:
            print("Doubly Linked List is empty, cannot delete head")
            return False

        if self.head.next_element is None:
            self.head = None
            print("Head deleted")
            return True

        self.head = self.head.next_element
        self.head.prev_element = None
        print("head deleted")
        return True

    def del_tail(self) -> bool:
        if self.head is None:
            print("The Doubly Linked List is empty, no element to delete")
            return False
        if self.head.next_element is None:
            self.head = None
            print("Doubly Linked List only has head. Head deleted")
            return True

        temp_node: DNode = self.head
        while temp_node.next_element is not None:
            temp_node = temp_node.next_element
        temp_node.prev_element.next_element = None
        print("Tail deleted")
        return True

    def del_value(self, value) -> bool:
        deleted: bool = False
        if self.head is None:
            print("Doubly Linked List is empty")
            return deleted

        curr_node: Optional[DNode] = self.get_head()
        # If deletion value matches head value:
        if curr_node.next_element is None:
            if curr_node.data == value:
                curr_node = None
            else:
                print("Item not found")
                return deleted

        if curr_node.data == value:
            # Point head to the next element of head
            self.head = curr_node.next_element
            if curr_node.next_element is not None:
                # Point next element of head to None
                curr_node.next_element.prev_element = None
                deleted = True
                print(str(curr_node.data), " is deleted!")
            return deleted

        # Traverse/search rest of list for node to delete
        while curr_node:
            if curr_node.data == value:
                if curr_node.next_element:
                    # Link next node and prev node to each other
                    prev_node = curr_node.prev_element
                    next_node = curr_node.next_element
                    prev_node.next_element = next_node
                    next_node.prev_element = prev_node
                else:
                    # if value matches last node:
                    curr_node.prev_element.next_element = None

                deleted = True
                break
            curr_node = curr_node.next_element

        if not deleted:
            print(str(value), " is not in list!")
        else:
            print(str(value), " is deleted!")
        return deleted

    def reverse(self) -> bool:
        if self.is_empty():
            print("List is empty, cannot reverse")
            return False

        curr = self.head
        nxt = curr.next_element
        curr.next_element = None
        curr.prev_element = nxt
        while nxt:
            nxt.prev_element = nxt.next_element
            nxt.next_element = curr
            curr = nxt
            nxt = nxt.prev_element

        self.head = curr
        print("List reversed!")
        return True

    def search(self, value) -> bool:
        # Start from first ele
        curr_node = self.get_head()

        # Traverse the list
        while curr_node:
            if curr_node.data == value:
                print("Found!")
                return True  # value found
            curr_node = curr_node.next_element
        print("Not Found!")
        return False  # value not found

    def remove_dups(self) -> None:
        # O(n^2) since using nested while loops
        if self.is_empty():
            print("list is empty, nothing to remove")
            return

        if self.head.next_element is None:
            print("list only has 1 element")
            return

        outer = self.head
        while outer:
            inner = outer
            while inner and inner.next_element:
                if outer.data == inner.next_element.data:
                    print("duplicate found, removing: ", outer.data)
                    new_next_ele = inner.next_element.next_element
                    inner.next_element = new_next_ele
                else:
                    inner = inner.next_element
            outer = outer.next_element
        return

    def __len__(self) -> int:
        # start from the first element
        curr = self.get_head()
        length: int = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length
