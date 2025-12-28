## Explanation

### Strategy (The "Why")

**Restate the problem:** We need to determine if a given undirected graph with n nodes and a list of edges forms a valid tree. A valid tree must be connected (all nodes reachable) and have no cycles.

**1.1 Constraints & Complexity:**

- **Input Size:** n nodes and a list of edges. The number of edges can vary.
- **Time Complexity:** O(n + e) where e is the number of edges - we build the graph (O(e)) and perform DFS (O(n + e)).
- **Space Complexity:** O(n + e) - we store the adjacency list and visited set.
- **Edge Case:** A valid tree with n nodes must have exactly n-1 edges. If it has more edges, there must be a cycle; if fewer, it's disconnected.

**1.2 High-level approach:**

The goal is to verify two conditions: (1) the graph has exactly n-1 edges (necessary for a tree), and (2) the graph is connected with no cycles. We use DFS to check connectivity and detect cycles.

![Tree vs graph visualization](https://assets.leetcode.com/static_assets/others/tree-graph.png)

**1.3 Brute force vs. optimized strategy:**

- **Brute Force:** Check all possible paths to detect cycles, which could be exponential in the worst case.
- **Optimized Strategy:** First check if there are exactly n-1 edges. Then use DFS to verify connectivity and detect cycles by tracking visited nodes and avoiding the parent node. This is O(n + e) time.
- **Optimization:** By checking the edge count first, we can quickly reject invalid graphs. Using DFS with parent tracking allows us to detect cycles efficiently without exploring all paths.

**1.4 Decomposition:**

1. Check if the number of edges equals n-1 (a tree with n nodes must have exactly n-1 edges).
2. Build an adjacency list representation of the graph.
3. Perform DFS starting from node 0, tracking visited nodes.
4. During DFS, if we encounter a visited node that is not the parent, we've found a cycle.
5. After DFS, check if all n nodes were visited (graph is connected).
6. Return True only if both conditions are met: exactly n-1 edges and connected with no cycles.

### Steps (The "How")

**2.1 Initialization & Example Setup:**

Let's use the example: `n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]`

- Number of edges: 4, which equals n-1 = 4 ✓
- Build adjacency list:
  - 0: [1, 2, 3]
  - 1: [0, 4]
  - 2: [0]
  - 3: [0]
  - 4: [1]

**2.2 Start Checking:**

We begin DFS from node 0.

**2.3 Trace Walkthrough:**

| Step | Node | Parent | Neighbors | Action                    | Visited        |
| ---- | ---- | ------ | -------- | ------------------------- | -------------- |
| 1    | 0    | -1     | [1,2,3]  | Visit 0, go to 1          | {0}            |
| 2    | 1    | 0      | [0,4]    | Skip 0 (parent), visit 4 | {0,1}          |
| 3    | 4    | 1      | [1]      | Skip 1 (parent), return   | {0,1,4}        |
| 4    | 1    | 0      | [0,4]    | Both visited, return      | {0,1,4}        |
| 5    | 0    | -1     | [1,2,3]  | Go to 2                   | {0,1,4}        |
| 6    | 2    | 0      | [0]      | Skip 0 (parent), return   | {0,1,2,4}      |
| 7    | 0    | -1     | [1,2,3]  | Go to 3                   | {0,1,2,4}      |
| 8    | 3    | 0      | [0]      | Skip 0 (parent), return   | {0,1,2,3,4}    |

**2.4 Increment and Loop:**

During DFS:
- We mark each node as visited when we first encounter it.
- For each neighbor, we skip the parent to avoid false cycle detection.
- If we encounter a visited node that is not the parent, we've found a cycle and return False.
- We continue until all reachable nodes are visited.

**2.5 Return Result:**

The result is True because:
1. The graph has exactly 4 edges (n-1 = 4) ✓
2. All 5 nodes are visited (graph is connected) ✓
3. No cycles were detected during DFS ✓

