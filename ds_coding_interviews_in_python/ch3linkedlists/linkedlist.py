from typing import Any, List

from nodes import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self) -> List[Any]:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_element
        nodes.append("None")
        return nodes

    def get_head(self) -> Node:
        return self.head

    # Insertion at Head
    def insert_at_head(self, data) -> Node:
        # Create a new node containing your specified value
        new_node = Node(data)
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
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head = new_node
            return

        # If list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

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
            print("List is empty, cannot delete head")
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
            print("List is empty")
            return deleted
        curr_node = self.get_head()
        prev_node = None
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
            print("List is Empty")
            return False
        temp = self.head
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True
