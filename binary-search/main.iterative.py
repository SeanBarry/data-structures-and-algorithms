# O(log(n)) time | O(1) space
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) -1)

# define a helper function
def binarySearchHelper(array, target, left, right):
    # while the pointers don't cross eachother
    while left <= right:
        # the midpoint is left + right floor divided by 2
        middle = (left + right) // 2
        # grab the value in the middle
        potentialMatch = array[middle]

        # if it matches, return the index
        if target == potentialMatch:
            return middle
        # if the target is less than the middle, move the right pointer
        # to the index before the middle
        elif target < potentialMatch:
            right = middle - 1
        # if the target is greater than the middle, move the left pointer
        # to the index after the middle
        else:
            left = middle + 1
    
    # The pointers crossed and the target wasn't found. Return
    # -1 or None or whatever is required
    return -1

