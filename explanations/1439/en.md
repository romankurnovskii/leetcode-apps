## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a matrix with sorted rows, we need to find the kth smallest sum among all possible arrays formed by choosing exactly one element from each row.

**1.1 Constraints & Complexity:**

- **Input Size:** The matrix has at most 40 rows and 40 columns. k can be up to 200.
- **Time Complexity:** O(k * log k * m) where m is the number of rows - we merge rows m-1 times, each merge taking O(k * log k) time.
- **Space Complexity:** O(k) - we maintain at most k candidate sums at each step.
- **Edge Case:** If k = 1, return the sum of the first element of each row. If all rows have only one element, return the sum of those elements.

**1.2 High-level approach:**

The goal is to merge rows two at a time, keeping only the k smallest sums at each step. This reduces the problem to repeatedly finding k smallest pairs, similar to the "Find K Pairs with Smallest Sums" problem.

![Matrix sum merging visualization](https://assets.leetcode.com/static_assets/others/matrix-sum-merge.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Generate all possible sums (up to n^m combinations) and sort them to find the kth smallest. This is exponential and impractical.
- **Optimized Strategy:** Use a min-heap to merge rows incrementally, keeping only the k smallest sums at each step. This is O(k * log k * m) time.
- **Optimization:** By maintaining only k candidates and using a heap, we avoid generating all combinations and solve efficiently.

**1.4 Decomposition:**

1. Start with the first row as the initial candidate sums.
2. For each subsequent row, merge it with the current candidate sums using a min-heap.
3. The merge operation finds the k smallest pairs between current sums and the new row.
4. After processing all rows, return the kth element from the final list of sums.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `mat = [[1,3,11],[2,4,6]]`, `k = 5`

- Matrix: `[[1,3,11],[2,4,6]]`
- Initial sums: `res = [1, 3, 11]` (first row)
- Next row: `[2, 4, 6]`

**2.2 Start Checking:**

We merge the first row with the second row to find k smallest sums.

**2.3 Trace Walkthrough:**

| Step | Current sums | New row | Heap operations | k smallest pairs |
| ---- | ------------ | ------- | --------------- | ---------------- |
| 1    | [1,3,11]     | [2,4,6] | Push (1+2, 1, 2, 0) | Start building |
| 2    | -            | -       | Pop (3), Push (1+4) | [3] |
| 3    | -            | -       | Pop (4), Push (3+2) | [3,4] |
| 4    | -            | -       | Pop (5), Push (3+4) | [3,4,5] |
| 5    | -            | -       | Pop (6), Push (1+6) | [3,4,5,6] |
| 6    | -            | -       | Pop (7) | [3,4,5,6,7] |

**2.4 Increment and Loop:**

We process each row sequentially, merging it with the accumulated sums from previous rows.

**2.5 Return Result:**

The result is `7`, which is the 5th smallest sum. The first 5 smallest sums are: 3 (1+2), 4 (1+4), 5 (3+2), 6 (3+4), and 7 (1+6).

