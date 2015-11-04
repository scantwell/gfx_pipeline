from numpy import matrix, cos, sin, radians, rint


class Point2D(object):

    def __init__(self, x, y):
        assert isinstance(x, int) or isinstance(x, float)
        assert isinstance(y, int) or isinstance(y, float)
        self._matrix = matrix([[x], [y], [1]])

    def __str__(self):
        return '({}, {})'.format(self._matrix.item(0), self._matrix.item(1))

    def round(self):
        self._matrix = self._matrix.round().astype(int)

    def rotate(self, x, y, degrees):
        rads = radians(degrees)
        #rotation_matrix = matrix([[cos(rads), -1 * sin(rads), (x * (1 - cos(rads)) + y * sin(rads))],
        #                          [sin(rads), cos(rads), (y * (1 - cos(rads)) - x * sin(rads))],
        #                          [0, 0, 1]])
        rotation_matrix = matrix([[cos(rads), -1 * sin(rads), 0],
                                  [sin(rads), cos(rads), 0],
                                  [0, 0, 1]])
        self._matrix = rotation_matrix.dot(self._matrix)

    def scale(self, x, y, sx, sy):
        #scale_matrix = matrix([[sx, 0, x*(1-sx)],
        #                       [0, sy, y*(1-sy)],
        #                       [0, 0, 1]])
        scale_matrix = matrix([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
        self._matrix = scale_matrix.dot(self._matrix)

    def translate(self, dx, dy):
        translation_matrix = matrix([[1, 0, dx],
                                     [0, 1, dy],
                                     [0, 0, 1]])
        self._matrix = translation_matrix.dot(self._matrix)

    def dot(self, mul):
        self._matrix = mul.dot(self._matrix)

    def x(self):
        return self._matrix.item(0)

    def y(self):
        return self._matrix.item(1)
