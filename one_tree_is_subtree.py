'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

'''

## this will test whether 2 tree equals
def isEqualTree(t1, t2):
    if not t1 and not t2:
        return True
    if t1 is not None and t2 is not None: # both are not empty
        return (t1.val == t2.val \
                and isEqualTree(t1.left, t2.left) \
                and isEqualTree(t1.right, t2.right)) # all 3 parts need to be equal
    else: # if one is empty and one is not
        return False



def isSubTree(t1, t2):
    # find t2 root in t1 first
    # check whether the rest equal
    # O(t1*t2)
