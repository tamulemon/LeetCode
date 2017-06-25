'''
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

'''
def sumOfLeftLeaves(root):
    if not root:
        return 0
    if root.left and (not root.left.left) and (not root.left.right): # leaf node
        return root.left.value + sumOfLeftLeaves(root.right)
    return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right) # not leaf node

