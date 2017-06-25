'''

Binary Search Tree:
The left sub-tree of a node has a key less than or equal to its parent node's key.
The right sub-tree of a node has a key greater than to its parent node's key


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

'''

# the root is the medium of the sorted array

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildBST(list):
    mid = len(list)//2
    root = TreeNode(list[mid])
    leftTree = buildBST(list[:mid])
    rightTree = buildBST(list[mid+1:])
    root.left = leftTree
    root.right = rightTree
    return root
