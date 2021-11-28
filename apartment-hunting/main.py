def apartmentHunting(blocks, reqs):
    # Precompute a list per requirement of the min distance the requirement is from each block
    minDistancesFromBlocks = list(
        map(lambda req: getMinDistances(blocks, req), reqs)
    )
    # at this point for each requirement we have a list with the min distance the requirement is from each block.
    # we can work out which distance is the highest, and that will be the final "score" for the block 
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    # now we just need to find at which index the minimum 'score' is and return it
	return getIdxAtMinValue(maxDistancesAtBlocks)

def distanceBetween(a, b):
	return abs(a - b)

def getMinDistances(blocks, req):
    # initialise an empty array with the same length as blocks
	minDistances = [0 for block in blocks]
    # initialise an index cache
	closestReqIdx = float("inf")
	
	for i in range(len(blocks)):
        # if the block has the requirement, set the closestIdx to i
		if blocks[i][req]:
			closestReqIdx = i
		
        # in the minDistances list, calculate the distance between i and the closest Idx
		minDistances[i] = distanceBetween(i, closestReqIdx)
    
    # now traverse the list in the opposite direction
	for i in reversed(range(len(blocks))):
        # if there is a req on the block, cache the block index
		if blocks[i][req]:
			closestReqIdx = i
        # this time we set the distance to the minimum of the distance already populated
        # from the left->right run, or the difference between the index and the closest index
		minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
		
    # return the list of min distances per block for this requirement
	return minDistances
			
# calculate the "score" of each block by taking the "max distance" the block is from a req
def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    # initialise a list the same length as the blocks list
	maxDistancesAtBlocks = [0 for blocks in blocks]

	for i in range(len(blocks)):
        # this lambda will create a list with the distances for each req for the block
		minDistancesAtBlock = list(map(lambda distances: distances[i] , minDistancesFromBlocks))
        # the max distance for the block is just the max value from the list created above
		maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
	
    # return the list of max distances at each block
	return maxDistancesAtBlocks

# this util returns the idx at which the minimum value is in the array 
def getIdxAtMinValue(array):
	idxAtMinValue = 0
	minValue = float('inf')
    # iterate through the list
	for i in range(len(array)):
        # save the currentValue
		currentValue = array[i]
        # if the currentValue is less than the minValue, update both variables
		if currentValue < minValue:
			minValue = currentValue
			idxAtMinValue = i
    # return the minValue
	return idxAtMinValue
