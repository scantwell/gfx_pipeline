from xpmcolorpalette import XPMColorPalette


class XPMPrinter(object):

    HEADER = '/* XPM */ \nstatic char *sco100[] = {\n/* width height num_colors chars_per_pixel */'
    COLORS_HEADER = '/*colors */'
    PIXEL_HEADER = '/*pixels */'
    CLOSE = "};"

    def __init__(self, height, width, colors, colors_per_pixel=1):
        assert isinstance(height, int) and height > 0
        assert isinstance(width, int) and width > 0
        assert isinstance(colors, XPMColorPalette)
        self.colors_per_pixel = colors_per_pixel
        self.palette = colors
        self.matrix = self._create_matrix(height, width)

    def drawpixel(self, x, y):
        self.matrix[y][x] = 'b'

    def _create_matrix(self, h, w):
        retval = [None] * h
        for i in range(0, h):
            retval[i] = [self.palette.background.symbol] * w
        return retval

    def print_it(self):
        print XPMPrinter.HEADER
        print '"{} {} {} {}",'.format(len(self.matrix[0]), len(self.matrix), len(self.palette.colors), self.colors_per_pixel)
        print XPMPrinter.COLORS_HEADER
        for c in self.palette.colors:
            print '"{} c {}",'.format(c.symbol, c.rgb)
        print XPMPrinter.PIXEL_HEADER
        for r in self.matrix:
            print '"{}",'.format(''.join(r))
        print XPMPrinter.CLOSE

    def __str__(self):
        return str(self.matrix)
