# Daily Coding Problem: Problem #7 [Medium]

# This problem was asked by Facebook.
# 
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# 
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# 
# You can assume that the messages are decodable. For example, '001' is not allowed.

from testing import testFunction

testCases = [
    (('111',), 3),
    (('101',), 1),
    (('241',), 2),
    (('221',), 3),
    (('',), 1),
]

# Because the number of ways we can interpret a single character (e.g. '1')
# depends on the next character, this problem is best solved by examining the
# encoded message backwards. We can reason inductively.
# 
# Suppose we have a message of unknown length: '12...75' and that there are N
# ways to decode this message. We add a character to the left end of the
# message and wish to know how many ways there are to decode the new message.
# Then there are three cases to consider:
#   1) There is only one way to interpret the new character (i.e. it is 3-9,
#      or 2 where the character to the right is 7-9). In this case, the number
#      of ways to decode the new message is simply N, because adding the new
#      character does not give us any additional choices.
#   2) There are two ways to interpret the new character: on its own, or as
#      as part of a 2-character encoding. I.e., the new character is 1, or 2
#      followed by 0-6. Then the number of ways to decode the new message is
#      N (for the case that we take the new character on its own) plus the
#      number of ways to decode the tail of the old message, '2...75' (for the
#      case that we take the new character as part of a 2-character encoding).
#   3) There are no ways to interpret the new character (i.e. it is 0).
#      Although the problem statement excludes the possibility that 0 appears
#      at the left of the full message, which would render it invalid, 0 may
#      still appear anywhere else in the message. Because we already need to
#      track the "previous" value of N for case #2, it is convenient to say
#      that N for the new message is 0. Then if we see a 1 or a 2 on the next
#      iteration, the formula for case 2 still holds.

def numDecodes(message):
    # N may start as 1, because we are guaranteed that the message is valid so
    # there must be at least one way to decode it.
    N = 1
    prevN = 0
    prevChar = ''

    for c in reversed(message):
        if c >= '3' and c <= '9' or c == '2' and prevChar >= '7' and prevChar <= '9':
            # N stays the same, and update prevN
            prevN = N
        elif c == '1' or c == '2':
            N, prevN = N + prevN, N
        elif c == '0':
            N, prevN = 0, N

    return N

testFunction(numDecodes, testCases)
