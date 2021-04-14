from typing import Any, List, Optional


class Stack:
    """
    Stack uses a Python list as main structure.
    End of stack_list is considered top of stack
    """

    def __init__(self) -> None:
        self.stack_list: List[Any] = list()

    def is_empty(self) -> bool:
        return self.size() == 0

    def top(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self) -> int:
        return len(self.stack_list)

    def push(self, value) -> None:
        self.stack_list.append(value)

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return None
        return self.stack_list.pop()
