from typing import List

def maxArea(height: List[int]) -> int:
    # initialise two pointers
    l, r = 0, len(height) - 1
    
    # set a result
    max_area = float("-inf")
    
    # while the pointers haven't crossed
    while l < r:
        # the sum is equal to the width of the container multiplied by the
        # height of the smallest wall in the container
        sum = (r - l) * min(height[l], height[r])
        
        # update the max_area so far using max()
        max_area = max(max_area, sum)
        
        # if the left wall is smaller than the right wall, increment the left
        # pointer with the hopes that the next wall will be larger
        if height[l] < height[r]:
            l += 1
        # otherwise if the right is equal to, or smaller than the left, decrement
        # the right pointer
        else:
            r -= 1
    # return the max_area that was recorded
    return max_area
        
    