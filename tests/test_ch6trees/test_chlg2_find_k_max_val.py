import pytest

from ds_coding_interviews_in_python.ch6trees.bst import BinarySearchTree
from ds_coding_interviews_in_python.ch6trees.chlg2_find_k_max_val import find_k_max_val_iter


@pytest.fixture
def bst() -> BinarySearchTree:
    bst = BinarySearchTree(5)
    bst.iter_insert(3)
    bst.iter_insert(7)
    bst.iter_insert(10)
    bst.iter_insert(15)
    bst.iter_insert(20)
    bst.iter_insert(21)
    bst.iter_insert(25)

    return bst


# Use with commented out tests below, code currently needs work to fix/run
# @pytest.fixture
# def counter() -> None:
#     print("\nsetting up global var counter")
#     counter = 0
#     yield counter
#     print("finishing up test set up counter")
#
#
# @pytest.fixture
# def current_max() -> None:
#     print("\nsetting up global var curr max")
#     current_max = None
#     yield current_max
#     print("finishing up test curr max")


def test_find_k_max_val_iter(bst) -> None:
    assert find_k_max_val_iter(bst.root, 3) == 20


def test_find_k_max_val_iter_k_zero(bst) -> None:
    assert find_k_max_val_iter(bst.root, 0) is None


def test_find_k_max_val_iter_k_too_great(bst) -> None:
    assert find_k_max_val_iter(bst.root, 10) is None


def test_find_k_max_val_iter_k_is_none(bst) -> None:
    assert find_k_max_val_iter(bst.root, None) is None


# Deal with later since these tests don't run properly since
# they make use of global variables
# def test_find_k_max_val_recursive(bst, counter, current_max) -> None:
#     assert find_k_max_val_recursive(bst.root, 3) == 20
#
#
# def test_find_k_max_val_recursive_k_zero(bst, counter, current_max) -> None:
#     assert find_k_max_val_recursive(bst.root, 0) is None
#
#
# def test_find_k_max_val_recursive_k_too_great(bst, counter, current_max) -> None:
#     assert find_k_max_val_recursive(bst.root, 10) is None
#
#
# def test_find_k_max_val_recursive_k_is_none(bst, counter, current_max) -> None:
#     assert find_k_max_val_recursive(bst.root, None) is None
