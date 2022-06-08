# 3 Sum

## Space Time Complexity

**Average**

O(N^2) time | O(1) | O(N) space (depending on which sorting algorithm is used by the library you use)

---

## Task

[Link to Leetcode](https://leetcode.com/problems/3sum/)

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

Sample Input:

```
nums = [-1,0,1,2,-1,-4]
```

Sample Output:

```
[[-1,-1,2],[-1,0,1]]
```

Sample Input 2:

```
nums = []
```

Sample Output 2:

```
[]
```

Constraints:

- `0 <= nums.length <= 3000`

- `-10^5 <= nums[i] <= 10^5`
