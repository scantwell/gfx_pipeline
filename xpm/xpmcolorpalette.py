__author__ = 'stephencantwell'
from xpm_color import XPMColor


class XPMColorPalette(object):

    def __init__(self, background=XPMColor('w', '#FFFFFF')):
        self.symbols = []
        self.colors = []
        self.background = background
        self.symbols.append(background.symbol)
        self.colors.append(background)

    def add_color(self, symbol, rgb):
        if symbol in self.symbols:
            raise RuntimeError('Symbol has already been defined.')
        self.symbols.append(symbol)
        self.colors.append(XPMColor(symbol, rgb))
