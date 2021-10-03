# O(log(N)) time | O(1) space
def shiftedBinarySearch(array, target):
    # initialise the pointers
    left = 0
    right = len(array) - 1

    while left <= right:
        # find the midpoint (floor divided)
        middle = (left + right) // 2
        # grab the potentialMatch value
        potentialMatch = array[middle]
        # grab the left and right values
        leftNum = array[left]
        rightNum = array[right]

        # if the potentialMatch is the target, return it
        if target == potentialMatch:
            return middle
        # If the left value is less than the potential match
        elif leftNum <= potentialMatch:
            # if target less than the potential match and the target is greater than the left value
            # then the left side is sorted and we can search it
            if target < potentialMatch and target >= leftNum:
                right = middle - 1
            else:
                # otherwise discard it and search the right side
                left = middle + 1
        else:
            # if the target it greater than the potentialMatch and less than the right value
            # then the right side is in sorted order and we can search it
            if target > potentialMatch and target <= rightNum:
                left = middle + 1
            else:
                # otherwise search left side
                right = middle - 1
            
    # return -1 as the while loop has ended and the target has not been found
    return -1