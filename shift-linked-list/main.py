# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) time | O(1) space
def shiftLinkedList(head, k):
    # create a counter for the length
    listLength = 1
    # initiate the listTail variable
    listTail = head

    # iterate through the LL to find the length 
    # at the end of the loop, we have the listTail node too
    while listTail.next is not None:
        listTail = listTail.next
        listLength += 1

    # use modulo to calculate the offset. Because it could be negative
    # we use abs(). We use modulo incase k is a number higher than the length
    # of the LL.
    offset = abs(k) % listLength

    # edge case: if k is 0, we won't perform any shifts and can return the head as is.
    if offset == 0:
        return head

    # if k is positive, the new tail will be the node kth from the end. So we can
    # subtract k from the list length to find the new tail position.
    # if k is negative, the new tail position will be the kth element from the start
    newTailPosition = listLength - offset if k > 0 else offset

    # we now do another loop, this time from 1 until the new tail position
    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next
        
    # finally, we can perform some swaps to shift the LL.
    # for the following LL:
    # head = 0 -> 1 -> 2 -> 3 -> 4 -> 5
    # k = 2
    # at this point the state will be:
    # 0 -> 1 -> 2 -> 3 -> 4 -> 5
    # |              |         |
    # head        newTail   listTail

    # 4 becomes the newHead
    newHead = newTail.next
    # 3.next becomes None as it's the new tail
    newTail.next = None
    # 5.next becomes the head as it's now the 2nd node in the list
    listTail.next = head

    # finally, we can return the shifted LL head
    return newHead
        