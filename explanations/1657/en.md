## 1657. Determine if Two Strings Are Close [Medium]

https://leetcode.com/problems/determine-if-two-strings-are-close

## Description
Two strings are considered close if you can attain one from the other using the following operations:
- Operation 1: Swap any two existing characters (i.e., freely reorder the string).
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character (i.e., swap all a's with b's, and all b's with a's).
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

**Examples**
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"

**Constraints**
- 1 <= word1.length, word2.length <= 10^5
- word1 and word2 contain only lowercase English letters.

## Hint
Operation 1 allows you to freely reorder the string. Operation 2 allows you to freely reassign the letters' frequencies.

## Explanation
To determine if two strings are close, you need to check two things:
1. Both strings must have the same set of unique characters. If one string has a character the other doesn't, you can't transform one into the other.
2. The frequency of each character (regardless of which character) must be the same in both strings. This is because you can swap the frequencies between characters using Operation 2, but you can't create or destroy frequencies.

This means you can sort the frequency counts of each string and compare them. If both the set of unique characters and the sorted frequency counts match, the strings are close. 