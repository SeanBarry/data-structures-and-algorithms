# Min Max Stack Construction

## Space Time Complexity

All operations should be O(1) time | O(1) space

The space usage of the stack itself is O(n)

---

## Task

Write a `MinMaxStack` class for a Min Max Stack. The class should support:

    - Pushing and popping values on and off the stack.

    - Peeking at the value at the top of the stack.

    - Getting both the minimum and the maximum values in the stack at any given
    point in time.

All class methods, when considered independently, should run in constant time
and with constant space.

Sample input:

```
// All operations below are performed sequentially
MinMaxStack()
push: -
getMin: 5
getMax: 5
peek: 5
push: -
getMin: 5
getMax: 7
peek: 7
push: -
getMin: 2
getMax: 7
peek: 2
pop: 2
pop: 7
getMin: 5
getMax: 5
peek: 5
```
