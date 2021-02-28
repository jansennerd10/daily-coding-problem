# Daily Coding Problem: Problem #2 [Hard]

# This problem was asked by Uber.
# 
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# 
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# 
# Follow-up: what if you can't use division?

from testing import testFunction

testCases = [
    (([1, 2, 3, 4, 5],), [120, 60, 40, 30, 24]),
    (([3, 2, 1],), [2, 3, 6]),
    (([],), []),
    (([0, 0, 0],), [0, 0, 0])
]

# Implementation without division; O(n) time, O(n) space
# (note that any solution must use at least O(n) space as that much is needed to store the output)
def calculateProducts(factors):
    # Each element of beforeProducts contains the product of all factors BEFORE that index.
    # For convenience, the special case of the first index (which has no factors before it) is assigned to 1.
    beforeProducts = [1 for _ in factors]
    # Similarly, afterProducts contains the product of all factors AFTER each index,
    # and the last index is assigned to 1.
    afterProducts = [1 for _ in factors]

    # Fill in the lists of beforeProducts and afterProducts.
    for i in range(0, len(factors) - 1):
        beforeProducts[i+1] = beforeProducts[i] * factors[i]

    for i in range(len(factors) - 1, 0, -1):
        afterProducts[i-1] = afterProducts[i] * factors[i]

    # Then, the output for each index is simply the product of all factors before that index
    # multiplied by the product of all factors after that index, both of which we already know!
    return [beforeProducts[i] * afterProducts[i] for i in range(len(factors))]

testFunction(calculateProducts, testCases)

# Note: The implementation with division would calculate the product of all the factors,
# and then for each index, divide by the factor at that index to get the output.
# The implementation is trivial, but breaks if any factor is 0 (due to division by 0).
# Special cases could be constructed to get around this issue, but the end result would
# likely be more complex than the no-division solution without providing any advantage
# in space or time complexity.
