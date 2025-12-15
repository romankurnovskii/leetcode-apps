## Explanation

### Strategy

**Restate the problem**  
For each cell `(i,j)` in a binary matrix, compute `onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]`.

**1.1 Constraints & Complexity**  
- **Input Size:** `1 <= m*n <= 1e5`.  
- **Time Complexity:** O(m*n) to count and build output.  
- **Space Complexity:** O(m + n) for row/col counts.  
- **Edge Case:** Single cell matrix.

**1.2 High-level approach**  
Precompute ones per row and column, derive zeros from lengths, then fill the answer.  
![Row/column accumulation](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** For each cell, scan its row and column — O(m*n*(m+n)).  
- **Optimized:** Precompute counts once — O(m*n).

**1.4 Decomposition**  
1. Count `onesRow` for each row and `onesCol` for each column.  
2. Derive `zerosRow[i] = n - onesRow[i]`, `zerosCol[j] = m - onesCol[j]`.  
3. For each cell, compute the formula and store in `res`.  
4. Return `res`.

### Steps

**2.1 Initialization & Example Setup**  
Example: `grid = [[0,1,1],[1,0,1],[0,0,1]]`.

**2.2 Start Checking**  
Compute `onesRow = [2,2,1]`, `onesCol = [1,1,3]`.

**2.3 Trace Walkthrough**  
| Cell (i,j) | onesRow[i] | onesCol[j] | zerosRow[i] | zerosCol[j] | diff |
|------------|------------|------------|-------------|-------------|------|
| (0,0)      | 2          | 1          | 1           | 2           | 0    |
| (0,1)      | 2          | 1          | 1           | 2           | 0    |
| (0,2)      | 2          | 3          | 1           | 0           | 4    |
| ...        | ...        | ...        | ...         | ...         | ...  |

**2.4 Increment and Loop**  
Fill every cell using the precomputed counts.

**2.5 Return Result**  
Produces `[[0,0,4],[0,0,4],[-2,-2,2]]` for the example.
## Explanation

### Strategy

**Restate the problem**

We are given a binary matrix and need to create a difference matrix where each cell `diff[i][j]` is calculated as: ones in row i + ones in column j - zeros in row i - zeros in column j.

**1.1 Constraints & Complexity**

- **Input Size:** The matrix can have up to 10^5 rows and columns, with total cells up to 10^5.
- **Time Complexity:** O(m*n) - We need to traverse the matrix twice: once to count ones in rows and columns, and once to build the result matrix.
- **Space Complexity:** O(m + n) - We store arrays for row and column counts.
- **Edge Case:** Empty matrix or single cell matrix are handled naturally by the algorithm.

**1.2 High-level approach**

The goal is to compute the difference matrix efficiently by precomputing row and column statistics. Instead of recalculating counts for each cell, we count ones in each row and column once, then use these counts to compute each cell's value.

![Matrix showing row and column counts with difference calculation](https://assets.leetcode.com/uploads/2022/11/06/image-20221106171729-5.png)

**1.3 Brute force vs. optimized strategy**

- **Brute Force:** For each cell (i, j), count ones and zeros in row i and column j separately. This results in O(m*n*(m+n)) time complexity, which is inefficient.
- **Optimized Strategy:** Precompute ones count for all rows and columns in O(m*n) time, then compute each cell in O(1) time using the precomputed values. Total time is O(m*n).
- **Why optimized is better:** We avoid redundant calculations by reusing row and column statistics across all cells in the same row or column.

**1.4 Decomposition**

1. **Count Row Statistics:** Traverse the matrix once to count the number of ones in each row.
2. **Count Column Statistics:** During the same traversal, count the number of ones in each column.
3. **Calculate Zeros:** For each row, zeros = total columns - ones. For each column, zeros = total rows - ones.
4. **Build Result Matrix:** For each cell (i, j), compute diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j].

### Steps

**2.1 Initialization & Example Setup**

Let's use the example: `grid = [[0,1,1],[1,0,1],[0,0,1]]`

- Matrix dimensions: 3 rows × 3 columns
- Initialize `ones_row = [0, 0, 0]` and `ones_col = [0, 0, 0]`

**2.2 Start Counting**

Traverse the matrix to count ones:
- Row 0: [0,1,1] → ones_row[0] = 2
- Row 1: [1,0,1] → ones_row[1] = 2
- Row 2: [0,0,1] → ones_row[2] = 1

- Column 0: [0,1,0] → ones_col[0] = 1
- Column 1: [1,0,0] → ones_col[1] = 1
- Column 2: [1,1,1] → ones_col[2] = 3

**2.3 Trace Walkthrough**

| Cell (i,j) | ones_row[i] | ones_col[j] | zeros_row[i] | zeros_col[j] | diff[i][j] |
|------------|-------------|-------------|--------------|--------------|------------|
| (0,0) | 2 | 1 | 1 | 2 | 2+1-1-2 = 0 |
| (0,1) | 2 | 1 | 1 | 2 | 2+1-1-2 = 0 |
| (0,2) | 2 | 3 | 1 | 0 | 2+3-1-0 = 4 |
| (1,0) | 2 | 1 | 1 | 2 | 2+1-1-2 = 0 |
| (1,1) | 2 | 1 | 1 | 2 | 2+1-1-2 = 0 |
| (1,2) | 2 | 3 | 1 | 0 | 2+3-1-0 = 4 |
| (2,0) | 1 | 1 | 2 | 2 | 1+1-2-2 = -2 |
| (2,1) | 1 | 1 | 2 | 2 | 1+1-2-2 = -2 |
| (2,2) | 1 | 3 | 2 | 0 | 1+3-2-0 = 2 |

**2.4 Build Result**

Create result matrix `res` with dimensions 3×3 and fill each cell using the formula.

**2.5 Return Result**

Return `[[0,0,4],[0,0,4],[-2,-2,2]]`, which matches the expected output.
