# Daily Coding Problem: Problem #4 [Hard]

# This problem was asked by Stripe.
# 
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# 
# You can modify the input array in-place.

from testing import testFunction

testCases = [
    # Given test cases
    (([3, 4, -1, 1],), 2),
    (([1, 2, 0],), 3),
    # Test proper handling of empty array
    (([],), 1),
    # Test proper output when NO positive integers present
    (([0, 0, 0],), 1),
    # Test proper handling of duplicate numbers
    (([1, 2, 2, 4],), 3),
    # Test proper handling of perfectly filled array
    (([1, 2, 3, 4],), 5),
]

def firstMissingInteger(arr):
    # Ensure i is initialized properly even if the array is empty
    i = 0

    # Approach:
    # Reorganize the array so that every positive integer less than or equal to
    # the size of the array occupies the index corresponding to its value (minus
    # one since arrays are 0-indexed).
    # Then, simply find the first index that is not populated in this way.
    # We do not have to worry about numbers larger than the size of the array:
    # if one exists, then a number less than the size of the array must be missing
    # to account for it.
    for i in range(len(arr)):
        # As long as the number at the current index is in range and not already
        # in the right place, swap it with the number at the corresponding index.
        # Although this is a nested loop, we can still guarantee linear time complexity,
        # because each element of the array is examined at *most* twice: once when
        # it is swapped into place, and possibly once more when the main loop reaches
        # that index.
        while arr[i] > 0 and arr[i] <= len(arr) and arr[i] != i + 1:
            if arr[arr[i] - 1] == arr[i]:
                # Duplicate number, and one instance is already in the right place.
                # Break (otherwise infinite loop...)
                break
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

    # Find the first un-populated index. In the case that the array is perfectly filled
    # from 1 to the size of the array, i will simply run all the way to len(arr) and
    # len(arr) + 1 will be returned at the end.
    i = 0
    while i < len(arr):
        if arr[i] != i + 1:
            break
        i = i + 1

    return i + 1

def fmiTestHarness(arr):
    # The problem statement requires that the solution run in constant space,
    # but may modify the input array in-place. Therefore, make a working copy
    # *before* calling the actual function so that the original input array
    # from the test case isn't modified and the output displays correctly.
    workingArr = arr[:]
    return firstMissingInteger(workingArr)

testFunction(fmiTestHarness, testCases)
