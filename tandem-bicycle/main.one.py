def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # sort the first array
    redShirtSpeeds = sorted(redShirtSpeeds)
    # sort the second array and reverse it if `fastest` is True
    blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=fastest)
    # initialise a variable to store the cumulated speed
    speed = 0

    # iterate through the array add the max speed at each index to the result
    for i in range(len(redShirtSpeeds)):
        speed = speed + max(redShirtSpeeds[i], blueShirtSpeeds[i])
        
    # return the result
    return speed

