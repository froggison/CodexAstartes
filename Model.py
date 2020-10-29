import csv


# order from CSV file: Model name, model points (base, no weapons), movement, weapon skill, ballistic skill,
# strength, toughness, wounds, attacks, leadership, save, invulnerable save, feel no pain, weapons, abilities,
# base size (diameter in inches)
class Model:
    def __init__(self, file):
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile)

            for row in readCSV:
                if len(row) != 16:
                    raise Exception("** Exception: Invalid CSV file for model")

                self.name = row[0]
                self.points = int(row[1])
                self.movement = int(row[2])
                self.weapon_skill = int(row[3])
                self.ballistic_skill = int(row[4])
                self.strength = int(row[5])
                self.toughness = int(row[6])
                self.wounds = int(row[7])
                self.attacks = int(row[8])
                self.leadership = int(row[9])
                self.save = int(row[10])
                self.invulnerable_save = int(row[11])
                self.feel_no_pain = int(row[12])
                self.weapons = row[13].split('-')
                self.abilities = row[14].split('-')
                self.base_size = float(row[15])

    def PrintModel(self):
        print("Name: " + self.name + " Movement: " + str(self.movement) + " Weapon Skill: " + str(self.weapon_skill) +
              " Ballistic Skill: " + str(self.ballistic_skill) + " Strength: " + str(self.strength) + " Toughness: " +
              str(self.toughness) + " Wounds: " + str(self.wounds) + " Attacks: " + str(self.attacks) + " Leadership: "
              + str(self.leadership) + " Save: " + str(self.save) + " Invulnerable Save: " + str(self.invulnerable_save)
              + " Feel No Pain: " + str(self.feel_no_pain) + " Weapons: " + str(self.weapons) + " Abilities: " +
              str(self.abilities))
