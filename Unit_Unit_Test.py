from Unit import Unit
from Exceptions import *
failed = 0

print("*** Starting Test 1 ***")
try:
    skitarii_5_man = Unit("Units/Skitarii_Rangers_5_Man.csv")
    print("Test 1 successful, no exceptions raised")
except Exception as e:
    print("Test 1 failed, exceptions raised")
    print(e)
    failed += 1

print("\n *** Starting Test 2 ***")
try:
    skitarii_5_man = Unit("Units/Skitarii_Rangers_5_Man_UNIT_TEST_1.csv")
    print("Test 2 failed, no exceptions raised")
    failed += 1
except CSVFileException as e:
    print("Test 2 successful, exceptions raised")
    print(e)

if failed == 0:
    print("\n Unit test for Unit successful, no failed cases")
else:
    print("\n Unit test for Unit failed, " + str(failed) + " failed cases")
