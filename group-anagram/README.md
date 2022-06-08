# Group Anagram

## Space Time Complexity

**Average**

O(MN) | O(M) space

where:

M is the number of strings

N is the average length of each string

---

## Task

[Link to Leetcode](https://leetcode.com/problems/group-anagrams/)

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Sample Input:

```
strs = ["eat","tea","tan","ate","nat","bat"]
```

Sample Output:

```
[["bat"],["nat","tan"],["ate","eat","tea"]]
```

Sample Input 2:

```
strs = [""]
```

Sample Output 2:

```
[[""]]
```

Constraints:

- `1 <= strs.length <= 10^4`

- `0 <= strs[i].length <= 100`

- `strs[i]` consists of lowercase English letters.
