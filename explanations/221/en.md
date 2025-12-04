## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Matrix dimensions are 1x1 to 300x300, and each cell contains '0' or '1'.
- **Time Complexity:** O(m * n) where m and n are the matrix dimensions. We visit each cell once.
- **Space Complexity:** O(m * n) for the DP table, though we could optimize to O(n) by using only one row.
- **Edge Case:** If the matrix contains only '0's, return 0.

**1.2 High-level approach:**
The goal is to find the largest square containing only '1's. We use dynamic programming where `dp[i][j]` represents the side length of the largest square ending at position (i, j).

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each cell, try all possible square sizes. This is O(m * n * min(m,n)^2) time.
- **Optimized Strategy:** Use DP. For each '1' cell, the square size is 1 plus the minimum of the three adjacent squares (top, left, top-left). This is O(m * n) time.
- **Why optimized is better:** DP allows us to compute the answer in a single pass, avoiding redundant calculations.

**1.4 Decomposition:**
1. Create a DP table where `dp[i][j]` is the side length of the largest square ending at (i, j).
2. For each cell with '1', if it's on the border, set `dp[i][j] = 1`.
3. Otherwise, set `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`.
4. Track the maximum side length found.
5. Return the area (side length squared).

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Example matrix:
```
[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]
```

Initialize `dp` as zeros, `res = 0`.

**2.2 Start Checking:**
Process each cell from top-left to bottom-right.

**2.3 Trace Walkthrough:**

| (i,j) | matrix[i][j] | dp[i-1][j] | dp[i][j-1] | dp[i-1][j-1] | dp[i][j] | res |
|-------|--------------|------------|------------|--------------|----------|-----|
| (0,0) | '1' | - | - | - | 1 | 1 |
| (1,2) | '1' | 1 | 1 | 1 | 2 | 2 |
| (2,2) | '1' | 1 | 2 | 1 | 2 | 2 |
| (2,3) | '1' | 1 | 2 | 2 | 3 | 3 |

**2.4 Increment and Loop:**
For each cell (i, j):
- If `matrix[i][j] == '1'`:
  - If `i == 0 or j == 0`: `dp[i][j] = 1`
  - Else: `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`
  - Update `res = max(res, dp[i][j])`

**2.5 Return Result:**
Maximum side length is 2, so area = 2² = 4. Return `4`.

