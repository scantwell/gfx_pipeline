import re

from d2.objects.line import Line
from d2.objects.polygon import Polygon
from d2.point2d import Point2D


class PostscriptParser(object):

    def __init__(self, fname):
        with open(fname, 'r', 0) as file:
            self._content = PostscriptParser._strip(file)
        self._index = 0

    def next_token(self):
        if self._index < len(self._content):
            line = self._content[self._index]
            self._index += 1
            return line.strip()
        else:
            raise StopIteration()

    def parse_objects(self):
        retval = []
        try:
            while True:
                line = self.next_token()
                tokens = line.split()
                name = tokens[-1:][0]
                pts = map(float, tokens[:-1])
                if name.lower() == 'moveto':
                    pt = Point2D(pts[0], pts[1])
                    retval.append(self._create_polygon(pt))
                elif name.lower() == 'line':
                    pt0, pt1 = Point2D(pts[0], pts[1]), Point2D(pts[2], pts[3])
                    retval.append(Line(pt0, pt1))
        except StopIteration:
            pass
        finally:
            return retval

    def _create_polygon(self, start):
        points = [start]
        line = self.next_token()
        while line != 'stroke':
            line = line.split()
            points.append(Point2D(float(line[0]), float(line[1])))
            line = self.next_token()
        return Polygon(points)

    @staticmethod
    def _strip(file):
        start_idx = 0
        end_idx = 0
        contents = file.readlines()
        for line in contents:
            if re.match(r'^\s*%\s*%\s*%\s*BEGIN\s*$', line):
                start_idx = contents.index(line) + 1
            if re.match(r'^\s*%\s*%\s*%\s*END\s*$', line):
                end_idx = contents.index(line)
        if end_idx == start_idx or end_idx < start_idx:
            raise RuntimeError('Could not find beginning of PS file.')
        return contents[start_idx:end_idx]
