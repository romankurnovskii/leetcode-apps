## Explanation

### Strategy (The "Why")

Given an $m \times n$ integer matrix where each row is sorted in ascending order and the first integer of each row is greater than the last integer of the previous row, we need to determine if a target value exists in the matrix.

**1.1 Constraints & Complexity:**

- **Input Size:** The matrix dimensions $m \times n$ can be up to $100 \times 100$.
- **Value Range:** Matrix elements and target are between $-10^4$ and $10^4$.
- **Time Complexity:** $O(\log(m \times n))$ - We use binary search on the flattened matrix, which has $m \times n$ elements.
- **Space Complexity:** $O(1)$ - We only use a constant amount of extra space.
- **Edge Case:** If the matrix is empty, return false. If target is less than the first element or greater than the last element, return false.

**1.2 High-level approach:**

The goal is to search for a target in a sorted 2D matrix.

![Search 2D Matrix](https://assets.leetcode.com/uploads/2020/10/05/mat3.jpg)

Since the matrix is sorted both row-wise and column-wise (with the additional property that the last element of a row is less than the first element of the next row), we can treat it as a 1D sorted array and use binary search.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Search through every element in the matrix. This takes $O(m \times n)$ time.
- **Optimized Strategy (Binary Search):** Treat the matrix as a flattened 1D sorted array and use binary search. Convert 1D indices to 2D coordinates when needed. This takes $O(\log(m \times n))$ time.
- **Why it's better:** Binary search reduces the time complexity from $O(m \times n)$ to $O(\log(m \times n))$, which is a significant improvement for large matrices.

**1.4 Decomposition:**

1. Treat the matrix as a 1D sorted array with indices from $0$ to $m \times n - 1$.
2. Use binary search on this 1D array.
3. Convert the 1D index to 2D coordinates: `row = index // n`, `col = index % n`.
4. Compare the element at the calculated position with the target.
5. Return true if found, false otherwise.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: $matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]$, $target = 3$

We initialize:
- `left = 0`, `right = 11` (3×4 - 1)

**2.2 Start Binary Search:**

We begin searching in the middle.

**2.3 Trace Walkthrough:**

| Iteration | left | right | mid | row | col | matrix[row][col] | Comparison | Action |
|-----------|------|-------|-----|-----|-----|------------------|-----------|--------|
| 1 | 0 | 11 | 5 | 1 | 1 | 11 | $11 > 3$ | Set `right = 4` |
| 2 | 0 | 4 | 2 | 0 | 2 | 5 | $5 > 3$ | Set `right = 1` |
| 3 | 0 | 1 | 0 | 0 | 0 | 1 | $1 < 3$ | Set `left = 1` |
| 4 | 1 | 1 | 1 | 0 | 1 | 3 | $3 == 3$ | **Found!** |

**2.4 Coordinate Conversion:**

- Index 5: `row = 5 // 4 = 1`, `col = 5 % 4 = 1` → `matrix[1][1] = 11`
- Index 1: `row = 1 // 4 = 0`, `col = 1 % 4 = 1` → `matrix[0][1] = 3`

**2.5 Return Result:**

We return `True` because target 3 is found at `matrix[0][1]`.

> **Note:** The key insight is that the matrix's sorted property allows us to treat it as a 1D sorted array. The conversion between 1D and 2D indices is straightforward: `row = index // n` and `col = index % n`.

