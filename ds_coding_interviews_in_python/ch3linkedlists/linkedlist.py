from node import Node


class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    # Insertion at Head
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        new_node = Node(data)
        # The new node points to the same node as the head
        new_node.next_element = self.head_node
        self.head_node = new_node  # Make the head point to the new node
        return self.head_node  # return the new list

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    # Supplementary print function
    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True




linked_list = LinkedList()

# print list
linked_list.print_list()

# test out insert at head method
print("Inserting values in list")
for i in range(1, 10):
    linked_list.insert_at_head(i)
linked_list.print_list()

linked_list = LinkedList()
linked_list.print_list()
# test out insert at tail method
linked_list.insert_at_tail(0)
linked_list.print_list()
linked_list.insert_at_tail(1)
linked_list.print_list()
linked_list.insert_at_tail(2)
linked_list.print_list()
linked_list.insert_at_tail(3)
linked_list.print_list()
