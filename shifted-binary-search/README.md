# Shifted Binary Search

## Space Time Complexity

**Iterative**

O(log(N)) time | O(1) space

where:

n is the number of elements in the array

**Recursive**

O(log(N)) time | O(log(N)) space

where:

n is the number of elements in the array

---

## Task

Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that the integers in the array have been shifted by some amount; in other words, they've been moved to the left or to the right by one or more positions. For example, `[1, 2, 3, 4]` might have turned into `[3, 4, 1, 2]`.

The function should use a variation of the Binary Search algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise `-1`.

Sample input:

```
array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
```

Sample output:

```
8
```
