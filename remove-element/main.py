def removeElement(nums, val):
    # initialise two pointers
    p1 = 0
    p2 = len(nums) - 1

    # iterate over values
    while p1 <= p2 and p1 < len(nums):
        # if the first pointer doesn't equal the value, increment it
        if nums[p1] != val:
            p1 += 1
        # if the second value equals the value, decrement it
        elif nums[p2] == val:
            p2 -= 1
        # swap the values if p1 is pointing to the target and p2 isn't, 
        # then increment p1
        elif nums[p1] == val and nums[p2] != val:
            swap(nums, p1, p2)
            p1 +=1
    # returning the position of p1 returns the length of the new results 
    return p1
            

# define a utility to swap values in an array in place
def swap(array, one, two):
    array[one], array[two] = array[two], array[one]
