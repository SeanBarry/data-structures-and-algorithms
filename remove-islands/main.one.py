# O(w * h) time | O(w * h) space
# w is width of input matrix
# h is height of input matrix
def removeIslands(matrix):
    # initialise an auxilliary data structure to store which values are ones connected to the border
    onesConnectedToBorder = [[False for _ in row] for row in matrix]

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
                
            # if the element is in the border and a one, find any others ones connected to it
            findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

    # finally, iterate through the inner section of the matrix (the
    # section that doesn't touch the border at all)
    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            # if the element is in the onesConnectedToBorder structure,
            # then ignore it
            if onesConnectedToBorder[row][col]:
                continue
            
            # if it's not in onesConnectedToBorder then it's an island or already 0, set it to 0
            matrix[row][col] = 0
            
    return matrix
			
def findOnesConnectedToBorder(matrix, startRow, startCol, onesConnectedToBorder):
    # initialise a stack
    stack = [[startRow, startCol]]

    # iterate through the stack
    while len(stack) > 0:
        # grab an item from the stack
        current = stack.pop()
        # destructure the row/col
        currentRow, currentCol = current

        # use the aux data structure to figure out if we've already processed this element or not
        alreadyVisited = onesConnectedToBorder[currentRow][currentCol]

        # if we have, skip it
        if alreadyVisited:
            continue
        
        # otherwise mark it as visited/processed
        onesConnectedToBorder[currentRow][currentCol] = True

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
        
        
		