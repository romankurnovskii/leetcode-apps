## Explanation

### Strategy (The "Why")

**1.1 Constraints & Complexity:**

* **Input Size:** n can be up to 5 * 10^4, and there are n-1 connections.
* **Time Complexity:** O(n) - We build the graph and traverse it once using DFS.
* **Space Complexity:** O(n) - We store the graph and use O(n) for recursion stack.
* **Edge Case:** If all roads already point toward city 0, return 0.

**1.2 High-level approach:**

The goal is to find the minimum number of road reversals needed so all cities can reach city 0. We treat the graph as undirected and use DFS from city 0, counting roads that need reversal.

![Graph traversal showing which roads need to be reversed]

**1.3 Brute force vs. optimized strategy:**

* **Brute Force:** Try all possible combinations of road reversals. This is exponential.
* **Optimized (DFS from Root):** Treat graph as undirected, start DFS from city 0. When traversing an edge in the original direction (away from 0), it needs reversal. This is O(n) time.
* **Why it's better:** We only need one DFS traversal to identify all roads that need reversal, making it O(n) instead of exponential.

**1.4 Decomposition:**

1. Build an undirected graph from connections, marking original direction.
2. Start DFS from city 0.
3. For each edge traversed:
   - If the edge was originally directed away from the current node (toward 0), it's correct, no reversal needed.
   - If the edge was originally directed toward the current node (away from 0), it needs reversal, increment count.
4. Return the count.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

We initialize:
* Build graph: 
  - 0: [(1,0)] (edge to 1, original direction)
  - 1: [(0,0), (3,1)]
  - 2: [(3,1)]
  - 3: [(1,0), (2,0)]
  - 4: [(0,1), (5,1)]
  - 5: [(4,0)]
* `res = 0`

**2.2 Start Checking/Processing:**

We call `dfs(0, -1)` starting from city 0.

**2.3 Trace Walkthrough:**

| Current | Neighbor | Direction | Action | res |
|---------|----------|-----------|--------|-----|
| 0 | 1 | 0 (toward 0) | Correct, no reversal | 0 |
| 1 | 3 | 1 (away from 0) | Needs reversal | 1 |
| 3 | 2 | 1 (away from 0) | Needs reversal | 2 |
| 0 | 4 | 1 (away from 0) | Wait, from 0's perspective... | |
| 4 | 0 | 1 (toward 0) | Correct | 2 |
| 4 | 5 | 1 (away from 0) | Needs reversal | 3 |

**2.4 Increment and Loop:**

After processing each edge, we continue DFS to the next city.

**2.5 Return Result:**

After processing all cities, `res = 3` is returned (roads [1,3], [2,3], and [4,5] need reversal).

