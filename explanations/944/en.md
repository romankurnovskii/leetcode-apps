## Explanation

### Strategy (The "Why")

**Restate the problem:** We are given an array of strings, all of the same length. When arranged in a grid (one string per row), we need to count how many columns are not sorted lexicographically (in non-decreasing order).

**1.1 Constraints & Complexity:**

- **Input Size:** The number of strings n can be up to 100, and each string length m can be up to 1000.
- **Time Complexity:** O(n * m) - we need to check each column, and for each column, we check all rows to see if it's sorted.
- **Space Complexity:** O(1) - we only use a constant amount of extra space to track the result.
- **Edge Case:** If all columns are sorted, we return 0. If there's only one string, all columns are trivially sorted.

**1.2 High-level approach:**

The goal is to check each column of the grid to see if it's sorted lexicographically (each character is greater than or equal to the character above it). We count how many columns fail this check.

![Column sorting visualization](https://assets.leetcode.com/static_assets/others/column-sorting.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** This is already the optimal approach - we must check each column and each row in that column to determine if it's sorted.
- **Optimized Strategy:** Iterate through each column, and for each column, check if any row violates the sorted order (current character < previous character). If we find a violation, we can immediately mark that column as unsorted and move to the next column. This is O(n * m) time.
- **Optimization:** By breaking early when we find a violation in a column, we avoid unnecessary comparisons, though the worst-case complexity remains the same.

**1.4 Decomposition:**

1. Get the dimensions: number of strings (rows) n and string length (columns) m.
2. For each column from 0 to m-1:
   - Check if the column is sorted by comparing each row with the previous row.
   - If we find any row where the character is less than the character in the previous row, the column is not sorted.
   - Increment the result counter for each unsorted column.
3. Return the total count of unsorted columns.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `strs = ["cba", "daf", "ghi"]`

- Number of rows n = 3, number of columns m = 3
- Grid arrangement:
  ```
  c b a
  d a f
  g h i
  ```
- Result `res = 0`

**2.2 Start Checking:**

We iterate through each column and check if it's sorted.

**2.3 Trace Walkthrough:**

| Column | Row 0 | Row 1 | Row 2 | Is Sorted? | Action | res |
|--------|-------|-------|-------|------------|--------|-----|
| 0 | 'c' | 'd' | 'g' | Yes (c < d < g) | Continue | 0 |
| 1 | 'b' | 'a' | 'h' | No (b > a) | Increment res | 1 |
| 2 | 'a' | 'f' | 'i' | Yes (a < f < i) | Continue | 1 |

**2.4 Increment and Loop:**

After checking each column, we move to the next column. If we find a violation (current character < previous character), we immediately break from the inner loop and move to the next column.

**2.5 Return Result:**

The result is 1, which means we need to delete 1 column (column 1) because it's not sorted lexicographically.

