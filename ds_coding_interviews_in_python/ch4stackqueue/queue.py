from typing import Any, List, Optional

from ds_coding_interviews_in_python.ch4stackqueue.stack import Stack


class Queue:
    """
    Queue uses a Python list as main structure.
    """

    def __init__(self) -> None:
        self.queue_list: List[Any] = list()

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return len(self.queue_list)

    def front(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.queue_list[0]

    def back(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.queue_list[-1]

    def enqueue(self, value) -> None:
        self.queue_list.append(value)

    def dequeue(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.queue_list.pop(0)


def reverse_k(queue: Queue, k: int) -> Optional[Queue]:
    """reverse_k reverses the first k elements of queue

    :param queue: Queue
    :param k: number of elements in Queue to reverse
    :return: Queue
    """
    if queue.is_empty():
        print("Queue is empty, nothing to reverse")
        return None

    # Use stack to help with those elements that need to be reversed
    stack: Stack = Stack()
    for i in range(k):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    for i in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

    return queue
