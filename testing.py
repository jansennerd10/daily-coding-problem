def testFunction(f, testCases):
    print("Testing " + str(f) + "...")
    for testCase in testCases:
        result = f(*testCase[0])
        if result == testCase[1]:
            print("\tPASS: " + str(testCase[0]) + " -> " + str(result))
        else:
            print("\033[31m\tFAIL: " + str(testCase[0]) + " -> " + str(result) + " (expected: " + str(testCase[1]) + ")\033[0m")