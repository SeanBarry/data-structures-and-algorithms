# O(n) time | O(1) space
def sunsetViews(buildings, direction):
    # initialise stack using list
    candidateBuildings = []

    # programmatically control direction of loop
    startIdx = 0 if direction == 'EAST' else len(buildings) - 1
    step = 1 if direction == 'EAST' else -1

    idx = startIdx

    while idx >= 0 and idx < len(buildings):
        # grab current building height as var
        buildingHeight = buildings[idx]

        # while the last building in the stack is equal or smaller than current, pop it
        while len(candidateBuildings) > 0 and buildings[candidateBuildings[-1]] <= buildingHeight:
            candidateBuildings.pop()

        # now add the building to the stack
        candidateBuildings.append(idx)

        # increment the loop to the next building
        idx += step

    # use python magic to reverse the array depending on the direction
    if direction == "WEST":
        return candidateBuildings[::-1]

    return candidateBuildings