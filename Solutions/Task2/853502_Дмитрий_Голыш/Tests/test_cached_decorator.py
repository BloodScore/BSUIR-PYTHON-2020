from cached_decorator import sum_func


def test_sum_func():
    assert sum_func(1, 2, 3)[0] == 6
    assert sum_func(0)[0] == 0
    assert sum_func(88, 12, 1)[0] == 101


def test_decorator():
    assert sum_func(0)[1] is False
    assert sum_func(1, 2, 3)[1] is False
    assert sum_func(1, 2, 3)[1] is True
    assert sum_func(4)[1] is False
    assert sum_func(4)[1] is True
