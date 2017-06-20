#. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

'''

def mergeTree(t1, t2): # recursive
    if t1 and t2:
        root = TreeNode(t1.val + t2.val)
        root.left = mergeTree(t1.left, t2.left)
        root.right = mergeTree(t1.right, t2.right)
        return root
    elif t1:
        return t1
    else:
        return t2