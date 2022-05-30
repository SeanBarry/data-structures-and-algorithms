# More complex solution but still runs in O(1)
def hammingWeight(n: int) -> int:
    res = 0
    
    while n:
        n &= (n - 1)
        res += 1
    return res
    