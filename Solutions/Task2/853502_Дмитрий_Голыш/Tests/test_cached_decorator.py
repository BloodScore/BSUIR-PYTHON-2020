from cached_decorator import sum_func


def test_decorator():
    assert sum_func(1, 2, 3, first=5) == 11
    assert sum_func(1, 2, 3, 5) == 11
    assert sum_func(1) == 1
    assert sum_func(5, 43) == 48
    assert sum_func(3, 2, first=1, fourth=5) == 11
    assert sum_func(43, 5) == 48

