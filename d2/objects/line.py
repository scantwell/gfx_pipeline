from d2.point2d import Point2D
from algorithms import cohen_sutherland, dda

class Line(object):

    def __init__(self, start, end):
        assert isinstance(start, Point2D) and isinstance(end, Point2D)
        self._start = start
        self._end = end

        if self._start.x() > self._end.x():
            self._start, self._end = self._end, self._start

    def __str__(self):
        return 'Line: \n    Start {}\n    End   {} '.format(self._start, self._end)

    def clip(self, xmin, xmax, ymin, ymax):
        x0, y0, x1, y1 = cohen_sutherland(self._start.x(),
                                          self._start.y(),
                                          self._end.x(),
                                          self._end.y(),
                                          xmin,
                                          ymin,
                                          xmax,
                                          ymax)
        if x0 is None:
            raise RuntimeError()
        else:
            self._start = Point2D(x0, y0)
            self._end = Point2D(x1, y1)


    def end(self):
        return self._end.x(), self._end.y()

    def rotate(self, degrees):
        self._start.rotate(self._start.x(), self._start.y(), degrees)
        self._end.rotate(self._start.x(), self._end.y(), degrees)

        if self._start.x() > self._end.x():
            self._start, self._end = self._end, self._start

    def scale(self, sx, sy):
        self._start.scale(self._start.x(), self._start.y(), sx, sy)
        self._end.scale(self._start.x(), self._start.y(), sx, sy)

    def scan_convert(self):
        return dda(self._start.x(), self._start.y(), self._end.x(), self._end.y())

    def start(self):
        return self._start.x(), self._start.y()

    def translate(self, dx, dy):
        self._start.translate(dx, dy)
        self._end.translate(dx, dy)