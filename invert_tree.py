'''
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

'''
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''


def invertTree(self, root):
    if not root:
        return
    else:
        temp = invertTree(root.left)
        root.left = invertTree(root.right)
        root.right = temp
    return root
        # or this because the right side of the = will be evaluated before the left side
        # root.left, root.right = invertTree(root.right), invertTree(root.left)

        # this will not work as the left will already be overwritten in the first line, so we need a temp
        # root.left = invertTree(root.right)
        # root.right = invertTree(root.left)


