## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `1 <= s.length <= 10^5`.
- **Time Complexity:** O(n) where n is the string length - we need to find distinct characters.
- **Space Complexity:** O(k) where k is the number of distinct characters - we store them in a set.
- **Edge Case:** All characters are the same, result is 1.

**1.2 High-level approach:**
The goal is to find the maximum number of substrings we can split the string into such that each substring starts with a distinct character. The answer is simply the number of distinct characters in the string.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible splits - exponential time.
- **Optimized Strategy:** Count distinct characters - each can start at most one substring - O(n) time.

**1.4 Decomposition:**
1. Count the number of distinct characters in the string.
2. This equals the maximum number of substrings we can create.
3. Return the count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `s = "abab"`. Distinct characters are {'a', 'b'}, so count is 2.

**2.2 Start Checking:**
We create a set of all characters in the string.

**2.3 Trace Walkthrough:**

| String | Distinct Chars | Count | Max Substrings |
|--------|----------------|-------|----------------|
| "abab" | {'a','b'} | 2 | 2 |
| "abcd" | {'a','b','c','d'} | 4 | 4 |
| "aaaa" | {'a'} | 1 | 1 |

**2.4 Increment and Loop:**
Not applicable - this is a direct calculation.

**2.5 Return Result:**
Return `res = 2` for "abab", which is the number of distinct characters.
