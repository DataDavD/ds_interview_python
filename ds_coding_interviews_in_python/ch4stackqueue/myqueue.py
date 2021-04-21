from typing import Any, List, Optional

from ds_coding_interviews_in_python.ch4stackqueue.stack import MyStack


class MyQueue:
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


class QueueStack:
    def __init__(self):
        self.main_stack = MyStack()
        self.buff_stack = MyStack()

    def size(self):
        return self.main_stack.size() + self.buff_stack.size()

    def enqueue(self, value) -> bool:
        """"O(1) since just pushing off main stack"""
        self.main_stack.push(value)
        print(f"{value} has been enqueued")
        return True

    def dequeue(self) -> Any:
        """O(n) if temp_stack is empty, but O(1) if temp stack is not empty.
        The solution is more efficient than using two stacks in enqueue method
        since we just perform one transfer instead of two, and sometimes none at all"""
        if self.main_stack.is_empty() and self.buff_stack.is_empty():
            print("queue is empty, nothing to dequeue")
            return None
        elif not self.main_stack.is_empty() and self.buff_stack.is_empty():
            while not self.main_stack.is_empty():
                val = self.main_stack.pop()
                self.buff_stack.push(val)
            return self.buff_stack.pop()
        else:
            return self.buff_stack.pop()


def reverse_k(queue: MyQueue, k: int) -> Optional[MyQueue]:
    """reverse_k reverses the first k elements of queue. The time complexity
    is O(n) where n is the queue size as we iterate over the entire queue: k elements
    are iterated over first, then (queue size - k) elements last.

    :param queue: Queue
    :param k: number of elements in Queue to reverse
    :return: Queue
    """
    if queue.is_empty():
        print("Queue is empty, nothing to reverse")
        return None
    if k > queue.size():
        print(f"{k} exceeds the queues length of {queue.size()}")
        return None
    if k < 0:
        print(f"{k} is negative; reverse_k function requires k be positive")
        return None

    # Use stack to help with those elements that need to be reversed
    stack: MyStack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())

    for i in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

    return queue
