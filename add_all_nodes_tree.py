'''
     7
    / \
  5    9
 /\    /\
4  6  8 10
'''

# construct a tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

n4 = TreeNode(4)
n6 = TreeNode(6)
n5 = TreeNode(5)
n7 = TreeNode(7)
n9 = TreeNode(9)
n8 = TreeNode(8)
n10 = TreeNode(10)

n5.left = n4
n5.right = n6
n9.left = n8
n9.right = n10
n7.left = n5
n7.right = n9

# in-order traverse
def inOrder(tree):
    if not tree:
        return
    if tree:
        if tree.left:
            inOrder(tree.left)
        print tree.val
        if tree.right:
            inOrder(tree.right)

# inOrder(n7)

# breath first tree traverse
def bft(tree):
    if not tree:
        return
    currentLevel = [tree]
    while len(currentLevel) > 0:
        node = currentLevel.pop(0)
        print node.val
        if node.left:
            currentLevel.append(node.left)
        if node.right:
            currentLevel.append(node.right)
    return

# bft(n7)

# sum all nodes witih recursion
def sumNodePreorder(tree):
    sumNodePreorder.total = 0 # declare as property of the function, otherwise, the inner function couldn't access it
    def helper(tree):
        if not tree:
            return 0
        sumNodePreorder.total += tree.val
        helper(tree.left)
        helper(tree.right)
        return sumNodePreorder.total
    helper(tree)
    return sumNodePreorder.total

print sumNodePreorder(n7)


# sum all nodes breadth first
def sumNodeBFS(tree):
    total = 0
    if not tree:
        return total
    currentLevel = [tree]
    while len(currentLevel)> 0:
        node = currentLevel.pop(0)
        total += node.val
        if node.left:
            currentLevel.append(node.left)
        if node.right:
            currentLevel.append(node.right)
    return total

print sumNodeBFS(n7)