# Daily Coding Problem: Problem #5 [Medium]

# This problem was asked by Jane Street.
# 
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# 
# Given this implementation of cons:
# 
# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# 
# Implement car and cdr.

from testing import testFunction

carTestCases = [
    ((3, 4), 3)
]

cdrTestCases = [
    ((3, 4), 4)
]

# Given definition of cons
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# car solution
def car(pair):
    return pair(lambda a, b: a)

# cdr solution
def cdr(pair):
    return pair(lambda a, b: b)

# Testing code

def carTestHarness(a, b):
    return car(cons(a, b))

def cdrTestHarness(a, b):
    return cdr(cons(a, b))

testFunction(carTestHarness, carTestCases)
testFunction(cdrTestHarness, cdrTestCases)
