# Problem 52: N-Queens II
**Difficulty:** Hard  
**Link:** https://leetcode.com/problems/n-queens-ii/

## Explanation

### Strategy (The "Why")

The problem asks us to count the number of distinct solutions to the n-queens puzzle, where we place $n$ queens on an $n \times n$ chessboard such that no two queens attack each other. Queens can attack horizontally, vertically, and diagonally.

**1.1 Constraints & Complexity:**

- **Input Constraints:** $1 \leq n \leq 9$, so the board size is small and manageable.
- **Time Complexity:** $O(n!)$ - In the worst case, we explore all possible placements. However, with pruning (skipping invalid positions), the actual runtime is much better in practice. The backtracking algorithm prunes branches early when conflicts are detected.
- **Space Complexity:** $O(n)$ - We use sets to track occupied columns and diagonals, each storing at most $n$ elements. The recursion stack depth is at most $n$.
- **Edge Case:** When $n = 1$, there is exactly one solution (placing a single queen on the only square).

**1.2 High-level approach:**

The goal is to count all valid placements of $n$ queens on an $n \times n$ board where no two queens attack each other. We use backtracking: place queens row by row, and whenever we detect a conflict, we backtrack and try the next position.

![N-Queens puzzle visualization](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Generate all possible placements of $n$ queens (there are $n^n$ possibilities) and check if each is valid. This requires $O(n^n \cdot n^2)$ time to check all placements and validate each one, which is extremely inefficient.
- **Optimized (Backtracking with Pruning):** Place queens row by row, and immediately skip (prune) any position that conflicts with previously placed queens. We track occupied columns and diagonals using sets for $O(1)$ conflict checking. This dramatically reduces the search space.
- **Emphasize the optimization:** By checking conflicts immediately and backtracking early, we avoid exploring entire subtrees of invalid solutions, making the algorithm feasible even though the problem space is exponential.

**1.4 Decomposition:**

1. **Track Constraints:** Maintain sets to track which columns, main diagonals (row - col), and anti-diagonals (row + col) are occupied by queens.
2. **Row-by-Row Placement:** Place one queen per row, trying each column position.
3. **Conflict Detection:** Before placing a queen, check if the column or either diagonal is already occupied.
4. **Backtrack:** If a valid position is found, recurse to the next row. After exploring that branch, remove the queen and try the next column.
5. **Count Solutions:** When all $n$ rows have queens placed (base case), increment the solution counter.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: $n = 4$.

We want to count the number of ways to place 4 queens on a $4 \times 4$ board.

Initialize:
- `cols = {}` (empty set for occupied columns)
- `diag1 = {}` (empty set for main diagonals, keyed by `row - col`)
- `diag2 = {}` (empty set for anti-diagonals, keyed by `row + col`)
- `res = 0` (solution counter)

**2.2 Start Placing Queens:**

We begin at row 0 and try placing a queen in each column.

**2.3 Trace Walkthrough:**

The backtracking process for $n = 4$:

| Row | Column Attempted | Conflict Check | Action | State After Placement |
|-----|------------------|---------------|--------|----------------------|
| 0 | 0 | No conflict | Place queen | `cols={0}`, `diag1={0}`, `diag2={0}` |
| 1 | 0 | Column 0 occupied | Skip | - |
| 1 | 1 | Diag1: (1-1=0) occupied | Skip | - |
| 1 | 2 | No conflict | Place queen | `cols={0,2}`, `diag1={0,-1}`, `diag2={0,3}` |
| 2 | 0 | Column 0 occupied | Skip | - |
| 2 | 1 | Diag2: (2+1=3) occupied | Skip | - |
| 2 | 2 | Column 2 occupied | Skip | - |
| 2 | 3 | Diag1: (2-3=-1) occupied | Skip | - |
| 2 | - | All columns failed | Backtrack | Remove queen from row 1, col 2 |
| 1 | 3 | No conflict | Place queen | `cols={0,3}`, `diag1={0,-2}`, `diag2={0,4}` |
| 2 | 1 | No conflict | Place queen | `cols={0,3,1}`, `diag1={0,-2,1}`, `diag2={0,4,3}` |
| 3 | 0 | Column 0 occupied | Skip | - |
| 3 | 1 | Column 1 occupied | Skip | - |
| 3 | 2 | Diag1: (3-2=1) occupied | Skip | - |
| 3 | 3 | Column 3 occupied | Skip | - |
| 3 | - | All columns failed | Backtrack | Remove queen from row 2, col 1 |
| 2 | 2 | Diag2: (2+2=4) not occupied, but... | Continue search | ... |
| ... | ... | ... | ... | ... |
| 3 | 3 | All rows placed | **Solution found!** | `res = 1` |

**2.4 Backtracking Process:**

When we reach row $n$ (all queens placed), we increment `res`. Then we backtrack by removing the last placed queen and trying the next column. This continues until all possibilities are explored.

**2.5 Return Result:**

For $n = 4$, the algorithm finds 2 distinct solutions. The function returns `res = 2`.

> **Note:** The key insight is using `row - col` and `row + col` as unique identifiers for diagonals. All squares on the same main diagonal have the same `row - col` value, and all squares on the same anti-diagonal have the same `row + col` value.

