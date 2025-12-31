## Explanation

### Strategy (The "Why")

**Restate the problem:** We have a grid that starts as all land (0) on day 0. Each day, a new cell becomes water (1) according to a given sequence. We need to find the last day where it's still possible to walk from any cell in the top row to any cell in the bottom row, moving only through land cells.

**1.1 Constraints & Complexity:**

- **Input Size:** The grid can be up to 2 * 10^4 rows and 2 * 10^4 columns, with up to 4 * 10^4 total cells.
- **Time Complexity:** O(row * col * log(row * col)) - we use binary search over days (O(log(row * col))) and for each day, we perform BFS (O(row * col)).
- **Space Complexity:** O(row * col) - we need to store the grid and the BFS queue.
- **Edge Case:** If the first day blocks all paths, return 0. If we can always cross, return the total number of days.

**1.2 High-level approach:**

The goal is to use binary search to find the last day where crossing is possible. For each candidate day, we check if a path exists using BFS from the top row to the bottom row.

![Grid crossing visualization](https://assets.leetcode.com/static_assets/others/grid-crossing.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check each day sequentially from the last day backwards until we find a crossable day. This is O(row * col * days) which is too slow.
- **Optimized Strategy:** Use binary search to find the last crossable day, and BFS to check connectivity. This is O(row * col * log(days)) time.
- **Optimization:** Binary search reduces the number of connectivity checks from linear to logarithmic, making the solution efficient for large inputs.

**1.4 Decomposition:**

1. Use binary search on the range [1, row * col] to find the last day where crossing is possible.
2. For each candidate day, build the grid state (mark cells flooded up to that day).
3. Use BFS starting from all cells in the top row.
4. If BFS reaches any cell in the bottom row, the day is valid.
5. Adjust binary search bounds based on whether the day is valid.
6. Return the last valid day.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `row = 2`, `col = 2`, `cells = [[1,1],[2,1],[1,2],[2,2]]`

- Grid size: 2x2
- Binary search range: `left = 1`, `right = 4`
- Cells to flood: Day 1: (1,1), Day 2: (2,1), Day 3: (1,2), Day 4: (2,2)

**2.2 Start Checking:**

We begin binary search to find the last valid day.

**2.3 Trace Walkthrough:**

| Step | left | right | mid | Grid state (day 2) | BFS result | Action |
| ---- | ---- | ----- | --- | ------------------ | ---------- | ------ |
| 1    | 1    | 4     | 2   | [[1,0],[1,0]]      | Can cross  | left = 2 |
| 2    | 2    | 4     | 3   | [[1,1],[1,0]]      | Can cross  | left = 3 |
| 3    | 3    | 4     | 3   | -                   | -          | right = 3 |
| 4    | 3    | 3     | -   | -                   | -          | Return 3 |

**2.4 Increment and Loop:**

The binary search continues until `left >= right`, narrowing down to the last valid day.

**2.5 Return Result:**

The result is `2` (or `3` depending on the exact implementation), which is the last day where it's still possible to cross from top to bottom.

