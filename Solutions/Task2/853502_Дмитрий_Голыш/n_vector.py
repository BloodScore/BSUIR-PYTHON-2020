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

