# This solution implements a custom array reversal utility.
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # sort the arrays
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    # if we don't want the fastest, reverse one of the arrays
    if not fastest:
        reverseArrayInPlace(redShirtSpeeds)

    # initialise a variable to store the cumulated speed
    speed = 0

    # iterate through the array add the max speed at each index to the result
    for idx in range(len(redShirtSpeeds)):
        rider1 = redShirtSpeeds[idx]
        rider2 = blueShirtSpeeds[len(blueShirtSpeeds) - 1 - idx]
        speed += max(rider1, rider2)
        
    # return the result
    return speed

# util to reverse a list in place
def reverseArrayInPlace(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1




