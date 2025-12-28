## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to find the maximum number of fruits three children can collect from an n×n grid. Each child starts from a different corner and makes exactly n-1 moves to reach (n-1, n-1). When multiple children enter the same room, only one collects the fruits.

**1.1 Constraints & Complexity:**

- **Input Size:** n is between 2 and 1000, and each cell has 0 to 1000 fruits.
- **Time Complexity:** O(n^2) - we iterate through the grid multiple times, each taking O(n^2) time.
- **Space Complexity:** O(n^2) - we use a copy of the grid for dynamic programming.
- **Edge Case:** When n = 2, each child makes 1 move to reach (1, 1).

**1.2 High-level approach:**

The goal is to maximize fruit collection by three children with different movement constraints. The first child must go along the diagonal. The other two children can take optimal paths using dynamic programming, and we need to ensure they don't overlap with the first child's path.

![Three children path visualization](https://assets.leetcode.com/static_assets/others/three-paths.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths for all three children, which would be exponential in complexity.
- **Optimized Strategy:** Use dynamic programming. The first child takes the diagonal (fixed path). For the other two children, use DP to find optimal paths that don't conflict with the first child's path. This is O(n^2) time.
- **Optimization:** By recognizing that the first child's path is fixed (diagonal) and using DP for the other two, we avoid exploring all path combinations and reduce complexity from exponential to polynomial.

**1.4 Decomposition:**

1. Mark inaccessible cells (cells that conflict with the first child's diagonal path) as 0.
2. Calculate the first child's total fruits from the diagonal.
3. Use DP for the second child (from top-right corner) to accumulate maximum fruits.
4. Use DP for the third child (from bottom-left corner) to accumulate maximum fruits.
5. Sum the first child's fruits with the optimal paths of the other two children just before the destination.
6. Return the total maximum fruits collected.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use a 4×4 grid example.

- First child: collects from diagonal (0,0), (1,1), (2,2), (3,3)
- Second child: starts at (0,3), moves toward (3,3)
- Third child: starts at (3,0), moves toward (3,3)

**2.2 Start Checking:**

We first mark inaccessible cells, then process each child's path.

**2.3 Trace Walkthrough:**

**Step 1: Mark inaccessible cells**
- Cells that would conflict with diagonal path are set to 0

**Step 2: First child (diagonal)**
- Collects: A[0][0] + A[1][1] + A[2][2] + A[3][3]

**Step 3: Second child DP**
- For each cell (i,j) where j > i, accumulate from best previous position
- A[i][j] += max(A[i-1][j-1], A[i-1][j], A[i-1][j+1])

**Step 4: Third child DP**
- For each cell (i,j) where i > j, accumulate from best previous position
- A[i][j] += max(A[i-1][j-1], A[i][j-1], A[i+1][j-1])

**Step 5: Final result**
- res = diagonal_sum + A[n-1][n-2] + A[n-2][n-1]

**2.4 Increment and Loop:**

For the second and third children:
- We iterate through valid cells (avoiding the diagonal).
- For each cell, we take the maximum from valid previous positions.
- We accumulate the maximum fruits along the path.

**2.5 Return Result:**

The result is the sum of fruits from all three optimal paths, ensuring no double-counting since the first child's path is separate from the other two's final positions.

