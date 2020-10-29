import tkinter as tk

import Constants
import Line_of_Sight
from Point import Point

failed = 0
print("*** Starting Test 1 ***")

if Line_of_Sight.CheckLinearCollision(Point(0, 0, 0), Point(25, 25, 0), Point(0, 25, 0), Point(25, 0, 0)):
    print("Test 1 successful, expression evaluated true")

else:
    print("Test 1 failed, expression evaluated false")
    failed += 1

print("\n" * 2)
print("*** Starting Test 2 ***")

if Line_of_Sight.CheckLinearCollision(Point(0, 0, 0), Point(25, 0, 0), Point(0, 25, 0), Point(25, 25, 0)):
    print("Test 2 failed, expression evaluated true")
    failed += 1

else:
    print("Test 2 successful, expression evaluated false")

print("\n" * 2)
print("*** Starting Test 3 ***")

if Line_of_Sight.CheckLinearCollision(Point(0, 0, 0), Point(10, 10, 0), Point(5, 0, 0), Point(15, 10, 0)):
    print("Test 3 failed, expression evaluated true")
    failed += 1

else:
    print("Test 3 successful, expression evaluated false")

print("\n" * 2)
print("*** Starting Test 4 ***")

if Line_of_Sight.CheckLinearCollision(Point(0, 0, 0), Point(44, 44, 0), Point(0, 22, 0), Point(21, 22, 0)):
    print("Test 4 failed, expression evaluated true")
    failed += 1

else:
    print("Test 4 successful, expression evaluated false")

print("\n" * 2)
print("*** Starting Test 5 ***")

if Line_of_Sight.CheckLinearCollision(Point(0, 0, 0), Point(44, 44, 0), Point(0, 22, 0), Point(23, 22, 0)):
    print("Test 5 successful, expression evaluated true")

else:
    print("Test 5 failed, expression evaluated false")
    failed += 1

print("\n" * 2)
print("*** Starting Test 6 ***")

if Line_of_Sight.CheckLinearCollision(Point(10, 0, 0), Point(10, 44, 0), Point(0, 0, 0), Point(44, 44, 0)):
    print("Test 6 successful, expression evaluated true")

else:
    print("Test 6 failed, expression evaluated false")
    failed += 1


print("\n" * 2)
print("*** Starting Test 7 ***")

if Line_of_Sight.CheckLinearCollision(Point(22, 0, 0), Point(22, 21, 0), Point(0, 0, 0), Point(44, 44, 0)):
    print("Test 7 failed, expression evaluated true")
    failed += 1

else:
    print("Test 7 successful, expression evaluated false")

print("\n" * 2)
print("*** Starting Test 8 ***")

if Line_of_Sight.CheckLinearCollision(Point(22, 0, 0), Point(22, 22, 0), Point(0, 0, 0), Point(44, 44, 0)):
    print("Test 8 successful, expression evaluated true")

else:
    print("Test 8 failed, expression evaluated false")
    failed += 1

print("\n" * 2)
print("*** Starting Test 9 ***")

if Line_of_Sight.CheckLinearCollision(Point(22, 0, 0), Point(22, 22, 0), Point(22, 44, 0), Point(22, 21, 0)):
    print("Test 9 successful, expression evaluated true")

else:
    print("Test 9 failed, expression evaluated false")
    failed += 1

print("\n" * 2)
print("*** Starting Test 10 ***")

if Line_of_Sight.CheckLinearCollision(Point(22, 0, 0), Point(22, 22, 0), Point(22, 44, 0), Point(22, 23, 0)):
    print("Test 10 failed, expression evaluated true")
    failed += 1

else:
    print("Test 10 successful, expression evaluated false")

print("\n" * 2)
print("*** Starting Test 11 ***")

if Line_of_Sight.CheckLinearCollision(Point(22, 20, 0), Point(22, 22, 0), Point(22, 44, 0), Point(22, 0, 0)):
    print("Test 11 successful, expression evaluated true")

else:
    print("Test 11 failed, expression evaluated false")
    failed += 1

print("\n" * 2)
if failed == 0:
    print("Unit Test for Line of Sight successful!")
else:
    print("Unit Test for Line of Sight failed, with " + str(failed) + " failed tests.")
