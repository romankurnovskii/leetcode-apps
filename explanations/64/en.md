# 64. Minimum Path Sum

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/minimum-path-sum/

## Problem Description

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
```

**Example 2:**
```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

**Constraints:**
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 200`
- `0 <= grid[i][j] <= 200`

## Explanation

### Strategy

This is a **dynamic programming problem** that requires finding the minimum path sum from top-left to bottom-right. The key insight is to use a DP table where each cell represents the minimum sum to reach that position.

**Key observations:**
- We can only move right or down
- The minimum sum to reach (i,j) = min(sum from (i-1,j), sum from (i,j-1)) + grid[i][j]
- We need to handle edge cases for first row and column
- The result is the value at the bottom-right corner

**High-level approach:**
1. **Create DP table**: Initialize with same dimensions as input grid
2. **Fill first row**: Each cell = previous cell + current value
3. **Fill first column**: Each cell = cell above + current value
4. **Fill remaining cells**: Use DP formula with min function
5. **Return result**: Return value at bottom-right corner

### Steps

Let's break down the solution step by step:

**Step 1: Initialize DP table**
- Create `dp` table with same dimensions as grid
- Set `dp[0][0] = grid[0][0]`

**Step 2: Fill first row**
- For each cell in first row: `dp[0][j] = dp[0][j-1] + grid[0][j]`

**Step 3: Fill first column**
- For each cell in first column: `dp[i][0] = dp[i-1][0] + grid[i][0]`

**Step 4: Fill remaining cells**
- For each cell (i,j): `dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]`

**Step 5: Return result**
- Return `dp[m-1][n-1]`

**Example walkthrough:**
Let's trace through the first example:

```
grid = [[1,3,1],[1,5,1],[4,2,1]]

Step 1: Initialize
dp = [[1,0,0],[0,0,0],[0,0,0]]

Step 2: Fill first row
dp[0][1] = dp[0][0] + grid[0][1] = 1 + 3 = 4
dp[0][2] = dp[0][1] + grid[0][2] = 4 + 1 = 5
dp = [[1,4,5],[0,0,0],[0,0,0]]

Step 3: Fill first column
dp[1][0] = dp[0][0] + grid[1][0] = 1 + 1 = 2
dp[2][0] = dp[1][0] + grid[2][0] = 2 + 4 = 6
dp = [[1,4,5],[2,0,0],[6,0,0]]

Step 4: Fill remaining cells
dp[1][1] = min(dp[0][1], dp[1][0]) + grid[1][1] = min(4,2) + 5 = 7
dp[1][2] = min(dp[0][2], dp[1][1]) + grid[1][2] = min(5,7) + 1 = 6
dp[2][1] = min(dp[1][1], dp[2][0]) + grid[2][1] = min(7,6) + 2 = 8
dp[2][2] = min(dp[1][2], dp[2][1]) + grid[2][2] = min(6,8) + 1 = 7

Result: dp[2][2] = 7
```

> **Note:** The key insight is that the minimum path sum to reach any cell is the minimum of the path sums from the cell above and the cell to the left, plus the current cell's value. This creates an optimal substructure that can be solved with dynamic programming.

### Solution

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Handle edge case
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Initialize DP table
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        # Return result
        return dp[m-1][n-1]
```

**Time Complexity:** O(m * n) - we visit each cell exactly once  
**Space Complexity:** O(m * n) - we need a DP table of the same size 