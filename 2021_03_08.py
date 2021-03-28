# Daily Coding Problem: Problem #11 [Medium]

# This problem was asked by Twitter.
# 
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# 
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# 
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

from testing import testFunction

testCases = [
    # Given test case
    (('de', ['dog', 'deer', 'deal']), ['deal', 'deer']),
    # Test that all dictionary items are returned when the query string is empty
    (('', ['dog', 'deer', 'deal']), ['deal', 'deer', 'dog']),
    # Test the case where one added string is a prefix of another
    (('d', ['do', 'doing', 'ear']), ['do', 'doing']),
]

# This problem is testing knowledge of the trie data structure.
# A trie is a tree structure that can store a list of strings in such a way
# that we can easily determine whether a given string is in the list, as well
# as answer other types of queries about the list (such as this problem, which
# asks to retrieve all strings starting with a particular substring).

# A trie is organized such that each child of the root node is assigned a
# character and contains below it all the strings that begin with that
# character. This is repeated for the length of each string, so that in the
# end each string is encoded as a path from the root to one of the leaves of
# the trie structure. The example dictionary given in the problem statement
# would be encoded like this:
# {
#   'd': {
#       'e': {
#           'a': {
#               'l': 'deal'
#           }
#           'e': {
#               'r': 'deer'
#           }
#       }
#       'o': {
#           'g': 'dog'
#       }
# }
# It isn't necessary to store the string at each leaf, as the string has
# already been encoded in the trie itself. We could simply store a value
# such as True instead, indicating that that path represents a valid string.
# But storing a reference to the string instead makes retrieving the strings
# later a bit simpler.

# In practice, however, the above structure is highly inefficient. Creating
# the full trie usually means creating a large number of maps that each have
# just one key. We can optimize by simply storing the string itself as soon
# as there is just a single path below a given node. So the above structure
# would become:
# {
#   'd': {
#       'e': {
#           'a': 'deal'
#           'e': 'deer'
#       }
#       'o': 'dog'
# }
# We can expand any "shortcut" node to a full node easily if another string
# is added that shares the same prefix.

# There is just one remaining issue to resolve: the ability to store two
# strings where one is a prefix of the other, as in 'do' and 'doing'. We can
# resolve this by giving each node a separate field which would contain the
# string terminating at that node, if any.
# TrieNode(None,
#   {
#       'd': TrieNode(None, {
#               'o': TrieNode('do', {
#                       'i': 'doing'
#                   })
#           })
#   })

class TrieNode:
    def __init__(self, string, children):
        self.string = string
        self.children = children

def autocomplete(query, dictionary):
    trie = TrieNode(None, {})

    # Add all the words in the dictionary to the trie data structure.
    # Normally, this would be done once in a separate function - there is no
    # advantage to doing it for just a single query.
    for word in dictionary:
        subtrie = trie
        for i in range(len(word)):
            # If there is no child node for the current character, add the
            # string as a "shortcut node".
            if not word[i] in subtrie.children:
                subtrie.children[word[i]] = word
                break
            # If the child we need to add to is already a "shortcut string",
            # expand it to a full node before continuing.
            if isinstance(subtrie.children[word[i]], str):
                oldString = subtrie.children[word[i]]
                if i == len(oldString) - 1:
                    # This is the last character of the old string; store the
                    # old string at the node itself instead of in its children.
                    newNode = TrieNode(oldString, {})
                else:
                    newNode = TrieNode(None, { oldString[i]: oldString })
                subtrie.children[word[i]] = newNode
            subtrie = subtrie.children[word[i]]
        if i == len(word) - 1 and isinstance(subtrie, TrieNode):
            # We've reached the end of the word and the current node is still a
            # full node. Store the current word at the node.
            subtrie.string = word

    # Now, look up the query in the trie and find all completions.
    subtrie = trie
    for i in range(len(query)):
        # If the current subtrie is a "shortcut node," check whether the query
        # is a prefix. If it is, the result has exactly one string. If not,
        # there are no results.
        if isinstance(subtrie, str):
            return [subtrie] if query[i:] == subtrie[i:len(subtrie)] else []
        if query[i] not in subtrie.children:
            return []
        subtrie = subtrie.children[query[i]]
    
    # subtrie now contains all completions of the query string.
    results = []
    # Maintain a list of nodes we have not yet examined. This functions as a
    # stack; we could use recursion instead.
    unprocessedSubtries = [subtrie]
    while unprocessedSubtries:
        subtrie = unprocessedSubtries.pop()
        if isinstance(subtrie, str):
            # If this is a shortcut node, just add the string to the results.
            results.append(subtrie)
        else:
            # Otherwise, push all child nodes onto the stack to be examined.
            unprocessedSubtries.extend(subtrie.children.values())
    
    return results

# This function exists to sort the results of autocomplete (making it easier to automatically verify the results).
# The problem statement does not specify any particular ordering for the returned strings, but we would like to be
# able to specify a list as the expected result and then compare it directly to the actual result.
def autocompleteTestHarness(query, dictionary):
    return sorted(autocomplete(query, dictionary))

testFunction(autocompleteTestHarness, testCases)
