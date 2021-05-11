def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# Average O(N^2) time | O(1) space
def selection_sort(array):
    currentIdx = 0

    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx

        for i in range(currentIdx + 1, len(array)):
            if array[i] < array[smallestIdx]:
                smallestIdx = i

        swap(currentIdx, smallestIdx, array)
        currentIdx += 1

    return array
