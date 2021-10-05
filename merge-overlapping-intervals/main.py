# O(nLog(n)) time | O(n) space
def mergeOverlappingIntervals(intervals):
    # sort the intervals by the first digit in each
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    # initialise the results list
    mergedIntervals = []
    # grab the first interval and set it as the current
    currentInterval = sortedIntervals[0]
    # add the current interval to the results list
    mergedIntervals.append(currentInterval)

    # now iterate through the sorted intervals. On the first iteration
    # the nextInterval is the same as the currentInterval so the first
    # part of the if statement will be executed. All this results in is
    # the mergedIntervals being identical to its state at the beginning
    for nextInterval in sortedIntervals:
        # grab useful values as variables
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        # if the intervals overlap
        if currentIntervalEnd >= nextIntervalStart:
            # then modify the value of the currentInterval such that the 
            # second element is the max of both second elements
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            # if they don't overlap then update the currentInterval to be the
            # next interval and insert it in to the results array
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    # finally return the intervals
    return mergedIntervals
        