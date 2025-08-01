# 125. Valid Palindrome

**Difficulty:** Easy  
**Link:** https://leetcode.com/problems/valid-palindrome/

## Problem Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

**Example 1:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

**Example 3:**
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints:**
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Explanation

### Strategy

This is a **two-pointer string problem** that requires checking if a string is a palindrome after preprocessing. The key insight is to use two pointers from both ends and compare characters while skipping non-alphanumeric characters.

**Key observations:**
- We need to ignore case (convert to lowercase)
- We need to skip non-alphanumeric characters (punctuation, spaces)
- We can use two pointers to compare from both ends
- Empty string after preprocessing is considered a palindrome

**High-level approach:**
1. **Use two pointers**: One from start, one from end
2. **Skip non-alphanumeric characters**: Move pointers until we find valid characters
3. **Compare characters**: Check if characters match (case-insensitive)
4. **Continue until pointers meet**: If all comparisons pass, it's a palindrome

### Steps

Let's break down the solution step by step:

**Step 1: Initialize pointers**
- `left = 0` (start of string)
- `right = len(s) - 1` (end of string)

**Step 2: Iterate while pointers don't cross**
While `left < right`:
- Skip non-alphanumeric characters from left
- Skip non-alphanumeric characters from right
- Compare characters (case-insensitive)
- If they don't match, return `false`
- Move pointers inward

**Step 3: Return result**
- If we reach the end without finding a mismatch, return `true`

**Example walkthrough:**
Let's trace through the first example:

```
s = "A man, a plan, a canal: Panama"

Initial state:
left = 0, right = 29

Step 1: left points to 'A', right points to 'a'
Both are alphanumeric, compare 'A' == 'a' (case-insensitive) ✓
left = 1, right = 28

Step 2: left points to ' ' (space), right points to 'm'
Skip space from left: left = 2
Compare 'm' == 'm' ✓
left = 3, right = 27

Step 3: left points to 'a', right points to 'a'
Compare 'a' == 'a' ✓
left = 4, right = 26

... (continuing this process)

Final comparison: All characters match
Result: Return true
```

> **Note:** The two-pointer approach is efficient because we only need to traverse the string once. We don't need to create a new cleaned string - we can process it in-place by skipping invalid characters.

### Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        # Iterate while pointers don't cross
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        # If we reach here, it's a palindrome
        return True
```

**Time Complexity:** O(n) - we visit each character at most once  
**Space Complexity:** O(1) - we only use a constant amount of extra space
