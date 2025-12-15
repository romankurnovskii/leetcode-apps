## Explanation

### Strategy

**Restate the problem**

We need to find all paths from node 0 to node n-1 in a directed acyclic graph (DAG). Each path is a sequence of nodes connected by edges.

**1.1 Constraints & Complexity**

- **Input Size:** The graph has 2 to 15 nodes.
- **Time Complexity:** O(2^n * n) - In the worst case, there can be exponentially many paths, and each path can have up to n nodes.
- **Space Complexity:** O(2^n * n) - We need to store all paths, and the recursion stack can go up to n levels.
- **Edge Case:** If there are no paths from 0 to n-1, we return an empty list.

**1.2 High-level approach**

Use depth-first search (DFS) to explore all possible paths from the source node (0) to the target node (n-1). As we traverse, we maintain the current path and add it to results when we reach the destination.

![Graph showing all paths from source to target](https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg)

**1.3 Brute force vs. optimized strategy**

- **Brute Force:** Generate all possible paths and filter those that end at n-1. This is inefficient and doesn't leverage the DAG structure.
- **Optimized Strategy:** Use DFS with backtracking to explore paths incrementally, only following edges that can potentially lead to the target. This naturally finds all valid paths.
- **Why optimized is better:** DFS with backtracking efficiently explores the graph structure without redundant computations, and backtracking allows us to reuse the path list.

**1.4 Decomposition**

1. **Initialize Result:** Create an empty list to store all paths.
2. **Start DFS:** Begin DFS from node 0 with an initial path containing just node 0.
3. **Explore Neighbors:** For each neighbor of the current node, add it to the path and recursively explore.
4. **Record Complete Paths:** When we reach node n-1, add the current path to results.
5. **Backtrack:** After exploring a neighbor, remove it from the path to try other paths.

### Steps

**2.1 Initialization & Example Setup**

Let's use the example: `graph = [[1,2],[3],[3],[]]`

- Nodes: 0, 1, 2, 3
- Edges: 0→1, 0→2, 1→3, 2→3
- Target: node 3

**2.2 Start DFS**

Initialize `res = []` and start DFS from node 0 with `path = [0]`.

**2.3 Trace Walkthrough**

| Current Node | Path | Neighbors | Action | Result |
|-------------|------|-----------|--------|--------|
| 0 | [0] | [1,2] | Explore 1 | - |
| 1 | [0,1] | [3] | Explore 3 | - |
| 3 | [0,1,3] | [] | Reached target! | Add [0,1,3] |
| 1 | [0,1] | [3] | Backtrack | - |
| 0 | [0] | [1,2] | Explore 2 | - |
| 2 | [0,2] | [3] | Explore 3 | - |
| 3 | [0,2,3] | [] | Reached target! | Add [0,2,3] |

**2.4 Backtrack and Continue**

After finding path [0,1,3], we backtrack by removing 3 and 1 from the path, returning to node 0. Then we explore the other neighbor (2) to find [0,2,3].

**2.5 Return Result**

After DFS completes, `res = [[0,1,3],[0,2,3]]`, which contains all paths from node 0 to node 3.
