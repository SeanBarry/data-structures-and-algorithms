from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    # set a slow and a fast pointer
    slow, fast = head, head
    
    # while the fast and the fast.next are not none
    while fast and fast.next is not None:
        # increment the slow by one, and the fast by two
        slow = slow.next
        fast = fast.next.next
        
        # if the pointers ever meet, there is a cycle
        if slow == fast:
            return True
    
    # if we break from the while loop, then the fast pointer has reached the end of the LL
    # so there can't be a cycle and we return False
    return False