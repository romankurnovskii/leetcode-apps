## 345. Reverse Vowels of a String [Easy]

https://leetcode.com/problems/reverse-vowels-of-a-string

## Description
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

**Examples**
Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"

**Constraints**
- 1 <= s.length <= 3 * 10^5
- s consist of printable ASCII characters.

## Hint
Use two pointers to find vowels from both ends and swap them.

## Explanation
We want to reverse only the vowels in the string. To do this efficiently, we use two pointers: one starting from the left, one from the right. We move each pointer until it finds a vowel. When both pointers are at vowels, we swap them.

We do this because it lets us reverse the vowels in-place, without affecting the other characters. Using two pointers is efficient and avoids unnecessary work, especially for long strings.

We keep moving the pointers toward each other, swapping vowels as we go, until they meet in the middle. This ensures every vowel is swapped exactly once, making the solution both correct and efficient.

