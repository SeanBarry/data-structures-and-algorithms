# O(n) | O(1) space
def subarraySort(array):
    # initialise two variables set to inf and -inf
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    # iterate through the array
    for i in range(len(array)):
        num = array[i]

        if isOutOfOrder(i, num, array):
            # if a number is out of order, save the min of it vs the current min as a var
            minOutOfOrder = min(minOutOfOrder, num)
            # if a number is out of order, save the miax of it vs the current max as a var
            maxOutOfOrder = max(maxOutOfOrder, num)
    
    # edge case - the input array is sorted so there is no 
    # min or max out of order. Check one of them, if it's still
    # the initialised value, return the base case [-1, -1]
    if minOutOfOrder == float("inf"):
        return [-1, -1]

    # at this point we have the smallest and largest numbers that are out of order
    subarrayLeftIdx = 0
    # iterate over the array from left to right. While the smallest out of order
    # number is bigger or equal to the current value, increment the index we are searching.
    # Once this exits, the index is the sorted position of our smallest unsorted value
    while minOutOfOrder >= array[subarrayLeftIdx]:
        subarrayLeftIdx += 1

    # iterate over the array from right to left. While the largest out of order
    # number is smaller or equal to the current value, decrement the index we are searching.
    # Once this exits, the index is the sorted position of our largest unsorted value
    subarrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subarrayRightIdx]:
        subarrayRightIdx -= 1
        
    # now we can return these two indices as we know the start and end of the
    # sub array that needs to be sorted
    return [subarrayLeftIdx, subarrayRightIdx]


# a helper function to return when a num is out of order
def isOutOfOrder(i, num, array):
    # on the left hand side, if the num is larger than the following value
    # return true, otherwise false
    if i == 0:
        return num > array[i + 1]

    # on the right hand side, if the num is smaller than the preceding value
    # return true, otherwise false
    if i == len(array) - 1:
        return num < array[i - 1]

    # otherwise assert that the number is greater than the following or smaller than
    # the preceding. If these are the case the number is out of order and the util
    # will return true
    return num > array[i + 1] or num < array[i - 1]