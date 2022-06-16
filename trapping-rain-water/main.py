from typing import List


def trap(height: List[int]) -> int:
    # if there are no elements in the list, return 0
    if not height:
        return 0
    
    # set up two pointers
    l, r = 0, len(height) - 1
    # store the maximum right and maximum left values
    leftMax, rightMax = height[l], height[r]
    # store the cumulative rain fall count
    res = 0
    
    # while the pointers never cross
    while l < r:
        # if the leftMax is less than the right max, increment the left pointer
        if leftMax < rightMax:
            l += 1
            # the new leftMax is the max of the existing value and the current one
            leftMax = max(leftMax, height[l])
            # then add difference between the leftMax and the current height to the result
            # note that this will be 0 if the leftMax has just been set
            res += leftMax - height[l]
        else:
            # decrement the right pointer
            r -= 1
            # the new rightMax is the max of the existing value and the current one
            rightMax = max(rightMax, height[r])
            # then add difference between the rightMax and the current height to the result
            # note that this will be 0 if the rightMax has just been set
            res += rightMax - height[r]
    # return the result
    return res