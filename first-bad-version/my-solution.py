# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
def firstBadVersion(n: int) -> int:
    # set pointers at the left and right most values
    left = 1
    right = n
    
    # record what the earliest_known_bad version is
    earliest_known_bad = n
    
    # binary search the array
    while left <= right:
        middle = (left + right) // 2
        
        is_bad = isBadVersion(middle)
        
        # if this version is bad, continue searching but be sure
        # to record this version as the "earliest_known_bad" version we know of
        if is_bad:
            right = middle - 1
            earliest_known_bad = middle
        else:
            left = middle + 1
            
    return earliest_known_bad
    