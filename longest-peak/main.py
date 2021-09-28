def longestPeak(array):
    longestPeakLength = 0

    # set up a pointer to aid looping through the array
    i = 1

    while i < len(array) - 1:
        # a peak is when the pointer has a lower integer to the left and
        # a higher integer to the right
        isPeak = array[i - 1] < array [i] and array[i] > array[i + 1]

        # if a peak hasnt been found, continue through the array
        if not isPeak:
            i += 1
            continue
        
        # once we do find a peak, keep decrementing a left pointer whilst
        # each subsequent digit to the left is lower. Use a check of >= 0
        # to ensure the bounds aren't exceeded
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx] < array [leftIdx + 1]:
            leftIdx -= 1
        
        # similarly for the right pointer, continue to increment it whilst
        # each subsequent digit lower than the previous. Use a check of 
        # the array length to stay in bounds
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
            
        # calculate the length of the peak
        currentPeakLength = rightIdx - leftIdx - 1
        
        # update the longestPeakLength var using max
        longestPeakLength = max(longestPeakLength, currentPeakLength)

        # continue the search from the rightIdx. This is just an optimisation
        # to ensure the complexity remains linear, otherwise we'd continue the
        # search on digits we know are part of a previous peak
        i = rightIdx
    return longestPeakLength