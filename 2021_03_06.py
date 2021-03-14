# Daily Coding Problem: Problem #8 [Easy]

# This problem was asked by Google.
# 
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# 
# Given the root to a binary tree, count the number of unival subtrees.
# 
# For example, the following tree has 5 unival subtrees:
# 
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

from testing import testFunction

class Node:
    def __init__(self, value, left = None, right = None):
        self.left = left
        self.right = right
        self.value = value

testCases = [
    # Given test case
    ((Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))),), 5),
    # Test that empty tree gives 0)
    ((None,), 0),
    # Test single node tree
    ((Node(1),), 1),
    # Test full unival tree
    ((Node(0, Node(0), Node(0, Node(0, Node(0), Node(0)), Node(0))),), 7),    
]

def numUnivalSubtrees_RecursiveHelper(root):
    # Returned tuple fields:
    # - Number of unival subtrees
    # - Whether this node is the root of a unival subtree
    if root == None:
        return (0, True)
    
    (leftSubtrees, leftIsUnival) = numUnivalSubtrees_RecursiveHelper(root.left)
    (rightSubtrees, rightIsUnival) = numUnivalSubtrees_RecursiveHelper(root.right)
    
    if leftIsUnival and rightIsUnival and (root.left == None or root.left.value == root.value) and (root.right == None or root.right.value == root.value):
        return (leftSubtrees + rightSubtrees + 1, True)

    return (leftSubtrees + rightSubtrees, False)


def numUnivalSubtrees_Recursive(root):
    (numSubtrees, _) = numUnivalSubtrees_RecursiveHelper(root)
    return numSubtrees

testFunction(numUnivalSubtrees_Recursive, testCases)
