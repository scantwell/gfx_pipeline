#! /usr/bin/python

import argparse
from numpy import matrix
from ps_parser import PostscriptParser
from xpm.xpm_printer import XPMPrinter
from xpm.xpmcolorpalette import XPMColorPalette


def apply_transformations(objects, options):
    for obj in objects:
        obj.scale(options.scale, options.scale)
        obj.rotate(options.rotate)
        obj.translate(options.trans_x, options.trans_y)


def clip(world, options):
    clipped_world = []
    for obj in world:
        try:
            obj.clip(options.wl, options.wr, options.wb, options.wt)
            clipped_world.append(obj)
        except RuntimeError:
            pass
    return clipped_world


def draw(points, xpm, options):
    for x, y in points:
        xpm.drawpixel(x, abs(y - 501))


def to_screen_coords(world, options):
    trans_matrix = matrix([[float(options.sr - options.sl)/(options.wr - options.wl), 0, (-1 * options.wl) * float(options.sr - options.sl)/(options.wr - options.wl) + options.sl],
                       [0, float(options.st - options.sb)/(options.wt - options.wb), (-1 * options.wb) * float(options.st - options.sb)/(options.wt - options.wb) + options.sb],
                       [0, 0, 1]])
    for obj in world:
        obj.to_screen_coords(trans_matrix)


def scan_convert(objects):
    points = set()
    for obj in objects:
        points.update(obj.scan_convert())
    return points


def print_world(world):
    for obj in world:
        print 'OBJECT {}'.format(obj)


def run(objects, options):
    apply_transformations(objects, options)
    clipped = clip(objects, options)
    to_screen_coords(clipped, options)
    points = scan_convert(clipped)
    palette = XPMColorPalette()
    palette.add_color('b', '#000000')
    xpm = XPMPrinter(502, 502, palette)
    draw(points, xpm, options)
    xpm.print_it()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Graphics Pipeline.')
    parser.add_argument('-a', dest='wl', type=int, default=0, help='World window lower bound in x dimension.')
    parser.add_argument('-b', dest='wb', type=int, default=0, help='World window lower bound in y dimension.')
    parser.add_argument('-c', dest='wr', type=int, default=499, help='World window upper bound in x dimension.')
    parser.add_argument('-d', dest='wt', type=int, default=499, help='World window upper bound in y dimension.')
    parser.add_argument('-f', dest='postscript', required=True, type=str, help='Postscript file')
    parser.add_argument('-j', dest='sl', type=int, default=0, help='Viewport lower bound in x dimension.')
    parser.add_argument('-k', dest='sb', type=int, default=0, help='Viewport lower bound in the y dimension.')
    parser.add_argument('-o', dest='sr', type=int, default=200, help='Viewport upper bound in the x dimension.')
    parser.add_argument('-p', dest='st', type=int, default=200, help='Viewport upper bound in the y dimension.')
    parser.add_argument('-m', dest='trans_x', type=int, default=0, help='Translation in the x direction.')
    parser.add_argument('-n', dest='trans_y', type=int, default=0, help='Translation in the y direction.')
    parser.add_argument('-s', dest='scale', type=float, default=1.0, help='Scale factor as floating point.')
    parser.add_argument('-r', type=int, dest='rotate', default=0, help='Counter clockwise rotation about the world origin.')
    options = parser.parse_args()
    world = PostscriptParser(options.postscript).parse_objects()
    run(world, options)
