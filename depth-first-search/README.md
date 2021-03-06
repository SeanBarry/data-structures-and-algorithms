# Depth-First Search

## Space Time Complexity

**Average** O(v + e) time | O(v) space

where:

v is the number of vertices

e is the number of edges

---

## Task

You're given a `Node` class that has a `name` and an array of optional `children` nodes. When put together, nodes form an acyclic tree-like structure.

Implement the `depthFirstSearch` method on the `Node` class, which takes in an empty array, traverses the tree using the Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes' names in the input array, and returns it.

Sample Input:

```
graph = A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
```

Sample Output:

```
["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
```
