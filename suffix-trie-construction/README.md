# Suffix Trie Construction

## Space Time Complexity

**Creating Suffix Trie**

O(n^2) time | O(n^2) space

where:

n is the number of characters in the input string

**Finding Strings in the Suffix Trie**

O(m) time | O(1) space

where:

m is the length of the input string

---

## Task

Write a `suffixTrie` class for a Suffix-Trie-like data structure.

The class should have a `root` property set to be the root node of the trie and should support:

- Creating the trie from a string; this will be done by calling the `populateSuffixTrieFrom` method upon class instantiation, which should populate the `root` of the class.

- Searching for strings in the trie.

Note that every string added to the trie should end with the special `endSymbol` character: `*`.

Sample input (for creation):

```
string = "babc"
```

Sample output (for creation)

```
// The structure below is the root of the trie.

{
  "c": {"*": true},
  "b": {
    "c": {"*": true},
    "a": {"b": {"c": {"*": true}}},
  },
  "a": {"b": {"c": {"*": true}}},
}
```

Sample input (for searching in the suffix trie above):

```
string = "abc"
```

Sample output (for searching in the suffix trie above):

```
true
```
