## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** String length `2 <= s.length <= 100`.
- **Time Complexity:** O(n) where n is the length of the string - we iterate through adjacent pairs once.
- **Space Complexity:** O(1) - we only use a constant amount of extra space for the result variable.
- **Edge Case:** A string with only 2 characters still has one pair to check.

**1.2 High-level approach:**
The goal is to calculate the sum of absolute differences between ASCII values of adjacent characters in the string. We iterate through the string, comparing each character with the next one.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Same as optimized - we need to check every adjacent pair, which requires O(n) time.
- **Optimized Strategy:** Single pass through the string, calculating differences as we go.

**1.4 Decomposition:**
1. Initialize a result variable to store the sum.
2. Iterate through the string from index 0 to length-2.
3. For each pair of adjacent characters, calculate the absolute difference of their ASCII values.
4. Add the difference to the result.
5. Return the final sum.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use `s = "hello"`. We initialize `res = 0`.

**2.2 Start Checking:**
We start at index 0 and compare each character with the next one.

**2.3 Trace Walkthrough:**

| Index | Current Char | Next Char | ASCII Diff | res |
|-------|--------------|-----------|------------|-----|
| 0 | 'h' (104) | 'e' (101) | \|104-101\| = 3 | 3 |
| 1 | 'e' (101) | 'l' (108) | \|101-108\| = 7 | 10 |
| 2 | 'l' (108) | 'l' (108) | \|108-108\| = 0 | 10 |
| 3 | 'l' (108) | 'o' (111) | \|108-111\| = 3 | 13 |

**2.4 Increment and Loop:**
After processing each pair, we move to the next index until we reach `len(s) - 2`.

**2.5 Return Result:**
Return `res = 13`, which is the sum of all absolute differences between adjacent characters.

