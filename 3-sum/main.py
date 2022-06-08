from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    # initialise a list for the results
    res = []
    # sort the input array of numbers
    nums.sort()
    
    # iterate over each using it as the "first" or "left" number
    for i, a in enumerate(nums):
        # if this isn't the first number and it's the same as the previous number, skip it
        if i > 0 and nums[i - 1] == a:
            continue
            
        # now that we already have a first number that isn't a duplicate, this just becomes two sum
        # set a left and right pointer
        l, r = i + 1, len(nums) - 1
        # while the two pointers don't cross
        while l < r:
            # the sum is all 3 values combined
            sum = a + nums[l] + nums[r]
            
            # if the sum is zero, we've found a result
            if sum == 0:
                # add the result to the results array
                res.append([a, nums[l], nums[r]])
                # at this point there still may be other results that work for the current
                # value `a` that we are enumerating over, so we need to increment the l pointer
                l += 1
                # but it's possible the value at the next l index may be the same value, so 
                # we need to continue to increment the left pointer value until it's no longer
                # the same, whilst also being careful not to pass the right pointer
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
            # standard 2 sum - if the sum is greater, decrement the right pointer
            elif sum > 0:
                r -= 1
            # standard 2 sum - if the sum is less, increment the left pointer
            elif sum < 0:
                l += 1
    # return our results
    return res
        