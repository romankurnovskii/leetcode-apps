## Explanation

### Strategy

**Restate the problem**  
Given two equal-length lowercase strings `s` and `t`, find the minimum number of character replacements in `t` to make it an anagram of `s`.

**1.1 Constraints & Complexity**  
- **Input Size:** up to 5×10^4 characters.  
- **Time Complexity:** O(n) to count frequencies.  
- **Space Complexity:** O(1) since alphabet size is fixed (26).  
- **Edge Case:** Already anagrams → 0 steps.

**1.2 High-level approach**  
Count letters in both strings; for each character, if `s` needs more than `t` has, that deficit contributes to the answer.  
![Frequency gap guiding replacements](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Try all replacement combinations — exponential.  
- **Optimized:** Frequency difference — O(n), straightforward.

**1.4 Decomposition**  
1. Count frequencies of `s` and `t`.  
2. For each letter, compute `max(0, count_s - count_t)` and sum.  
3. That sum is the number of replacements needed in `t`.  
4. Return the sum.

### Steps

**2.1 Initialization & Example Setup**  
Example: `s="leetcode"`, `t="practice"`.

**2.2 Start Checking**  
Build `count_s`, `count_t`.

**2.3 Trace Walkthrough**  
| Char | count_s | count_t | deficit (if s needs more) |
|------|---------|---------|----------------------------|
| e    | 3       | 1       | +2                         |
| l    | 1       | 0       | +1                         |
| t    | 1       | 1       | 0                          |
| c    | 1       | 2       | 0                          |
| o    | 1       | 0       | +1                         |
| d    | 1       | 0       | +1                         |
| ...  | ...     | ...     | ...                        |
Total = 5.

**2.4 Increment and Loop**  
Sum deficits over all 26 letters.

**2.5 Return Result**  
Return the total replacements (5 in the example).

