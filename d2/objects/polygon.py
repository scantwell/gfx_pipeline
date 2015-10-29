from algorithms import dda, sutherland_hodgman

class Polygon(object):

    def __init__(self, points):
        if points[0].x() == points[-1].x() and points[0].y() == points[-1].y():
            points = points[:-1]
        assert len(points) > 2
        self._points = points

    def __str__(self):
        return 'Polygon: \n  Points {} '.format(self._points)

    def clip(self, xmin, xmax, ymin, ymax):
        self._points = sutherland_hodgman(self._points, xmin, xmax, ymin, ymax)

    def rotate(self, degrees):
        for p in self._points:
            p.rotate(0, 0, degrees)

    def scale(self, sx, sy):
        for p in self._points:
            p.scale(0, 0, sx, sy)

    def scan_convert(self):
        points = set()
        if len(self._points) == 0:
            return points
        start = self._points[-1]
        for vertex in self._points:
            points.update(dda(start.x(), start.y(), vertex.x(), vertex.y()))
            start = vertex
        return points

    def translate(self, dx, dy):
        for p in self._points:
            p.translate(dx, dy)
