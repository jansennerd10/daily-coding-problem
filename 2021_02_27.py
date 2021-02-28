# Daily Coding Problem: Problem #1 [Easy]

# This problem was recently asked by Google.
# 
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# 
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# 
# Bonus: Can you do this in one pass?

from testing import testFunction

testCases = [
    ((17, [10, 15, 3, 7]), True),
    ((0, []), False),
    ((17, [5, 20, -3, 16]), True),
    ((17, [5, 20, -4, 16]), False),
]

# Naive implementation: O(n^2) time, O(1) space (n = length of numbers list)
def doTheyAddUp(k, numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(i, len(numbers)):
            if(numbers[i] + numbers[j] == k):
                return True

    return False

# One-pass implementation: O(n) time (assuming constant-time dictionary access), O(n) space (assuming reasonable dictionary implementation)
def doTheyAddUp_OnePass(k, numbers):
    seen = {}
    for num in numbers:
        seen[num] = True
        if(k-num in seen):
            return True
    
    return False

testFunction(doTheyAddUp, testCases)
testFunction(doTheyAddUp_OnePass, testCases)
