class Node:
    head = None

    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = None
        self.head = Node(value)

    def getValue(self):
        return self.value
    def setValue(self, newValue):
        self.value = newValue
    def getNext(self):
        return self.next
    def setNext(self, nextNode):
        self.next = nextNode

    def isEmpty(self):
        return self.head == None


    def addNodeToHead(self, newValue):
        tempNode = Node(newValue)
        tempNode.setNext(self.head)
        self.head = tempNode


    def listSize(self):
        curr = self.head
        ct = 0
        while curr != None:
            ct += 1
            curr = curr.getNext()

    def searchNode(self, valueToFind):
        curr = self.head
        while curr != None
            if curr.getValue() == valueToFind:
                return curr
            else:
                curr = curr.getNext()
        return None
    
tempNode = Node(93)

print tempNode.getValue()

print tempNode.getNext()
