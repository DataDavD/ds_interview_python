from linkedlist import LinkedList, DoublyLinkedList
from setops import union, intersect, find_nth_node_from_end

LINE_LENGTH = 100
STAR = "*"

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

# Test insert after method
linked_list.print_list()
linked_list.insert_after_item(3, 99)
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

# Test out reversing the list
linked_list.print_list()
linked_list.reverse()
linked_list.print_list()

# Test out finding mid the list
print("testing out finding mid brute force method")
linked_list.print_list()
linked_list.find_mid_brute()
linked_list.print_list()
linked_list.del_head()
linked_list.print_list()
linked_list.find_mid_brute()
print("end testing out finding mid brute force method")
print("testing out finding mid optimal method")
linked_list.print_list()
linked_list.find_mid_optimal()
linked_list.print_list()
linked_list.del_head()
linked_list.print_list()
linked_list.find_mid_optimal()
linked_list.print_list()
print("end testing out finding mid optimal method")

# Detect loop
linked_list = LinkedList()

linked_list.insert_at_head(21)
linked_list.insert_at_head(14)
linked_list.insert_at_head(7)

# Test length method
linked_list.print_list()
print("length of linked list is:")
print(len(linked_list))

# Test removing dupes
print("Test removing dupes")
lst = LinkedList()
lst.insert_at_head(7)
lst.insert_at_head(7)
lst.insert_at_head(7)
lst.insert_at_head(22)
lst.insert_at_head(14)
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.print_list()
lst.remove_dups()
lst.print_list()
print("End test removing dupes")

# Adding a loop
head = linked_list.get_head()
node = linked_list.get_head()
linked_list.print_list()

for i in range(4):
    if node.next_element is None:
        node.next_element = head.next_element
        break
    node = node.next_element
linked_list.detect_loop()


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
dlinked_list.insert_at_tail(0)
dlinked_list.print_list()
dlinked_list.insert_at_tail(1)
dlinked_list.print_list()
dlinked_list.insert_at_tail(2)
dlinked_list.print_list()
dlinked_list.insert_at_tail(3)
dlinked_list.print_list()

# Test insert after method
dlinked_list.print_list()
dlinked_list.insert_after_item(3, 99)
dlinked_list.print_list()

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

# Test out reversing list
# Test out reversing the list
dlinked_list.print_list()
dlinked_list.reverse()
dlinked_list.print_list()

dlinked_list = DoublyLinkedList()

# Print list
dlinked_list.print_list()

# Test insert at head method
print("Inserting values in list")
for i in range(1, 4):
    dlinked_list.insert_at_head(i)
dlinked_list.print_list()
dlinked_list.reverse()
dlinked_list.print_list()

# Test removing dupes
print("Test removing dupes in doubly linked list")
d_lst = DoublyLinkedList()
d_lst.insert_at_head(7)
d_lst.insert_at_head(7)
d_lst.insert_at_head(7)
d_lst.insert_at_head(22)
d_lst.insert_at_head(14)
d_lst.insert_at_head(21)
d_lst.insert_at_head(14)
d_lst.insert_at_head(7)
d_lst.print_list()
d_lst.remove_dups()
d_lst.print_list()
d_lst = DoublyLinkedList()
d_lst.insert_at_head(7)
d_lst.print_list()
d_lst.remove_dups()
d_lst.print_list()
d_lst = DoublyLinkedList()
d_lst.print_list()
d_lst.remove_dups()
d_lst.print_list()
print("End test removing dupes in doubly linked lists")


print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print("TESTING LINKED LIST SET OPS")
print(STAR * LINE_LENGTH)
print("TESTING UNION")
lst = LinkedList()
lst.insert_at_head(5)
lst.insert_at_head(100)
lst.insert_at_head(8)
lst.insert_at_head(22)
d_lst = DoublyLinkedList()
d_lst.insert_at_head(7)
d_lst.insert_at_head(8)
d_lst.insert_at_head(7)
d_lst.insert_at_head(7)
d_lst.insert_at_head(22)
d_lst.insert_at_head(14)
d_lst.insert_at_head(21)
d_lst.insert_at_head(14)
d_lst.insert_at_head(7)
d_lst2 = DoublyLinkedList()
d_lst2.insert_at_head(8)
d_lst2.insert_at_head(8)
d_lst2.insert_at_head(8)
d_lst.print_list()
d_lst2.print_list()
result = union(d_lst, d_lst2)
result.print_list()
result = union(lst, d_lst2)
result.print_list()
print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print("TESTING INTERSET")
result = intersect(d_lst, d_lst2)
result.print_list()
result = intersect(d_lst, lst)
result.print_list()
result = intersect(d_lst2, lst)
result.print_list()
print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print("DONE TESTING LIST SET OPS")
print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print(STAR * LINE_LENGTH)
print("TESTING FIND Nth Node from End Op")
lst = LinkedList()
lst.insert_at_head(5)
lst.insert_at_head(100)
lst.insert_at_head(8)
lst.insert_at_head(22)
d_lst = DoublyLinkedList()
d_lst.insert_at_head(7)
d_lst.insert_at_head(8)
d_lst.insert_at_head(7)
d_lst.insert_at_head(7)
d_lst.insert_at_head(22)
d_lst.insert_at_head(14)
d_lst.insert_at_head(21)
d_lst.insert_at_head(14)
d_lst.insert_at_head(7)
d_lst2 = DoublyLinkedList()
d_lst2.insert_at_head(8)
d_lst2.insert_at_head(8)
d_lst2.insert_at_head(8)
result = find_nth_node_from_end(lst, 1)
lst.print_list()
result = find_nth_node_from_end(d_lst, 10)
d_lst.print_list()
result = find_nth_node_from_end(d_lst, 4)
d_lst.print_list()
print(result)
lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)
lst.print_list()
print(find_nth_node_from_end(lst, 5))
print(find_nth_node_from_end(lst, 1))
print(find_nth_node_from_end(lst, 10))

