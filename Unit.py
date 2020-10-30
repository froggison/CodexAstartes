import csv
from Model import Model
from Exceptions import CSVFileException


class Unit:
    def __init__(self, file, unit_id=''):
        self.models = []
        self.unit_id = unit_id
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile)

            for row in readCSV:
                if len(row) != 1:
                    raise CSVFileException("** Exception: Invalid CSV file for Unit")
                self.models.append(Model(row[0]))

    def PrintUnit(self):
        for model in self.models:
            model.PrintModel()
