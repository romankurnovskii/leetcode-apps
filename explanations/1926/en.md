## Explanation

### Strategy (The "Why")

Given an $m \times n$ maze with walls ('+') and empty cells ('.'), an entrance cell, and exits at the boundaries (but not the entrance), we need to find the nearest exit from the entrance. We can only move in 4 directions (up, down, left, right).

**1.1 Constraints & Complexity:**

- **Input Size:** The maze dimensions can be up to $100 \times 100$.
- **Value Range:** Maze cells are either '+' (wall) or '.' (empty).
- **Time Complexity:** $O(m \times n)$ - In the worst case, we visit all cells once using BFS.
- **Space Complexity:** $O(m \times n)$ - The queue and visited set can contain all cells in the worst case.
- **Edge Case:** If the entrance is at a boundary and there are no other exits, return -1. If there's no path to any exit, return -1.

**1.2 High-level approach:**

The goal is to find the shortest path from the entrance to the nearest exit.

We use BFS (breadth-first search) to explore the maze level by level. The first boundary cell we reach (that's not the entrance) is the nearest exit.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all possible paths and find the shortest. This would be exponential.
- **Optimized Strategy (BFS):** Use BFS to explore the maze level by level. BFS guarantees we find the shortest path. This takes $O(m \times n)$ time.
- **Why it's better:** BFS finds the shortest path efficiently and guarantees optimality. It explores all cells at distance $d$ before exploring cells at distance $d+1$.

**1.4 Decomposition:**

1. Initialize a queue with the entrance and mark it as visited.
2. While the queue is not empty:
   - Dequeue a cell and check if it's an exit (boundary and not entrance).
   - If yes, return the number of steps.
   - Otherwise, explore all 4-directionally adjacent empty cells.
   - Add unvisited empty cells to the queue with incremented step count.
3. If the queue is empty and no exit found, return -1.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]$, $entrance = [1,2]$

We initialize:
- `queue = deque([(1, 2, 0)])`
- `visited = {(1, 2)}`

**2.2 Start BFS:**

We begin exploring the maze.

**2.3 Trace Walkthrough:**

| Step | Queue | Dequeue | Is Exit? | Neighbors | Queue After |
|------|-------|---------|----------|-----------|-------------|
| 0 | [(1,2,0)] | (1,2,0) | No | (1,1), (1,3), (0,2), (2,2) | [(1,1,1), (1,3,1), (0,2,1), (2,2,1)] |
| 1 | [...] | (1,1,1) | No | (1,0) | [(1,3,1), (0,2,1), (2,2,1), (1,0,2)] |
| 2 | [...] | (1,3,1) | No | - | [(0,2,1), (2,2,1), (1,0,2)] |
| 3 | [...] | (0,2,1) | **Yes!** | - | Return 1 |

**2.4 Explanation:**

- From entrance (1,2), we can reach (0,2) in 1 step.
- (0,2) is at the top boundary and is not the entrance, so it's an exit.

**2.5 Return Result:**

We return 1, which is the number of steps to reach the nearest exit.

> **Note:** The key insight is to use BFS, which explores cells in order of distance from the start. The first boundary cell we reach (excluding the entrance) is guaranteed to be the nearest exit.

