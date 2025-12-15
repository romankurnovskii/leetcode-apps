## Explanation

### Strategy

**Restate the problem**  
Construct a non-negative matrix that matches given row sums and column sums.

**1.1 Constraints & Complexity**  
- **Input Size:** up to 500 rows/cols.  
- **Time Complexity:** O(m*n) greedy fill.  
- **Space Complexity:** O(m*n) for the output matrix.  
- **Edge Case:** Trivial 1x1 matrix equals the shared sum.

**1.2 High-level approach**  
Greedy: at cell (i,j), place `min(rowSum[i], colSum[j])`, then decrement both sums; proceed row by row.  
![Greedy fill consuming row/col budgets](https://assets.leetcode.com/static_assets/public/images/LeetCode_logo.png)

**1.3 Brute force vs. optimized strategy**  
- **Brute Force:** Search all matrices satisfying sums — exponential.  
- **Optimized:** Greedy works because any feasible solution can allocate the minimal remaining budget without violating totals.

**1.4 Decomposition**  
1. Initialize `res` with zeros.  
2. For each cell `(i,j)`:  
   - `val = min(rowSum[i], colSum[j])`  
   - Set `res[i][j] = val`, update rowSum/colSum.  
3. Continue until all cells processed.  
4. Return `res`.

### Steps

**2.1 Initialization & Example Setup**  
Example: `rowSum=[3,8]`, `colSum=[4,7]`, res all zeros.

**2.2 Start Checking**  
At (0,0): min(3,4)=3 → res[0][0]=3; rowSum=[0,8], colSum=[1,7].

**2.3 Trace Walkthrough**  
| Cell | rowSum before | colSum before | placed | rowSum after | colSum after |
|------|---------------|---------------|--------|--------------|--------------|
| (0,0)| 3             | 4             | 3      | 0            | 1            |
| (0,1)| 0             | 7             | 0      | 0            | 7            |
| (1,0)| 8             | 1             | 1      | 7            | 0            |
| (1,1)| 7             | 7             | 7      | 0            | 0            |

**2.4 Increment and Loop**  
Proceed left-to-right, top-to-bottom.

**2.5 Return Result**  
Matrix satisfies all row/column sums.

