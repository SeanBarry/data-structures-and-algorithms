

# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    # If the array is empty, return 0
	if not len(array):
		return 0
    # if the array has only one element, return it
	elif len(array) == 1:
		return array[0]
	
    # create first and second "holder" variables
	second = array[0]
	first = max(array[0], array[1])
	
    # iterate through the array from 2 onwards
	for i in range(2,len(array)):
        # recalculate the holder variables
		current = max(first, second + array[i])
		second = first
		first = current
	
    # return the first variable as it's the highest sum
	return first
		


# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
	
    # clone the array
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
	
    for i in range(2, len(array)):
        # the max sum is whatever is biggest out of:
        # - the previous max sum
        # - the previous previous max sum + the element in the array
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
		
    # return the final value in the max sums array
    return maxSums[-1]

		