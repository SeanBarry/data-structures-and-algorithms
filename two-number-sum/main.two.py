def twoNumberSum(array, targetSum):
    leftIdx = 0
    rightIdx = len(array) - 1
    array.sort()
	
    while leftIdx < rightIdx:
    	currentSum = array[leftIdx] + array[rightIdx]
		
    	if currentSum == targetSum:
    		return [array[leftIdx], array[rightIdx]]
    	elif currentSum < targetSum:
    		leftIdx += 1
    	elif currentSum > targetSum:
    		rightIdx -= 1
		
    return []
