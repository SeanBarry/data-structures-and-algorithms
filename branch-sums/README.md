# Branch Sums

## Space Time Complexity

**Average** O(N) time | O(N) space

where:

N is the number of nodes in the tree

**Note**

Why O(N) space?

There will be as many entries in the results array as there are branches. There will be as many branches as there are leaves. In a balanced tree there are roughly N / 2 leaves, which means the space complexity is O(N / 2) which sanitises to O(N).

---

## Task

Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum to rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree branch is a path of nodes in a tree that starts at the root node and ends at any leaf node.

Each Binary Tree node has an integer `value`, a `left` child node and a `right` child node. Children nodes can either be `BinaryTree` nodes themselves or `None`/`Null`

Sample Input:

```
 tree =    1
        /     \
       2       3
     /   \    /  \
    4     5  6    7
  /   \  /
 8    9 10
```

Sample Output:

```
[15, 16, 18, 10, 11]
// 15 == 1 + 2 + 4 + 8
// 16 == 1 + 2 + 4 + 9
// 18 == 1 + 2 + 5 + 10
// 10 == 1 + 3 + 6
// 11 == 1 + 3 + 7
```
