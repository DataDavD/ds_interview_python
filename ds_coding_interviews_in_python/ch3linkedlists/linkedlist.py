import nntplib
from typing import Any, List, Optional

from ds_coding_interviews_in_python.ch3linkedlists.nodes import Node, DNode


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

    def insert_after_item(self, x, data) -> None:
        if self.head is None:
            print("Linked List is Empty")
            return
        else:
            temp = self.head
            while temp:
                if temp.data == x:
                    break
                temp = temp.next_element
            if temp is None:
                print("item not in list")
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
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
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

        curr_node: DNode = self.get_head()
        # If deletion value matches head value:
        if curr_node.next_element is None:
            if curr_node.data == value:
                curr_node = Node
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
