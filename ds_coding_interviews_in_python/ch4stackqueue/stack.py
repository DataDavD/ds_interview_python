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


def sort_stack(stack: Optional[Stack]) -> Optional[Stack]:
    """
    Sort stack in ascending order so that when elements are popped out they are
    shown in ascending order
    :return: Optional[Stack
    """
    temp_stack = Stack()

    while not stack.is_empty():
        curr_val = stack.pop()
        if temp_stack.top() is not None and curr_val >= int(temp_stack.top()):
            temp_stack.push(curr_val)
        else:
            while not temp_stack.is_empty():
                stack.push(temp_stack.pop())
            temp_stack.push(curr_val)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack
