import sys
from typing import Any


class TwoStacks:
    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = self.size

    # Method to push an element x to stack1
    def push1(self, x) -> None:

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow")
            sys.exit("Stack Overflow")

    # Method to push an element x to stack2
    def push2(self, x) -> None:

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow")
            sys.exit("Stack Overflow")

    # Method to pop an element from first stack
    def pop1(self) -> Any:
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow")
            sys.exit("Stack Underflow")

    # Method to pop an element from second stack
    def pop2(self) -> Any:
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow")
            sys.exit("Stack Underflow")
