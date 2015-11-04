from d2.point2d import Point2D

TOP = 0b1000
LEFT = 0b0001
RIGHT = 0b0010
BOTTOM = 0b0100


def get_code(x, y, wl, wb, wr, wt):
    code = 0b0000
    if x < wl:
        code |= LEFT
    elif x > wr:
        code |= RIGHT
    if y < wb:
        code |= BOTTOM
    elif y > wt:
        code |= TOP
    return code


def cohen_sutherland(x0, y0, x1, y1, wl, wb, wr, wt):
    code_1 = get_code(x0, y0,  wl, wb, wr, wt)
    code_2 = get_code(x1, y1, wl, wb, wr, wt)
    while True:
        # If both of the codes are 0 then they must both be inside the window.
        # Thus we break from the loop.
        if (code_1 | code_2) == 0:
            return x0, y0, x1, y1
        # Completely outside
        elif not (code_1 & code_2) == 0:
            return None, None, None, None
        else:
            x = 0
            y = 0
            code = code_1
            if code == 0:
                code = code_2
            # Point is to the left
            if (code & LEFT) > 0:
                y = y0 + (y1 - y0) * (wl - x0) / (x1 - x0)
                x = wl
            # Point is below bottom
            elif (code & BOTTOM) > 0:
                x = x0 + (x1 - x0) * (wb - y0) / (y1 - y0)
                y = wb
            # Point is to the right
            elif (code & RIGHT) > 0:
                y = y0 + (y1 - y0) * (wr - x0) / (x1 - x0)
                x = wr
            # Point is on top
            elif (code & TOP) > 0:
                x = x0 + (x1 - x0) * (wt - y0) / (y1 - y0)
                y = wt
            else:
                print 'Failed to determine which side the point lies on.'
        if code == code_1:
            x0 = int(x)
            y0 = int(y)
            code_1 = get_code(x0, y0, wl, wb, wr, wt)
        else:
            x1 = int(x)
            y1 = int(y)
            code_2 = get_code(x1, y1, wl, wb, wr, wt)
    return x0, y0, x1, y1


def dda(x0, y0, x1, y1):
    points = set()
    if x0 > x1:
        x0, y0, x1, y1 = x1, y1, x0, y0
    x = x0
    y = y0
    dx = x1 - x0
    dy = y1 - y0
    if dx == 0:
        if y0 > y1:
            y0, y1 = y1, y0
        for i in range(int(round(y0)), int(round(y1))):
            points.add((int(round(x0)), int(i)))
        return points
    elif dy == 0:
        for i in range(int(round(x0)), int(round(x1))):
            points.add((int(i), int(round(y0))))
        return points
    m = float(dy)/dx
    sign = 1
    if m < 0:
        sign = -1
    if abs(m) < 1:
        dx = 1
        dy = m
    else:
        dx = 1.0/abs(m)
        dy = sign * 1
    while x < x1:
        points.add((int(round(x)), int(round(y))))
        x += dx
        y += dy
    return points


def find_intersection(vx0, vy0, vx1, vy1, rx0, ry0, rx1, ry1):
    if vx0 > vx1:
        vx0, vy0, vx1, vy1 = vx1, vy1, vx0, vy0
    if rx0 > rx1:
        rx0, ry0, rx1, ry1 = rx1, ry1, rx0, ry0
    dv = vx1 - vx0, vy1 - vy0
    dr = rx1 - rx0, ry1 - ry0
    try:
        t0 = float(((vx0 - rx0)*dr[1] + (ry0 - vy0)*dr[0]))/(dv[1] * dr[0] - dv[0] * dr[1])
        if t0 < 0:
            raise ArithmeticError('Line intersects before segment.')
        if t0 > 1:
            raise ArithmeticError('Line intersects after segment.')
        t0_x = vx0 + t0 * dv[0]
        t0_y = vy0 + t0 * dv[1]
        return t0_x, t0_y
    except ZeroDivisionError:
        pass


# defined as to the left of the line ray.
def is_inside(x0, y0, x1, y1, px, py):
    dx = x1 - x0
    dy = y1 - y0
    return (px - x0)*dy < (py - y0)*dx


def sutherland_hodgman(p, left, right, bottom, top):
    edges = [(left, bottom), (right, bottom), (right, top), (left, top)]
    e0 = edges[-1]
    for e1 in edges:
        if len(p) == 0:
            return []
        retval = []
        p0 = p[-1]
        for p1 in p:
            if is_inside(e0[0], e0[1], e1[0], e1[1], p0.x(), p0.y()):
                if is_inside(e0[0], e0[1], e1[0], e1[1], p1.x(), p1.y()):
                    retval.append(p1)
                else:
                    x, y = find_intersection(p0.x(), p0.y(), p1.x(), p1.y(), e0[0], e0[1], e1[0], e1[1])
                    retval.append(Point2D(x, y))
            elif is_inside(e0[0], e0[1], e1[0], e1[1], p1.x(), p1.y()):
                x, y = find_intersection(p0.x(), p0.y(), p1.x(), p1.y(), e0[0], e0[1], e1[0], e1[1])
                retval.append(Point2D(x, y))
                retval.append(p1)
            p0 = p1
        p = retval
        e0 = e1
    return p

