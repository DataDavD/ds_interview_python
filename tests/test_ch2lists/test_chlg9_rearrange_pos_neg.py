from ds_coding_interviews_in_python.ch2lists.chlg9_rearrange_pos_neg import (
    rearrange,
    rearrange_aux_lists,
    rearrange_inplace, rearrange_pythonic,
)


def test_rearrange() -> None:
    lst = [10, -1, 20, 4, 5, -9, -6]
    expect = [-6, -9, -1, 10, 20, 4, 5]
    assert rearrange(lst) == expect


def test_rearrange_aux() -> None:
    lst = [10, -1, 20, 4, 5, -9, -6]
    expect = [-1, -9, -6, 10, 20, 4, 5]
    assert rearrange_aux_lists(lst) == expect


def test_rearrange_inplace() -> None:
    lst = [10, -1, 20, 4, 5, -9, -6]
    expect = [-1, -9, -6, 4, 5, 10, 20]
    assert rearrange_inplace(lst) == expect

def test_rearrange_pythonic() -> None:
    lst = [10, -1, 20, 4, 5, -9, -6]
    expect = [-1, -9, -6, 10, 20, 4, 5]
    assert rearrange_pythonic(lst) == expect
