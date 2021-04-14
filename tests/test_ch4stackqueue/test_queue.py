import pytest

from ds_coding_interviews_in_python.ch4stackqueue.queue import Queue


@pytest.fixture
def queue() -> Queue:
    q = Queue()
    for i in range(1, 11):
        q.enqueue(i)
    return q


def test_is_empty() -> None:
    q = Queue()
    assert q.is_empty() is True


def test_front(queue) -> None:
    assert queue.front() == 1


def test_back(queue) -> None:
    assert queue.back() == 10


def test_size(queue) -> None:
    assert queue.size() == 10


def test_enqueue(queue) -> None:
    queue.enqueue(20)
    assert queue.size() == 11
    assert queue.back() == 20


def test_dequeue(queue) -> None:
    result = queue.dequeue()
    assert result == 1
