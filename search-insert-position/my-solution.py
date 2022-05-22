def searchInsert(nums: List[int], target: int) -> int:
    # set pointers
    left, right = 0, len(nums) - 1
    # init these variables so we can use them outside the while loop
    middle, potential_match = None, None

    # perform a binary search
    while left <= right:
        middle = (left + right) // 2
        
        potential_match = nums[middle]
        
        if target == potential_match:
            return middle
        elif target < potential_match:
            right = middle - 1
        else:
            left = middle + 1
    
    # at the end, if the potential match is smaller than the
    # target then the target would be _after_ it in the list
    # e.g.  [2, 3]
    #           pm   t
    #      [2,  3,   5]
    if potential_match < target:
        return middle + 1
    # if the potential match is greater than the target then
    # the target would be in its position
    # e.g.  [2, 5]
    #           t    pm
    #      [2,  3,   5]
    #
    elif potential_match > target:
        return middle