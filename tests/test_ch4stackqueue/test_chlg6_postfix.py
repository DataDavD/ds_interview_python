import pytest

from ds_coding_interviews_in_python.ch4stackqueue.chlg6_postfix import eval_postfix


def test_eval_postfix() -> None:
    test_exp = "921*-8-4+"
    assert eval_postfix(test_exp) == 3


def test_eval_postfix_one_val() -> None:
    test_exp = "1"
    assert eval_postfix(test_exp) == 1


def test_eval_postfix_except() -> None:
    with pytest.raises(TypeError):
        eval_postfix("921*-8--4+")
