# Node Depths

## Space Time Complexity

**Average** O(N) time | O(h) space

where:

N is the number of nodes in the tree

h is the height of the tree

---

## Task

The distance between a node in a Binary Tree and the tree's root is called the node's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes' depths.

Each `BinaryTree` node has an integer `value`, a `left` child node, and a `right` child node. Children nodes can either be `BinaryTree` nodes themselves or `None`/`Null`.

Sample Input:

```
tree =    1
       /     \
      2       3
    /   \   /   \
   4     5 6     7
 /   \
8     9
```

Sample Output:

```
16
```
