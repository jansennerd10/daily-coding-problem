
def testFunction(f, testCases):
    """
    Applies the given test cases to the given function, and prints the results.

    Parameters
    ----------
    f
        The function to test.
    testCases
        List of 2-element tuples each representing a test case.
        The first element of each tuple is itself a tuple containing the arguments to the function.
        The second element is the expected result for the specified arguments.
    """
    print("Testing " + str(f) + "...")
    for testCase in testCases:
        result = f(*testCase[0])
        if result == testCase[1]:
            print("\tPASS: " + str(testCase[0]) + " -> " + str(result))
        else:
            print("\033[31m\tFAIL: " + str(testCase[0]) + " -> " + str(result) + " (expected: " + str(testCase[1]) + ")\033[0m")