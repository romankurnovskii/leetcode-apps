## Explanation

### Strategy

**Restate the problem**  
Count the number of contiguous subarrays where prices strictly descend by exactly 1 each day (a "smooth descent period"), including all single-day windows.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= n <= 1e5`.  
- **Time Complexity:** O(n) — single pass to accumulate lengths.  
- **Space Complexity:** O(1) — constant counters only.  
- **Edge Case:** A single element always forms a valid period.

**1.2 High-level approach**  
Traverse once, maintain the current descending run length; each position contributes that run length to the answer.  
![Sliding window over descending runs](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Enumerate all subarrays and check descent — O(n²) checks.  
- **Optimized:** Track run lengths in one pass — O(n). Avoids quadratic enumeration.

**1.4 Decomposition**  
1. Start run length at 1.  
2. For each next price, if `prices[i] == prices[i-1]-1`, extend run; else reset to 1.  
3. Add the current run length to `res`.  
4. Return `res`.

### Steps

**2.1 Initialization & Example Setup**  
Example: `prices = [3,2,1,4]`  
Set `run = 1`, `res = 1` (first day alone).

**2.2 Start Checking**  
Scan from index 1 to end, updating run and `res`.

**2.3 Trace Walkthrough**  
| i | prices[i] | Condition                     | run | res (cum) |
|---|-----------|--------------------------------|-----|-----------|
| 0 | 3         | start                          | 1   | 1         |
| 1 | 2         | 2 == 3-1 → extend              | 2   | 3         |
| 2 | 1         | 1 == 2-1 → extend              | 3   | 6         |
| 3 | 4         | 4 != 1-1 → reset               | 1   | 7         |

**2.4 Increment and Loop**  
Each step updates `run` (either +1 or reset to 1) and adds it to `res`.

**2.5 Return Result**  
Final `res = 7` for the example.

