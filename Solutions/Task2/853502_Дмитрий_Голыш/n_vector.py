import random


class SizeException(BaseException):
    def __init__(self, operation):
        self.info = 'You cannot ' + operation + ' vectors of different sizes!'


class Vector:
    def __init__(self, dimension, coordinates):
        self.dimension = dimension
        self.coordinates = coordinates[:]

    def __str__(self):
        str_vector = '('
        str_vector += '; '.join(map(str, self.coordinates))
        str_vector += ')'
        return str_vector

    def __getitem__(self, item):
        return self.coordinates[item]

    def __len__(self):
        return self.dimension

    def __add__(self, other):  # raise exception
        if len(self) == len(other):
            return Vector(self.dimension, [self[i] + other[i] for i in range(len(self))])
        else:
            raise SizeException('summarize')

    def __sub__(self, other):  # raise exception
        if len(self) == len(other):
            return Vector(self.dimension, [self[i] - other[i] for i in range(len(self))])
        else:
            raise SizeException('subtract')

    def __mul__(self, other):
        if isinstance(other, Vector):  # raise exception
            if len(self) == len(other):
                return sum([self[i] * other[i] for i in range(len(self))])
            else:
                raise SizeException('multiply')
        else:
            return Vector(self.dimension, [self[i] * other for i in range(len(self))])

    __rmul__ = __mul__

    def __abs__(self):
        return sum(self.coordinates) ** 0.5

    def __eq__(self, other):
        return (self.dimension == other.dimension) and (self.coordinates == other.coordinates)


def main():
    # n = random.randint(1, 10)
    n = 5
    # print(5 is 5)
    # print(abs(-8))

    temp = [random.randint(-10, 10) for _ in range(n)]
    n_vector_a = Vector(n, temp)

    n = random.randint(1, 10)
    temp = [random.randint(-10, 10) for _ in range(n)]
    n_vector_b = Vector(n, temp)

    print('a: ', n_vector_a)
    print('b: ', n_vector_b)

    print()

    try:
        print('a + b: ', n_vector_a + n_vector_b, '\n')
    except SizeException as se:
        print(se.info)

    try:
        print('a - b: ', n_vector_a - n_vector_b, '\n')
    except SizeException as se:
        print(se.info)

    try:
        print('a * b: ', n_vector_a * n_vector_b, '\n')
    except SizeException as se:
        print(se.info, '\n')

    print('a == b: ', n_vector_a == n_vector_b, '\n')

    print('b * 5: ', n_vector_b * 5, '\n')
    print('5 * a: ', 5 * n_vector_a, '\n')


if __name__ == '__main__':
    main()
