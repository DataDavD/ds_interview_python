import pytest

from ds_coding_interviews_in_python.ch4stackqueue.queue import Queue, QueueStack, reverse_k


@pytest.fixture
def queue() -> Queue:
    q = Queue()
    for i in range(1, 11):
        q.enqueue(i)
    return q


@pytest.fixture
def queue_stack() -> QueueStack:
    qs = QueueStack()
    for i in range(1, 11):
        qs.enqueue(i)
    return qs


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


def test_reverse_k(queue) -> None:
    result = reverse_k(queue, 5)
    assert result.dequeue() == 5


def test_reverse_k_emtpy() -> None:
    queue = Queue()
    assert reverse_k(queue, 5) is None


def test_reverse_k_neg_k(queue) -> None:
    k = -1
    assert reverse_k(queue, k) is None


def test_reverse_k_too_large_k(queue) -> None:
    k = 100
    assert reverse_k(queue, k) is None


def test_queue_stack_size(queue_stack) -> None:
    assert queue_stack.size() == 10


def test_queue_stack_enqueue(queue_stack) -> None:
    queue_stack.enqueue(10)
    assert queue_stack.size() == 11


def test_queue_stack_dequeue(queue_stack) -> None:
    result = queue_stack.dequeue()
    assert result == 1
    assert queue_stack.size() == 9
