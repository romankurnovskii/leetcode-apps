## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Input Size:** `2 <= n, m <= 100`, `1 <= k <= m`.
- **Time Complexity:** O(m * n + m log m) where m is the number of rows. We count soldiers in each row (O(m * n)), then sort (O(m log m)).
- **Space Complexity:** O(m) - we store strength and index for each row.
- **Edge Case:** If k = m, return all row indices. If all rows have the same strength, return the first k indices.

**1.2 High-level approach:**

The goal is to find the k weakest rows, where weakness is determined by the number of soldiers (1s) in the row, with row index as a tiebreaker. We calculate the strength (number of soldiers) for each row, sort by strength (and index as tiebreaker), and return the first k indices.

![Visualization showing a matrix with soldiers (1s) and civilians (0s), with rows sorted by strength from weakest to strongest]

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each row, count soldiers, then sort all rows. This is the same as the optimized approach.
- **Optimized Strategy:** Count soldiers for each row, store (strength, index) pairs, sort by strength then index, return first k indices.
- **Why it's better:** By storing (strength, index) pairs and sorting once, we efficiently find the k weakest rows in O(m log m) time after counting.

**1.4 Decomposition:**

1. For each row, count the number of soldiers (1s).
2. Store (strength, row_index) pairs in a list.
3. Sort the list by strength (ascending), then by index (ascending) as tiebreaker.
4. Extract the first k indices from the sorted list.
5. Return the list of k weakest row indices.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example:
```
mat = [[1,1,0,0,0],
       [1,1,1,1,0],
       [1,0,0,0,0],
       [1,1,0,0,0],
       [1,1,1,1,1]]
k = 3
```

**2.2 Start Checking:**

Calculate strength for each row.

**2.3 Trace Walkthrough:**

| Row | Row index | Soldiers count | Strength | (strength, index) |
|-----|-----------|----------------|----------|-------------------|
| [1,1,0,0,0] | 0 | 2 | 2 | (2, 0) |
| [1,1,1,1,0] | 1 | 4 | 4 | (4, 1) |
| [1,0,0,0,0] | 2 | 1 | 1 | (1, 2) |
| [1,1,0,0,0] | 3 | 2 | 2 | (2, 3) |
| [1,1,1,1,1] | 4 | 5 | 5 | (5, 4) |

After sorting by (strength, index):
- (1, 2) - weakest
- (2, 0) - second weakest
- (2, 3) - third weakest (tie broken by index)
- (4, 1)
- (5, 4)

**2.4 Increment and Loop:**

Extract first k = 3 indices: [2, 0, 3]

**2.5 Return Result:**

Return `res = [2, 0, 3]` - the indices of the 3 weakest rows.

