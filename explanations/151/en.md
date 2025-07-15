## Description

Given an input string, reverse the order of the words.

Example:
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

Constraints:
```
- 1 <= s.length <= 10^4
- s contains English letters and spaces.
- There is at least one word in s.
```

## Hint

> Split the string into words, reverse the list, and join them back.

## Explanation

Let's think of the sentence as a row of blocks, each block being a word. To reverse the sentence, we break it into blocks, flip the order, and stick them back together.

We do this because splitting and reversing is much easier than trying to move words around in the original string. Python's split and join functions make this super efficient, and by removing extra spaces, we make sure the result is clean and matches the requirements.

This approach is both simple and effective, making it a great example of using built-in tools to solve a problem quickly.
