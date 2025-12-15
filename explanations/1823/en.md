## Explanation

### Strategy

**Restate the problem**  
`n` players in a circle, eliminate every `k`th; return the winner’s label (1-indexed).

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= k <= n <= 500`.  
- **Time Complexity:** O(n) using the Josephus recurrence.  
- **Space Complexity:** O(1).  
- **Edge Case:** n=1 → winner=1.

**1.2 High-level approach**  
Use the Josephus recurrence: winner (0-indexed) updates as `winner = (winner + k) % i` for i from 2..n; convert to 1-indexed at the end.  
![Josephus circular elimination](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Simulate with a queue/list and remove elements — O(n*k).  
- **Optimized:** Closed-form recurrence — O(n).

**1.4 Decomposition**  
1. Set `winner = 0` (for i=1).  
2. For `i` from 2 to `n`: `winner = (winner + k) % i`.  
3. Return `winner + 1`.

### Steps

**2.1 Initialization & Example Setup**  
Example: `n=5, k=2`; start `winner=0`.

**2.2 Start Checking**  
Iterate i=2..5 updating winner.

**2.3 Trace Walkthrough**  
| i | winner before | update formula       | winner after |
|---|---------------|----------------------|--------------|
| 2 | 0             | (0+2)%2 = 0          | 0            |
| 3 | 0             | (0+2)%3 = 2          | 2            |
| 4 | 2             | (2+2)%4 = 0          | 0            |
| 5 | 0             | (0+2)%5 = 2          | 2            |

**2.4 Increment and Loop**  
Loop until i = n.

**2.5 Return Result**  
Return `winner + 1` → 3 for the example.

