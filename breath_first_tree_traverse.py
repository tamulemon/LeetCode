def breathFirstTreeTraverse(root):
    currLevel = [root]
    nextLevel = []
    while currLevel:
        while currLevel:
            aNode = currLevel.pop()
            for child in aNode.children:
                print child
                nextLevel.append(child)
        currLevel = nextLevel
