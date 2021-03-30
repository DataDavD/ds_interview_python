from ds_coding_interviews_in_python.ch2lists.chlg8_rrotate import right_rotate, right_rotate_optimal


def test_right_rotate() -> None:
    lst = [10, 20, 30, 40, 50]
    k = 3
    expect = [30, 40, 50, 10, 20]
    assert right_rotate(lst, k) == expect

    lst2 = [10, 20, 30, 40, 50]
    k2 = 0
    expect2 = [10, 20, 30, 40, 50]
    assert right_rotate(lst2, k2) == expect2

    lst3 = list()
    k3 = 3
    expect3 = list()
    assert right_rotate(lst3, k3) == expect3

    lst4 = ['right', 'rotate', 'python']
    k4 = 4
    expect4 = ['python', 'right', 'rotate']
    assert right_rotate(lst4, k4) == expect4

def test_right_rotate_optimal() -> None:
    lst = [10, 20, 30, 40, 50]
    k = 3
    expect = [30, 40, 50, 10, 20]
    assert right_rotate_optimal(lst, k) == expect

    lst2 = [10, 20, 30, 40, 50]
    k2 = 0
    expect2 = [10, 20, 30, 40, 50]
    assert right_rotate_optimal(lst2, k2) == expect2

    lst3 = list()
    k3 = 3
    expect3 = list()
    assert right_rotate_optimal(lst3, k3) == expect3

    lst4 = ['right', 'rotate', 'python']
    k4 = 4
    expect4 = ['python', 'right', 'rotate']
    assert right_rotate_optimal(lst4, k4) == expect4
