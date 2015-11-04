from algorithms import dda, sutherland_hodgman, find_intersection


class Polygon(object):

    def __init__(self, points):
        if points[0].x() == points[-1].x() and points[0].y() == points[-1].y():
            points = points[:-1]
        assert len(points) > 2
        self._points = points

    def __str__(self):
        return 'Polygon: \n  Points {} '.format(map(str, self._points))

    def clip(self, xmin, xmax, ymin, ymax):
        self._points = sutherland_hodgman(self._points, xmin, xmax, ymin, ymax)

    def rotate(self, degrees):
        for p in self._points:
            p.rotate(0, 0, degrees)

    def scale(self, sx, sy):
        for p in self._points:
            p.scale(0, 0, sx, sy)

    def scan_convert_dda(self):
        points = set()
        if len(self._points) == 0:
            return points
        start = self._points[-1]
        for vertex in self._points:
            points.update(dda(start.x(), start.y(), vertex.x(), vertex.y()))
            start = vertex
        return points

    def scan_convert(self):
        points = set()
        if len(self._points) == 0:
            return points
        self._round_points_to_integers()
        y_dim = [v.y() for v in self._points]
        ymin = min(y_dim)
        ymax = max(y_dim)
        for y in range(0, 501):
            extrema = self.get_extrema(y, ymin, ymax)
            even_bit = 0
            for x in range(0, 501):
                while len(extrema) and extrema[0][0] == x:
                    even_bit = not even_bit
                    extrema.remove(extrema[0])
                if even_bit == 1:
                    points.add((x, y))
        return points

    def get_extrema(self, y, ymin, ymax):
        extrema = []
        start = self._points[-1]
        for end in self._points:
            # Horizontal line
            if (end.y() - start.y()) == 0:
                pass
            # Intersecting the top point we do not include
            elif y == max([end.y(), start.y()]):
                pass
            elif ymin <= y and y < ymax:
                try:
                    ex, ey = find_intersection(start.x(), start.y(), end.x(), end.y(), 0, y, 501, y)
                    extrema.append((round(ex), round(ey)))
                except ArithmeticError:
                    pass
            start = end
        extrema.sort(key=lambda tup: tup[0])
        return extrema

    def to_screen_coords(self, m_matrix):
        for p in self._points:
            p.dot(m_matrix)

    def translate(self, dx, dy):
        for p in self._points:
            p.translate(dx, dy)


# Private

    def _round_points_to_integers(self):
        for p in self._points:
            p.round()