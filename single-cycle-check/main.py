# helper function for code clarity
def getNextIdx(currentIdx, array):
    # get the value we need to jump by
	jump = array[currentIdx]
    
    # this logic helps us wrap around the edges of the array
	nextIdx = (currentIdx + jump) % len(array)
	# The commented out part isn't needed in Python because the mod
	# operator in Python does this for us. In other languages it would
	# be needed as the value returned could be negative

	return nextIdx # if nextIdx >=0 else nextIdx + len(array)

# O(n) time | O(1) space
def hasSingleCycle(array):
    # track the number of elements visited
	numElementsVisited = 0
    # track the current index
	currentIdx = 0
	
    # loop as many times as there are elements to visit
	while numElementsVisited < len(array):
        # if we are back at the first element before the loop ends, the cycle is closed early so we
        # can return False
		if numElementsVisited > 0 and currentIdx == 0:
			return False
        # increment the count
		numElementsVisited += 1
        # jump to the next index in the array 
		currentIdx = getNextIdx(currentIdx, array)
		
	return currentIdx == 0
	
	
		
		
