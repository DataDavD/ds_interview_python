from linkedlist import LinkedList, DoublyLinkedList


# Playing around with Linked List
print("Playing around with Linked List")
linked_list = LinkedList()

# Print list
linked_list.print_list()

# Test insert at head method
print("Inserting values in list")
for i in range(1, 11):
    linked_list.insert_at_head(i)
linked_list.print_list()
ll = linked_list.to_list()
print(ll)

# Test insert at tail method
linked_list = LinkedList()
linked_list.print_list()
# Test insert at tail method
linked_list.insert_at_tail(0)
linked_list.print_list()
linked_list.insert_at_tail(1)
linked_list.print_list()
linked_list.insert_at_tail(2)
linked_list.print_list()
linked_list.insert_at_tail(3)
linked_list.print_list()

# Test search method
linked_list = LinkedList()
print("Inserting values in list")
for i in range(1, 10):
    linked_list.insert_at_head(i)
linked_list.print_list()
linked_list.print_list()
linked_list.search(7)

# Test out delete at head method
linked_list.del_head()
linked_list.print_list()

# Test out delete specific value
linked_list.print_list()
linked_list.del_value(5)
linked_list.print_list()


# Playing around with Doubly Linked List
print("Playing around with Doubly Linked List")
dlinked_list = DoublyLinkedList()

# Print list
dlinked_list.print_list()

# Test insert at head method
print("Inserting values in list")
for i in range(1, 11):
    dlinked_list.insert_at_head(i)
dlinked_list.print_list()
ll = dlinked_list.to_list()
print(ll)

# Test insert at tail method
# dlinked_list = DoublyLinkedList()
# dlinked_list.print_list()
# # Test insert at tail method
# dlinked_list.insert_at_tail(0)
# dlinked_list.print_list()
# dlinked_list.insert_at_tail(1)
# dlinked_list.print_list()
# dlinked_list.insert_at_tail(2)
# dlinked_list.print_list()
# dlinked_list.insert_at_tail(3)
# dlinked_list.print_list()

# Test search method
# dlinked_list = DoublyLinkedList()
# print("Inserting values in list")
# for i in range(1, 10):
#     dlinked_list.insert_at_head(i)
# dlinked_list.print_list()
# dlinked_list.print_list()
# dlinked_list.search(7)

# Test out delete at head method
dlinked_list.del_head()
dlinked_list.print_list()


# Test out delete at head method
dlinked_list.del_tail()
dlinked_list.print_list()

dlinked_list.print_list()
dlinked_list.del_value(9)
dlinked_list.print_list()
dlinked_list.del_value(2)
dlinked_list.print_list()
dlinked_list.del_value(1)
dlinked_list.print_list()
