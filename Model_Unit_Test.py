from Model import Model

failed = 0

print("*** Starting Test 1 ***")
# noinspection PyBroadException
try:
    skitarii_ranger = Model('Models/Skitarii_Ranger.csv')
    print("Unit test 1 successful, model was created successfully")
    skitarii_ranger.PrintModel()

except Exception as e:
    print("Unit test 1 failed, model did not create successfully")
    failed += 1

print("\n" * 2)
if failed == 0:
    print("Model unit test successfully completed")
else:
    print("Model unit test failed. " + str(failed) + " failed test(s).")
