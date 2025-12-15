## Explanation

### Strategy

**Restate the problem**  
Given grid size `n`, start position, and instructions `s`, for each suffix of `s` compute how many moves stay within the grid.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= n, m <= 500`, m = |s|.  
- **Time Complexity:** O(m²) in the straightforward simulation (m up to 500 is fine).  
- **Space Complexity:** O(1) extra besides output.  
- **Edge Case:** Single instruction that immediately leaves → 0 for that suffix.

**1.2 High-level approach**  
For each starting index i, simulate moves from that suffix until leaving bounds.  
![Suffix simulation on grid](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force / Direct:** Simulate each suffix independently — O(m²). Acceptable for m=500.  
- **Optimized:** Could precompute deltas, but unnecessary here.

**1.4 Decomposition**  
1. Map instructions to direction deltas.  
2. For each i in [0..m-1], start from `startPos`, step through `s[i:]` until out of bounds.  
3. Count steps that remain in bounds.  
4. Store counts in `res`.

### Steps

**2.1 Initialization & Example Setup**  
Example: `n=3, start=[0,1], s="RRDDLU"`, m=6.

**2.2 Start Checking**  
For each suffix, reset position and simulate.

**2.3 Trace Walkthrough**  
| start i | suffix   | path validity count |
|---------|----------|---------------------|
| 0       | RRDDLU   | 1                   |
| 1       | RDDLU    | 5                   |
| 2       | DDLU     | 4                   |
| 3       | DLU      | 3                   |
| 4       | LU       | 1                   |
| 5       | U        | 0                   |

**2.4 Increment and Loop**  
Repeat for all suffix starts.

**2.5 Return Result**  
Return the array of counts, e.g., `[1,5,4,3,1,0]`.

