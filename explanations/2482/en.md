## Explanation

### Strategy

**Constraints & Edge Cases**

* **Matrix Size:** The input is an m x n binary matrix where m and n can be up to 10^5, but m * n is at most 10^5. This means the matrix could be very wide or very tall.
* **Time Complexity:** We need O(m * n) time to process all elements, which is optimal since we must examine each cell at least once. **Time Complexity: O(m * n)**, **Space Complexity: O(m + n)** for storing row and column counts.
* **Edge Case:** If the matrix is all zeros or all ones, the calculation still works correctly.

**High-level approach**

The problem asks us to create a difference matrix where each cell `diff[i][j]` equals `onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]`.

Since `zerosRow[i] = n - onesRow[i]` and `zerosCol[j] = m - onesCol[j]`, we can simplify:
- `diff[i][j] = onesRow[i] + onesCol[j] - (n - onesRow[i]) - (m - onesCol[j])`
- `diff[i][j] = 2 * onesRow[i] + 2 * onesCol[j] - n - m`

However, the direct approach of counting ones first, then building the result is clearer.

**Brute force vs. optimized strategy**

* **Brute Force:** For each cell `(i, j)`, count ones in row i and column j separately. This would be O(m * n * (m + n)) time, which is too slow.
* **Optimized:** Count ones in each row and column once (O(m * n)), then build the result matrix using these precomputed values (O(m * n)). This is O(m * n) total time, which is optimal.

**Decomposition**

1. **Count Ones:** First pass through the matrix to count ones in each row and column.
2. **Calculate Zeros:** For each row i, zeros = n - onesRow[i]. For each column j, zeros = m - onesCol[j].
3. **Build Result:** For each cell `(i, j)`, compute `onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]`.

### Steps

1. **Initialization & Example Setup**
   Let's use `grid = [[0,1,1],[1,0,1],[0,0,1]]` as our example.
   - Initialize `onesRow = [0, 0, 0]` and `onesCol = [0, 0, 0]`.
   - Initialize `res` as a 3x3 matrix filled with zeros.

2. **Count Ones**
   Iterate through the matrix and count ones:
   - Row 0: `onesRow[0] = 2` (two ones)
   - Row 1: `onesRow[1] = 2` (two ones)
   - Row 2: `onesRow[2] = 1` (one one)
   - Column 0: `onesCol[0] = 1` (one one)
   - Column 1: `onesCol[1] = 1` (one one)
   - Column 2: `onesCol[2] = 3` (three ones)

3. **Build Result Matrix**
   For each cell `(i, j)`:
   - Calculate `zerosRow[i] = n - onesRow[i]`
   - Calculate `zerosCol[j] = m - onesCol[j]`
   - Set `res[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]`

4. **Trace Walkthrough**

| Cell (i,j) | onesRow[i] | onesCol[j] | zerosRow[i] | zerosCol[j] | Calculation | Result |
|------------|------------|------------|-------------|-------------|-------------|--------|
| (0,0)      | 2          | 1          | 1           | 2           | 2+1-1-2     | 0      |
| (0,1)      | 2          | 1          | 1           | 2           | 2+1-1-2     | 0      |
| (0,2)      | 2          | 3          | 1           | 0           | 2+3-1-0     | 4      |
| (1,0)      | 2          | 1          | 1           | 2           | 2+1-1-2     | 0      |
| (1,1)      | 2          | 1          | 1           | 2           | 2+1-1-2     | 0      |
| (1,2)      | 2          | 3          | 1           | 0           | 2+3-1-0     | 4      |
| (2,0)      | 1          | 1          | 2           | 2           | 1+1-2-2     | -2     |
| (2,1)      | 1          | 1          | 2           | 2           | 1+1-2-2     | -2     |
| (2,2)      | 1          | 3          | 2           | 0           | 1+3-2-0     | 2      |

5. **Return Result**
   Return the completed `res` matrix: `[[0,0,4],[0,0,4],[-2,-2,2]]`.
