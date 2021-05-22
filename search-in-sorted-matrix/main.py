def searchInSortedMatrix(matrix, target):
    colPointer = len(matrix[0]) - 1
    rowPointer = 0

    while colPointer > -1 and rowPointer < len(matrix):
        if target < matrix[rowPointer][colPointer]:
            colPointer -= 1

        if target > matrix[rowPointer][colPointer]:
            rowPointer += 1

        if target == matrix[rowPointer][colPointer]:
            return [rowPointer, colPointer]

    return [-1, -1]
