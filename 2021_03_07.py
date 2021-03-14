# Daily Coding Problem: Problem #9 [Hard]

# This problem was asked by Airbnb.
# 
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# 
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# 
# Follow-up: Can you do this in O(N) time and constant space?

from testing import testFunction

testCases = [
    # Given test cases
    (([2, 4, 6, 2, 5],), 13),
    (([5, 1, 1, 5],), 10),
    # Correct handling of negative numbers
    (([5, 1, 1, -5],), 6),
    # Correct handling of empty list
    (([],), 0),
    # Correct handling of all negative numbers
    (([-5, -1, -1, -5],), 0),
]

# O(n) time; O(1) space
def largestSum(numbers):
    # Note that the smallest sum we should ever return is 0, which we would
    # obtain simply by choosing no numbers (in the case they were all negative).
    largestSumWithoutPrevious = 0
    largestSumWithPrevious = 0
    largestSumWithCurrent = 0

    for number in numbers:
        # For each number we encounter, we can choose to use it or not.
        # If we choose to use it, then the largest sum we can get is the
        # current number plus the largest sum we could obtain without using
        # the previous number (since it is adjacent). If we choose not to use
        # it, then the largest sum we can get is simply the largest sum we can
        # get from all the numbers not including the current one.
        largestSumWithCurrent = max(largestSumWithoutPrevious + number, largestSumWithPrevious)

        # Now we simply shift the largest sum values backwards to set up for
        # the next iteration.
        largestSumWithoutPrevious, largestSumWithPrevious = largestSumWithPrevious, largestSumWithCurrent

    return largestSumWithCurrent

testFunction(largestSum, testCases)
