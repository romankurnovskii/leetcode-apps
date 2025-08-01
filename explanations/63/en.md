# 63. Unique Paths II

**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/unique-paths-ii/

## Problem Description

You are given an `m x n` integer array `grid`. There is a robot initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

An obstacle and space are marked as `1` or `0` respectively in `grid`. A path that the robot takes cannot include **any** square that is an obstacle.

Return *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The testcases are generated so that the answer will be less than or equal to `2 * 10^9`.

**Example 1:**
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right → Right → Down → Down
2. Down → Down → Right → Right
```

**Example 2:**
```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
```

**Constraints:**
- `m == obstacleGrid.length`
- `n == obstacleGrid[i].length`
- `1 <= m, n <= 100`
- `obstacleGrid[i][j]` is `0` or `1`.

## Explanation

### Strategy

This is a **dynamic programming problem** that extends the unique paths problem to handle obstacles. The key insight is to use a DP table where each cell represents the number of ways to reach that position, with obstacles blocking paths.

**Key observations:**
- We can only move right or down
- Obstacles (value 1) block all paths through them
- The number of paths to reach (i,j) = paths from (i-1,j) + paths from (i,j-1)
- If a cell is an obstacle, it has 0 paths
- We need to handle edge cases for first row and column

**High-level approach:**
1. **Create DP table**: Initialize with same dimensions as input grid
2. **Handle first cell**: If start is obstacle, return 0
3. **Fill first row/column**: Handle edge cases
4. **Fill remaining cells**: Use DP formula with obstacle checks
5. **Return result**: Return value at bottom-right corner

### Steps

Let's break down the solution step by step:

**Step 1: Handle edge cases**
- If start or end is obstacle, return 0

**Step 2: Initialize DP table**
- Create `dp` table with same dimensions as grid
- Set `dp[0][0] = 1` (if not obstacle)

**Step 3: Fill first row**
- For each cell in first row, if not obstacle and previous cell is reachable, set to 1

**Step 4: Fill first column**
- For each cell in first column, if not obstacle and previous cell is reachable, set to 1

**Step 5: Fill remaining cells**
- For each cell (i,j), if not obstacle: `dp[i][j] = dp[i-1][j] + dp[i][j-1]`

**Example walkthrough:**
Let's trace through the first example:

```
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]

Step 1: Initialize
dp = [[1,0,0],[0,0,0],[0,0,0]]

Step 2: Fill first row
dp = [[1,1,1],[0,0,0],[0,0,0]]

Step 3: Fill first column
dp = [[1,1,1],[1,0,0],[1,0,0]]

Step 4: Fill remaining cells
dp[1][1] = 0 (obstacle)
dp[1][2] = dp[0][2] + dp[1][1] = 1 + 0 = 1
dp[2][1] = dp[1][1] + dp[2][0] = 0 + 1 = 1
dp[2][2] = dp[1][2] + dp[2][1] = 1 + 1 = 2

Result: dp[2][2] = 2
```

> **Note:** The key insight is that the number of paths to reach any cell is the sum of paths from the cell above and the cell to the left, but only if the current cell is not an obstacle. This creates a natural DP structure.

### Solution

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Handle edge cases
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If start or end is obstacle, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Initialize DP table
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        # Fill first row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        
        # Fill first column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        
        # Fill remaining cells
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return result
        return dp[m-1][n-1]
```

**Time Complexity:** O(m * n) - we visit each cell exactly once  
**Space Complexity:** O(m * n) - we need a DP table of the same size 