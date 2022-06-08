from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    # initialise a results array with a 1 at each index
    products = [1] * len(nums)

    # store the "prefix" product (the product of all digits before the current digit)
    # this needs to be initialised to 1 to begin with as there is no prefix for the first digit
    leftRunningProduct = 1
    # make a left -> right pass through the array
    for i in range(len(nums)):
        # set the current index in the products array to the value of the prefix
        products[i] = leftRunningProduct
        # multiply the prefix value by the value in the nums array so we have the prefix ready
        # for when we move to the next digit
        leftRunningProduct *= nums[i]

    # store the "postfix" product (the product of all digits after the current digit)
    # this needs to be initialised to 1 to begin with as there is no postfix for the last digit
    rightRunningProduct = 1
    # make a right -> left pass through the array
    for i in reversed(range(len(nums))):
        # multiply the current index in the products array by the value of the postfix
        products[i] *= rightRunningProduct
        # multiply the postfix value by the value in the nums array so we have the postfix ready
        # for when we move to the next digit
        rightRunningProduct *= nums[i]

    # return the results list
    return products
