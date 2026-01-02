## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a string with expansion patterns like "3(ab)" meaning "ababab", we need to find the k-th character in the fully expanded string.

**1.1 Constraints & Complexity:**

- **Input Size:** The string length can be up to 100, and k can be up to 10^9.
- **Time Complexity:** O(n) where n is the string length - we process the string once to expand it.
- **Space Complexity:** O(n * expansion_factor) - we need to store the expanded string.
- **Edge Case:** If k is greater than the expanded string length, return empty string. If there are nested expansions, we need to handle them recursively.

**1.2 High-level approach:**

The goal is to expand the string by processing numbers and parentheses, then return the k-th character.

![String expansion visualization](https://assets.leetcode.com/static_assets/others/string-expand.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Fully expand the string and return the k-th character. This may be memory-intensive for large expansions.
- **Optimized Strategy:** For very large k, we could calculate without full expansion, but for reasonable sizes, full expansion is acceptable.
- **Optimization:** We expand the string and return the character at index k-1.

**1.4 Decomposition:**

1. Process the string character by character.
2. When encountering a digit, parse the number.
3. When encountering '(', find the matching ')' and extract the substring.
4. Repeat the substring the specified number of times.
5. Continue until the string is fully expanded.
6. Return the k-th character (index k-1).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "2(ab)"`, `k = 4`

- Original: `"2(ab)"`
- Expanded: `"abab"`
- Result variable: `res = ""`

**2.2 Start Checking:**

We expand the string.

**2.3 Trace Walkthrough:**

| Step | Process | Result |
| ---- | ------- | ------ |
| 1    | Parse "2" | count = 2 |
| 2    | Find "(ab)" | substr = "ab" |
| 3    | Repeat 2 times | "abab" |
| 4    | Get k-th (4th) | 'b' |

**2.4 Increment and Loop:**

After expansion, we return the character at position k-1.

**2.5 Return Result:**

The result is `'b'`, which is the 4th character in the expanded string "abab".

