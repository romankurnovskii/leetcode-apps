## Explanation

### Strategy (The "Why")

Given an $m \times n$ 2D binary grid, we need to return the number of islands. An island is formed by connecting adjacent lands (1s) horizontally or vertically. Water (0s) surrounds islands.

**1.1 Constraints & Complexity:**

- **Input Size:** The grid dimensions $m \times n$ can be up to $300 \times 300$.
- **Value Range:** Grid values are '0' (water) or '1' (land).
- **Time Complexity:** $O(m \times n)$ - We visit each cell at most once during DFS.
- **Space Complexity:** $O(m \times n)$ - In the worst case, the recursion stack can be as deep as the number of cells in an island (if the entire grid is one island).
- **Edge Case:** If the grid is empty, return 0. If there are no islands (all water), return 0.

**1.2 High-level approach:**

The goal is to count the number of connected components of '1's in the grid.

![Number of Islands](https://assets.leetcode.com/uploads/2021/03/10/2021-03-10-at-14-50-16.png)

We use DFS (depth-first search) to explore each island. When we find a '1', we start DFS to mark all connected '1's as visited (by changing them to '0'), then count this as one island.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** There isn't really a brute force approach - we must traverse the grid to find islands.
- **Optimized Strategy (DFS):** Use DFS to explore each island. Mark visited cells by changing '1' to '0' to avoid revisiting. Each DFS call from an unvisited '1' represents one island.
- **Why it's better:** DFS efficiently explores each connected component (island). By marking visited cells, we ensure each island is counted exactly once.

**1.4 Decomposition:**

1. Iterate through each cell in the grid.
2. If we find a '1' (land), increment the island count and start DFS.
3. In DFS, mark the current cell as visited (change to '0') and recursively explore all 4-directionally adjacent cells that are '1'.
4. After DFS completes, continue searching for the next island.
5. Return the total island count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]$

The grid:
```
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0
```

We initialize:
- `res = 0`

**2.2 Start Exploring:**

We iterate through each cell.

**2.3 Trace Walkthrough:**

| Cell (i,j) | Value | Action | Island Count |
|------------|-------|--------|--------------|
| (0,0) | '1' | Start DFS, mark all connected '1's | 1 |
| (0,4) | '0' | Skip | 1 |
| (1,4) | '0' | Skip | 1 |
| ... | ... | ... | ... |

**DFS from (0,0):**
- Mark (0,0) as '0', explore neighbors
- (0,1): '1' → mark '0', explore
- (1,0): '1' → mark '0', explore
- Continue until all connected '1's are marked '0'

**2.4 Final Grid:**

After DFS:
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```

All '1's have been visited and marked as '0'.

**2.5 Return Result:**

We return 1, which is the number of islands in the grid.

> **Note:** The key is to mark visited cells by changing '1' to '0'. This serves two purposes: it marks the cell as visited (avoiding revisiting) and it naturally creates a base case for the recursion (DFS stops when it encounters '0').

