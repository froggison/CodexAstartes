import csv
from Exceptions import CSVFileException


# Order of weapon stats coming from CSV file: name, points, range, type, strength, ap, damage, abilities
class Weapon:
    def __init__(self, file):
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile)

            for row in readCSV:
                if len(row) != 8:
                    raise CSVFileException("** Exception: Invalid CSV file for Weapon")

                self.name = row[0]
                self.points = row[1]
                self.range = int(row[2])
                self.type = row[3]
                self.strength = row[4]
                self.ap = row[5]
                self.damage = row[6]
                self.abilities = row[7].split('-')

    def PrintWeapon(self):
        print("Name: " + self.name + " Points: " + self.points + " Range: " + str(self.range) + " Type: " + self.type +
              " Strength: " + self.strength + " AP: " + self.ap + " Damage: " + self.damage + " Abilities: " +
              str(self.abilities))
