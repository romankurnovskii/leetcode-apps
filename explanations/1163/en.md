## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the lexicographically largest substring of a given string. The answer is always a suffix of the string (substring starting from some index to the end).

**1.1 Constraints & Complexity:**

- **Input Size:** String length can be up to 4×10^5.
- **Time Complexity:** O(n) - we use two pointers and each character is compared at most a constant number of times.
- **Space Complexity:** O(1) - we only use a few variables, not counting the output string.
- **Edge Case:** If all characters are the same, return the entire string.

**1.2 High-level approach:**

The goal is to find the starting index of the lexicographically largest suffix. We use two pointers to compare suffixes and eliminate candidates that cannot be the answer.

![Suffix comparison visualization](https://assets.leetcode.com/static_assets/others/suffix-comparison.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Compare all n suffixes lexicographically, which requires O(n^2) time.
- **Optimized Strategy:** Use two pointers with smart skipping. We maintain two candidate starting indices i and j, and compare them character by character. When we find a difference, we can skip many positions. This is O(n) time.
- **Optimization:** By intelligently skipping positions when we know one candidate is better than another, we avoid comparing all suffixes explicitly and reduce complexity from O(n^2) to O(n).

**1.4 Decomposition:**

1. Initialize two pointers: i=0 (current best candidate) and j=1 (next candidate to compare).
2. Compare suffixes starting at i and j character by character using offset k.
3. If characters match, increment k and continue.
4. If s[i+k] < s[j+k], s[j:] is larger, so update i to skip smaller prefixes.
5. If s[i+k] > s[j+k], s[i:] is larger, so skip j and continue.
6. Return the suffix starting at i.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "abab"`

- Initialize: i=0, j=1, k=0
- Compare s[0:] = "abab" vs s[1:] = "bab"

**2.2 Start Checking:**

We begin comparing the two suffixes character by character.

**2.3 Trace Walkthrough:**

| Step | i | j | k | s[i+k] | s[j+k] | Comparison | Action                    |
| ---- | - | - | - | ------ | ------ | ---------- | ------------------------- |
| 1    | 0 | 1 | 0 | 'a'    | 'b'    | a < b      | Update i=max(0+0+1,1)=1, j=2, k=0 |
| 2    | 1 | 2 | 0 | 'b'    | 'a'    | b > a      | Skip j: j=2+0+1=3, k=0    |
| 3    | 1 | 3 | 0 | 'b'    | -      | j+k >= n   | Return s[1:] = "bab"      |

**2.4 Increment and Loop:**

During comparison:
- If characters match, we increment k to compare the next characters.
- If s[i+k] < s[j+k], we know s[j:] is better, so we update i to skip the smaller prefix.
- If s[i+k] > s[j+k], we know s[i:] is better, so we skip j to the next candidate.
- We continue until j+k reaches the end of the string.

**2.5 Return Result:**

The result is "bab", which is the lexicographically largest substring. We verify: comparing all suffixes ["abab", "bab", "ab", "b"], "bab" is the largest.

