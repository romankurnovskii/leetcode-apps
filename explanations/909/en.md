## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**
- **Input Size:** `2 <= n <= 20`, board is n×n.
- **Time Complexity:** O(n²) - BFS through board squares.
- **Space Complexity:** O(n²) - visited set and queue.
- **Edge Case:** No path to n², return -1.

**1.2 High-level approach:**
The goal is to find the minimum dice rolls to reach square n². We use BFS, where each move can advance 1-6 squares, and we must follow snakes/ladders if encountered.

**1.3 Brute force vs. optimized strategy:**
- **Brute Force:** Try all paths - exponential time.
- **Optimized Strategy:** BFS finds shortest path - polynomial time.

**1.4 Decomposition:**
1. Convert square numbers to board coordinates (Boustrophedon style).
2. Use BFS starting from square 1.
3. For each square, try moves 1-6.
4. If destination has snake/ladder, follow it.
5. Track minimum moves to reach n².

### Steps (The "How")

**2.1 Initialization & Example Setup:**
Let's use a 6×6 board. Square 1 is at (5,0). Initialize queue with (1, 0), visited = {1}.

**2.2 Start Checking:**
We perform BFS through possible moves.

**2.3 Trace Walkthrough:**

| Square | Moves | Next Squares | Snakes/Ladders | New Square |
|--------|-------|--------------|----------------|------------|
| 1 | 0 | 2-7 | 2->15 | 15 |
| 15 | 1 | 16-21 | - | 16,17,18,19,20,21 |
| ... | ... | ... | ... | ... |
| 36 | 4 | - | - | Goal! |

**2.4 Increment and Loop:**
After each move, we increment move count and continue.

**2.5 Return Result:**
Return `res = 4`, the minimum dice rolls needed.

