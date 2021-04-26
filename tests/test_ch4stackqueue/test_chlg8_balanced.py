from ds_coding_interviews_in_python.ch4stackqueue.chlg8_balanced import (
    is_balanced,
    is_balanced_other_solution,
)


def test_is_balanced_true() -> None:
    exp = "{[({})]}"
    assert is_balanced(exp) is True


def test_is_balanced_false() -> None:
    exp = "{[({})}"
    assert is_balanced(exp) is False


def test_is_balanced_false_2() -> None:
    exp = "({[}])"
    assert is_balanced(exp) is False


def test_is_balanced_false_3() -> None:
    exp = "{[([({))]}}"
    assert is_balanced(exp) is False


def test_is_balanced_empty() -> None:
    exp = ""
    assert is_balanced(exp) is True


def test_is_balanced_other_solution_true() -> None:
    exp = "{[({})]}"
    assert is_balanced_other_solution(exp) is True


def test_is_balanced_other_solution_false() -> None:
    exp = "{[({})}"
    assert is_balanced_other_solution(exp) is False


def test_is_balanced_other_solution_false_2() -> None:
    exp = "({[}])"
    assert is_balanced_other_solution(exp) is False


def test_is_balanced_other_solution_false_3() -> None:
    exp = "{[([({))]}}"
    assert is_balanced_other_solution(exp) is False


def test_is_balanced_other_solution_empty() -> None:
    exp = ""
    assert is_balanced_other_solution(exp) is True
