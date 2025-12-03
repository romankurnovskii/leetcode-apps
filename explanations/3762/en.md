## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

- **Constraints:** $1 \leq n \leq 4 \times 10^4$ elements, $1 \leq k \leq 10^9$, $1 \leq q \leq 4 \times 10^4$ queries.
- **Time Complexity:** $O(n + q \times m \log m)$ where $m$ is the average subarray length. For each query, we extract and sort the subarray.
- **Space Complexity:** $O(n)$ for the validity check array and $O(m)$ for each query's subarray.
- **Edge Case:** If a subarray cannot be equalized (elements have different modulo $k$), return $-1$ for that query.

**1.2 High-level approach:**

The goal is to find the minimum operations to make all elements in a subarray equal, where each operation can add or subtract $k$. Key insight: elements can only be equalized if they all have the same remainder modulo $k$. The minimum operations is achieved by converting all elements to the median value (after dividing by $k$).

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each query, try all possible target values and calculate operations. This is exponential.
- **Optimized Strategy:** Precompute validity (check if all elements have same modulo $k$). For valid queries, extract subarray, divide by $k$, find median, and calculate sum of absolute differences from median. This is $O(q \times m \log m)$ where $m$ is subarray length.
- **Why optimized is better:** The median property minimizes sum of absolute differences, and precomputing validity avoids unnecessary processing.

**1.4 Decomposition:**

1. Precompute `last_match_idx`: for each index, find the rightmost index where all elements from current index have the same modulo $k$.
2. For each query, check validity using `last_match_idx`.
3. If valid, extract subarray and divide each element by $k$.
4. Sort the normalized subarray and find the median.
5. Calculate sum of absolute differences from median.
6. Return the result (or $-1$ if invalid).

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `nums = [1,4,7]`, `k = 3`, `queries = [[0,1],[0,2]]`

We precompute validity: all elements have remainder 1 modulo 3, so both queries are valid.

**2.2 Start Checking:**

For each query, we check validity and calculate operations.

**2.3 Trace Walkthrough:**

**Query 1: [0,1]**
- Subarray: `[1,4]`
- Normalized (divide by k): `[0,1]` (since 1//3=0, 4//3=1)
- Sorted: `[0,1]`
- Median: `0` (or `1`, both work)
- Operations: `|0-0| + |1-0| = 1`

**Query 2: [0,2]**
- Subarray: `[1,4,7]`
- Normalized: `[0,1,2]`
- Sorted: `[0,1,2]`
- Median: `1`
- Operations: `|0-1| + |1-1| + |2-1| = 1 + 0 + 1 = 2`

**2.4 Increment and Loop:**

For each query `[l, r]`:
- Check: `if last_match_idx[l] < r: return -1`
- Extract: `subarray = [nums[i] // k for i in range(l, r+1)]`
- Sort: `subarray.sort()`
- Median: `median = subarray[len(subarray) // 2]`
- Calculate: `operations = sum(abs(x - median) for x in subarray)`

**2.5 Return Result:**

For the example, we return `[1, 2]` - 1 operation for the first query, 2 operations for the second.

