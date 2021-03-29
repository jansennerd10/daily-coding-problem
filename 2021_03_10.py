# Daily Coding Problem: Problem #13 [Hard]

# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from testing import testFunction

# We will assume that k is positive.
testCases = [
    # Given test case
    ((2, 'abcba'), 3),
    # Test correct handling of empty string
    ((2, ''), 0),
    # Test the case where the entire string should be included
    ((3, 'abcba'), 5),
]

# O(n) time (n = length of s) assuming O(1) dict access; O(k) space
def longestSubstring(k, s):
    longestLength = 0
    currentStart = 0
    currentLetterCounts = {}
    numUniqueLetters = 0

    for i in range(len(s)):
        # As we examine each index, note whether or not we are adding a unique
        # character that isn't in the current substring.
        if not s[i] in currentLetterCounts:
            numUniqueLetters += 1
            currentLetterCounts[s[i]] = 1
        else:
            currentLetterCounts[s[i]] += 1
        # If we've exceeded k, pull up the the other end behind us until we
        # drop a unique character again.
        # Note that while this is a nested loop, runtime is still O(n) because
        # the inner loop examines each index of the string at most once
        # globally.
        while numUniqueLetters > k:
            if currentLetterCounts[s[currentStart]] == 1:
                # Deleting letter counts as they reach zero allows us to
                # operate in O(k) space, since the dict will have at most
                # k+1 entries.
                del currentLetterCounts[s[currentStart]]
                numUniqueLetters -= 1
            else:
                currentLetterCounts[s[currentStart]] -= 1
            currentStart += 1
        # Now we know the length of the longest substring that contains at most
        # k distinct characters and ends at index i.
        currentLength = i - currentStart + 1
        if currentLength > longestLength:
            longestLength = currentLength

    return longestLength

testFunction(longestSubstring, testCases)
