class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeLinkedLists(headOne, headTwo):
    # initialise the pointers
    p1 = headOne
    p2 = headTwo
    p1Prev = None

    # traverse until one of the nodes is None 
    while p1 is not None and p2 is not None:
        # easy case, the value of p1 (the first list)
        # is lower than the node in the second list.
        # all we do here is set p1Prev to p1, and set p1 to p1.next
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else:
            # edge case - the node is the first in the list
            # so it's None. We can't access .next in this instance
            if p1Prev is not None:
                # overwrite the link between the prev and p1
                p1Prev.next = p2
            # set p2 to be the previous
            p1Prev = p2
            # p2 is now the next element in the second list
            p2 = p2.next
            # finally, write the connection from the new previous
            # which is the element in the second list that we are swapping
            # to point to p1
            p1Prev.next = p1
            
        # if our loop exits because p1 is None, then all values left in p2 are greater than p1, so connect p1 to p2
        if p1 is None:
            p1Prev.next = p2
    # use a ternary to return the head with the lowest value
    return headOne if headOne.value < headTwo.value else headTwo
