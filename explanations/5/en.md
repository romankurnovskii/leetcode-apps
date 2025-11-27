## Explanation

### Strategy (The "Why")

Given a string `s`, we need to return the longest palindromic substring in `s`.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to $1000$.
- **Value Range:** String contains only digits and English letters.
- **Time Complexity:** $O(n^2)$ - For each character, we expand outward, which can take $O(n)$ time. We do this for $n$ characters.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the string is empty, return empty string. If all characters are the same, return the entire string.

**1.2 High-level approach:**

The goal is to find the longest palindromic substring.

We use the "expand around centers" approach. For each character (and between characters for even-length palindromes), we expand outward to find the longest palindrome centered at that position.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible substrings and check if each is a palindrome. This takes $O(n^3)$ time.
- **Optimized Strategy (Expand Around Centers):** For each possible center, expand outward to find the longest palindrome. This takes $O(n^2)$ time.
- **Why it's better:** The expand-around-centers approach reduces time complexity from $O(n^3)$ to $O(n^2)$ by avoiding checking all substrings explicitly.

**1.4 Decomposition:**

1. For each character in the string:
   - Expand around it as center (odd-length palindromes).
   - Expand around it and next character as center (even-length palindromes).
2. Track the longest palindrome found.
3. Return the longest palindrome.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $s = "babad"$

We initialize:
- `res = ""`
- `res_len = 0`

**2.2 Start Expanding:**

We begin expanding around each center.

**2.3 Trace Walkthrough:**

| Center | Type | Expansion | Palindrome | Length | Update? |
|--------|------|-----------|------------|--------|---------|
| 'b' (0) | Odd | b | "b" | 1 | Yes |
| 'a' (1) | Odd | aba | "aba" | 3 | Yes |
| 'a' (1) | Even | a | "a" | 1 | No |
| 'b' (2) | Odd | bab | "bab" | 3 | No (same length) |
| ... | ... | ... | ... | ... | ... |

**2.4 Final Result:**

The longest palindrome found is "aba" or "bab" (both length 3).

**2.5 Return Result:**

We return "bab" (or "aba"), which is the longest palindromic substring.

> **Note:** The key insight is that every palindrome has a center. By checking all possible centers (characters and between characters), we can find the longest palindrome. We expand outward from each center until characters don't match.

