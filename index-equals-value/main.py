# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    # initialising a binary search
    left = 0
    right = len(array) - 1

    # while pointers haven't crossed
    while left <= right:
        # grab the middle idx and value
        middleIdx = (left + right) // 2
        middleValue = array[middleIdx]

        # if the middle value is less than it's index, then 
        # nothing to the left can have the same value as its index
        # so continue the binary search on the right subarray
        if middleValue < middleIdx:
            left = middleIdx + 1
        # if the value matches the index and the index is 0, then
        # it has to be the first instance of an element with the same
        # value as its index
        elif middleValue == middleIdx and middleIdx == 0:
            return middleIdx
        # if the value matches the index and the previous value is less than
        # its index then this has to be the first instance of an element with the same
        # value as its index
        elif middleValue == middleIdx and array[middleIdx - 1] < middleValue - 1:
            return middleIdx
        # this case handles the remaining TWO cases where we want to search the left sub array:
        # - we already found an index that matched its value, but now we are trying to find another
        # one earlier in the array
        # - the middle value is greater than the index, so all values to the right cannot match their index
        else:
            right = middleIdx - 1
    
    # return -1 if the while loop ends without returning an index
    return -1