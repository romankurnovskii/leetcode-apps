## Explanation

### Strategy (The "Why")

**Restate the problem:** We have a binary string (only 'A' and 'B') and two types of queries: flip a character at index j, or compute the minimum deletions needed to make substring s[l..r] alternating (no two adjacent characters equal).

**1.1 Constraints & Complexity:**

- **Input Size:** String length n can be up to 10^5, and there can be up to 10^5 queries.
- **Time Complexity:** O(n + q log n) where n is string length and q is number of queries. Initialization is O(n), each flip is O(log n), and each query is O(log n) using Fenwick Tree.
- **Space Complexity:** O(n) for the Fenwick Tree and the converted array.
- **Edge Case:** If a substring is already alternating, no deletions are needed, so return 0.

**1.2 High-level approach:**

The goal is to efficiently track "violations" (adjacent identical characters) and support fast updates and range queries. We use a Fenwick Tree (Binary Indexed Tree) to count violations, where each violation represents one character that needs to be deleted.

![Fenwick Tree for violations visualization](https://assets.leetcode.com/static_assets/others/fenwick-tree.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each query, scan the substring to count violations, which would be O(n) per query, leading to O(q*n) total time.
- **Optimized Strategy:** Use a Fenwick Tree to store violation counts. Each flip updates at most 2 positions in O(log n) time, and each range query takes O(log n) time. Total: O(n + q log n).
- **Optimization:** The Fenwick Tree allows us to answer range sum queries (count violations in a range) and update single positions efficiently, making it ideal for this dynamic problem.

**1.4 Decomposition:**

1. Convert the string to a 0-1 array (A=0, B=1).
2. Initialize Fenwick Tree: mark positions where adjacent characters are equal as violations.
3. For each query:
   - If type 1 (flip): update the character, then update violation status at positions i and i+1.
   - If type 2 (query): return the count of violations in range [l, r] using range sum query.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "ABA"`, `queries = [[2,1,2],[1,1],[2,0,2]]`.

- Convert to array: A = [0, 1, 0]
- Initialize Fenwick Tree: Check adjacent pairs
  - A[0] == A[1]? 0 != 1, no violation
  - A[1] == A[2]? 1 != 0, no violation
- Tree initially has no violations

**2.2 Start Processing:**

We process each query sequentially.

**2.3 Trace Walkthrough:**

| Query | Type | Parameters | Before | Action | After | Violations in Range | Result |
|-------|------|------------|--------|--------|-------|---------------------|--------|
| 0 | 2 | [1,2] | "ABA" | Query range [1,2] | - | 0 | 0 |
| 1 | 1 | [1] | "ABA" | Flip s[1]: B→A | "AAA" | Update: A[1]==A[0]? Yes, add violation at 1. A[1]==A[2]? Yes, add violation at 2. | - |
| 2 | 2 | [0,2] | "AAA" | Query range [0,2] | - | 2 (positions 1 and 2) | 2 |

**2.4 Increment and Loop:**

After processing all queries, we return the results for type-2 queries.

**2.5 Return Result:**

The result is `[0, 2]`. The first query finds 0 violations in "BA" (already alternating). After flipping, "AAA" has 2 violations, requiring 2 deletions to make it alternating (e.g., delete two 'A's to get "A").
