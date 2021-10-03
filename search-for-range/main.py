# O(log(n)) time | O(1) space
def searchForRange(array, target):
    # create the result, which will either be returned as is, or altered then returned
    finalRange = [-1, -1]

    # call binary search twice, once expanding left, once expanding right
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array) - 1, finalRange, False)

    # return the results
    return finalRange

# create an altered binary search helper
def alteredBinarySearch(array, target, left, right, finalRange, goLeft):
    # while left pointer is less or equal to right
    while left <= right:
        # identify the middle of the array
        middle = (left + right) // 2
        # grab the value there
        potentialMatch = array[middle]

        # as in a normal binary search, adjust which half of the array you query
        if target < potentialMatch:
            right = middle - 1
        elif target > potentialMatch:
            left = middle + 1

        # if the middle value matches the target
        if potentialMatch == target:
            # if this is the "left" call
            if goLeft:
                # if the match value is at the start of the array, or the previous value
                # does not equal the match value, then we are at the first instance of the target
                if middle == 0 or array[middle - 1] != target:
                    # update the results index with the array index on the left
                    finalRange[0] = middle
                    # important to return at this point otherwise the while loop won't exit.
                    return
                else: 
                    # search again using in the left array
                    right = middle - 1
            else:
                 # if the match value is at the end of the array, or the next value
                # does not equal the match value, then we are at the last instance of the target
                if middle == len(array) -1 or array[middle + 1] != target:
                    # update the results index with the array index on the left
                    finalRange[1] = middle
                    # important to return at this point otherwise the while loop won't exit.
                    return
                else:
                    # search again using in the right array
                    left = middle + 1
