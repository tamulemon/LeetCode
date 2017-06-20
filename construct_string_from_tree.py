'''
Note: this qustion has problem, skip
preorder 


Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"



Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"
'''

def tree2str(t):
    outputStr = ''

    if not t:
        return ''
    if  t.left:
        left = '({})'.format(tree2str(t.left))
    if t.right:
        right = '({})'.format(tree2str(t.right))
    return
    '{}{}{}'.format(t.val, left, right)