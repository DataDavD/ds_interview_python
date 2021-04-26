from typing import Any, List, Optional, Union


class MyStack:
    """
    MyStack uses a Python list as main structure.
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


class MinStack(MyStack):
    """
    MinStack inherits from MyStack and changes pop and push methods to construct
    a min method that returns the minimum value in the stack in O(1) time complexity.
    """

    def __init__(self) -> None:
        super().__init__()
        self.temp_stack = MyStack()

    def push(self, value) -> None:
        if self.is_empty():
            self.stack_list.append(value)
            self.temp_stack.push(value)

        else:
            if value > self.temp_stack.top():
                temp_val = self.temp_stack.pop()
                self.temp_stack.push(value)
                if temp_val:
                    self.temp_stack.push(temp_val)

            else:
                self.temp_stack.push(value)

            self.stack_list.append(value)

    def pop(self) -> Optional[Any]:
        if self.is_empty():
            return None

        if self.top() == self.temp_stack.top():
            self.temp_stack.pop()
            return self.stack_list.pop()
        else:
            return self.stack_list.pop()

    def min(self) -> Optional[Union[int, float]]:
        if self.is_empty():
            print("Stack is empty, no minimu, returning -1")
            return None
        else:
            return self.temp_stack.top()


class MinStack2:
    # Another way to create MinStack
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()

    # Removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.top() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.top())

    # Returns minimum value in O(1) Time
    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.top()
        # In case the stack is empty
        return None


def sort_stack(stk: MyStack) -> MyStack:
    """
    Sort stack in ascending order so that when elements are popped out they are
    shown in ascending order. Uses a temp stack to order elements in ascending order.
    Inner and outer loops traverse all n elements of the stack, so time complexity is
    O(n^2)

    :param stk: Stack
    :return: Stack
    """
    temp_stack = MyStack()

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


def insert(stk: MyStack, value) -> MyStack:
    if stk.is_empty() or value < stk.top():
        stk.push(value)
    else:
        temp_val = stk.pop()
        insert(stk, value)
        stk.push(temp_val)

    return stk


def sort_stack_recursive(stk: MyStack) -> MyStack:
    """
    Sort stack in ascending order so that when elements are popped out they are
    shown in ascending order. Uses a temp stack to order elements in ascending order.
    Function is recursively called on all n elements. So, in the worst case, there are n
    calls to insert for each element. This pushes the time complexity to O(n^2). However,
    unliked sort_stack function space complexity is constant, O(1).

    :param stk: Stack
    :return: Stack
    """

    if stk.is_empty() is False:
        # Pop the top element off the stack
        val = stk.pop()

        # Sort the remaining stack recursively
        sort_stack_recursive(stk)

        # Push the top element back into the sorted stack
        insert(stk, val)

    return stk
