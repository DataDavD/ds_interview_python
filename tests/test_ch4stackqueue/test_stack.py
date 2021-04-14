import pytest

from ds_coding_interviews_in_python.ch4stackqueue.stack import Stack


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
