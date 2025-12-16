## Explanation

### Strategy (The "Why")

**Restate the problem:** We have a string of 'A' and 'B', and two types of queries: flip a character, or find minimum deletions to make a substring alternating.

**1.1 Constraints & Complexity:**

- **Input Size:** `1 <= n <= 10^5`, `1 <= q <= 10^5`
- **Time Complexity:** O(n + q log n) - Initialize Fenwick tree + q queries
- **Space Complexity:** O(n) - Fenwick tree
- **Edge Case:** Empty string, single character (always alternating)

**1.2 High-level approach:**

Use a Fenwick Tree (Binary Indexed Tree) to track "violations" - adjacent identical characters. Each violation requires 1 deletion. For query type 2, count violations in the range. For query type 1, update violations at affected positions.

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** For each type 2 query, scan the substring and count violations. This is O(q * n) time.
- **Optimized (Fenwick Tree):** Precompute violations, use Fenwick tree for range sum queries and point updates. This is O(n + q log n) time.
- **Why it's better:** Fenwick tree allows O(log n) range queries and updates, making it efficient for many queries.

**1.4 Decomposition:**

1. Convert string to 0-1 array (A=0, B=1)
2. Initialize Fenwick tree with violations (adjacent identical)
3. For each query:
   - Type 1: Flip character, update violations at i and i+1
   - Type 2: Query range sum of violations

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]]`

- Convert to array: `A = [0, 1, 0]`
- Initialize Fenwick tree

**2.2 Initialize Violations:**

```python
for i in range(n - 1):
    if A[i] == A[i+1]:
        bit.add(i + 1, 1)
```

For `"ABA"`: No violations initially (A≠B, B≠A)

**2.3 Process Queries:**

**Query 1: [2, 1, 2]** - Query substring `s[1:3] = "BA"`
- Range sum: `bit.query(2) - bit.query(1) = 0 - 0 = 0`
- Result: `0` (already alternating)

**Query 2: [1, 1]** - Flip `s[1]` from B to A
- `A[1] ^= 1` → `A = [0, 0, 0]`
- Update violations:
  - At position 0: `A[0] == A[1]` → add 1
  - At position 2: `A[1] == A[2]` → add 1

**Query 3: [2, 0, 2]** - Query substring `s[0:3] = "AAA"`
- Range sum: `bit.query(2) - bit.query(0) = 2 - 0 = 2`
- Result: `2` (need to delete 2 characters)

**2.4 Fenwick Tree Operations:**

- `add(i, delta)`: Update tree at position i
- `query(i)`: Get prefix sum up to position i
- Range query `[l, r]`: `query(r) - query(l)`

**Time Complexity:** O(n + q log n) - Initialize + q queries  
**Space Complexity:** O(n) - Fenwick tree

