# Valid Parenthesis

## Space Time Complexity

**Average** O(N) | O(N) space

---

## Task

[Link to Leetcode](https://leetcode.com/problems/valid-parentheses)

Given a string `s` containing just the characters `'(', ')', '{', '}', '[' and ']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.

- Open brackets must be closed in the correct order.

Sample Input:

```
s = "()"
```

Sample Output:

```
true
```

Sample Input 2:

```
s = "()[]{}"
```

Sample Output 2:

```
true
```

Sample Input 3:

```
s = "(]"
```

Sample Output 3:

```
false
```

Constraints:

- `1 <= s.length <= 10^4`
- `s consists of parentheses only '()[]{}'`
