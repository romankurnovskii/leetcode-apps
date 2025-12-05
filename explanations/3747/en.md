## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count beautiful substrings where vowels equal consonants and their product is divisible by k. A substring is beautiful if it has equal numbers of vowels and consonants, and (vowels × consonants) % k == 0.

**1.1 Constraints & Complexity:**
- Input size: `1 <= s.length <= 1000`, `1 <= k <= 1000`
- **Time Complexity:** O(n²) where n is the string length, as we check all possible substrings
- **Space Complexity:** O(1) as we only use constant extra space for counters
- **Edge Case:** If k = 1, any substring with vowels == consonants is beautiful since any number is divisible by 1

**1.2 High-level approach:**
For each possible starting position, we expand the substring and maintain counts of vowels and consonants. When both counts are equal and their product is divisible by k, we found a beautiful substring.

![Substring expansion visualization](https://assets.leetcode.com/static_assets/others/substring-expansion.png)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Generate all substrings and check each one. This is what we do, O(n²).
- **Optimized Strategy (for larger constraints):** Use prefix sums and hash maps to count in O(n) time, but for n ≤ 1000, the O(n²) approach is acceptable.

**1.4 Decomposition:**
1. Iterate through all possible starting positions
2. For each starting position, expand the substring character by character
3. Maintain counts of vowels and consonants
4. Check if vowels == consonants and (vowels × consonants) % k == 0
5. Count valid beautiful substrings

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use the example: `s = "baeyh"`, `k = 2`
- Define vowels set: `{'a', 'e', 'i', 'o', 'u'}`
- Initialize `res = 0`

**2.2 Start Checking:**
We begin checking substrings starting from index 0.

**2.3 Trace Walkthrough:**
Using the example `s = "baeyh"`, `k = 2`:

| Start | End | Substring | Vowels | Consonants | Equal? | Product % k | Beautiful? | res |
|-------|-----|-----------|--------|------------|--------|-------------|-------------|-----|
| 0 | 0 | "b" | 0 | 1 | No | - | No | 0 |
| 0 | 1 | "ba" | 1 | 1 | Yes | 1 % 2 = 1 | No | 0 |
| 0 | 2 | "bae" | 2 | 1 | No | - | No | 0 |
| 0 | 3 | "baey" | 2 | 2 | Yes | 4 % 2 = 0 | Yes | 1 |
| 0 | 4 | "baeyh" | 2 | 3 | No | - | No | 1 |
| 1 | 1 | "a" | 1 | 0 | No | - | No | 1 |
| 1 | 2 | "ae" | 2 | 0 | No | - | No | 1 |
| 1 | 3 | "aey" | 2 | 1 | No | - | No | 1 |
| 1 | 4 | "aeyh" | 2 | 2 | Yes | 4 % 2 = 0 | Yes | 2 |

**2.4 Increment and Loop:**
For each valid beautiful substring found, we increment the result counter. We continue checking all possible substrings.

**2.5 Return Result:**
After processing all substrings, `res = 2`, which represents the two beautiful substrings: "baey" and "aeyh".
