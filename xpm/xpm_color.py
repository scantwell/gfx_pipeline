__author__ = 'stephencantwell'


class XPMColor(object):

    def __init__(self, symbol, rgb):
        assert isinstance(symbol, str)
        assert isinstance(rgb, str)
        self.symbol = symbol
        self.rgb = rgb
