## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count the number of negative numbers in a matrix that is sorted in non-increasing order both row-wise and column-wise. This means values decrease as we move right in any row, and also decrease as we move down in any column.

**1.1 Constraints & Complexity:**

- **Input Size:** The matrix has dimensions m × n, where 1 ≤ m, n ≤ 100, and each element is between -100 and 100.
- **Time Complexity:** O(m + n) - we traverse at most m + n steps by moving either up or right at each step, never revisiting any position.
- **Space Complexity:** O(1) - we only use a constant amount of extra space for variables.
- **Edge Case:** If all elements are positive, we traverse only the last row or first column. If all elements are negative, we traverse only the first row or last column.

**1.2 High-level approach:**

The goal is to efficiently count negative numbers by leveraging the sorted property of the matrix. The negative numbers form a "staircase" pattern where all negative values are contiguous in the bottom-right region.

![Staircase pattern of negative numbers](https://assets.leetcode.com/static_assets/others/matrix-staircase.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Iterate through every cell in the matrix and count negatives. This requires O(m × n) time as we visit every element.
- **Optimized Strategy:** Start from a corner (bottom-left or top-right) and trace the outline of the staircase. At each step, we either move up or right, eliminating entire rows or columns from consideration. This is O(m + n) time.
- **Optimization:** By using the sorted property, we can eliminate entire rows or columns in a single comparison, reducing the time complexity from O(m × n) to O(m + n).

**1.4 Decomposition:**

1. Start from the bottom-left corner of the matrix.
2. Check if the current element is negative.
3. If negative, all elements to the right in the current row are also negative (due to row-wise sorting), so count them all and move up.
4. If non-negative, all elements below in the current column are also non-negative (due to column-wise sorting), so move right.
5. Continue until we've processed all rows or columns.
6. Return the total count of negative numbers.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]`

- Matrix dimensions: `m = 4`, `n = 4`
- Start position: `r = 3` (bottom row), `c = 0` (leftmost column)
- Result counter: `res = 0`

**2.2 Start Checking:**

We begin at the bottom-left corner `grid[3][0] = -1`, which is negative.

**2.3 Trace Walkthrough:**

| Step | r   | c   | grid[r][c] | Is Negative? | Action                          | res |
| ---- | --- | --- | ---------- | ------------ | ------------------------------- | --- |
| 1    | 3   | 0   | -1         | Yes          | Count 4 negatives, move up       | 4   |
| 2    | 2   | 0   | 1          | No           | Move right                      | 4   |
| 3    | 2   | 1   | 1          | No           | Move right                      | 4   |
| 4    | 2   | 2   | -1         | Yes          | Count 2 negatives, move up      | 6   |
| 5    | 1   | 2   | 1          | No           | Move right                      | 6   |
| 6    | 1   | 3   | -1         | Yes          | Count 1 negative, move up       | 7   |
| 7    | 0   | 3   | -1         | Yes          | Count 1 negative, move up       | 8   |

**2.4 Increment and Loop:**

After each step, we either:
- Decrement `r` (move up) when we find a negative, counting all negatives to the right in that row
- Increment `c` (move right) when we find a non-negative, skipping all non-negatives below in that column

We continue until `r < 0` or `c >= n`.

**2.5 Return Result:**

The result is 8, which is the total number of negative numbers in the matrix.

