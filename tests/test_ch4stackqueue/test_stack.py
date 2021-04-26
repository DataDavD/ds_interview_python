from typing import List

import pytest

from ds_coding_interviews_in_python.ch4stackqueue.stack import (
    MinStack,
    MyStack,
    sort_stack,
    sort_stack_recursive,
)


@pytest.fixture
def stack() -> MyStack:
    stack = MyStack()
    for i in range(1, 11):
        stack.push(i)
    return stack


@pytest.fixture
def min_stack() -> MinStack:
    stack = MinStack()
    for i in range(1, 11):
        stack.push(i)
    return stack


def test_is_empty() -> None:
    stack = MyStack()
    assert stack.is_empty() is True


def test_top(stack) -> None:
    assert stack.top() == 10


def test_size(stack) -> None:
    assert stack.size() == 10


def test_push(stack) -> None:
    stack.push(20)
    assert stack.size() == 11
    assert stack.top() == 20


def test_pop(stack) -> None:
    result = stack.pop()
    assert result == 10


def test_min_stack_is_empty() -> None:
    stack = MinStack()
    assert stack.is_empty() is True


def test_min_stack_top(min_stack) -> None:
    assert min_stack.top() == 10


def test_min_stack_size(min_stack) -> None:
    assert min_stack.size() == 10


def test_min_stack_push(min_stack) -> None:
    min_stack.push(20)
    assert min_stack.size() == 11
    assert min_stack.top() == 20


def test_min_stack_pop(min_stack) -> None:
    result = min_stack.pop()
    assert result == 10


def test_min_stack_min() -> None:
    min_stack = MinStack()
    min_stack.push(-1)
    min_stack.push(-5)
    min_stack.push(-100)
    min_stack.pop()
    min_stack.pop()
    min_stack.push(-1000)
    for i in range(1, 11):
        min_stack.push(i)
    assert min_stack.min() == -1000


def test_min_stack_min_2() -> None:
    min_stack = MinStack()
    min_stack.push(9)
    min_stack.push(3)
    min_stack.push(1)
    min_stack.push(4)
    min_stack.push(2)
    min_stack.push(5)
    assert min_stack.min() == 1


def test_min_stack_min_none() -> None:
    min_stack = MinStack()
    assert min_stack.min() is None


def test_sort_stack() -> None:
    stack = MyStack()
    stack.push(10)
    stack.push(100)
    stack.push(15)
    stack.push(5)
    stack.push(21)
    result = [5, 10, 15, 21, 100]
    stack = sort_stack(stack)
    test_list = list()
    for i in range(stack.size()):
        test_list.append(stack.pop())
    assert test_list == result


def test_sort_stack_none() -> None:
    stack = MyStack()
    result: List[int] = list()
    stack = sort_stack(stack)
    test_list = list()
    for i in range(stack.size()):
        test_list.append(stack.pop())
    assert test_list == result


def test_sort_stack_recursive() -> None:
    stack = MyStack()
    stack.push(10)
    stack.push(100)
    stack.push(15)
    stack.push(5)
    stack.push(21)
    result = [5, 10, 15, 21, 100]
    stack = sort_stack_recursive(stack)
    test_list = list()
    for i in range(stack.size()):
        test_list.append(stack.pop())
    assert test_list == result


def test_sort_stack_recursive_none() -> None:
    stack = MyStack()
    result: List[int] = list()
    stack = sort_stack_recursive(stack)
    test_list = list()
    for i in range(stack.size()):
        test_list.append(stack.pop())
    assert test_list == result
