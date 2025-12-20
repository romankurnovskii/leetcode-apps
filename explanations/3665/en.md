## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count the number of unique paths from the top-left corner (0,0) to the bottom-right corner (m-1, n-1) in a grid where mirrors can reflect the robot's movement. The robot can only move right or down. When attempting to move into a mirror cell, the robot is reflected: moving right into a mirror reflects down, and moving down into a mirror reflects right. If a reflection lands in another mirror, the process continues.

**1.1 Constraints & Complexity:**

- **Input Size:** Grid dimensions m and n can be up to 500.
- **Time Complexity:** O(m * n) - we use memoization with 3D DP (i, j, direction), and each state is computed at most once.
- **Space Complexity:** O(m * n) - we store a 3D DP table of size m * n * 2 (two directions per cell).
- **Edge Case:** If the starting or ending cell is a mirror, the problem states they are always 0 (non-mirror), so we don't need to handle that case.

**1.2 High-level approach:**

The goal is to use dynamic programming with memoization, tracking not just the position (i, j) but also the direction from which we arrived at that position. This is crucial because when we're at a mirror cell, the reflection depends on the direction we came from.

![Mirror path reflection visualization](https://assets.leetcode.com/static_assets/others/mirror-reflection.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths recursively without memoization, which would be exponential O(2^(m+n)) in the worst case.
- **Optimized Strategy:** Use 3D dynamic programming with memoization, tracking position (i, j) and direction (dir). The direction is necessary because when at a mirror, the reflection depends on how we arrived. This is O(m * n) time.
- **Optimization:** By memoizing states (i, j, dir), we avoid recalculating the same subproblems, reducing time complexity from exponential to polynomial.

**1.4 Decomposition:**

1. Use a 3D DP table where dp[i][j][dir] represents the number of ways to reach (i,j) with direction dir.
2. Direction dir = 0 means we came from the left (moved right to reach here), dir = 1 means we came from above (moved down to reach here).
3. For each cell (i, j) with direction dir:
   - If the cell is a mirror (grid[i][j] == 1), reflect based on direction:
     - If dir == 0 (came from left), reflect down (move to i+1, j with dir=1).
     - If dir == 1 (came from above), reflect right (move to i, j+1 with dir=0).
   - If the cell is not a mirror, try both moves: right and down.
4. Use memoization to avoid recalculating the same states.
5. Return the result modulo 10^9 + 7.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `grid = [[0,1,0],[0,0,1],[1,0,0]]`

- Grid dimensions: m = 3, n = 3
- Starting position: (0, 0) with dir = 0
- Destination: (2, 2)
- Mirrors at: (0,1), (1,2), (2,0)

**2.2 Start Processing:**

We begin recursive DFS from (0, 0) with direction 0.

**2.3 Trace Walkthrough:**

| Position (i,j) | Direction | Cell Type | Action | Next States |
|----------------|-----------|-----------|--------|-------------|
| (0,0) | 0 | 0 (empty) | Try both moves | (0,1) dir=0, (1,0) dir=1 |
| (0,1) | 0 | 1 (mirror) | Reflect down | (1,1) dir=1 |
| (1,0) | 1 | 0 (empty) | Try both moves | (1,1) dir=0, (2,0) dir=1 |
| (1,1) | 0 | 0 (empty) | Try both moves | (1,2) dir=0, (2,1) dir=1 |
| (1,1) | 1 | 0 (empty) | Try both moves | (1,2) dir=0, (2,1) dir=1 |
| (1,2) | 0 | 1 (mirror) | Reflect down | (2,2) dir=1 ✓ |
| (2,0) | 1 | 1 (mirror) | Reflect right | (2,1) dir=0 |
| (2,1) | 0 | 0 (empty) | Try both moves | (2,2) dir=0 ✓ |

**2.4 Increment and Loop:**

The recursive DFS explores all valid paths, using memoization to avoid recalculating the same (i, j, dir) states.

**2.5 Return Result:**

The result is 5, which represents the total number of unique valid paths from (0,0) to (2,2) considering all mirror reflections.

