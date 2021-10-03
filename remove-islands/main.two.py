# O(w * h) time | O(w * h) space
# w is width of input matrix
# h is height of input matrix
def removeIslands(matrix):
    # iterate through each element in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # initialise some variables to indicate if the row/col are in the border
            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue
                
            if matrix[row][col] != 1:
                continue
                
            # if the element is in the border and a one, change it and any connections to a 2
            changeOnesConnectedToBorderToTwos(matrix, row, col)
	
    # iterate through all elements in the matrix
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            color = matrix[row][col]
			
            # subtract 1 from 1s (islands)
            if color == 1:
                matrix[row][col] = 0

            # subtract 1 from 2s (1s connected to border)
            if color == 2:
                matrix[row][col] = 1

	return matrix
			
def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    # initialise a stack
    stack = [[startRow, startCol]]

    # iterate through the stack
    while len(stack) > 0:
        # grab an item from the stack
        current = stack.pop()
        # destructure the row/col
        currentRow, currentCol = current

        # set the element value to 2
        matrix[currentRow][currentCol] = 2

        # find all neighbours of this element
        neighbours = getNeighbours(matrix, currentRow, currentCol)

        # iterate through the neighbours
        for neighbour in neighbours:
            # destructure their values
            row, col = neighbour

            # if they aren't a 1, skip them
            if matrix[row][col] != 1:
                continue

            # otherwise add them to the stack so we can find their neighbours too
            stack.append(neighbour)
           
def getNeighbours(matrix, row, col):
    neighbours = []

    numRows = len(matrix)
    numCols = len(matrix[row])

    # up neighbour
    if row - 1 >= 0:
        neighbours.append([row - 1, col])
    # down neighbour
    if row + 1 < numRows:
        neighbours.append([row + 1, col])
    # left neighbour
    if col - 1 >= 0:
        neighbours.append([row, col - 1])
    # right neighbour
    if col + 1 < numCols:
        neighbours.append([row, col + 1])
        
    return neighbours
        