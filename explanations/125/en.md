## 125. Valid Palindrome [Easy]

https://leetcode.com/problems/valid-palindrome

## Description
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or *`false`* otherwise.*

**Examples**

```tex
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints**
```tex
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters
```

## Explanation

### Strategy
Let's restate the problem: You're given a string that may contain letters, numbers, spaces, and punctuation marks. You need to determine if it's a palindrome after cleaning it up (removing non-alphanumeric characters and converting to lowercase).

This is a **two-pointer problem** that involves string preprocessing and then checking for palindrome properties.

**What is given?** A string that may contain various characters including letters, numbers, spaces, and punctuation.

**What is being asked?** Determine if the cleaned string (only alphanumeric characters, all lowercase) is a palindrome.

**Constraints:** The string can be up to 200,000 characters long and contains only printable ASCII characters.

**Edge cases:** 
- Empty string (should return true)
- String with only non-alphanumeric characters (should return true)
- Single character (should return true)
- String with mixed case and punctuation

**High-level approach:**
The solution involves two main steps:
1. **Preprocessing**: Clean the string by removing non-alphanumeric characters and converting to lowercase
2. **Palindrome check**: Use two pointers to check if the cleaned string reads the same forward and backward

**Decomposition:**
1. **Clean the string**: Remove all non-alphanumeric characters and convert to lowercase
2. **Initialize pointers**: Place one pointer at the start and one at the end
3. **Compare characters**: Move pointers inward while comparing characters
4. **Return result**: Return true if all characters match, false otherwise

**Brute force vs. optimized strategy:**
- **Brute force**: Create a new cleaned string and then check if it equals its reverse. This takes O(n) time and O(n) space.
- **Optimized**: Use two pointers to check palindrome property in-place. This takes O(n) time and O(1) space.

### Steps
Let's walk through the solution step by step using the first example: `s = "A man, a plan, a canal: Panama"`

**Step 1: Preprocessing**
- Remove all non-alphanumeric characters: spaces, commas, colons
- Convert all letters to lowercase
- Result: `"amanaplanacanalpanama"`

**Step 2: Initialize pointers**
- `left = 0` (points to the first character: 'a')
- `right = 24` (points to the last character: 'a')

**Step 3: Compare characters**
- `s[left] = 'a'`, `s[right] = 'a'`
- `'a' == 'a'` ✓, so move both pointers inward
- `left = 1`, `right = 23`

**Step 4: Continue comparison**
- `s[left] = 'm'`, `s[right] = 'm'`
- `'m' == 'm'` ✓, so move both pointers inward
- `left = 2`, `right = 22`

**Step 5: Continue until pointers meet**
- Continue this process, comparing characters at both ends
- Move pointers inward after each successful comparison
- Stop when `left >= right`

**Step 6: Check result**
- If we reach the middle without finding a mismatch, it's a palindrome
- In this case, all characters match, so return `true`

**Why this works:**
A palindrome reads the same forward and backward. By using two pointers that start at opposite ends and move inward, we can efficiently check this property. If at any point the characters don't match, we know it's not a palindrome. If we reach the middle with all characters matching, it must be a palindrome.

> **Note:** The key insight is that we don't need to create a new cleaned string. We can process the original string character by character, skipping non-alphanumeric characters and converting case on-the-fly.

**Time Complexity:** O(n) - we process each character at most once  
**Space Complexity:** O(1) - we only use a constant amount of extra space for the pointers
