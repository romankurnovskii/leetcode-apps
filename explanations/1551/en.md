## Explanation

### Strategy

**Restate the problem**  
Array is `[1,3,5,...,2n-1]`; in one operation, decrement one element and increment another. Find min operations to make all elements equal.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= n <= 1e4`.  
- **Time Complexity:** O(n) to sum needed moves.  
- **Space Complexity:** O(1).  
- **Edge Case:** n=1 → 0 operations.

**1.2 High-level approach**  
Target value is `n` (the average). Pair symmetric elements; each pair needs `(target - current_lower)` moves. Sum over first half.  
![Balancing around the center value](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Simulate operations — inefficient.  
- **Optimized:** Direct formula using symmetry — O(n).

**1.4 Decomposition**  
1. Target = n.  
2. For i in [0 .. n/2 - 1], current = 2*i+1.  
3. Add `target - current` to result.  
4. Return result.

### Steps

**2.1 Initialization & Example Setup**  
Example: n=3; array [1,3,5], target=3.

**2.2 Start Checking**  
Only i=0 in first half: current=1 → need 2 moves.

**2.3 Trace Walkthrough**  
| i | current | target | add to res |
|---|---------|--------|------------|
| 0 | 1       | 3      | 2          |

**2.4 Increment and Loop**  
Loop over first half (integer division).

**2.5 Return Result**  
Return accumulated moves (2 for n=3).

