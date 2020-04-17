import pytest
from n_vector import Vector, SizeException


@pytest.fixture(scope='module')
def create_vector():
    a = Vector(3, [1, 2, 3])
    b = Vector(3, [4, 5, 6])
    c = Vector(2, [1, 2])

    return a, b, c


def test_sum(create_vector):
    assert create_vector[0] + create_vector[1] == Vector(3, [5, 7, 9])
    assert create_vector[0] + create_vector[2] == SizeException('summarize')


def test_len(create_vector):
    assert len(create_vector[0]) == 3


def test_abs(create_vector):
    assert abs(create_vector[0]) == 6 ** 0.5


def test_subs(create_vector):
    assert create_vector[0] - create_vector[1] == Vector(3, [-3, -3, -3])
    assert create_vector[0] - create_vector[2] == SizeException('subtract')


def test_mul(create_vector):
    assert create_vector[0] * 5 == Vector(3, [5, 10, 15])


def test_scal_mul(create_vector):
    assert create_vector[0] * create_vector[1] == 32
    assert create_vector[0] * create_vector[2] == SizeException('multiply')


def test_equal(create_vector):
    assert (create_vector[0] == create_vector[1]) is False


def test_get_item(create_vector):
    assert create_vector[0][1] == 2


def test_str(create_vector):
    assert str(create_vector[0]) == '(1; 2; 3)'

