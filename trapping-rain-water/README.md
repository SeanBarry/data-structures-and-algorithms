# Trapping Rain Water

## Space Time Complexity

**Average**

O(N) time | O(1) space

---

## Task

[Link to Leetcode](https://leetcode.com/problems/trapping-rain-water/)

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

Sample Input:

```
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Sample Output:

```
6
// Explanation: The above elevation map (black section) is represented by array
// [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water are being trapped.
```

Sample Input 2:

```
height = [4,2,0,3,2,5]
```

Sample Output 2:

```
9
```

Constraints:

- `n == height.length`

- `1 <= n <= 2 * 10^4`

- `0 <= height[i] <= 10^5`
