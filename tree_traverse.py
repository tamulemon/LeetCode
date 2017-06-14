# tree traverse
# - In order : left, root, right
# - pre order : root, left , right
# - post order: left, right, root
#
# balanced tree: except the leaf node, each level is full, has 2^n nodes

def preorder(tree):
    if tree != None:
        print(tree.root())
        preorder(tree.left())
        preorder(tree.right())

def postorder(tree):
    if tree != None:
        postorder(tree.left())
        postorder(tree.right())
        print(tree.root())



def isLeftTreeSmallerThanRightTree(minVal, maxVal, tree):
    if tree == None:
        return True
    # print tree["node"]
    if minVal <= tree["node"] <= maxVal:
        if tree["left"] != None:
            isLeftTreeSmallerThanRightTree(minVal, tree["node"], tree["left"])
        if tree["right"] != None:
            isLeftTreeSmallerThanRightTree(tree["node"], maxVal, tree["right"])

    return False

tree1 = {"node": 5, "left": {"node": 3, "left" : {"node": 1, "left":None, "right":None}, "right" : {"node": 4, "left":None, "right":None}}, "right":None}
tree2 = {"node": 5, "left": {"node": 3, "left" : {"node": 1, "left":None, "right":None}, "right" : {"node": 9, "left":None, "right":None}}, "right":None}

print isLeftTreeSmallerThanRightTree(float("-inf"), float("inf"), tree1)
print isLeftTreeSmallerThanRightTree(float("-inf"), float("inf"), tree2)