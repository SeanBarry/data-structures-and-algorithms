def longestSubstringWithoutDuplication(string):
    # declare a cache for the positions of the most recent appearance of each character
    lastSeen = {}
    # declare a cache for the indices that create out current longest substring
    longest = [0, 1]
    # declare a cache for the current substring startIdx
    startIdx = 0

    # iterate over the string
    for i, char in enumerate(string):
        # if the character has been seen before
        if char in lastSeen:
            # update the startIdx to the max of startIdx and the lastSeen index + 1
            startIdx = max(startIdx, lastSeen[char] + 1)
        # update the longest indices if the current substring is longer
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        # update the lastSeen cache with the current index 
        lastSeen[char] = i
    # return the substring
    return string[longest[0]: longest[1]]