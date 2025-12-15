## Explanation

### Strategy

**Restate the problem**  
For each query `[l_i, r_i]`, decide if the subarray can be rearranged into an arithmetic progression.

**1.1 Constraints & Complexity**  
- **Input Size:** `n, m <= 500`.  
- **Time Complexity:** O(m * k log k), where k is subarray length (sort each subarray).  
- **Space Complexity:** O(k) per query for the sorted copy.  
- **Edge Case:** Subarray of length 2 is always arithmetic.

**1.2 High-level approach**  
Extract subarray, sort it, ensure consecutive differences are equal.  
![Sorted subarray check](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Try all permutations — factorial blowup.  
- **Optimized:** Sorting then one pass diff check — O(k log k).

**1.4 Decomposition**  
1. For each query, copy subarray `nums[l:r+1]`.  
2. Sort it.  
3. Compute common diff = `sorted[1]-sorted[0]`.  
4. Verify all consecutive diffs match; if any differ, mark false; else true.

### Steps

**2.1 Initialization & Example Setup**  
Example: `nums=[4,6,5,9,3,7]`, query `[0,2]` → subarray `[4,6,5]`.

**2.2 Start Checking**  
Sort → `[4,5,6]`, diff = 1.

**2.3 Trace Walkthrough**  
| Subarray (sorted) | Step | Diff check          | OK? |
|-------------------|------|----------------------|-----|
| [4,5,6]           | 4→5  | 1 == diff            | ✓   |
|                   | 5→6  | 1 == diff            | ✓   |

**2.4 Increment and Loop**  
Repeat for each query independently.

**2.5 Return Result**  
Append boolean for each query into `res`.

