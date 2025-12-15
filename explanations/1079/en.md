## Explanation

### Strategy

**Restate the problem**  
Count all non-empty sequences that can be formed from the multiset of tiles (letters), respecting available counts.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= len(tiles) <= 7`.  
- **Time Complexity:** O(n! * n) in worst case (backtracking over permutations), acceptable for n <= 7.  
- **Space Complexity:** O(n) recursion depth + O(1) counts.  
- **Edge Case:** Single tile → exactly 1 sequence.

**1.2 High-level approach**  
Use backtracking with frequency counts; at each step, pick a letter with remaining count, decrement, recurse, then restore.  
![Backtracking over letter counts](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Generate all permutations with duplicates and then deduplicate — costly.  
- **Optimized:** Use counts to avoid generating identical branches; count as we go.

**1.4 Decomposition**  
1. Build frequency map of letters.  
2. DFS: for each letter with count > 0, use it (res++), decrement, recurse, restore.  
3. Sum all counts encountered.  
4. Return `res`.

### Steps

**2.1 Initialization & Example Setup**  
Example: `tiles = "AAB"`; counts: A:2, B:1, `res=0`.

**2.2 Start Checking**  
Try each available letter, recurse with updated counts.

**2.3 Trace Walkthrough**  
| Path    | Counts after pick | res increment | Notes        |
|---------|-------------------|---------------|--------------|
| A       | A:1,B:1           | +1            | recurse more |
| AA      | A:0,B:1           | +1            | recurse      |
| AAB     | A:0,B:0           | +1            | dead end     |
| AB      | A:1,B:0           | +1            | recurse      |
| ...     | ...               | ...           | ...          |

**2.4 Increment and Loop**  
Each pick adds 1 to `res` (for the new sequence) before deeper recursion.

**2.5 Return Result**  
Final `res = 8` for the example.

