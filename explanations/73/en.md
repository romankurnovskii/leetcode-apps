## 73. Set Matrix Zeroes [Medium]

https://leetcode.com/problems/set-matrix-zeroes

## Description
Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it [in place](https://en.wikipedia.org/wiki/In-place_algorithm).

**Examples**

```tex
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

**Constraints**
```tex
- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1
```

**Follow up:**
- A straightforward solution using `O(mn)` space is probably a bad idea.
- A simple improvement uses `O(m + n)` space, but still not the best solution.
- Could you devise a constant space solution?

## Explanation

### Strategy
Let's restate the problem: You're given a matrix where if any element is 0, you need to set its entire row and column to 0. The challenge is to do this in-place without using extra space.

This is a **matrix manipulation problem** that requires careful handling to avoid overwriting information we need later.

**What is given?** An m x n matrix that may contain zeros.

**What is being asked?** Set entire rows and columns to zero if they contain a zero element, doing this in-place.

**Constraints:** The matrix can be up to 200x200, with integer values ranging from -2³¹ to 2³¹-1.

**Edge cases:** 
- Matrix with no zeros
- Matrix with all zeros
- Matrix with zeros in first row/column
- Single row or column matrix

**High-level approach:**
The solution involves using the first row and first column as markers to track which rows and columns need to be set to zero, then applying the changes.

**Decomposition:**
1. **Use first row/column as markers**: Track which rows and columns contain zeros
2. **Handle first row/column separately**: Since they're used as markers, handle them specially
3. **Apply zeros**: Set entire rows and columns to zero based on the markers
4. **Clean up**: Handle the first row and column based on their original state

**Brute force vs. optimized strategy:**
- **Brute force**: Create a copy of the matrix and mark rows/columns. This takes O(mn) space.
- **Optimized**: Use the first row and column as markers. This takes O(1) space.

### Steps
Let's walk through the solution step by step using the first example: `matrix = [[1,1,1],[1,0,1],[1,1,1]]`

**Step 1: Check if first row/column should be zero**
- Check if first row contains any zeros: `[1,1,1]` - no zeros
- Check if first column contains any zeros: `[1,1,1]` - no zeros
- Set flags: `firstRowZero = false`, `firstColZero = false`

**Step 2: Use first row/column as markers**
- For each element `matrix[i][j]` where `i > 0` and `j > 0`:
  - If `matrix[i][j] == 0`:
    - Set `matrix[i][0] = 0` (mark row i)
    - Set `matrix[0][j] = 0` (mark column j)

**Step 3: Apply zeros based on markers**
- For each row `i` from 1 to m-1:
  - If `matrix[i][0] == 0`, set entire row i to zero
- For each column `j` from 1 to n-1:
  - If `matrix[0][j] == 0`, set entire column j to zero

**Step 4: Handle first row and column**
- If `firstRowZero`, set first row to zero
- If `firstColZero`, set first column to zero

**Why this works:**
By using the first row and column as markers, we can track which rows and columns need to be zeroed without using extra space. The key insight is that we can safely overwrite the first row and column since we've already recorded their original state.

> **Note:** The key insight is that we can use the first row and column as markers to track which rows and columns contain zeros, allowing us to solve the problem in O(1) space.

**Time Complexity:** O(mn) - we visit each element at most twice  
**Space Complexity:** O(1) - we only use a constant amount of extra space for flags
