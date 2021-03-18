from ds_coding_interviews_in_python.ch2lists.chlg4_find_list_prods import (
    find_product,
    find_product_sol1,
    find_product_sol2,
)


def test_find_product() -> None:
    lst = [1, 2, 3, 4]
    lst2 = [4, 2, 1, 5, 0]
    result = [24, 12, 8, 6]
    result2 = [0, 0, 0, 0, 40]
    assert find_product(lst) == result
    assert find_product(lst2) == result2

    assert find_product_sol1(lst) == result
    assert find_product_sol1(lst2) == result2

    assert find_product_sol2(lst) == result
    assert find_product_sol2(lst2) == result2
