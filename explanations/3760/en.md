## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum number of substrings we can split a string into such that each substring starts with a distinct character. No two substrings can start with the same character.

**1.1 Constraints & Complexity:**
- Input size: `1 <= s.length <= 10^5`
- **Time Complexity:** O(n) - single pass to count distinct characters
- **Space Complexity:** O(1) - using a set of at most 26 characters (lowercase English letters)
- **Edge Case:** If all characters are the same (e.g., "aaaa"), we can only have 1 substring

**1.2 High-level approach:**
The key insight is that each substring must start with a distinct character. Since we can only use each starting character once, the maximum number of substrings equals the number of distinct characters in the string.

![Distinct characters visualization](https://assets.leetcode.com/static_assets/others/distinct-characters.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all possible ways to split the string, which is exponential
- **Optimized Strategy:** Simply count distinct characters - each distinct character can start exactly one substring, so the answer is the count of distinct characters
- **Emphasize the optimization:** The constraint that each substring must start with a distinct character directly limits the answer to the number of distinct characters

**1.4 Decomposition:**
1. Count the number of distinct characters in the string
2. Since each substring must start with a distinct character, and we can only use each character once as a start
3. The maximum number of substrings equals the number of distinct characters
4. Return the count

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `s = "abab"`
- Distinct characters: 'a' and 'b' (2 distinct characters)
- We can split into: "a" and "bab" (starts with 'a' and 'b')

**2.2 Start Checking:**
We count distinct characters in the string.

**2.3 Trace Walkthrough:**

| String | Distinct Characters | Count | Maximum Substrings |
|--------|-------------------|-------|-------------------|
| "abab" | {'a', 'b'} | 2 | 2 |
| "abcd" | {'a', 'b', 'c', 'd'} | 4 | 4 |
| "aaaa" | {'a'} | 1 | 1 |

**2.4 Increment and Loop:**
We iterate through the string once to collect all distinct characters in a set.

**2.5 Return Result:**
For "abab", we have 2 distinct characters, so the maximum number of substrings is 2. We can split as "a" + "bab" where "a" starts with 'a' and "bab" starts with 'b'.
