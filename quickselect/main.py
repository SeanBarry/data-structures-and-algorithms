# Best - O(n) time | O(1) space
# Average - O(n) time | O(1) space
# Worst - O(n^2) time | O(1) space
def quickselect(array, k):
    # set the position as a var to mitigate against "off by 1" errors
    position = k - 1

    return quickselectHelper(array, 0, len(array) - 1, position)

def quickselectHelper(array, startIdx, endIdx, position):
    # There should always be a kth smallest value so execute until you find it
    while True:
        # if these pointers overlap, something has gone wrong
        if startIdx > endIdx:
            raise Exception("Your algorithm should never arrive here!")
        
        # set up vars for quick sort
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx

        # this is just standard quick sort logic
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1

        swap(pivotIdx, rightIdx, array)

        # the pivot has now been swapped with the value at the right pointer. At this point
        # in quick sort we'd recursively search the smallest sub array, but in quickselect
        # if the rightIdx is the position we are looking for, then we know it's the kth smallest value
        if rightIdx == position:
            return array[rightIdx]
        # if the sorted pivot is smaller than the position we're looking for, search the right array
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            # if the sorted pivot is larger than the position we're looking for, search the left array
            endIdx = rightIdx - 1

	
# util to swap two values in an array
def swap(one, two, array):
    array[one], array[two] = array[two], array[one]