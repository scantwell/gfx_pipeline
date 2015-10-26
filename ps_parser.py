import re
from old.line import Line
from old.point2d import Point2D


class PostscriptParser(object):

    @staticmethod
    def parse(fname):
        retval = []
        with open(fname, 'r', 0) as file:
            content = PostscriptParser._strip(file)
            for line in content:
                tokens = line.split()
                name = tokens[-1:][0]
                if name.lower() == 'line':
                    tokens = map(float, tokens[:-1])
                    pt0 = Point2D(tokens[0], tokens[1])
                    pt1 = Point2D(tokens[2], tokens[3])
                    retval.append(Line(pt0, pt1))
                else:
                    raise RuntimeError('Failed to parse line. Got {} instead.'.format(name))
        return retval

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
