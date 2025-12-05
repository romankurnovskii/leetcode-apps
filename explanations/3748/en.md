## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count beautiful substrings where vowels equal consonants and their product is divisible by k. This is similar to problem 3747 but with larger constraints (n ≤ 50000), requiring an optimized approach.

**1.1 Constraints & Complexity:**
- Input size: `1 <= s.length <= 5 * 10^4`, `1 <= k <= 1000`
- **Time Complexity:** O(n * sqrt(k)) where n is string length, as we iterate through valid x values and use prefix sums
- **Space Complexity:** O(n) for the prefix array and hash map
- **Edge Case:** If k = 1, any substring with vowels == consonants is beautiful

**1.2 High-level approach:**
The key insight is that if a substring has vowels == consonants == x, then x² must be divisible by k. We find all valid x values, then use prefix sums to efficiently count substrings with exactly x vowels and x consonants.

![Prefix sum with modulo visualization](https://assets.leetcode.com/static_assets/others/prefix-sum-modulo.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Check all O(n²) substrings, which is too slow for n ≤ 50000.
- **Optimized Strategy:** Precompute valid x values where x² % k == 0, then use prefix sums to count substrings of length 2x with equal vowels and consonants in O(n) per x.

**1.4 Decomposition:**
1. Find all x such that x² % k == 0 (valid counts for vowels/consonants)
2. Build prefix sum array where +1 for vowel, -1 for consonant
3. For each valid x, count substrings of length 2x with prefix difference 0
4. Sum up all valid substrings

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `s = "baeyh"`, `k = 2`
- Find valid x: x = 2 (since 2² % 2 = 0)
- Build prefix: [0, -1, 0, 1, 0, -1] (b=-1, a=+1, e=+1, y=-1, h=-1)

**2.2 Start Checking:**
We iterate through valid x values and count matching substrings.

**2.3 Trace Walkthrough:**
Using the example `s = "baeyh"`, `k = 2`, valid x = 2:

| i | prefix[i] | Looking for length 4 substrings | count_map | Matches | res |
|---|-----------|--------------------------------|-----------|---------|-----|
| 0 | 0 | - | {0:1} | 0 | 0 |
| 1 | -1 | - | {0:1, -1:1} | 0 | 0 |
| 2 | 0 | - | {0:2, -1:1} | 0 | 0 |
| 3 | 1 | Check prefix[3-4]=prefix[-1] (skip) | {0:2, -1:1, 1:1} | 0 | 0 |
| 4 | 0 | Check prefix[0]=0, count=2 | {0:3, -1:1, 1:1} | 2 | 2 |

Substrings found: "baey" (indices 0-3, prefix[0]=0, prefix[4]=0) and "aeyh" (indices 1-4, prefix[1]=-1, prefix[5]=-1, but we need prefix difference 0).

**2.4 Increment and Loop:**
For each position, we check if there's a matching prefix value 2x positions earlier that creates a beautiful substring.

**2.5 Return Result:**
After processing, `res = 2`, representing the beautiful substrings of length 4 with 2 vowels and 2 consonants.

