def underscorifySubstring(string, substring):
    # Get locations of all occurrences of substring in string
    # Collapse locations to remove overlapping occurrences
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)


# iterate through string, find all start/end indices of substring
def getLocations(string, substring):
    locations = []
    startIdx = 0

    while startIdx < len(string):
        # use the native .find method to find the start index of substring
        # passing the start index as the second argument to .find()
        index = string.find(substring, startIdx)

        # if the substring is found, append the start and end indices to the locations list
        if index != -1:
            locations.append([index, index + len(substring)])
            # increment the start index to avoid finding the substring again
            # incrementing it by one ensures if there are overlapping occurrences of the substring
            # they are found
            startIdx = index + 1
        else:
            break
    return locations


def collapse(locations):
    # if there are no locations, just return the empty array
    if len(locations) == 0:
        return locations

    # initialise a new array with the first location in it
    new_locations = [locations[0]]
    # set the previous variable to the first locations array
    previous = new_locations[0]

    # iterate through the rest of the locations array
    for i in range(1, len(locations)):
        current_location = locations[i]
        # if the current location overlaps with the previous one, mutate the previous one
        # such that the current endIdx overwrites the previous endIdx
        if current_location[0] <= previous[1]:
            previous[1] = current_location[1]
        else:
            # otherwise, add the current location to the new locations array
            new_locations.append(current_location)
            # update the previous variable to the current location
            previous = current_location

    return new_locations


# insert underscores into the string at the given locations
def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False
    finalChars = []
    i = 0
    # iterate through the string and the locations at the same time
    while stringIdx < len(string) and locationsIdx < len(locations):
        # if the current string index is equal to the current location index
        if stringIdx == locations[locationsIdx][i]:
            # append an underscore
            finalChars.append("_")
            # flip this variable value to the opposite
            inBetweenUnderscores = not inBetweenUnderscores
            # if we aren't in between underscores, increment the location index as we've
            # just closed the underscores after a substring, and want to continue to the next location
            if not inBetweenUnderscores:
                locationsIdx += 1
            # flip the i variable to ensure we flip between using the start/end location indices
            i = 0 if i == 1 else 1

        # ensure we append the other characters to the final string
        finalChars.append(string[stringIdx])
        stringIdx += 1
    # we've broken out of the while loop so need to make sure we finish the task
    # if the locationsIdx is less than the length of the locations array,
    # then there is an underscore at the very end of the string which we need to add
    if locationsIdx < len(locations):
        finalChars.append("_")
    # otherwise, there may have been a last underscore in the middle of the string, so we need to
    # add the rest of the string to the finalChars array
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])

    # create a string from the finalChars list and return it
    return "".join(finalChars)
