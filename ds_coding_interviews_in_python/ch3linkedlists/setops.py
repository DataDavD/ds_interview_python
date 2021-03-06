from typing import Any, Optional, Union

from ds_coding_interviews_in_python.ch3linkedlists.linkedlist import DoublyLinkedList, LinkedList


def union(
    list_1: Union[LinkedList, DoublyLinkedList], list_2: Union[LinkedList, DoublyLinkedList]
) -> Union[LinkedList, DoublyLinkedList]:
    # O(l^2) where l = m + n
    # and m and n are the sizes of list_1 and list_2, respectively
    # the ^2 part is because we have to traverse the whole union list
    # in order to remove duplicates
    if list_1.is_empty():
        print("list_1 is empty, returning list_2")
        return list_2
    elif list_2.is_empty():
        print("list_2 is empty, returning list_1")
        return list_1

    start = list_1.get_head()

    while start.next_element:
        start = start.next_element

    # Link last element of first list to head of second list
    start.next_element = list_2.get_head()
    list_1.remove_dups()
    return list_1


def intersect(
    list_1: Union[LinkedList, DoublyLinkedList], list_2: Union[LinkedList, DoublyLinkedList]
) -> Optional[Union[LinkedList, DoublyLinkedList]]:
    # Max(O(mn), O(min(m, n)^2)), where m and n are the sizes of
    # list_1 and list_2, respectively
    if list_1.is_empty():
        print("list_1 is empty, nothing to return since there is no intersection")
        return None
    elif list_2.is_empty():
        print("list_2 is empty, nothing to return since there is no intersection")
        return None
    result = LinkedList()
    curr = list_1.get_head()

    # Traverse list_1 while searchingn list_2
    # and insert in result if value matches/exists
    while curr is not None:
        val = curr.data
        if list_2.search(val):
            result.insert_at_head(val)
        curr = curr.next_element

    # Remove any dupes
    result.remove_dups()
    if len(result) > 0:
        print(f"intersection of {list_1.to_list()} and {list_2.to_list()} found!")
        return result
    else:
        print("no intersection found !")
    return result


def find_nth_node_from_end(lst: Union[LinkedList, DoublyLinkedList], n: int) -> Any:
    # Double Iteration method
    # O(n)
    if lst.is_empty():
        print("list is empty")
        return -1

    ix_len = lst.__len__() - 1
    pos = ix_len - n + 1
    curr = lst.get_head()
    count = 0

    if pos < 0 or pos > ix_len:
        print(f"parameter value provided: {n}, exceeds list length")
        return -1

    while count != pos:
        curr = curr.next_element
        count += 1

    if curr:
        return curr.data
    else:
        return -1
