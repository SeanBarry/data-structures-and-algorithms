# O(wh) time | O(wh) space
# where w is the width of the matrix and h is the height of the matrix
# OR
# O(N) time | O(N) space
# where n is the number of elements in the matrix
def riverSizes(matrix):
    # initialise a cache of visited nodes that has the same dimensions as the matrix
    visited = [[False for _ in row] for row in matrix]
    # initialise the array of river sizes
    rivers = []

    # iterate through each row and column in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # if a node has already been visited, skip it
            if visited[i][j] == True:
                continue

            # otherwise call the helper function
            riverFinder(matrix, i, j, visited, rivers)

    return rivers


def riverFinder(matrix, i, j, visited, rivers):
    # initialise a river length count
    riverLength = 0
    # create a queue with the current node in it
    queue = [[i, j]]

    # while there are items in the queue
    while len(queue) > 0:
        # grab an item and grab the row/col numbers from it
        current = queue.pop()
        row = current[0]
        col = current[1]

        # if it has already been visited, don't process it
        if visited[row][col]:
            continue

        # mark the node as visited
        visited[row][col] = True

        # if the value is 0, the node is land so skip it
        if matrix[row][col] == 0:
            continue

        # it must be part of a river so increment the count
        riverLength += 1

        # if there is an unvisited node above it, add it to the queue
        if row > 0 and not visited[row - 1][col]:
            queue.append([row - 1, col])

        # if there is an unvisited node below it, add it to the queue
        if row < len(matrix) - 1 and not visited[row + 1][col]:
            queue.append([row + 1, col])
            
        # if there is an unvisited node to the left of it, add it to the queue
        if col > 0 and not visited[row][col - 1]:
            queue.append([row, col - 1])
            
        # if there is an unvisited node to the right of it, add it to the queue
        if col < len(matrix[0]) - 1 and not visited[row][col + 1]:
            queue.append([row, col + 1])

    # If the helper has found any river, add it to the results array
    if riverLength > 0:
        rivers.append(riverLength)
                