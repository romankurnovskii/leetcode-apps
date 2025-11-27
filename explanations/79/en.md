## Explanation

### Strategy (The "Why")

Given an $m \times n$ board of characters and a string `word`, we need to determine if `word` exists in the board. The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**1.1 Constraints & Complexity:**

- **Input Size:** The board dimensions can be up to $6 \times 6$, and word length can be up to $15$.
- **Value Range:** Board and word contain only lowercase and uppercase English letters.
- **Time Complexity:** $O(m \times n \times 4^L)$ where $L$ is the length of the word. In the worst case, we explore $4^L$ paths from each starting cell.
- **Space Complexity:** $O(L)$ - The recursion stack can be as deep as the word length.
- **Edge Case:** If the word is empty, return true. If the board doesn't contain all characters of the word, return false.

**1.2 High-level approach:**

The goal is to find if a word exists in the board by following adjacent cells.

We use DFS (depth-first search) with backtracking. We try starting from each cell, and for each cell, we explore all 4 directions recursively. We mark visited cells to avoid revisiting.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths from all starting positions. This would be exponential.
- **Optimized Strategy (DFS with Backtracking):** Use DFS to explore paths, marking visited cells and backtracking when a path doesn't work. This is the standard approach.
- **Why it's better:** DFS with backtracking efficiently explores paths and prunes invalid ones early by marking visited cells and restoring them when backtracking.

**1.4 Decomposition:**

1. Try starting from each cell in the board.
2. For each starting cell, use DFS:
   - Check if current cell matches the current character of the word.
   - Mark the cell as visited.
   - Explore all 4 directions recursively.
   - If word is found, return true.
   - Backtrack: restore the cell.
3. Return false if word not found from any starting position.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]$, $word = "ABCCED"$

We initialize:
- Start DFS from (0,0) with character 'A'

**2.2 Start DFS:**

We begin exploring paths.

**2.3 Trace Walkthrough:**

| Step | Position | Character | Match? | Action | Next |
|------|----------|-----------|--------|--------|------|
| 1 | (0,0) | 'A' | Yes | Mark, explore | (0,1) or (1,0) |
| 2 | (0,1) | 'B' | Yes | Mark, explore | (0,2) or (1,1) |
| 3 | (0,2) | 'C' | Yes | Mark, explore | (0,3) or (1,2) |
| 4 | (1,2) | 'C' | Yes | Mark, explore | (1,3) or (2,2) |
| 5 | (1,3) | 'E' | Yes | Mark, explore | (2,3) |
| 6 | (2,3) | 'D' | No | Backtrack | - |
| 7 | (2,2) | 'E' | Yes | Mark, explore | (2,3) |
| 8 | (2,3) | 'D' | Yes | **Found!** | Return True |

**2.4 Explanation:**

The path found: (0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (2,3) spells "ABCCED".

**2.5 Return Result:**

We return `True` because the word "ABCCED" exists in the board.

> **Note:** The key is to use DFS with backtracking. We mark cells as visited during exploration and restore them when backtracking. This allows us to explore all possible paths while avoiding infinite loops.

