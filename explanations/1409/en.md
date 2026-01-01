## Explanation

### Strategy (The "Why")

**Restate the problem:** Given a permutation of integers from 1 to m and a list of queries, we need to process each query by finding the position of the queried number, recording that position, and then moving the number to the front of the permutation.

**1.1 Constraints & Complexity:**

- **Input Size:** The permutation size m can be up to 10^3, and the number of queries can be up to 10^3.
- **Time Complexity:** O(q * m) where q is the number of queries and m is the permutation size - for each query, we need to find the element (O(m)) and move it (O(m)).
- **Space Complexity:** O(m) - we need to store the permutation list.
- **Edge Case:** If the query is already at the front, we still record its position (0) and move it (no change). If a query appears multiple times, we process each occurrence.

**1.2 High-level approach:**

The goal is to simulate the process: for each query, find its index in the current permutation, record it, remove it from its position, and insert it at the front.

![Permutation query visualization](https://assets.leetcode.com/static_assets/others/permutation-query.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** This is essentially what we do - for each query, search for the element and move it. The problem constraints make this approach acceptable.
- **Optimized Strategy:** The straightforward approach of using list operations (index, pop, insert) is efficient enough for the given constraints.
- **Optimization:** We could use a more complex data structure, but for the given constraints, the simple list approach is clear and efficient.

**1.4 Decomposition:**

1. Initialize the permutation as a list of integers from 1 to m.
2. For each query:
   - Find the index of the queried number in the permutation.
   - Record this index in the result.
   - Remove the number from its current position.
   - Insert it at the beginning of the permutation.
3. Return the list of recorded positions.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `m = 5`, `queries = [3, 1, 2, 1]`

- Initial permutation: `p = [1, 2, 3, 4, 5]`
- Result list: `res = []`

**2.2 Start Checking:**

We begin processing each query one by one.

**2.3 Trace Walkthrough:**

| Step | Query | p before | Index | p after | res |
| ---- | ----- | --------- | ----- | -------- | --- |
| 1    | 3     | [1,2,3,4,5] | 2 | [3,1,2,4,5] | [2] |
| 2    | 1     | [3,1,2,4,5] | 1 | [1,3,2,4,5] | [2,1] |
| 3    | 2     | [1,3,2,4,5] | 2 | [2,1,3,4,5] | [2,1,2] |
| 4    | 1     | [2,1,3,4,5] | 1 | [1,2,3,4,5] | [2,1,2,1] |

**2.4 Increment and Loop:**

After processing each query, we move to the next query in the list.

**2.5 Return Result:**

The result is `[2, 1, 2, 1]`, which are the positions of each queried number before it was moved to the front.

