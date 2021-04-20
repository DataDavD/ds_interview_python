import pytest

from ds_coding_interviews_in_python.ch4stackqueue.stack import (
    Stack,
    sort_stack,
    sort_stack_recursive,
)


@pytest.fixture
def stack() -> Stack:
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    return stack


def test_is_empty() -> None:
    stack = Stack()
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


def test_sort_stack() -> None:
    stack = Stack()
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
    stack = Stack()
    result = list()
    stack = sort_stack(stack)
    test_list = list()
    for i in range(stack.size()):
        test_list.append(stack.pop())
    assert test_list == result


def test_sort_stack_recursive() -> None:
    stack = Stack()
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
    stack = Stack()
    result = list()
    stack = sort_stack_recursive(stack)
    test_list = list()
    for i in range(stack.size()):
        test_list.append(stack.pop())
    assert test_list == result
