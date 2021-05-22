# Selection Sort

## Space Time Complexity

**Best** O(N^2) time | O(1) space

**Average** O(N^2) time | O(1) space

**Worst** O(N^2) time | O(1) space

---

## Task

Write a function that takes in an array of integers and returns a sorted version of that array. Use the Selection Sort algorithm to sort the array.

Sample Input:

`[8, 5, 2, 9, 5, 6, 3]`

Sample Output:

`[2, 3, 5, 5, 6, 8, 9]`

Selection sort works by creating a pointer, which to begin with is set to index 0 of the list. While the pointer is not beyond the right bound of the list, a variable of 'smallestIndex' is stored. In each iteration of the unsorted list, the algorithm stores the index of the lowest value in `smallestIndex`. At the end of the list, it swaps the smallest value it found with the value the pointer is currently on. It then increases the value of the pointer.
