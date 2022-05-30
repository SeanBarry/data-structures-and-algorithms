from typing import List


def singleNumber(nums: List[int]) -> int:
    # initialise a result var to 0
    res = 0
    # iterate through the array
    for num in nums:
        # perform an XOR operation on each num
        res = res ^ num
    
    # return the result
    return res