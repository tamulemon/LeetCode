'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

# the tortoise and hare method for cycle detection:

# a fast pointer, moves 2 steps at a time
# a slow pointer, moves 1 step at a time
# if there is a cycle, the 2 pointers will eventually meet
# if not, they will finish linked list and never meet

def hasCycle(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False