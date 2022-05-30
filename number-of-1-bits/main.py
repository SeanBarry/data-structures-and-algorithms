def hammingWeight(n: int) -> int:
    # initialise a result var at 0
    res = 0
    
    # while n is not zero
    while n:
        # use modulo to know if there is a '1' bit present. Add the result to `res`
        res = res + n % 2
        # then shift all bits to the right so we can evaluate the next bit
        n = n >> 1
    # return the count of 1 bits
    return res
    