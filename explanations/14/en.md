## 14. Longest Common Prefix [Easy]

https://leetcode.com/problems/longest-common-prefix

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Examples**
```text
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Constraints:**
```text
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
```

**Primary Pattern: String Manipulation**

## Understanding

You're given a list of strings and need to find the longest prefix that all strings share. A prefix is the beginning part of a string. For example, in ["flower", "flow", "flight"], all three strings start with "fl", so that's the longest common prefix.

Think of it like finding the longest shared beginning among all the words. If there's no shared beginning at all, you return an empty string.

## Strategy

### Identifying the Pattern

**Primary Pattern: String Manipulation**

The clues that point to string manipulation are:
- The problem explicitly asks for "prefix" operations on strings
- You need to compare characters at the same positions across multiple strings
- The solution involves character-by-character comparison and string building

This is a classic string manipulation problem where you need to process multiple strings simultaneously, comparing them character by character.

### Steps

**Logic:** The key insight is that the longest common prefix cannot be longer than the shortest string in the array. You can optimize by:

1. Find the shortest string length (this limits the maximum possible prefix length)
2. Compare characters at each position across all strings
3. Stop when you find a mismatch or reach the end of the shortest string
4. Build the result string as you go

**High-level approach:**
- Use the shortest string as a reference to avoid index out of bounds
- Compare characters position by position across all strings
- Build the common prefix incrementally
- Handle edge cases (empty array, single string, no common prefix)

**Implementation steps:**
1. Handle edge cases (empty array, single string)
2. Find the minimum length among all strings
3. Iterate through each character position up to the minimum length
4. For each position, check if all strings have the same character
5. If they match, add to result; if not, return current result
6. Return the accumulated prefix

> **Note:** The optimized solution uses the shortest string length to avoid unnecessary comparisons and potential index errors.
