## Explanation

### Strategy (The "Why")

Given two integers $m$ and $n$ representing a robot's position at the top-left corner of an $m \times n$ grid, we need to find the number of unique paths the robot can take to reach the bottom-right corner. The robot can only move either down or right at any point in time.

**1.1 Constraints & Complexity:**

- **Input Size:** $m$ and $n$ can be up to $100$.
- **Value Range:** $m$ and $n$ are positive integers.
- **Time Complexity:** $O(m \times n)$ - We fill a DP table of size $m \times n$.
- **Space Complexity:** $O(m \times n)$ - We use a DP table. This can be optimized to $O(n)$ by using only one row.
- **Edge Case:** If $m = 1$ or $n = 1$, there's only one path (straight line).

**1.2 High-level approach:**

The goal is to count the number of unique paths from top-left to bottom-right.

We use dynamic programming. The number of paths to reach cell $(i, j)$ equals the sum of paths from cell $(i-1, j)$ and cell $(i, j-1)$.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths using recursion. This takes exponential time.
- **Optimized Strategy (DP):** Use dynamic programming to store the number of paths to each cell. This takes $O(m \times n)$ time.
- **Why it's better:** DP reduces time complexity from exponential to polynomial by storing results of subproblems and avoiding redundant calculations.

**1.4 Decomposition:**

1. Create a DP table where `dp[i][j]` represents the number of paths to cell $(i, j)$.
2. Initialize first row and column to 1 (only one path: straight line).
3. For each cell $(i, j)$:
   - `dp[i][j] = dp[i-1][j] + dp[i][j-1]` (can come from above or left).
4. Return `dp[m-1][n-1]`.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $m = 3$, $n = 7$

We initialize:
- `dp = [[1] * 7 for _ in range(3)]`

**2.2 Start Filling DP Table:**

We fill the table row by row.

**2.3 Trace Walkthrough:**

| i | j | dp[i-1][j] | dp[i][j-1] | dp[i][j] |
|---|---|------------|------------|----------|
| 0 | 0-6 | - | - | 1 (initialized) |
| 1 | 0 | 1 | - | 1 (initialized) |
| 1 | 1 | 1 | 1 | $1 + 1 = 2$ |
| 1 | 2 | 1 | 2 | $1 + 2 = 3$ |
| 1 | 3 | 1 | 3 | $1 + 3 = 4$ |
| ... | ... | ... | ... | ... |
| 2 | 6 | 7 | 20 | $7 + 20 = 27$ |

**2.4 Final Result:**

After filling: `dp[2][6] = 28` (number of unique paths)

**2.5 Return Result:**

We return 28, which is the number of unique paths from (0,0) to (2,6).

> **Note:** The key insight is that the number of paths to any cell equals the sum of paths from the cell above and the cell to the left. This creates optimal substructure, making DP the perfect approach.

