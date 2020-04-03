import pytest
from n_vector import Vector


@pytest.fixture(scope='module')
def create_vector():
    a = Vector(3, [1, 2, 3])
    b = Vector(3, [4, 5, 6])
    return a, b


def test_sum(create_vector):
    assert create_vector[0] + create_vector[1] == Vector(3, [5, 7, 9])


def test_len(create_vector):
    assert len(create_vector[0]) == 3


def test_abs(create_vector):
    assert abs(create_vector[0]) == 6 ** 0.5
