def isMonotonic(array):
    if len(array) < 2:
        return True;
	
    start = array[0]
    end = array[len(array) - 1]
    trendingUp = end > start
	
    for i in range(1, len(array) - 1):
        if trendingUp and array[i] < array[i - 1]:
            return False;
        elif not trendingUp and array[i] > array[i - 1]:
            return False;
	
    return True