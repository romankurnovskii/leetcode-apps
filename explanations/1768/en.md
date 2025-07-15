## Merge Strings Alternately [Easy]
https://leetcode.com/problems/merge-strings-alternately

## Description

You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example:
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

Constraints:
```
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
```

## Hint

> In most cases, LeetCode Easy problems have a straightforward solution that can be derived from the description or the examples provided.

## Explanation

Imagine you have two strings, like two lines of colored beads. You want to make a new necklace by picking one bead from the first string, then one from the second, and keep going! If one string runs out, just add the rest from the other.

We use two pointers to keep track of our position in each string, because this lets us alternate letters easily and ensures we don't miss any. By appending the remaining part of the longer string at the end, we make sure no letters are left out—this is important for correctness, especially when the strings are different lengths.

**Example:**  
word1 = "ab", word2 = "pqrs"  
- Take 'a' and 'p' → "ap"
- Take 'b' and 'q' → "apbq"
- word1 is done, so add the rest of word2: "rs"
- Final answer: "apbqrs"

We use a list to collect the letters because lists in Python are efficient for appending, and then join them at the end for the final string.
