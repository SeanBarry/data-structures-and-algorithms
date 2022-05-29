from typing import List


def maxSubArray(nums: List[int]) -> int:
    # initialise a var to store the largest sum as the first array item
    largest_sum = nums[0]
    # initialise another var to store the running sum
    sum = 0
    
    # iterate through the array
    for num in nums:
        # if the sum from previous indices is less than 0, reset the sum.
        # those indices don't count towards the sum as their value is negative
        if sum < 0:
            sum = 0
        # add the current number to the sum
        sum += num
        
        # set the largest_sum to the max of itself and the current sum
        largest_sum = max(sum, largest_sum)

    # return the largest sum
    return largest_sum