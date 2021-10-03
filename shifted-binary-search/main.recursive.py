# O(log(N)) time | O(log(n)) space
def binarySearchHelper(array, target, left, right):
    # if the left is greater than the right, return -1
    if left > right:
        return -1

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
            return binarySearchHelper(array, target, left, middle - 1)
        else:
             # otherwise discard it and search the right side
            return binarySearchHelper(array, target, middle + 1, right)
    else:
        # if the target it greater than the potentialMatch and less than the right value
        # then the right side is in sorted order and we can search it
        if target > potentialMatch and target <= rightNum:
            return binarySearchHelper(array, target, middle + 1, right)
        else:
            # otherwise search left side
            return binarySearchHelper(array, target, left, middle - 1)

def shiftedBinarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)
        