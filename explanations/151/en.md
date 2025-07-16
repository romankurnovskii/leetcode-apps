## 151. Reverse Words in a String [Medium]

https://leetcode.com/problems/reverse-words-in-a-string

## Description
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

**Examples**
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

**Constraints**
- 1 <= s.length <= 10^4
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

## Hint
Split the string into words, reverse the list, and join them back.

## Explanation
Let's think of the sentence as a row of blocks, each block being a word. To reverse the sentence, we break it into blocks, flip the order, and stick them back together.

We do this because splitting and reversing is much easier than trying to move words around in the original string. Python's split and join functions make this super efficient, and by removing extra spaces, we make sure the result is clean and matches the requirements.

This approach is both simple and effective, making it a great example of using built-in tools to solve a problem quickly.
