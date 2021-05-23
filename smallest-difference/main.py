def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    pointerOne = 0
    pointerTwo = 0
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
	
    while pointerOne < len(arrayOne) and pointerTwo < len(arrayTwo):
        first = arrayOne[pointerOne]
        second = arrayTwo[pointerTwo]

        if first < second:
           current = second - first
           pointerOne += 1
        elif second < first:
            current = first - second
            pointerTwo += 1
        else:
            return [first, second]
		
        if smallest > current:
            smallest = current
            smallestPair = [first, second]
		
    return smallestPair
