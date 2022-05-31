# Counting Bits

## Space Time Complexity

O(N) time | O(N) space

---

## Task

[Link to Leetcode](https://leetcode.com/problems/counting-bits/)

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i (0 <= i <= n)`, `ans[i]` is the number of `1`'s in the binary representation of `i`.

Sample input:

```
n = 2
```

Sample output:

```
[0,1,1]
// 0 --> 0
// 1 --> 1
// 2 --> 10
```

Sample input 2:

```
n = 5
```

Sample output 2:

```
[0,1,1,2,1,2]
// 0 --> 0
// 1 --> 1
// 2 --> 10
// 3 --> 11
// 4 --> 100
// 5 --> 101
```

Constraints:

`0 <= n <= 10^5`

Follow up:

It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?
Can you do it without using any built-in function (i.e., like `__builtin_popcount` in C++)?
