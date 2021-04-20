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


def sort_stack(stk: Optional[Stack]) -> Optional[Stack]:
    """
    Sort stack in ascending order so that when elements are popped out they are
    shown in ascending order. Uses a temp stack to order elements in descending order.
    Inner and outer loops traverse all n elements of the stack, so time complexity is
    O(n^2)
    :return: Optional[Stack
    """
    temp_stack = Stack()

    while stk.is_empty() is False:
        curr_val = stk.pop()
        if temp_stack.top() is not None and curr_val >= int(temp_stack.top()):
            temp_stack.push(curr_val)
        else:
            while temp_stack.is_empty() is False:
                stk.push(temp_stack.pop())
            temp_stack.push(curr_val)

    while not temp_stack.is_empty():
        stk.push(temp_stack.pop())

    return stk


def insert(stk: Optional[Stack], value) -> Optional[Stack]:
    if stk.is_empty() or value < stk.top():
        stk.push(value)
    else:
        temp_val = stk.pop()
        insert(stk, value)
        stk.push(temp_val)

    return stk


def sort_stack_recursive(stk: Optional[Stack]) -> Optional[Stack]:

    if stk.is_empty() is False:
        # Pop the top element off the stack
        val = stk.pop()

        # Sort the remaining stack recursively
        sort_stack_recursive(stk)

        # Push the top element back into the sorted stack
        insert(stk, val)

    return stk
