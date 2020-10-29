from Terrain import Terrain
from Point import Point as Point

coordinates = [Point(0, 0, 0), Point(1, 0, 0), Point(0, 1, 0), Point(1, 1, 0), Point(0, 0, 1), Point(1, 0, 1),
               Point(0, 1, 1), Point(1, 1, 1)]

failed = 0

print("*** Starting Test 1 ***")
try:
    terrain1 = Terrain(coordinates, "RUINS", "Terrain 1")
    print("Test 1 SUCCESSFUL, no exception expected")
except Exception as e:
    print("Test 2 FAILED, no exception expected")
    print(e)
    failed += 1

print("\n" * 2)
print("*** Starting Test 2 ***")
try:
    terrain2 = Terrain(coordinates, "RUNS", "Terrain 2")
    print("Test 2 FAILED, exception expected")
    failed += 1
except Exception as e:
    print(e)
    print("Test 2 SUCCESSFUL, exception expected")

print("\n" * 3)
print("*** Starting Test 3 ***")
try:
    terrain3 = Terrain(coordinates, "RUINS", 1)
    print("Test 3 FAILED, exception expected")
    failed += 1
except Exception as e:
    print(e)
    print("Test 3 SUCCESSFUL, exception expected")

print("\n" * 2)
print("*** Starting Test 4 ***")
try:
    coordinates4 = [Point(0, 0, 0), Point(0, 1, 0), Point(1, 0, 0), Point(1, 1, 0), Point(0, 0, 1), Point(0, 1, 0)]
    terrain4 = Terrain(coordinates4, "RUINS", "Terrain 4")
    print("Test 4 FAILED, exception expected")
    failed += 1
except Exception as e:
    print(e)
    print("Test 4 SUCCESSFUL, exception expected")

print("\n" * 2)
if failed == 0:
    print("Unit test was successful!")
else:
    print("Unit test failed with " + str(failed) + " failures.")
