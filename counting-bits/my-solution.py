from typing import List

# O(N(log(N)))
def countBits(n: int) -> List[int]:
    # initialise the results array
    res = [0] * (n + 1)
    
    # iterate through the array
    for i in range(len(res)):
        # count the bits in this index
        bit_count = 0
        # store the current index in its own variable
        current = i
        # while the current number is not 0
        while current:
            # current % 2 tells us if the bit in position 1 is 1 or 0
            # add the result of that to the bit count
            bit_count += current % 2
            # bit shift everything to the right so we can repeat the operation until
            # the number is zero
            current = current >> 1
        # when the number is zero, bit_count is the number of bits in the index
        res[i] = bit_count
    
    # return the result
    return res