## Explanation

### Strategy (The "Why")

Given an $m \times n$ board of characters and a string `word`, we need to determine if `word` exists in the board. The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically neighboring).

**1.1 Constraints & Complexity:**

- **Input Size:** The board dimensions can be up to $6 \times 6$, and word length can be up to $15$.
- **Value Range:** Board contains only lowercase and uppercase English letters.
- **Time Complexity:** $O(m \times n \times 4^L)$ where $L$ is the length of the word. In the worst case, we explore all paths of length $L$ from each cell.
- **Space Complexity:** $O(L)$ - The recursion depth is at most $L$ (the word length).
- **Edge Case:** If the word is empty, return true. If the board is empty, return false.

**1.2 High-level approach:**

The goal is to find if a word can be formed by traversing adjacent cells in the board.

We use DFS (depth-first search) with backtracking. For each cell, we check if it matches the first character of the word. If yes, we mark it as visited and recursively search for the remaining characters in adjacent cells. After exploring, we unmark it (backtrack).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths from all starting positions. This would be exponential.
- **Optimized Strategy (DFS with Backtracking):** Use DFS to explore paths, marking cells as visited and backtracking when a path doesn't work. This is the standard approach.
- **Why it's better:** DFS with backtracking efficiently explores paths without storing all possible paths explicitly. The backtracking allows us to reuse the board for different paths.

**1.4 Decomposition:**

1. For each cell in the board:
   - Start DFS if the cell matches the first character of the word.
2. In DFS:
   - Base case: if we've matched all characters, return true.
   - Check bounds and if current cell matches the current character.
   - Mark cell as visited (temporarily modify board).
   - Recursively search in 4 directions.
   - Unmark cell (backtrack).
3. Return true if any starting position leads to the word, false otherwise.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]$, $word = "ABCCED"$

We initialize:
- Start DFS from (0,0) since board[0][0] = 'A' matches word[0]

**2.2 Start DFS:**

We begin searching for the word.

**2.3 Trace Walkthrough:**

| Step | Position | Character | Match? | Action | Mark |
|------|----------|-----------|--------|--------|------|
| 1 | (0,0) | 'A' | Yes | Mark, search neighbors | '#' |
| 2 | (0,1) | 'B' | Yes | Mark, search neighbors | '#' |
| 3 | (0,2) | 'C' | Yes | Mark, search neighbors | '#' |
| 4 | (1,2) | 'C' | Yes | Mark, search neighbors | '#' |
| 5 | (1,1) | 'E' | Yes | Mark, search neighbors | '#' |
| 6 | (2,1) | 'D' | Yes | Found word! | Return True |

**2.4 Path Found:**

The path: $(0,0) \rightarrow (0,1) \rightarrow (0,2) \rightarrow (1,2) \rightarrow (1,1) \rightarrow (2,1)$ forms "ABCCED".

**2.5 Return Result:**

We return `True` because the word "ABCCED" exists in the board.

> **Note:** The key insight is to use DFS with backtracking. We mark cells as visited during exploration and unmark them when backtracking, allowing the same cell to be used in different paths if needed. This is more space-efficient than storing visited cells separately.

