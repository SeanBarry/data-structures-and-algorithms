from typing import List

# O(N)
def countBits(n: int) -> List[int]:
    # initialise the results array
    res = [0] * (n + 1)
    # store the most significant bit
    offset = 1

    # iterate from 1 to n
    for i in range(1, n + 1):
        # if the index is equal to the most significant bit * 2, then
        # we have a new most significant bit, so set it
        if i == offset * 2:
            offset = i
        # the result is equal to the formula: 1 + dp[i - offset] # dp = dynamic program (cache)
        res[i] = 1 + res[i - offset]
    # return the result
    return res

    