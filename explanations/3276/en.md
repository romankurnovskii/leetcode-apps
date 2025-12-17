## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to select one or more cells from a grid such that no two selected cells are in the same row, and all selected values are unique. We want to maximize the sum of selected cell values.

**1.1 Constraints & Complexity:**

- **Input Size:** Grid dimensions are at most 10x10, and values are between 1 and 100. The small size allows for exponential solutions.
- **Time Complexity:** O(V * R^V) where V is the number of unique values and R is the number of rows. With memoization, this is more efficient in practice.
- **Space Complexity:** O(V * 2^R) for memoization - we store states based on which rows are used and which values we've processed.
- **Edge Case:** If all values in a row are the same, we can only select one value from that row.

**1.2 High-level approach:**

The goal is to use dynamic programming with memoization. We process values in descending order (greedy approach), and for each value, we decide which row to select it from (if any), ensuring we don't violate constraints.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Try all combinations of cells, checking constraints. This is exponential and inefficient.
- **Optimized Strategy:** Use DFS with memoization, processing values in descending order. Track which rows have been used and which values we've processed. This reduces redundant computations significantly.
- **Optimization:** Memoization based on (row_set, value_idx) avoids recomputing the same subproblems, and processing in descending order ensures we consider optimal choices first.

**1.4 Decomposition:**

1. Collect all unique values from the grid and sort them in descending order.
2. Create a mapping from each value to the list of rows containing it.
3. Use DFS with memoization: for each value, try selecting it from each available row, or skip it.
4. Track used rows to ensure no two cells from the same row are selected.
5. Return the maximum score achievable.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example input: `grid = [[1,2,3],[4,3,2],[1,1,1]]`

- Unique values (descending): [4, 3, 2, 1]
- Value to rows mapping: {4: [1], 3: [0,1], 2: [0,1], 1: [0,2]}

**2.2 Start DFS:**

We process values in descending order, making optimal choices.

**2.3 Trace Walkthrough:**

| Value | Available Rows | Decision | Used Rows | Score |
|-------|----------------|----------|-----------|-------|
| 4 | [1] | Select from row 1 | {1} | 4 |
| 3 | [0,1] | Row 1 used, select from row 0 | {0,1} | 4+3=7 |
| 2 | [0,1] | Both rows used, skip | {0,1} | 7 |
| 1 | [0,2] | Row 0 used, select from row 2 | {0,1,2} | 7+1=8 |

**2.4 Increment and Loop:**

The DFS explores all possibilities and returns the maximum score.

**2.5 Return Result:**

The maximum score is 8, achieved by selecting values 4 (row 1), 3 (row 0), and 1 (row 2). This matches the example output.

