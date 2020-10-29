from Point import Point


class Terrain:
    def __init__(self, coordinates, terrain_type, name):

        if not isinstance(name, str):
            raise Exception("** EXCEPTION: Terrain name is not a string")
        self.name = name

        if not isinstance(terrain_type, str):
            raise Exception("** EXCEPTION: Terrain type is not a string")
        self.terrain_type = terrain_type

        if terrain_type.upper() not in ["RUINS", "FOREST", "CRATER"]:
            raise Exception("** EXCEPTION: Terrain type is not valid for " + self.name)

        if len(coordinates) != 8:
            raise Exception("** EXCEPTION: Incorrect number of coordinate points for terrain " + self.name)

        for i in coordinates:
            if not isinstance(i, Point):
                raise Exception("** EXCEPTION: A coordinate in " + str(self.name) + "is not of class Point")

        self.coordinates = coordinates
