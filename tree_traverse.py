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
    if tree is None:
        return True
    # print tree["node"]
    if minVal <= tree["node"] <= maxVal:
        if tree["left"]:
            isLeftTreeSmallerThanRightTree(minVal, tree["node"], tree["left"])
        if tree["right"]:
            isLeftTreeSmallerThanRightTree(tree["node"], maxVal, tree["right"])

    return False

tree1 = {"node": 5, "left": {"node": 3, "left" : {"node": 1, "left":None, "right":None}, "right" : {"node": 4, "left":None, "right":None}}, "right":None}
tree2 = {"node": 5, "left": {"node": 3, "left" : {"node": 1, "left":None, "right":None}, "right" : {"node": 9, "left":None, "right":None}}, "right":None}

print isLeftTreeSmallerThanRightTree(float("-inf"), float("inf"), tree1)
print isLeftTreeSmallerThanRightTree(float("-inf"), float("inf"), tree2)


def maxDepth(root):
     if not root: # or if root is not None
         return 0

     return 1 + max(maxDepth(root.left), maxDepth(root.right))


def breathFirstTraverse(root):
    if not root:
        return
    currentLevel = []
    nextLevel = []

    currentLevel.append(root)
    while currentLevel:
        for node in currentLevel:
            nextLevel.extend([node.left, node.right])
            currentLevel = nextLevel
