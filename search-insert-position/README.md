# Search Insert Position

## Space Time Complexity

**Average** O(log(N)) | O(1) space

---

## Task

[Link to Leetcode](https://leetcode.com/problems/search-insert-position/)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

Sample Input:

```
nums = [1,3,5,6], target = 5
```

Sample Output:

```
2
```

Sample Input 2:

```
nums = [1,3,5,6], target = 2
```

Sample Output 2:

```
1
```

Constraints:

`1 <= nums.length <= 10^4`

`-10^4 <= nums[i] <= 10^4`

`nums contains distinct values sorted in ascending order.`

`-10^4 <= target <= 10^4`
