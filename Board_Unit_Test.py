from Board import Board

failed = 0

print("*** Starting Test 1 ***")
try:
    board1 = Board('Test_Boards/Test_Board1.csv')
    print("Test successful, no exceptions expected")
    board1.ShowBoard()
except Exception as e:
    print("Test 1 failed, no exceptions expected")
    print(e)
    failed += 1

print("\n" * 2)
print("*** Starting Test 2 ***")
try:
    board1 = Board('Test_Boards/Test_Board2.csv')
    print("Test 2 failed, exceptions expected")
    failed += 1
except Exception as e:
    print("Test 2 successful, exceptions expected")
    print(e)

print("\n" * 2)
print("*** Starting Test 3 ***")
try:
    board1 = Board('Test_Boards/Test_Board3.csv')
    print("Test failed 3, exceptions expected")
    failed += 1
except Exception as e:
    print("Test 3 successful, exceptions expected")
    print(e)


print("\n" * 2)
print("*** Starting Test 4 ***")
try:
    board1 = Board('Test_Boards/Test_Board4.csv')
    print("Test failed 4, exceptions expected")
    failed += 1
except Exception as e:
    print("Test 4 successful, exceptions expected")
    print(e)


print("\n" * 2)
if failed == 0:
    print("Unit test for 'Board' was successful!")
else:
    print("Unit test for 'Board' failed with " + str(failed) + " failures.")
