import Constants


class Point:
    def __init__(self, x, y, z):
        if (isinstance(x, int) + isinstance(x, float)) == False or (isinstance(x, int) + isinstance(y, float)) == False\
                or (isinstance(x, int) + isinstance(z, float)) == False:
            raise Exception("** Exception: invalid type for Point")

        if x < 0 or y < 0 or z < 0 or x > Constants.BOARD_X or y > Constants.BOARD_Y:
            raise Exception("** Exception: invalid coordinates for Point")

        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
