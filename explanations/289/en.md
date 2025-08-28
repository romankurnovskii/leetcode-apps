## 289. Game of Life [Medium]

https://leetcode.com/problems/game-of-life

## Description
According to [Wikipedia's article](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life): "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an `m x n` grid of cells, where each cell has an initial state: **live** (represented by a `1`) or **dead** (represented by a `0`). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the `m x n` grid `board`. In this process, births and deaths occur **simultaneously**.

Given the current state of the `board`, **update** the `board` to reflect its next state.

**Note** that you do not need to return anything.

**Examples**

```tex
Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
```

**Constraints**
```tex
- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] is 0 or 1
```

**Follow up:**
- Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
- In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

## Explanation

### Strategy
Let's restate the problem: You're given a 2D grid representing the current state of Conway's Game of Life, where each cell is either alive (1) or dead (0). You need to update the board to the next generation based on specific rules about cell survival and reproduction.

This is a **simulation problem** that requires careful handling to update all cells simultaneously without interfering with the calculation of other cells.

**What is given?** An m x n grid where each cell is either 0 (dead) or 1 (live).

**What is being asked?** Update the board to the next generation based on the Game of Life rules.

**Constraints:** The grid can be up to 25x25, and all cells contain only 0 or 1.

**Edge cases:** 
- Grid with all dead cells
- Grid with all live cells
- Single row or column
- Grid with live cells on borders

**High-level approach:**
The solution involves using a two-pass approach where we first mark cells with their next state using special values, then convert these markers to the final states.

**Decomposition:**
1. **First pass**: Mark cells with their next state using special values (2 for live→dead, 3 for dead→live)
2. **Second pass**: Convert special values to final states (2→0, 3→1)
3. **Count neighbors**: For each cell, count its eight neighbors to determine its fate

**Brute force vs. optimized strategy:**
- **Brute force**: Create a copy of the board and update it. This takes O(mn) space.
- **Optimized**: Use special values to mark next states in-place. This takes O(1) space.

### Steps
Let's walk through the solution step by step using the first example: `board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]`

**Step 1: First pass - mark cells with next state**
- For each cell, count its eight neighbors
- Apply Game of Life rules and mark with special values:
  - `2` = currently live, will die (live→dead)
  - `3` = currently dead, will live (dead→live)
  - `0` = currently dead, will stay dead
  - `1` = currently live, will stay live

**Step 2: Count neighbors for each cell**
- For cell `board[0][1] = 1` (live):
  - Neighbors: `[0,0,1,0,0,1,1,1]` = 4 live neighbors
  - Rule 3: More than 3 live neighbors → dies
  - Mark as `2` (live→dead)

- For cell `board[1][2] = 1` (live):
  - Neighbors: `[1,0,1,1,1,0,0,0]` = 4 live neighbors
  - Rule 3: More than 3 live neighbors → dies
  - Mark as `2` (live→dead)

**Step 3: Second pass - convert special values**
- Convert `2` → `0` (dead)
- Convert `3` → `1` (live)
- Final board: `[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]`

**Why this works:**
By using special values (2 and 3) to mark the next state, we can update the board in-place without losing information about the current state. The two-pass approach ensures all cells are updated simultaneously as required.

> **Note:** The key insight is using special values to represent both current and next states, allowing us to solve the problem in-place while maintaining the requirement that all cells update simultaneously.

**Time Complexity:** O(mn) - we visit each cell twice  
**Space Complexity:** O(1) - we only use a constant amount of extra space
