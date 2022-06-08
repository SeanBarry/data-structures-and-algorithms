from collections import defaultdict
from typing import List

# this solution works by counting the number of letters in each word, and then appending
# the word to a list in a dictionary where the key is the count of letters in the word:
# e.g.:
# {
#    "1a1b1t": ["bat", "tab"],
#    "1a1e1t": ["eat", "ate"]
# }
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # initialise a hashmap to store the results. Use defaultdict with a default list
    # so we can append to it without having to deal with keys that don't yet exist
    res = defaultdict([list])
    
    # iterate through each string
    for s in strs:
        # initialise an array of zeroes, with 26 indices
        # each index corresponds to a letter in the alphabet
        # this list will be used to count how many times a letter
        # occurs in the word
        count = [0] * 26
        
        # for each letter in the string
        for c in s:
            # we can resolve the letter to an index in the count list above
            # by using ord(). By subtracting the value for "a" from the value for this
            # letter, we will end up with an array index value
            # E.G.:
            # the value returned by ord("a") is 97
            # the value returned by ord("c") is 99
            # 99 - 97 = 2 
            # so letter c will resolve to index 2, which corresponds to its
            # zero-positioned index in the alphabet
            count[ord(c) - ord("a")] += 1
        
        # we cannot use lists as the key in a dict in python, so instead we can convert it 
        # to a tuple, and then append the word to the key that corresponds to the count
        # of letters for this word
        res[tuple(count)].append(s)
    
    # now we return the values in the dict, the keys aren't needed
    return res.values()
    
    