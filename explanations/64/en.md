## Explanation

### Strategy (The "Why")

Given a grid filled with non-negative numbers, we need to find a path from the top-left corner to the bottom-right corner that minimizes the sum of all numbers along the path. We can only move right or down at each step.

**1.1 Constraints & Complexity:**

- **Input Size:** The grid dimensions $m \times n$ can be up to $200 \times 200$.
- **Value Range:** Each grid cell contains a value between $0$ and $100$.
- **Time Complexity:** $O(m \times n)$ - We iterate through each cell of the grid exactly once.
- **Space Complexity:** $O(m \times n)$ - We use a DP table of the same size as the grid. This can be optimized to $O(\min(m, n))$ by using only one row or column at a time.
- **Edge Case:** If the grid has only one cell, we return that cell's value. The starting and ending positions are fixed.

**1.2 High-level approach:**

The goal is to find the minimum path sum from top-left to bottom-right.

![Minimum Path Sum](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

This is a classic dynamic programming problem. At each cell, we can only arrive from the cell above or the cell to the left. We choose the path with minimum sum.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths from top-left to bottom-right, calculating the sum for each path. This would be exponential time $O(2^{m+n})$.
- **Optimized Strategy (Dynamic Programming):** Use DP to store the minimum path sum to reach each cell. For cell $(i, j)$, the minimum sum is the minimum of: (minimum sum to reach $(i-1, j)$) or (minimum sum to reach $(i, j-1)$), plus the current cell's value.
- **Why it's better:** DP reduces the time complexity from exponential to polynomial. We compute each subproblem once and reuse the results, avoiding redundant path calculations.

**1.4 Decomposition:**

1. Initialize a DP table where `dp[i][j]` represents the minimum path sum to reach cell $(i, j)$.
2. Set the base case: `dp[0][0] = grid[0][0]`.
3. Fill the first row: each cell can only be reached from the left.
4. Fill the first column: each cell can only be reached from above.
5. Fill remaining cells: take the minimum of the cell above and the cell to the left, then add the current cell's value.
6. Return `dp[m-1][n-1]`, which is the minimum path sum to the bottom-right corner.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $grid = [[1,3,1],[1,5,1],[4,2,1]]$

We initialize:
- `dp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]`
- `dp[0][0] = 1` (starting position)

**2.2 Start Calculating:**

We begin by filling the first row and first column.

**2.3 Trace Walkthrough:**

**Fill first row:**
- `dp[0][1] = dp[0][0] + grid[0][1] = 1 + 3 = 4`
- `dp[0][2] = dp[0][1] + grid[0][2] = 4 + 1 = 5`

**Fill first column:**
- `dp[1][0] = dp[0][0] + grid[1][0] = 1 + 1 = 2`
- `dp[2][0] = dp[1][0] + grid[2][0] = 2 + 4 = 6`

**Fill remaining cells:**

| Cell | From Above | From Left | Min | Current Value | Result |
|------|------------|-----------|-----|---------------|--------|
| $(1,1)$ | $dp[0][1] = 4$ | $dp[1][0] = 2$ | $2$ | $5$ | $2 + 5 = 7$ |
| $(1,2)$ | $dp[0][2] = 5$ | $dp[1][1] = 7$ | $5$ | $1$ | $5 + 1 = 6$ |
| $(2,1)$ | $dp[1][1] = 7$ | $dp[2][0] = 6$ | $6$ | $2$ | $6 + 2 = 8$ |
| $(2,2)$ | $dp[1][2] = 6$ | $dp[2][1] = 8$ | $6$ | $1$ | $6 + 1 = 7$ |

**2.4 Final DP Table:**

```
dp = [[1, 4, 5],
      [2, 7, 6],
      [6, 8, 7]]
```

**2.5 Return Result:**

We return `dp[2][2] = 7`, which is the minimum path sum.

The optimal path: $1 \rightarrow 3 \rightarrow 1 \rightarrow 1 \rightarrow 1 = 7$ (right, right, down, down).

> **Note:** The key insight is that we can only move right or down, so each cell's minimum path sum depends only on the cell above it and the cell to its left. This creates optimal substructure, making DP the perfect approach.

