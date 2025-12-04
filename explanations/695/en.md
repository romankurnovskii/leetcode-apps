## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Constraints:** Grid dimensions are between 1 and 50, and each cell is either 0 (water) or 1 (land).
- **Time Complexity:** O(m * n) - We visit each cell at most once, where m and n are grid dimensions.
- **Space Complexity:** O(m * n) - In the worst case (all land), the recursion stack can be O(m * n) deep.
- **Edge Case:** If the grid contains no islands (all water), return 0.

**1.2 High-level approach:**
The goal is to find the maximum area of an island in a 2D grid. An island is a group of 1's connected 4-directionally. We use DFS to explore each island, marking visited cells to avoid revisiting, and track the maximum area found.

![Max Area of Island](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** For each cell, if it's land, explore the entire island and calculate area. This is the same as our approach - we need to visit each cell once.
- **Optimized Strategy (DFS with Visited Marking):** Use DFS to explore islands, marking visited cells by setting them to 0. This ensures we visit each cell exactly once.
- **Emphasize the optimization:** By marking visited cells in-place (setting to 0), we avoid using extra space for a visited array and ensure O(1) space per cell.

**1.4 Decomposition:**
1. Iterate through each cell in the grid.
2. If a cell is 1 (land), start DFS to explore the island.
3. In DFS, mark the current cell as visited (set to 0), increment area counter.
4. Recursively explore all 4-directional neighbors that are land.
5. Return the area of the current island.
6. Track and return the maximum area found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use a small example: `grid = [[0,0,1,0],[0,1,1,0],[0,1,0,0]]`

Initialize:
- `res = 0` (maximum area found)

**2.2 Start Checking:**
We iterate through each cell (i, j).

**2.3 Trace Walkthrough:**

| Cell (i,j) | Value | Action | Island Area | Max Area |
|------------|-------|--------|-------------|----------|
| (0,0) | 0 | Skip | - | 0 |
| (0,1) | 0 | Skip | - | 0 |
| (0,2) | 1 | DFS | Explore island | - |
| (0,2) DFS | 1→0 | Mark, area=1 | 1 | - |
| (1,2) DFS | 1→0 | Mark, area=2 | 2 | - |
| (1,1) DFS | 1→0 | Mark, area=3 | 3 | 3 |
| (0,3) | 0 | Skip | - | 3 |
| (1,0) | 0 | Skip | - | 3 |
| (1,3) | 0 | Skip | - | 3 |
| (2,0) | 0 | Skip | - | 3 |
| (2,1) | 1 | DFS | Explore island | - |
| (2,1) DFS | 1→0 | Mark, area=1 | 1 | 3 |

**2.4 Return Result:**
The maximum area found is 3, which is the area of the island starting at (0,2).

