import Constants
import csv
from Terrain import Terrain
from Point import Point
import tkinter as tk


class Board:
    def __init__(self, file):
        self.terrain = []
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile)

            for row in readCSV:
                if len(row) != 10:
                    raise Exception("** Exception: CSV file for Board invalid")
                coords = []
                for i in range(2, len(row)):
                    coords_from_file = row[i].split('-')
                    if len(coords_from_file) != 3:
                        raise Exception("** Exception: CSV file for Board invalid")

                    x = float(coords_from_file[0])
                    y = float(coords_from_file[1])
                    z = float(coords_from_file[2])
                    coords.append(Point(x, y, z))

                self.terrain.append(Terrain(coordinates=coords, name=row[0].strip(), terrain_type=row[1].strip()))

    def ShowBoard(self):
        root = tk.Tk()
        root.geometry(str(Constants.BOARD_X * Constants.SCREEN_RATIO) + "x" + str(Constants.BOARD_Y *
                                                                                  Constants.SCREEN_RATIO))
        canvas = tk.Canvas(root, width=(Constants.BOARD_X * Constants.SCREEN_RATIO), height=(Constants.BOARD_Y *
                                                                                             Constants.SCREEN_RATIO))
        canvas.pack()

        for piece in self.terrain:
            if piece.terrain_type.upper() == "RUINS":
                terrain_color = "red"
            else:
                terrain_color = "grey"
            canvas.create_line(piece.coordinates[0].x * Constants.SCREEN_RATIO, piece.coordinates[0].y *
                               Constants.SCREEN_RATIO, piece.coordinates[1].x * Constants.SCREEN_RATIO,
                               piece.coordinates[1].y * Constants.SCREEN_RATIO, fill=terrain_color)
            canvas.create_line(piece.coordinates[1].x * Constants.SCREEN_RATIO, piece.coordinates[1].y *
                               Constants.SCREEN_RATIO, piece.coordinates[2].x * Constants.SCREEN_RATIO,
                               piece.coordinates[2].y * Constants.SCREEN_RATIO, fill=terrain_color)
            canvas.create_line(piece.coordinates[2].x * Constants.SCREEN_RATIO, piece.coordinates[2].y *
                               Constants.SCREEN_RATIO, piece.coordinates[3].x * Constants.SCREEN_RATIO,
                               piece.coordinates[3].y * Constants.SCREEN_RATIO, fill=terrain_color)
            canvas.create_line(piece.coordinates[3].x * Constants.SCREEN_RATIO, piece.coordinates[3].y *
                               Constants.SCREEN_RATIO, piece.coordinates[0].x * Constants.SCREEN_RATIO,
                               piece.coordinates[0].y * Constants.SCREEN_RATIO, fill=terrain_color)
        tk.mainloop()

    def GetTerrain(self):
        return self.terrain
