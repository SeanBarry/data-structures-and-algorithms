def sortedSquaredArray(array):
    smallIdx = 0
    largeIdx = len(array) - 1
    sorted = [0 for _ in array]
	
    for idx in reversed(range(len(array))):
	    small = array[smallIdx]
	    large = array[largeIdx]
		
	    if abs(large) > abs(small):
	    	sorted[idx] = large * large
	    	largeIdx -= 1
	    else:
	    	sorted[idx] = small * small
	    	smallIdx += 1
    
    return sorted
