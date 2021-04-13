from typing import Optional, Union

from ds_coding_interviews_in_python.ch3linkedlists.linkedlist import LinkedList, DoublyLinkedList


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
