## Explanation

### Strategy

**Restate the problem**  
Sort all vowels in the string by ASCII order while leaving consonants in place.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= |s| <= 1e5`.  
- **Time Complexity:** O(n log n) to sort extracted vowels; O(n) if counting-sort on 10 vowel chars.  
- **Space Complexity:** O(n) for the output list.  
- **Edge Case:** No vowels → string unchanged.

**1.2 High-level approach**  
Extract vowels, sort them, then rebuild the string by replacing vowel positions with sorted vowels.  
![Extract-sort-rebuild pipeline](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Repeatedly scan to find next smallest vowel — O(n²).  
- **Optimized:** One pass extract + one sort + one rebuild — O(n log n).

**1.4 Decomposition**  
1. Collect vowels into a list.  
2. Sort the vowel list.  
3. Rebuild string: if char is vowel, take next from sorted list; else keep consonant.  
4. Join result.

### Steps

**2.1 Initialization & Example Setup**  
Example: `s = "lEetcOde"`; vowels extracted: `['E','e','O','e']`.

**2.2 Start Checking**  
Sort vowels → `['E','O','e','e']`.

**2.3 Trace Walkthrough**  
| Index | Char | Is vowel? | Replacement        | Result so far |
|-------|------|-----------|--------------------|---------------|
| 0     | l    | No        | l                  | l             |
| 1     | E    | Yes       | E (sorted[0])      | lE            |
| 2     | e    | Yes       | O (sorted[1])      | lEO           |
| 3     | t    | No        | t                  | lEOt          |
| 4     | c    | No        | c                  | lEOtc         |
| 5     | O    | Yes       | e (sorted[2])      | lEOtce        |
| 6     | d    | No        | d                  | lEOtced       |
| 7     | e    | Yes       | e (sorted[3])      | lEOtcede      |

**2.4 Increment and Loop**  
Advance through string, consuming sorted vowels sequentially.

**2.5 Return Result**  
Final string: `"lEOtcede"`.

