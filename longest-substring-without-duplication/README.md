# Longest Substring Without Duplication

## Space Time Complexity

O(n) time | O(min(n, a)) space

where:

n is the length of the input string

and:

a is the length of the alphabet the string is written in

As our cache stores the total number of letters in our string, it can never be longer than the length of the alphabet. As such for a really long string the cache size will be limited by the alphabet size.

---

## Task

Write a function that takes in a string and returns its longest substring without duplicate characters.

You can assume that there will only be one longest substring without duplication.

Sample input:

```
string = "clementisacap"
```

Sample output:

```
"mentisac"
```
