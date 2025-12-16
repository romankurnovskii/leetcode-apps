## Explanation

### Strategy

**Constraints & Edge Cases**

* **Matrix Size:** rowSum and colSum have length 1-500, with values up to 10^8. The sum of rowSum equals sum of colSum (guaranteed).
* **Time Complexity:** We iterate through each cell once, taking the minimum of rowSum[i] and colSum[j]. **Time Complexity: O(m * n)**, **Space Complexity: O(m * n)** for the result matrix.
* **Edge Case:** If all row and column sums are 0, return a zero matrix.

**High-level approach**

The problem asks us to construct a matrix given row and column sums. We use a greedy approach: for each cell, place the minimum of the remaining row sum and column sum, then update both.

**Brute force vs. optimized strategy**

* **Brute Force:** Try all possible matrix configurations and check if they satisfy the constraints. This would be exponential.
* **Optimized:** Greedy approach - for each cell (i,j), place `min(rowSum[i], colSum[j])`, then subtract this value from both rowSum[i] and colSum[j]. This ensures we always make progress and never exceed constraints.

**Decomposition**

1. **Initialize Matrix:** Create an m x n matrix filled with zeros.
2. **Greedy Placement:** For each cell (i,j), place the minimum of rowSum[i] and colSum[j].
3. **Update Sums:** Subtract the placed value from both rowSum[i] and colSum[j].

### Steps

1. **Initialization & Example Setup**
   Let's use `rowSum = [3,8]`, `colSum = [4,7]` as our example.
   - Initialize `res = [[0,0],[0,0]]`.
   - m = 2, n = 2.

2. **Process Cells**
   For cell (0,0):
   - `val = min(rowSum[0], colSum[0]) = min(3, 4) = 3`.
   - `res[0][0] = 3`.
   - `rowSum[0] -= 3` → `rowSum = [0, 8]`.
   - `colSum[0] -= 3` → `colSum = [1, 7]`.

3. **Trace Walkthrough**

| Cell (i,j) | rowSum[i] | colSum[j] | val = min(...) | res[i][j] | Updated rowSum | Updated colSum |
|------------|-----------|-----------|----------------|-----------|----------------|----------------|
| (0,0)      | 3         | 4         | 3              | 3         | [0, 8]         | [1, 7]         |
| (0,1)      | 0         | 7         | 0              | 0         | [0, 8]         | [1, 7]         |
| (1,0)      | 8         | 1         | 1              | 1         | [0, 7]         | [0, 7]         |
| (1,1)      | 7         | 7         | 7              | 7         | [0, 0]         | [0, 0]         |

4. **Result Matrix**
   `res = [[3,0],[1,7]]`
   - Row 0: 3 + 0 = 3 ✓
   - Row 1: 1 + 7 = 8 ✓
   - Col 0: 3 + 1 = 4 ✓
   - Col 1: 0 + 7 = 7 ✓

5. **Return Result**
   Return the constructed matrix.
