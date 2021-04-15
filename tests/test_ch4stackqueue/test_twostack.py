import pytest

from ds_coding_interviews_in_python.ch4stackqueue.twostack import TwoStacks


@pytest.fixture
def two_stack() -> TwoStacks:
    two_stack = TwoStacks(20)
    for i in range(1, 11):
        two_stack.push1(i)
    for i in range(11, 21):
        two_stack.push2(i)
    return two_stack


def test_pop1(two_stack) -> None:
    result = two_stack.pop1()
    assert result == 10


def test_pop2(two_stack) -> None:
    result = two_stack.pop2()
    assert result == 20


def test_stack_overflow_1(two_stack) -> None:
    with pytest.raises(SystemExit) as pytest_wrapped_sysexist:
        two_stack.push1(100)
    assert pytest_wrapped_sysexist.type == SystemExit
    assert pytest_wrapped_sysexist.value.code == "Stack Overflow"


def test_stack_overflow_2(two_stack) -> None:
    with pytest.raises(SystemExit) as pytest_wrapped_sysexist:
        two_stack.push2(100)
    assert pytest_wrapped_sysexist.type == SystemExit
    assert pytest_wrapped_sysexist.value.code == "Stack Overflow"


def test_stack_underflow_1() -> None:
    two_stack = TwoStacks(0)
    with pytest.raises(SystemExit) as pytest_wrapped_sysexist:
        two_stack.pop1()
    assert pytest_wrapped_sysexist.type == SystemExit
    assert pytest_wrapped_sysexist.value.code == "Stack Underflow"


def test_stack_underflow_2() -> None:
    two_stack = TwoStacks(0)
    with pytest.raises(SystemExit) as pytest_wrapped_sysexist:
        two_stack.pop2()
    assert pytest_wrapped_sysexist.type == SystemExit
    assert pytest_wrapped_sysexist.value.code == "Stack Underflow"
