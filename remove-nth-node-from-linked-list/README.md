# Remove Nth Node From Linked List

## Space Time Complexity

O(N) time | O(1) space

---

## Task

Write a function that takes in the head of a Singly Linked List and an integer `n` and removes the nth node from the end of the list.

The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).

Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done, even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed to be removed, your function should simply mutate its `value` and `next` pointer.

Note that your function doesn't need to return anything.

You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.

Each `LinkedList` node has an integer `value` as well as a `next` node pointing to the next node in the list or `None` / `null` if it's the tail of the list.

Sample Input:

```
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
n = 4
```

Sample Output:

```
// No output required
// The 4th node from the end of the list (with value 6) has been removed
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
```
