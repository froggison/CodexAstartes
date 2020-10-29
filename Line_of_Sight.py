from Point import Point


def CheckLinearCollision(point_a, point_b, point_c, point_d):
    if not isinstance(point_a, Point):
        raise Exception("** Exception: Point A is not a valid point")
    if not isinstance(point_b, Point):
        raise Exception("** Exception: Point B is not a valid point")
    if not isinstance(point_c, Point):
        raise Exception("** Exception: Point C is not a valid point")
    if not isinstance(point_d, Point):
        raise Exception("** Exception: Point D is not a valid point")

    if point_a.x != point_b.x:
        slope1 = (point_a.y - point_b.y) / (point_a.x - point_b.x)
        intersect1 = point_a.y - slope1 * point_a.x

        slope2 = (point_c.y - point_d.y) / (point_c.x - point_d.x)
        intersect2 = point_c.y - slope2 * point_c.x

        if slope1 == slope2:
            return False

        cross = (intersect2 - intersect1) / (slope1 - slope2)

        if ((cross < max(min(point_a.x, point_b.x), min(point_c.x, point_d.x))) or
                (cross > min(max(point_a.x, point_b.x), max(point_c.x, point_d.x)))):
            return False
        return True

    elif point_c.x == point_a.x == point_d.x:
        if (min(point_a.y, point_b.y) < min(point_c.y, point_d.y) < max(point_a.y, point_b.y)) \
                or (min(point_a.y, point_b.y) < max(point_c.y, point_d.y) < max(point_a.y, point_b.y)
                    or (min(point_a.y, point_b.y) > min(point_c.y, point_d.y)
                        and max(point_a.y, point_b.y) < max(point_c.y, point_d.y))):
            return True

    else:
        if min(point_c.x, point_d.x) < point_a.x < max(point_c.x, point_d.x):

            slope = (point_c.y - point_d.y) / (point_c.x - point_d.x)
            intercept = point_c.y - slope * point_c.x
            cross = slope * point_a.x + intercept
            if min(point_a.y, point_b.y) <= cross <= max(point_a.y, point_b.y):
                return True

    return False
