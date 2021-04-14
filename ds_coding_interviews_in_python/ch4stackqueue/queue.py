from typing import Any, List, Optional


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
