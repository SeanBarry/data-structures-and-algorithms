# Remove Islands

## Space Time Complexity

O(wh) time | O(wh) space

where:

w is the width of the matrix

h is the height of the matrix

OR

O(N) time | O(N) space

where:

n is the number of elements in the matrix

---

## Task

You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only `0`s and `1`s. The matrix represents a two-toned image, where each `1` represents black and each `0` represents white. An island is defined as any number of `1`s that are horizontally or vertically adjacent (but not diagonally adjacent) and that don't touch the border of the image. In other words, a group of horizontally or vertically adjacent `1`s isn't an island if any of those `1`s are in the first row, last row, first column, or last column of the input matrix.

Note that an island can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example.

You can think of islands as patches of black that don't touch the border of the two-toned image.

Write a function that returns a modified version of the input matrix, where all of the islands are removed. You remove an island by replacing it with `0`s.

Naturally, you're allowed to mutate the input matrix.

Sample input:

```
matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1],
]
```

Sample output:

```
[
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1],
]
```

## Notes

The differences between solution one and two are:

- solution one uses an auxilliary datastructure to store which nodes have a value of 1 and are connected to the border
- solution two instead mutates the original matrix such that nodes with a a value of one that are connected to the border have their value incremented to two. Then at the end it iterates through the entire matrix and subtracts 1 from any nodes with value 2 or 1.

They both have the same time/space complexity - but solution two's space complexity is probably better in the average case because the space complexity of O(wh) comes from the usage of a stack. In the average case, this stack won't use O(wh) space.
