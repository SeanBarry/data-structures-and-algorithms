from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # initialise a cache to count the occurrences
    cache = {}
    # initialise a list of buckets, each bucket containing a list
    # the list in each bucket is populated with the digits that occur
    # the same number of times as `i - 1`
    # E.G.
    # input = [1, 1, 1, 2, 2, 3]
    #                  
    # freq = [[3],[2],[1],[],[],[]]
    freq = [[] for _ in nums]
    
    # count the occurences of each digit
    for num in nums:
        cache[num] = 1 + cache.get(num, 0)
    
    # iterate through the counts, placing each number in
    # the correct bucket corresponding to how many times it occurred
    for n, c in cache.items():
        freq[c - 1].append(n)
        
    # create an array of results
    res = []
    # now iterate from the end of the buckets array
    for i in reversed(range(len(freq))):
        # if there are any digits that occured i number of times
        for n in freq[i]:
            # then place them in the results array
            res.append(n)
            # we want to stop executing when the results array is the length of k
            if len(res) == k:
                # and finally return the results
                return res