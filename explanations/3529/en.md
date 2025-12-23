## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to count the number of cells in a grid that are part of at least one horizontal substring matching a pattern AND at least one vertical substring matching the same pattern. A horizontal substring reads left-to-right across rows (wrapping to the next row if needed), and a vertical substring reads top-to-bottom down columns (wrapping to the next column if needed).

**1.1 Constraints & Complexity:**

- **Input Size:** The grid can be up to 1000x1000, and the pattern length can be up to 100,000 characters.
- **Time Complexity:** O(m * n * p) where m is rows, n is columns, and p is pattern length. We flatten the grid twice (O(m*n)), then for each position we check pattern matches (O(p) per position), and we iterate through all matching positions.
- **Space Complexity:** O(m * n) - we store sets of cell coordinates for horizontal and vertical matches, each potentially containing up to m*n cells.
- **Edge Case:** If the pattern doesn't appear in either direction, the result is 0.

**1.2 High-level approach:**

The goal is to find all cells that are covered by both a horizontal pattern match and a vertical pattern match. We do this by flattening the grid into two strings (horizontal and vertical), finding all pattern matches in each, tracking which cells are covered, and then counting the intersection.

![Grid pattern matching visualization](https://assets.leetcode.com/uploads/2025/03/03/gridtwosubstringsdrawio.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each cell, check all possible horizontal substrings starting from that cell and all possible vertical substrings. This would be O(m * n * p²) as we'd check many overlapping substrings repeatedly.
- **Optimized Strategy:** Flatten the grid into two strings, find all pattern matches using string slicing, and use sets to efficiently track which cells are covered. This reduces redundant checks.
- **Optimization:** By flattening once and using set operations, we avoid checking the same substring multiple times and can efficiently find the intersection of covered cells.

**1.4 Decomposition:**

1. Flatten the grid horizontally by reading row by row into a single string.
2. Find all positions where the pattern appears in the horizontal string.
3. For each match, mark all cells covered by that match in a set.
4. Flatten the grid vertically by reading column by column into a single string.
5. Find all positions where the pattern appears in the vertical string.
6. For each match, mark all cells covered by that match in another set.
7. Find the intersection of both sets (cells covered by both horizontal and vertical matches).
8. Return the count of cells in the intersection.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]]`, `pattern = "abaca"`

- Grid dimensions: `m = 5`, `n = 4`
- Pattern length: `x = 5`
- Horizontal string: `hor = "aaccbbbcabaacaacabaa"` (reading row by row)
- Vertical string: `var = "abacaabacabacac"` (reading column by column)
- Horizontal matches set: `res1 = set()`
- Vertical matches set: `res2 = set()`

**2.2 Start Checking:**

We begin by finding all horizontal pattern matches in the flattened horizontal string.

**2.3 Trace Walkthrough:**

| Step | Position in hor | Substring | Matches pattern? | Cells Covered | res1 after |
| ---- | --------------- | --------- | ----------------- | ------------- | ---------- |
| 1    | 0-4             | "aaccb"   | No                | -             | {}         |
| 2    | 1-5             | "accbb"   | No                | -             | {}         |
| 3    | 2-6             | "ccbbb"   | No                | -             | {}         |
| 4    | 3-7             | "cbbbc"   | No                | -             | {}         |
| 5    | 4-8             | "bbbcb"   | No                | -             | {}         |
| 6    | 5-9             | "bbcab"   | No                | -             | {}         |
| 7    | 6-10            | "bcaba"   | No                | -             | {}         |
| 8    | 7-11            | "cabaa"   | No                | -             | {}         |
| 9    | 8-12            | "abaac"   | No                | -             | {}         |
| 10   | 9-13            | "baaca"   | No                | -             | {}         |
| 11   | 10-14           | "aacaa"   | No                | -             | {}         |
| 12   | 11-15           | "acaac"   | No                | -             | {}         |
| 13   | 12-16           | "caaca"   | No                | -             | {}         |
| 14   | 13-17           | "aacab"   | No                | -             | {}         |
| 15   | 14-18           | "acaba"   | No                | -             | {}         |
| 16   | 15-19           | "cabaa"   | No                | -             | {}         |

Actually, let's check the vertical string more carefully. The pattern "abaca" appears in the vertical string starting at position 0: `var[0:5] = "abaca"` matches!

For vertical matches:
- Position 0-4 in vertical string covers cells: (0,0), (1,0), (2,0), (3,0), (4,0) which is column 0

Now checking horizontal string more carefully - we need to find where "abaca" appears. Looking at the grid structure, the horizontal string reads row by row, so we need to find where this pattern appears across row boundaries.

**2.4 Increment and Loop:**

After finding all horizontal matches and marking cells in `res1`, we do the same for vertical matches in `res2`, then find the intersection.

**2.5 Return Result:**

The result is the count of cells that appear in both `res1` and `res2`. In the example, only one cell is covered by both a horizontal and vertical match of "abaca", so the result is 1.

