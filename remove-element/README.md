# Remove Element

## Link

[Leetcode - Remove Element](https://leetcode.com/problems/remove-element/)

## Space Time Complexity

O(n) time | O(1) space

where:

n is the number of elements in the array

---

## Task

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the `first part` of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the firs`k` elements.

Return `k` after placing the final result in the first `k` slots of `nums`. Do `not` allocate extra space for another array. You must do this by modifying the input array `with O(1) extra memory.`

Sample input:

```
nums = [3,2,2,3], val = 3
```

Sample output:

```
2, nums = [2,2,_,_]
// Your function should return k = 2, with the first two elements of nums being 2.
```
