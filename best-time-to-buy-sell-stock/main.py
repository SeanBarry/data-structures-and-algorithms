from typing import List 

def maxProfit(prices: List[int]) -> int:
    # set up two pointers
    l, r = 0, 1
    # set maxProfit to 0
    maxP = 0
    
    # iterate until the right pointer is out of bounds
    while r < len(prices):
        # if the left price is lower than the right price
        if prices[l] < prices[r]:
            # calculate the profit
            profit = prices[r] - prices[l]
            # use max to update maxP
            maxP = max(maxP, profit)
        else:
            # if left is LESS than right, then set left to the value of right
            l = r
        # iterate right always, regardless of which block of the if executes
        r += 1

    # return maxProfit which is zero by default
    return maxP
            
