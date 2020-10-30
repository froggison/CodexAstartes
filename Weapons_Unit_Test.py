from Exceptions import CSVFileException
from Weapon import Weapon

failed = 0

print("*** Starting Case 1 ***")

try:
    galvanic_rifle = Weapon("Weapons/Galvanic_Rifle.csv")
    print("Case 1 successful, no exceptions thrown")
    galvanic_rifle.PrintWeapon()
except CSVFileException as e:
    print("Case 1 failed, exceptions thrown")
    print(e)
    failed += 1

if failed == 0:
    print("\nUnit Test for Weapon successful, all cases passed")
else:
    print("\n Unit test for Weapon failed, " + str(failed) + " test case(s) failed")
