# Product of Array Except Self

## Space Time Complexity

**Average**

O(N) time | O(1) space

---

## Task

[Link to Leetcode](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array `nums`, return an array answer such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

Sample Input:

```
nums = [1,2,3,4]
```

Sample Output:

```
[24,12,8,6]
```

Sample Input 2:

```
nums = [-1,1,0,-3,3]
```

Sample Output 2:

```
[0,0,9,0,0]
```

Constraints:

- `2 <= nums.length <= 10^5`

- `-30 <= nums[i] <= 30`

- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in `O(1)` extra space complexity? (The output array does not count as extra space for space complexity analysis.)
