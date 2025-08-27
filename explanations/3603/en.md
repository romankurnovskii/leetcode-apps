## 3603. Minimum Cost Path with Alternating Directions II [Medium]

https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii

## Description

You are given two integers `m` and `n` representing the number of rows and columns of a grid, respectively.

The cost to enter cell `(i, j)` is defined as `(i + 1) * (j + 1)`.

You are also given a 2D integer array `waitCost` where `waitCost[i][j]` defines the cost to **wait** on that cell.

The path will always begin by entering cell `(0, 0)` on move 1 and paying the entrance cost.

At each step, you follow an alternating pattern:
- On **odd-numbered** seconds, you must move **right** or **down** to an **adjacent** cell, paying its entry cost.
- On **even-numbered** seconds, you must **wait** in place for **exactly** one second and pay `waitCost[i][j]` during that second.

Return the **minimum** total cost required to reach `(m - 1, n - 1)`.

**Examples**

**Example 1:**

```sh
Input: m = 1, n = 2, waitCost = [[1,2]]

Output: 3

Explanation:
- Start at cell (0, 0) at second 1 with entry cost 1.
- Second 1: Move right to cell (0, 1) with entry cost 2.
- Total cost: 1 + 2 = 3.
```

**Example 2:**

```sh
Input: m = 2, n = 2, waitCost = [[3,5],[2,4]]

Output: 9

Explanation:
- Start at cell (0, 0) at second 1 with entry cost 1.
- Second 1: Move down to cell (1, 0) with entry cost 2.
- Second 2: Wait at cell (1, 0), paying waitCost[1][0] = 2.
- Second 3: Move right to cell (1, 1) with entry cost 4.
- Total cost: 1 + 2 + 2 + 4 = 9.
```

**Example 3:**

```sh
Input: m = 2, n = 3, waitCost = [[6,1,4],[3,2,5]]

Output: 16

Explanation:
- Start at cell (0, 0) at second 1 with entry cost 1.
- Second 1: Move right to cell (0, 1) with entry cost 2.
- Second 2: Wait at cell (0, 1), paying waitCost[0][1] = 1.
- Second 3: Move down to cell (1, 1) with entry cost 4.
- Second 4: Wait at cell (1, 1), paying waitCost[1][1] = 2.
- Second 5: Move right to cell (1, 2) with entry cost 6.
- Total cost: 1 + 2 + 1 + 4 + 2 + 6 = 16.
```

**Constraints**
```tex
1 <= m, n <= 10^5
2 <= m * n <= 10^5
waitCost.length == m
waitCost[0].length == n
0 <= waitCost[i][j] <= 10^5
```

## Explanation

### Strategy

Let's restate the problem:
- We have a grid where each cell has an entry cost and a wait cost.
- On odd seconds, we must move right or down; on even seconds, we must wait in place.
- The goal is to reach the bottom-right cell with the minimum total cost.

**Type:** Array, Dynamic Programming, Matrix

**What is being asked?**
- Find the minimum cost path from the top-left to the bottom-right, following the alternating move/wait pattern.

**What is given?**
- Grid dimensions, entry cost formula, and wait cost matrix.

**Constraints/Edge Cases:**
- Large grids (up to 10^5 cells).
- Must alternate between moving and waiting.

**High-Level Plan:**
- Use dynamic programming or Dijkstra's algorithm to track the minimum cost to reach each cell, considering the move/wait alternation.
- For each cell, track the cost to reach it at both odd and even time steps (parity).
- At each move, update the cost for the next cell and the next parity.

### Steps

1. **Model the problem as a DP or shortest path problem:**
   - State: (i, j, parity) where parity is 1 (move) or 0 (wait).
2. **Initialize the DP table or cost matrix:**
   - Start at (0, 0) with cost 1 (entry cost).
3. **For each cell, update possible moves:**
   - On move steps, try moving right or down, paying the entry cost.
   - On wait steps, stay in place and pay the wait cost.
4. **Continue until reaching (m-1, n-1):**
   - The answer is the minimum cost to reach the bottom-right cell.

**Example Walkthrough:**

Suppose m = 2, n = 2, waitCost = [[3,5],[2,4]]

- Start at (0,0): cost = 1
- Move down to (1,0): cost += 2 (entry) → total = 3
- Wait at (1,0): cost += 2 (wait) → total = 5
- Move right to (1,1): cost += 4 (entry) → total = 9

> **Note:** The alternation between move and wait is key; you cannot move twice in a row or wait twice in a row.

> **Note:** This solution uses a simple recursive approach with memoization for clarity. It is not the most optimized for large grids, but it is easy to follow and matches the problem's alternating move/wait pattern step by step.

**Advanced:**
For large grids, you can use an iterative DP or Dijkstra's algorithm for better performance. See the community explanations above for optimized versions.
