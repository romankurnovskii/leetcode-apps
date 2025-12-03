# Problem 240: Search a 2D Matrix II
**Difficulty:** Medium  
**Link:** https://leetcode.com/problems/search-a-2d-matrix-ii/

## Explanation

### Strategy (The "Why")

The problem asks us to search for a target value in a 2D matrix where each row is sorted left-to-right and each column is sorted top-to-bottom.

**1.1 Constraints & Complexity:**

- **Input Constraints:** Matrix dimensions are $1 \leq m, n \leq 300$, with values in $[-10^9, 10^9]$.
- **Time Complexity:** $O(m + n)$ - We start from top-right and move at most $m$ steps down and $n$ steps left.
- **Space Complexity:** $O(1)$ - We only use constant extra space for pointers.
- **Edge Case:** Empty matrix or target not found.

**1.2 High-level approach:**

The goal is to efficiently search the sorted matrix. We start from the top-right corner and eliminate either a row or column at each step based on the comparison with the target.

![Search 2D Matrix](https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check every cell in the matrix. This takes $O(m \times n)$ time.
- **Optimized (Top-Right Search):** Start from top-right corner. If current value > target, move left (eliminate column). If current value < target, move down (eliminate row). This takes $O(m + n)$ time.
- **Emphasize the optimization:** By starting at the top-right, we can eliminate an entire row or column at each step, reducing search space efficiently.

**1.4 Decomposition:**

1. **Initialize Position:** Start at top-right corner `(row=0, col=n-1)`.
2. **Compare and Move:** If current value equals target, return `True`. If greater, move left. If smaller, move down.
3. **Boundary Check:** Continue until we go out of bounds or find the target.
4. **Return Result:** Return `False` if target not found.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's trace through an example: `matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]`, `target = 5`.

Start at `(row=0, col=4)` with value `15`.

**2.2 Start Searching:**

Compare `15` with `target = 5`.

**2.3 Trace Walkthrough:**

| Step | row | col | matrix[row][col] | Compare | Action |
|------|-----|-----|------------------|---------|--------|
| 1 | 0 | 4 | 15 | 15 > 5 | Move left (col=3) |
| 2 | 0 | 3 | 11 | 11 > 5 | Move left (col=2) |
| 3 | 0 | 2 | 7 | 7 > 5 | Move left (col=1) |
| 4 | 0 | 1 | 4 | 4 < 5 | Move down (row=1) |
| 5 | 1 | 1 | 5 | 5 == 5 | **Found!** |

**2.4 Search Complete:**

Target `5` found at position `(1, 1)`.

**2.5 Return Result:**

The function returns `True`.

> **Note:** Starting from top-right (or bottom-left) is key because it allows us to eliminate either a row or column at each step, unlike starting from top-left or bottom-right.

