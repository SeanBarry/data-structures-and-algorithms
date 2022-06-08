# Container With Most Water

## Space Time Complexity

**Average**

O(N) time | O(1) space

---

## Task

[Link to Leetcode](https://leetcode.com/problems/container-with-most-water/)

You are given an integer array height of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Sample Input:

```
height = [1,8,6,2,5,4,8,3,7]
```

Sample Output:

```
49
```

Sample Input 2:

```
height = [1,1]
```

Sample Output 2:

```
1
```

Constraints:

- `n == height.length`

- `2 <= n <= 10^5`

- `0 <= height[i] <= 10^4`
