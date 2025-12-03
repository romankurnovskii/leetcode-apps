## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** The board dimensions are $1 \leq m, n \leq 200$. Each cell contains either 'X' or 'O'.
- **Time Complexity:** $O(m \times n)$ where $m$ and $n$ are the board dimensions. We visit each cell at most twice (once for marking, once for conversion).
- **Space Complexity:** $O(m \times n)$ in the worst case for the recursion stack when the entire board is 'O'.
- **Edge Case:** If the board is empty or all cells are 'X', no changes are needed.

**1.2 High-level approach:**

The goal is to capture (convert to 'X') all 'O' regions that are completely surrounded by 'X', while preserving 'O' regions that touch the border. We use a two-pass approach: first mark border-connected 'O's, then convert remaining 'O's to 'X's.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each 'O' region, check if it touches the border. If not, convert it to 'X'. This requires multiple DFS/BFS traversals and is less efficient.
- **Optimized Strategy:** Start from border cells and mark all 'O's connected to borders as 'E' (escape). Then convert remaining 'O's to 'X' and 'E's back to 'O'. This requires only two passes.
- **Why optimized is better:** The optimized approach is more efficient as it processes border-connected regions first, avoiding unnecessary checks for interior regions.

**1.4 Decomposition:**

1. Perform DFS/BFS from all border cells that contain 'O'.
2. Mark all 'O's connected to borders as 'E' (escape marker).
3. Convert all remaining 'O's (surrounded regions) to 'X'.
4. Convert all 'E's back to 'O' to restore border-connected regions.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example:
```
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
```

We have a $4 \times 4$ board. We'll use DFS to mark border-connected 'O's.

**2.2 Start Checking:**

We iterate through all border cells (first row, last row, first column, last column) and perform DFS from any 'O' cells found.

**2.3 Trace Walkthrough:**

| Step | Action | Board State |
|------|--------|-------------|
| Initial | Start | All 'O's are unmarked |
| 1 | DFS from (3,1) - bottom border | Mark (3,1) as 'E' |
| 2 | Check borders | No other border 'O's found |
| 3 | Convert remaining 'O' to 'X' | (1,1), (1,2), (2,2) -> 'X' |
| 4 | Convert 'E' back to 'O' | (3,1) -> 'O' |

**2.4 Increment and Loop:**

The DFS function recursively marks all connected 'O's:
- Check if current cell is out of bounds or not 'O', return if so.
- Mark current cell as 'E'.
- Recursively call DFS on all 4 neighbors (up, down, left, right).

**2.5 Return Result:**

After processing:
- Border-connected 'O' at (3,1) remains as 'O'.
- Surrounded 'O's at (1,1), (1,2), (2,2) are converted to 'X'.

Final result:
```
[["X","X","X","X"],
 ["X","X","X","X"],
 ["X","X","X","X"],
 ["X","O","X","X"]]
```

