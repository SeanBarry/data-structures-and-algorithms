# Length of Last Word

## Space Time Complexity

**Average** O(N) | O(1) space

---

## Task

[Link to Leetcode](https://leetcode.com/problems/length-of-last-word/)

Given a string `s` consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Sample Input:

```
s = "Hello World"
```

Sample Output:

```
5 // The last word is "World" with length 5.
```

Sample Input 2:

```
s = "   fly me   to   the moon  "
```

Sample Output 2:

```
4 // The last word is "moon" with length 4.
```

Constraints:

- `1 <= s.length <= 104`
- `s` consists of only English letters and spaces ' '.
- There will be at least one word in `s`.
