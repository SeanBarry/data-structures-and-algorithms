def twoNumberSum(array, targetSum):
    cache = {}

    for num in array:
        unknown = targetSum - num
        if unknown in cache:
            return [unknown, num]
        else:
            cache[num] = True

    return []
