import pytest

from ds_coding_interviews_in_python.ch3linkedlists.linkedlist import LinkedList


@pytest.fixture
def linked_list() -> LinkedList:
    linked_list = LinkedList()
    for i in range(1, 11):
        linked_list.insert_at_head(i)
    return linked_list


def test_get_head(linked_list) -> None:
    assert linked_list.get_head().data == 10
