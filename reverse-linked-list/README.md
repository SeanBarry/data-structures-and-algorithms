# Reverse Linked List

## Space Time Complexity

O(N) time | O(1) space

---

## Task

Write a function that takes in the head of a Singly Linked List, reverses the list in place (i.e., doesn't create a brand new list), and returns its new head.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or to `None` / `null` if the node is the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, the head will never be `None` / `null`

Sample input:

```
// the head node with value 0
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5
```

Sample output:

```
// the head node with value 5
5 -> 4 -> 3 -> 2 -> 1 -> 0
```
