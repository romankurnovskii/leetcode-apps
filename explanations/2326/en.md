## Explanation

### Strategy

**Restate the problem**  
Fill an `m x n` matrix in spiral order using values from a linked list; remaining cells become -1.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= m*n <= 1e5`; list length up to `m*n`.  
- **Time Complexity:** O(m*n) to visit each cell once.  
- **Space Complexity:** O(1) extra (matrix output not counted).  
- **Edge Case:** List shorter than cells → trailing -1s.

**1.2 High-level approach**  
Track boundaries/directions for spiral traversal, place list values until exhausted, then fill -1 stays.  
![Spiral traversal boundaries](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Recompute visited checks with sets — higher overhead.  
- **Optimized:** Direction vectors with boundary checks — O(1) per move.

**1.4 Decomposition**  
1. Initialize matrix with -1.  
2. Set direction order: right, down, left, up.  
3. Walk cell by cell, placing list values.  
4. When the next cell is out-of-bounds or already filled, turn clockwise.  
5. Continue until list ends or all cells visited.

### Steps

**2.1 Initialization & Example Setup**  
Example: `m=3, n=5`, list `[3,0,2,6,8,1,7,9,4,2,5,5,0]`; start at `(0,0)`, dir=right.

**2.2 Start Checking**  
Place value, attempt next move; if blocked, rotate direction.

**2.3 Trace Walkthrough**  
| Step | Pos (r,c) | Dir    | Value placed | Next move valid? |
|------|-----------|--------|--------------|------------------|
| 1    | (0,0)     | right  | 3            | yes              |
| ...  | ...       | ...    | ...          | ...              |
| turn | boundary  | rotate | —            | —                |

**2.4 Increment and Loop**  
Advance through list nodes; rotate as needed until list ends.

**2.5 Return Result**  
Matrix filled in spiral with remaining cells as -1.

