'''
Reverse a singly linked list.

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''

# rule of thumb: save next node
# reverse current and previous node
# move pointeres

def reverseList(head):
    if not head:
        return None

    prevNode = None
    while head:
        curNode = head  # move current node to headh
        head = head.next # move head to next
        curNode.next = prevNode # reverse
        prevNode = curNode # move tail

    return  curNode

# recursive method
def reverseList2(head, prev = None):
    if not head:
        return prev
    nextNode = head.next
    head.next = prev
    reverseList2(nextNode, head)